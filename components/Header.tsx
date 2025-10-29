import React from 'react';
import { SparklesIcon } from './IconComponents';

const Header: React.FC = () => {
    return (
        <header className="bg-gray-800/50 backdrop-blur-sm border-b border-gray-700/50 p-4 shadow-lg">
            <div className="container mx-auto flex items-center justify-center">
                <SparklesIcon className="w-8 h-8 text-cyan-400 mr-3" />
                <h1 className="text-2xl font-bold tracking-tight text-white">
                    AI Bitcoin Puzzle Assistant
                </h1>
            </div>
        </header>
    );
};

export default Header;
