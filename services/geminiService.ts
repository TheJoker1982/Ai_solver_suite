import { GoogleGenAI, Chat, GenerateContentStreamRequest, Part } from "@google/genai";
import {
  PUZZLE_ADDRESS_MAPPINGS,
  COORDINATE_ANALYSIS_DATA,
  PUZZLE_STRATEGY_DATA,
  TRANSACTION_DATA,
  BACKEND_CONFIG_DATA,
  BLOCK_DATA,
  LIGHTNING_NETWORK_DATA,
  USER_CONSTANTS_DATA,
  PROVEN_FRAMEWORK_DATA,
  MINUS_ONE_MASTER_DATA,
  OFFSET_HEIGHT_DATA,
  PHONETIC_ANALYSIS_DATA,
  SIGNATURE_DATA,
  LARGE_TX_DATA,
  POLLARD_KANGAROO_SCRIPT_DATA,
  PUZZLE_71_SOLVER_WEB_SCRIPT_DATA,
  PUZZLE_71_SOLVER_HEADLESS_SCRIPT_DATA,
  AI_OPTIMIZED_COLLISION_SYSTEM_DATA,
} from '../constants';
import type { ChatMode } from "../types";
import { toolDeclarations } from "../tools/toolDeclarations";

const API_KEY = process.env.API_KEY;
if (!API_KEY) {
  throw new Error("API_KEY environment variable not set");
}

const ai = new GoogleGenAI({ apiKey: API_KEY });

const baseSystemInstruction = `You are an expert AI assistant specializing in a specific, complex Bitcoin puzzle database. Your goal is to answer user questions based *only* on the extensive data provided below. The user may also upload a file; if file content is provided in the prompt, you must base your answer on that file content in conjunction with the database. If the user asks for edits or modifications to the file content, your response should consist *only* of the complete, modified file content, enclosed within a single Markdown code block. Be helpful, clear, and analytical. Format your responses using Markdown for readability.

Here is the entire dataset you must use:

### Puzzle Address Mappings
\`\`\`json
${PUZZLE_ADDRESS_MAPPINGS}
\`\`\`

### Coordinate Analysis Data
\`\`\`json
${COORDINATE_ANALYSIS_DATA}
\`\`\`

### Puzzle Strategy Data
\`\`\`json
${PUZZLE_STRATEGY_DATA}
\`\`\`

### Transaction Data
\`\`\`json
${TRANSACTION_DATA}
\`\`\`

### Backend Config Data
\`\`\`json
${BACKEND_CONFIG_DATA}
\`\`\`

### Block Data
\`\`\`json
${BLOCK_DATA}
\`\`\`

### Lightning Network Data
\`\`\`json
${LIGHTNING_NETWORK_DATA}
\`\`\`

### User Constants Data
\`\`\`json
${USER_CONSTANTS_DATA}
\`\`\`

### Proven Framework Data
\`\`\`json
${PROVEN_FRAMEWORK_DATA}
\`\`\`

### Minus One Master Data
\`\`\`json
${MINUS_ONE_MASTER_DATA}
\`\`\`

### Offset Height Data
\`\`\`json
${OFFSET_HEIGHT_DATA}
\`\`\`

### Phonetic Analysis Data
\`\`\`json
${PHONETIC_ANALYSIS_DATA}
\`\`\`

### Signature Data
\`\`\`json
${SIGNATURE_DATA}
\`\`\`

### Large Transaction Data
\`\`\`json
${LARGE_TX_DATA}
\`\`\`

### Pollard Kangaroo Script for 1PWW
\`\`\`javascript
${POLLARD_KANGAROO_SCRIPT_DATA}
\`\`\`

### Puzzle 71 Web Solver Script
\`\`\`python
${PUZZLE_71_SOLVER_WEB_SCRIPT_DATA}
\`\`\`

### Puzzle 71 Headless Solver Script
\`\`\`python
${PUZZLE_71_SOLVER_HEADLESS_SCRIPT_DATA}
\`\`\`

### AI-Optimized Collision System Script
\`\`\`python
${AI_OPTIMIZED_COLLISION_SYSTEM_DATA}
\`\`\`

Now, answer the user's questions based on this data.`;

const toolsSystemInstruction = `You have access to a set of specialized tools to help solve the Bitcoin puzzle. When a user's query can be answered using a tool, you should call it. If a tool requires parameters that the user has not provided, you MUST ask clarifying questions to get the necessary information. Do not guess missing parameters. The available tools are: 'analyze_bitcoin_string', 'transform_and_concatenate', 'create_bitcoin_transaction', 'check_user_credentials', 'get_team_progress', 'crack_private_key_pollard_kangaroo', 'solve_puzzle_71', 'run_ai_collision_detection', 'verify_puzzle_key', and 'sign_ownership_message'. Only use the tools when the user's request directly implies their use. For general questions, use the provided database.`;

export function createChatSession(mode: ChatMode): Chat {
  let modelName: string;
  const config: any = {};
  let history: { role: string; parts: Part[] }[] = [];

  switch (mode) {
    case 'thinking':
      modelName = 'gemini-2.5-pro';
      config.systemInstruction = baseSystemInstruction;
      config.thinkingConfig = { thinkingBudget: 32768 };
      break;
    
    case 'search':
      modelName = 'gemini-2.5-flash';
      config.tools = [{ googleSearch: {} }];
      // No system instruction for search, we will format the prompt directly.
      break;

    case 'tools':
      modelName = 'gemini-2.5-pro';
      config.systemInstruction = `${baseSystemInstruction}\n\n${toolsSystemInstruction}`;
      config.tools = toolDeclarations;
      break;

    case 'standard':
    default:
      modelName = 'gemini-2.5-flash';
      config.systemInstruction = baseSystemInstruction;
      break;
  }

  return ai.chats.create({
    model: modelName,
    config,
    history,
  });
}