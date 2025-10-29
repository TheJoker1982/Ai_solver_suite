import { FunctionDeclaration, Type } from '@google/genai';

export const toolDeclarations: { functionDeclarations: FunctionDeclaration[] }[] = [
    {
        functionDeclarations: [
            {
                name: 'analyze_bitcoin_string',
                description: 'Analyzes a Bitcoin-related string (e.g., address, private key, transaction hash) to determine its type, format, and validity. If a private key is provided, it derives the corresponding public key and address.',
                parameters: {
                    type: Type.OBJECT,
                    properties: {
                        input_string: {
                            type: Type.STRING,
                            description: 'The Bitcoin-related string to analyze.',
                        },
                    },
                    required: ['input_string'],
                },
            },
            {
                name: 'transform_and_concatenate',
                description: 'Takes multiple input strings, applies specified transformations (e.g., base64, hex, reverse), and concatenates them in order.',
                parameters: {
                    type: Type.OBJECT,
                    properties: {
                        inputs: {
                            type: Type.ARRAY,
                            description: 'An array of objects, each with a value and a transformation to apply.',
                            items: {
                                type: Type.OBJECT,
                                properties: {
                                    value: {
                                        type: Type.STRING,
                                        description: 'The string value to transform.',
                                    },
                                    transform: {
                                        type: Type.STRING,
                                        description: 'The transformation to apply.',
                                        enum: ['none', 'base64', 'hex', 'reverse'],
                                    },
                                },
                                required: ['value', 'transform'],
                            },
                        },
                    },
                    required: ['inputs'],
                },
            },
            {
                name: 'create_bitcoin_transaction',
                description: 'Creates a Bitcoin transaction between two addresses for a specified amount. This is an operational tool.',
                parameters: {
                    type: Type.OBJECT,
                    properties: {
                        from_address: {
                            type: Type.STRING,
                            description: 'The source Bitcoin address.',
                        },
                        to_address: {
                            type: Type.STRING,
                            description: 'The destination Bitcoin address.',
                        },
                        amount_btc: {
                            type: Type.NUMBER,
                            description: 'The amount of BTC to send.',
                        },
                    },
                    required: ['from_address', 'to_address', 'amount_btc'],
                },
            },
            {
                name: 'check_user_credentials',
                description: 'Checks user credentials against the system database to perform a login.',
                parameters: {
                    type: Type.OBJECT,
                    properties: {
                        username: {
                            type: Type.STRING,
                            description: 'The username for the login attempt.',
                        },
                        password: {
                            type: Type.STRING,
                            description: 'The password for the login attempt.',
                        },
                    },
                    required: ['username', 'password'],
                },
            },
            {
                name: 'get_team_progress',
                description: 'Retrieves the current progress of the puzzle-solving team.',
                parameters: {
                    type: Type.OBJECT,
                    properties: {},
                },
            },
            {
                name: 'crack_private_key_pollard_kangaroo',
                description: "Runs the Pollard's Kangaroo algorithm to crack a private key from a public key, based on the provided script.",
                parameters: {
                    type: Type.OBJECT,
                    properties: {
                        public_key: {
                            type: Type.STRING,
                            description: 'The public key to attempt to crack. For example, the one for 1PWW.',
                        },
                    },
                    required: ['public_key'],
                },
            },
            {
                name: 'solve_puzzle_71',
                description: 'Runs the solver for Bitcoin Puzzle 71. Can test a specific candidate or a general strategy.',
                parameters: {
                    type: Type.OBJECT,
                    properties: {
                        candidate_modification: {
                            type: Type.STRING,
                            description: 'Optional. A specific candidate modification string to test, e.g., "OR (1 << 38) | (1 << 51)".',
                        },
                    },
                },
            },
            {
                name: 'run_ai_collision_detection',
                description: 'Runs the AI-optimized collision detection system for Puzzle 71.',
                parameters: {
                    type: Type.OBJECT,
                    properties: {
                        target_address: {
                            type: Type.STRING,
                            description: 'Optional target address. Defaults to the main Puzzle 71 address if not provided.',
                        },
                    },
                },
            },
            {
                name: 'verify_puzzle_key',
                description: 'Performs cryptographic verification to confirm if a private key corresponds to a Bitcoin address. Defaults to the Puzzle 71 address if not specified.',
                parameters: {
                    type: Type.OBJECT,
                    properties: {
                        key_value: {
                            type: Type.STRING,
                            description: 'The private key value, provided as a string.',
                        },
                        key_type: {
                            type: Type.STRING,
                            description: 'The format of the key_value.',
                            enum: ['bits', 'hex', 'decimal'],
                        },
                        target_address: {
                            type: Type.STRING,
                            description: 'Optional. The Bitcoin address to verify against. Defaults to the Puzzle 71 address.',
                        }
                    },
                    required: ['key_value', 'key_type'],
                }
            },
            {
                name: 'sign_ownership_message',
                description: 'Signs a message with a private key to prove ownership of the corresponding address.',
                parameters: {
                    type: Type.OBJECT,
                    properties: {
                        private_key_hex: {
                            type: Type.STRING,
                            description: 'The private key in hexadecimal format.',
                        },
                        message: {
                            type: Type.STRING,
                            description: 'The message to sign.',
                        },
                    },
                    required: ['private_key_hex', 'message'],
                }
            }
        ],
    },
];