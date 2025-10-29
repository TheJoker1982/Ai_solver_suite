import React, { useState, useEffect, useRef } from 'react';
import type { Message, ChatMode } from '../types';
import MessageComponent from './Message';
import InputBar from './InputBar';
import { createChatSession } from '../services/geminiService';
import { processFile } from '../utils';
import { Chat, FunctionCall, GenerateContentResponse, Part } from '@google/genai';
import { implementedTools } from '../tools/toolImplementations';

const Chatbot: React.FC = () => {
    const [messages, setMessages] = useState<Message[]>([
        { id: 'initial-bot-message', text: `Hello! I am an AI assistant with access to a special Bitcoin puzzle database. You can also upload files (\`.zip\`, \`.json\`, \`.csv\`, \`.html\`) for analysis or editing.

When you switch to **Tools** mode, you can ask me to perform specific actions using the following operational tools:
*   \`analyze_bitcoin_string\`
*   \`transform_and_concatenate\`
*   \`create_bitcoin_transaction\`
*   \`check_user_credentials\`
*   \`get_team_progress\`
*   \`crack_private_key_pollard_kangaroo\`
*   \`solve_puzzle_71\`
*   \`run_ai_collision_detection\`

How can I help you today?`, sender: 'bot' }
    ]);
    const [isLoading, setIsLoading] = useState(false);
    const [chatMode, setChatMode] = useState<ChatMode>('standard');
    const chatContainerRef = useRef<HTMLDivElement>(null);
    const chatSessionRef = useRef<Chat | null>(null);

    useEffect(() => {
        if (chatContainerRef.current) {
            chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
        }
    }, [messages]);

    useEffect(() => {
        // Reset chat session when mode changes
        chatSessionRef.current = null;
    }, [chatMode]);


    const handleSendMessage = async (userMessage: string, file?: File) => {
        setIsLoading(true);
        // Clear suggested actions from the last message
        setMessages(prev => prev.map(msg => ({ ...msg, suggestedActions: [] })));

        // 1. Prepare user message for display and processing
        let userQuery = userMessage;
        let displayMessage = userMessage;
        if (file) {
            displayMessage = displayMessage 
                ? `${displayMessage}\n\n*Attachment: ${file.name}*` 
                : `*Attachment: ${file.name}*`;
        }

        const newUserMessage: Message = {
            id: `user-${Date.now()}`,
            text: displayMessage,
            sender: 'user',
            attachment: file ? { name: file.name } : undefined,
        };
        
        const botMessageId = `bot-${Date.now()}`;
        const newBotMessage: Message = { id: botMessageId, text: '', sender: 'bot', isStreaming: true };
        setMessages(prev => [...prev, newUserMessage, newBotMessage]);

        // 2. Process file content if it exists
        if (file) {
            try {
                const thinkingMessage = `Processing file: ${file.name}...`;
                setMessages(prev => prev.map(msg => msg.id === botMessageId ? { ...msg, text: thinkingMessage } : msg));
                const fileContent = await processFile(file);
                userQuery = userMessage
                    ? `Based on the content of the uploaded file "${file.name}", please answer the following question: ${userMessage}\n\n### File Content:\n\`\`\`\n${fileContent}\n\`\`\``
                    : `Analyze the following content from the uploaded file "${file.name}":\n\n### File Content:\n\`\`\`\n${fileContent}\n\`\`\``;
            } catch (error) {
                const errorMessage = error instanceof Error ? error.message : "Could not read the file.";
                setMessages(prev => prev.map(msg => msg.id === botMessageId ? { ...msg, text: `Error processing file: ${errorMessage}`, isStreaming: false } : msg));
                setIsLoading(false);
                return;
            }
        }
        
        if (chatMode === 'search' && !file) {
            userQuery = `You are a helpful and knowledgeable assistant. Please answer the following user query based on the provided Google Search results. Be concise, clear, and cite your sources. Query: "${userMessage}"`;
        }
        
        let finalBotText = '';
        let groundingMetadata: any = null;
        let aggregatedSuggestedActions: string[] = [];

        try {
            // 3. Initialize chat session if it doesn't exist
            if (!chatSessionRef.current) {
                chatSessionRef.current = createChatSession(chatMode);
            }
            const chat = chatSessionRef.current;

            let stream = await chat.sendMessageStream({ message: userQuery });
            
            let keepProcessing = true;
            
            while (keepProcessing) {
                const functionCalls: FunctionCall[] = [];
                let currentText = '';

                // 4. Process the stream from the API
                for await (const chunk of stream) {
                    const responseChunk = chunk as GenerateContentResponse;

                    const metadata = responseChunk.candidates?.[0]?.groundingMetadata;
                    if (metadata && !groundingMetadata) {
                        groundingMetadata = metadata;
                    }

                    if (responseChunk.functionCalls) {
                        functionCalls.push(...responseChunk.functionCalls);
                    }
                    
                    const chunkText = responseChunk.text;
                    if (chunkText) {
                        currentText += chunkText;
                        setMessages(prev => prev.map(msg => msg.id === botMessageId ? { ...msg, text: finalBotText + currentText } : msg));
                    }
                }
                
                finalBotText += currentText;

                // 5. If there are function calls, execute them
                if (functionCalls.length > 0) {
                    const toolIndicator = `\n\n*Running tool${functionCalls.length > 1 ? 's' : ''}: ${functionCalls.map(fc => `\`${fc.name}\``).join(', ')}...*`;
                    setMessages(prev => prev.map(msg => msg.id === botMessageId ? { ...msg, text: finalBotText + toolIndicator } : msg));
                    
                    const functionResponses: Part[] = [];

                    for (const call of functionCalls) {
                        const tool = implementedTools[call.name];
                        if (tool) {
                            const toolResult = await tool(call.args);
                            functionResponses.push({
                                functionResponse: {
                                    name: call.name,
                                    response: { result: toolResult.result },
                                }
                            });
                             if (toolResult.suggestedActions) {
                                aggregatedSuggestedActions.push(...toolResult.suggestedActions);
                             }
                        }
                    }

                    // 6. Send tool results back to the model
                    stream = await chat.sendMessageStream({ functionResponses });
                } else {
                    keepProcessing = false;
                }
            }

        } catch (error) {
            const errorMessage = error instanceof Error ? error.message : "An unknown error occurred.";
            finalBotText += `\n\nError: ${errorMessage}`;
        } finally {
             setMessages(prev =>
                prev.map(msg =>
                    msg.id === botMessageId 
                    ? { ...msg, text: finalBotText, isStreaming: false, groundingMetadata, suggestedActions: aggregatedSuggestedActions.length > 0 ? [...new Set(aggregatedSuggestedActions)] : undefined } 
                    : msg
                )
            );
            setIsLoading(false);
        }
    };

    return (
        <div className="flex flex-col h-full bg-gray-800 max-w-4xl mx-auto rounded-lg shadow-2xl my-4">
             <style>{`
                .blinking-cursor {
                    display: inline-block;
                    width: 8px;
                    height: 1.2em;
                    background-color: #9ca3af;
                    animation: blink 1s step-end infinite;
                    margin-left: 4px;
                }

                @keyframes blink {
                    50% {
                        opacity: 0;
                    }
                }
                 @keyframes fade-in {
                    from { opacity: 0; transform: translateY(-5px); }
                    to { opacity: 1; transform: translateY(0); }
                }
                .animate-fade-in {
                    animation: fade-in 0.3s ease-out forwards;
                }
                .prose {
                    max-width: 100% !important;
                }
                .prose p, .prose li {
                   word-break: break-word;
                }
                .prose pre {
                  background-color: #1f2937;
                  border: 1px solid #374151;
                  padding: 1em;
                  border-radius: 0.5rem;
                  font-size: 0.875em;
                  white-space: pre-wrap;
                  word-break: break-all;
                }
                .prose code {
                    background-color: #374151;
                    padding: 0.2em 0.4em;
                    margin: 0;
                    font-size: 0.85em;
                    border-radius: 0.25rem;
                }
                .prose pre code {
                    background-color: transparent;
                    padding: 0;
                }

            `}</style>
            <div ref={chatContainerRef} className="flex-1 overflow-y-auto p-6">
                {messages.map((msg, index) => {
                    let associatedAttachmentName: string | undefined;
                    const isLastBotMessage = msg.sender === 'bot' && index === messages.length -1;
                    if (msg.sender === 'bot' && index > 0 && messages[index - 1].sender === 'user' && messages[index - 1].attachment) {
                        associatedAttachmentName = messages[index - 1].attachment!.name;
                    }
                    return <MessageComponent 
                                key={msg.id} 
                                message={msg} 
                                associatedAttachmentName={associatedAttachmentName}
                                onSuggestedAction={(prompt) => handleSendMessage(prompt)}
                                isLastBotMessage={isLastBotMessage}
                            />;
                })}
            </div>
            <InputBar 
              onSendMessage={handleSendMessage} 
              isLoading={isLoading}
              chatMode={chatMode}
              onSetChatMode={setChatMode} 
            />
        </div>
    );
};

export default Chatbot;