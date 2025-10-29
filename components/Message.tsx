import React from 'react';
import { BotIcon, UserIcon, DownloadIcon, PlayIcon } from './IconComponents';
import type { Message } from '../types';
import { marked } from 'marked';

interface MessageProps {
    message: Message;
    associatedAttachmentName?: string;
    onSuggestedAction: (prompt: string) => void;
    isLastBotMessage: boolean;
}

const GroundingSources: React.FC<{ chunks: NonNullable<NonNullable<Message['groundingMetadata']>['groundingChunks']> }> = ({ chunks }) => (
    <div className="mt-4 border-t border-gray-600 pt-3">
      <h4 className="text-xs font-semibold text-gray-400 mb-2">Sources:</h4>
      <ul className="list-decimal list-inside text-sm space-y-1">
        {chunks.map((chunk, index) => (
          <li key={index}>
            <a href={chunk.web.uri} target="_blank" rel="noopener noreferrer" className="text-blue-400 hover:underline" title={chunk.web.title}>
              {chunk.web.title || chunk.web.uri}
            </a>
          </li>
        ))}
      </ul>
    </div>
  );

const SuggestedActions: React.FC<{ actions: string[], onActionClick: (prompt: string) => void }> = ({ actions, onActionClick }) => (
    <div className="mt-4 border-t border-gray-600 pt-3">
        <div className="flex flex-wrap gap-2">
            {actions.map((action, index) => (
                <button
                    key={index}
                    onClick={() => onActionClick(action)}
                    className="flex items-center gap-2 bg-gray-600/50 hover:bg-gray-600 text-gray-200 text-sm px-3 py-1.5 rounded-lg transition-colors"
                >
                    <PlayIcon className="w-4 h-4 text-cyan-400" />
                    {action}
                </button>
            ))}
        </div>
    </div>
);

const MessageComponent: React.FC<MessageProps> = ({ message, associatedAttachmentName, onSuggestedAction, isLastBotMessage }) => {
    const [isHovered, setIsHovered] = React.useState(false);
    const isBot = message.sender === 'bot';

    const renderer = new marked.Renderer();
    renderer.link = (href, title, text) => `<a href="${href}" target="_blank" rel="noopener noreferrer" title="${title || ''}" class="text-blue-400 hover:underline">${text}</a>`;
    
    const parsedText = marked(message.text, { renderer });

    const extractContentFromCodeBlock = (text: string): string | null => {
        const trimmed = text.trim();
        const codeBlockRegex = /^```(?:\w+)?\n([\s\S]+)\n```$/;
        const match = trimmed.match(codeBlockRegex);
        if (match && match[1]) {
            return match[1];
        }
        return null;
    };
    
    const codeContent = extractContentFromCodeBlock(message.text);
    const canDownload = isBot && associatedAttachmentName && codeContent !== null;

    const handleDownload = () => {
        if (!codeContent || !associatedAttachmentName) return;
    
        const blob = new Blob([codeContent], { type: 'text/plain;charset=utf-8' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = `edited-${associatedAttachmentName}`;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(url);
    };


    return (
        <div className={`flex items-start gap-3 my-4 ${isBot ? 'justify-start' : 'justify-end'}`}>
            {isBot && (
                <div className="w-8 h-8 rounded-full bg-gradient-to-br from-cyan-500 to-blue-600 flex items-center justify-center flex-shrink-0">
                    <BotIcon className="w-5 h-5 text-white" />
                </div>
            )}
            <div
                className={`max-w-2xl p-4 rounded-2xl relative ${
                    isBot
                        ? 'bg-gray-700 rounded-tl-none'
                        : 'bg-blue-600 rounded-tr-none text-white'
                }`}
                onMouseEnter={() => setIsHovered(true)}
                onMouseLeave={() => setIsHovered(false)}
            >
                <div className="prose prose-invert prose-sm" dangerouslySetInnerHTML={{ __html: parsedText }} />
                {message.isStreaming && <span className="blinking-cursor"></span>}
                {message.groundingMetadata?.groundingChunks && message.groundingMetadata.groundingChunks.length > 0 && (
                    <GroundingSources chunks={message.groundingMetadata.groundingChunks} />
                )}
                 {canDownload && isHovered && !message.isStreaming && (
                    <button
                        onClick={handleDownload}
                        className="absolute top-2 right-2 p-1.5 bg-gray-800 rounded-md text-gray-400 hover:bg-gray-900 hover:text-white transition-opacity opacity-75 hover:opacity-100"
                        aria-label={`Download edited-${associatedAttachmentName}`}
                        title={`Download edited-${associatedAttachmentName}`}
                    >
                        <DownloadIcon className="w-4 h-4" />
                    </button>
                )}
                {isLastBotMessage && !message.isStreaming && message.suggestedActions && message.suggestedActions.length > 0 && (
                    <SuggestedActions actions={message.suggestedActions} onActionClick={onSuggestedAction} />
                )}
            </div>
            {!isBot && (
                <div className="w-8 h-8 rounded-full bg-gray-600 flex items-center justify-center flex-shrink-0">
                    <UserIcon className="w-5 h-5 text-gray-300" />
                </div>
            )}
        </div>
    );
};

export default MessageComponent;