import React from 'react';
import Header from './components/Header';
import Chatbot from './components/Chatbot';

const App: React.FC = () => {
  return (
    <div className="flex flex-col h-screen bg-gray-900 text-white font-sans">
      <Header />
      <main className="flex-1 overflow-hidden">
        <Chatbot />
      </main>
    </div>
  );
};

export default App;
