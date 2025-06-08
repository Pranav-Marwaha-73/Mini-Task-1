import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        print(f"⛏️ Mining Block {self.index} with difficulty {difficulty}...")
        start_time = time.time()
        target = '0' * difficulty
        attempts = 0

        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.compute_hash()
            attempts += 1

        end_time = time.time()
        print(f"✅ Block {self.index} mined!")
        print(f"⏱️ Time taken: {end_time - start_time:.2f} seconds")
        print(f"🔁 Nonce attempts: {attempts}")
        print(f"🔒 Final Hash: {self.hash}")
        print("=" * 60)

# Set mining difficulty (e.g., 4 leading zeros)
difficulty = 4

# Create and mine a block
block = Block(1, time.time(), "Mining Demo", "0")
block.mine_block(difficulty)
