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

# Create the Genesis Block
genesis_block = Block(0, time.time(), "Genesis Block", "0")

# Create Block 1 linked to Genesis
block1 = Block(1, time.time(), "Block 1 Data", genesis_block.hash)

# Create Block 2 linked to Block 1
block2 = Block(2, time.time(), "Block 2 Data", block1.hash)

# Blockchain as a list
blockchain = [genesis_block, block1, block2]

# Display all blocks
def display_chain(chain):
    for block in chain:
        print(f"Index: {block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")
        print("=" * 60)

print("🔗 Initial Blockchain:")
display_chain(blockchain)

# Challenge: Tamper Block 1
print("\n⚠️ Tampering Block 1's data...")
block1.data = "Tampered Data"
block1.hash = block1.compute_hash()  # Recalculate hash for tampered block

# Now observe invalid chain
print("\n🔍 Blockchain after Tampering:")
display_chain(blockchain)

# Check hash validity
def validate_chain(chain):
    for i in range(1, len(chain)):
        if chain[i].previous_hash != chain[i-1].hash:
            print(f"❌ Block {i} is INVALID! Hash mismatch.")
            return False
    print("✅ All blocks are valid.")
    return True

print("\n🛡️ Chain Validation Result:")
validate_chain(blockchain)
