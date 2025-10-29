import React, { useState, useRef } from 'react';
import { SendIcon, BrainIcon, SearchIcon, ChatBubbleIcon, PaperclipIcon, ToolsIcon } from './IconComponents';
import type { ChatMode } from '../types';

interface InputBarProps {
    onSendMessage: (message: string, file?: File) => void;
    isLoading: boolean;
    chatMode: ChatMode;
    onSetChatMode: (mode: ChatMode) => void;
}

const modes: { id: ChatMode; name: string; description: string; icon: React.FC<{className?: string}> }[] = [
    { id: 'standard', name: 'Standard', description: 'Standard model for analyzing provided data.', icon: ChatBubbleIcon },
    { id: 'thinking', name: 'Thinking', description: 'Uses a more powerful model for complex analysis.', icon: BrainIcon },
    { id: 'tools', name: 'Tools', description: 'Enables the AI to use specialized Bitcoin puzzle tools.', icon: ToolsIcon },
    { id: 'search', name: 'Search', description: 'Uses Google Search for up-to-date information.', icon: SearchIcon },
];

const InputBar: React.FC<InputBarProps> = ({ onSendMessage, isLoading, chatMode, onSetChatMode }) => {
    const [inputValue, setInputValue] = useState('');
    const [file, setFile] = useState<File | null>(null);
    const fileInputRef = useRef<HTMLInputElement>(null);

    const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        if (e.target.files && e.target.files.length > 0) {
            setFile(e.target.files[0]);
        }
    };

    const handleRemoveFile = () => {
        setFile(null);
        if (fileInputRef.current) {
            fileInputRef.current.value = '';
        }
    };

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if ((inputValue.trim() || file) && !isLoading) {
            onSendMessage(inputValue.trim(), file ?? undefined);
            setInputValue('');
            handleRemoveFile();
        }
    };

    return (
        <div className="p-4 bg-gray-800 border-t border-gray-700">
            <div className="flex items-center justify-center gap-2 mb-3">
                {modes.map((mode) => (
                     <div key={mode.id} className="relative group">
                        <input
                            type="radio"
                            id={mode.id}
                            name="chat-mode"
                            value={mode.id}
                            checked={chatMode === mode.id}
                            onChange={() => onSetChatMode(mode.id)}
                            className="sr-only"
                            disabled={isLoading}
                        />
                        <label
                            htmlFor={mode.id}
                            className={`flex items-center gap-2 px-3 py-2 text-sm font-medium rounded-md cursor-pointer transition-colors ${
                                chatMode === mode.id
                                    ? 'bg-blue-600 text-white'
                                    : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
                            } ${isLoading ? 'cursor-not-allowed opacity-50' : ''}`}
                        >
                            <mode.icon className="w-5 h-5" />
                           {mode.name}
                        </label>
                        <div className="absolute bottom-full mb-2 w-max max-w-xs p-2 text-xs text-white bg-gray-900 rounded-md opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none">
                            {mode.description}
                        </div>
                    </div>
                ))}
            </div>
            <div className="bg-gray-700 rounded-lg">
                {file && (
                     <div className="px-3 pt-2 text-sm">
                        <div className="bg-gray-600/50 py-1 px-2 rounded-md text-gray-300 flex items-center justify-between animate-fade-in">
                            <span className="truncate" title={file.name}>Attached: {file.name}</span>
                            <button onClick={handleRemoveFile} disabled={isLoading} className="ml-2 text-gray-400 hover:text-white disabled:opacity-50 text-lg">&times;</button>
                        </div>
                    </div>
                )}
                <form onSubmit={handleSubmit} className="flex items-center gap-2 p-2">
                     <input
                        type="file"
                        ref={fileInputRef}
                        onChange={handleFileChange}
                        style={{ display: 'none' }}
                        accept=".zip,.json,.csv,.html,text/*,application/json"
                    />
                    <button
                        type="button"
                        onClick={() => fileInputRef.current?.click()}
                        disabled={isLoading}
                        className="p-3 rounded-full text-gray-300 disabled:opacity-50 hover:bg-gray-600 hover:text-white transition-colors"
                        aria-label="Attach file"
                    >
                        <PaperclipIcon className="w-6 h-6" />
                    </button>
                    <textarea
                        value={inputValue}
                        onChange={(e) => setInputValue(e.target.value)}
                        onKeyDown={(e) => {
                            if (e.key === 'Enter' && !e.shiftKey) {
                                e.preventDefault();
                                handleSubmit(e);
                            }
                        }}
                        placeholder={file ? "Add a comment about the file..." : "Ask a question..."}
                        className="flex-1 bg-transparent text-white placeholder-gray-400 focus:outline-none resize-none"
                        rows={1}
                        disabled={isLoading}
                    />
                    <button
                        type="submit"
                        disabled={isLoading || (!inputValue.trim() && !file)}
                        className="p-3 rounded-full bg-blue-600 text-white disabled:bg-gray-500 disabled:cursor-not-allowed hover:bg-blue-700 transition-colors"
                        aria-label="Send message"
                    >
                        <SendIcon className="w-6 h-6" />
                    </button>
                </form>
            </div>
        </div>
    );
};

export default InputBar;