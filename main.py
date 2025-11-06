import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
from ecdsa import SigningKey, SECP256k1
import time
import json
import requests
import multiprocessing
import openai
from datetime import datetime

# Your API key
OPENAI_API_KEY = "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"

class BitcoinSearchApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bitcoin Puzzle Solver")
        self.setup_gui()
        self.is_searching = False
        self.searched_ranges = set()

    def setup_gui(self):
        # Configure main window
        self.root.geometry("700x600")

        # Create main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Add search controls
        ttk.Label(main_frame, text="Bitcoin Puzzle Solver", font=('Helvetica', 16)).grid(row=0, column=0, columnspan=2, pady=10)

        # Progress display
        self.progress_text = scrolledtext.ScrolledText(main_frame, height=20, width=80)
        self.progress_text.grid(row=1, column=0, columnspan=2, pady=10)

        # Control buttons
        self.start_button = ttk.Button(main_frame, text="Start Search", command=self.start_search)
        self.start_button.grid(row=2, column=0, pady=10)

        self.stop_button = ttk.Button(main_frame, text="Stop Search", command=self.stop_search)
        self.stop_button.grid(row=2, column=1, pady=10)
        self.stop_button['state'] = 'disabled'

    def log_message(self, message):
        self.progress_text.insert(tk.END, f"{datetime.now().strftime('%H:%M:%S')}: {message}\n")
        self.progress_text.see(tk.END)

    def check_balance(self, address):
        try:
            response = requests.get(f"https://blockchain.info/balance?active={address}")
            data = response.json()
            return data[address]['final_balance'] / 100000000
        except:
            return 0

    def search_range(self, start_range, end_range):
        x_coord = "88b21e000000000000000000ce4d8f02ff3c229d7f5e761d6d65b5ff11d02713"
        y_coord = "3c0ce2b39ea1f1538b12539497"
        x_target = int(x_coord, 16)
        y_target = int(y_coord, 16)

        for k in range(start_range, end_range):
            if not self.is_searching:
                break

            patterns = [
                k,
                k << 16,
                k << 32,
                k | 0x0001
            ]

            for test_k in patterns:
                try:
                    point = (test_k * SECP256k1.generator)

                    if (point.x() == x_target or hex(point.x()).startswith(x_coord)) and \
                       (point.y() == y_target or hex(point.y()).startswith(y_coord)):

                        # Generate address and check balance
                        key = SigningKey.from_secret_exponent(test_k, curve=SECP256k1)
                        address = key.get_verifying_key().to_string().hex()
                        balance = self.check_balance(address)

                        if balance >= 0.001:  # $100 equivalent in BTC
                            self.log_message(f"Found valuable address!\nPrivate key: {hex(test_k)}\nAddress: {address}\nBalance: {balance} BTC")

                except Exception as e:
                    continue

            if k % 1000 == 0:
                self.log_message(f"Checked through {k} values...")

    def use_openai(self, start_range, end_range):
        openai.api_key = OPENAI_API_KEY

        prompt = f"""
        Help search for Bitcoin private key in range {start_range} to {end_range}
        with coordinates:
        x: 88b21e000000000000000000ce4d8f02ff3c229d7f5e761d6d65b5ff11d02713
        y: 3c0ce2b39ea1f1538b12539497
        """

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are analyzing Bitcoin addresses."},
                    {"role": "user", "content": prompt}
                ]
            )
            self.log_message(f"OpenAI suggestion: {response.choices[0].message.content}")
        except Exception as e:
            self.log_message(f"OpenAI API error: {e}")

    def search_thread(self):
        chunk_size = 1000000
        current_range = 0

        while self.is_searching:
            start_range = current_range
            end_range = current_range + chunk_size

            if (start_range, end_range) not in self.searched_ranges:
                self.log_message(f"Searching range {start_range} to {end_range}")
                self.search_range(start_range, end_range)
                self.use_openai(start_range, end_range)
                self.searched_ranges.add((start_range, end_range))

            current_range += chunk_size

        self.start_button['state'] = 'normal'
        self.stop_button['state'] = 'disabled'

    def start_search(self):
        self.is_searching = True
        self.start_button['state'] = 'disabled'
        self.stop_button['state'] = 'normal'
        self.log_message("Starting search...")

        # Start search in separate thread
        search_thread = threading.Thread(target=self.search_thread)
        search_thread.daemon = True
        search_thread.start()

    def stop_search(self):
        self.is_searching = False
        self.log_message("Stopping search...")

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = BitcoinSearchApp()
    app.run()