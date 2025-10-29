import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { Buffer } from 'buffer';

// Polyfill Buffer for the crypto libraries that expect it to be a global.
// This needs to be done at the application's entry point to ensure it's available
// before any other modules are loaded, preventing a race condition.
// Using 'globalThis' is the modern, universal way to ensure it's available.
(globalThis as any).Buffer = Buffer;

const rootElement = document.getElementById('root');
if (!rootElement) {
  throw new Error("Could not find root element to mount to");
}

const root = ReactDOM.createRoot(rootElement);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
