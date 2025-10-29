export interface Message {
  id: string;
  text: string;
  sender: 'user' | 'bot';
  isStreaming?: boolean;
  groundingMetadata?: {
    groundingChunks?: {
      web: {
        uri: string;
        title: string;
      };
    }[];
  };
  attachment?: {
    name: string;
  };
  suggestedActions?: string[];
}

export type ChatMode = 'standard' | 'thinking' | 'search' | 'tools';