import random

# Mock data setup
# PoW: validator with highest computational power
pow_validators = {
    "MinerA": random.randint(10, 100),
    "MinerB": random.randint(10, 100),
    "MinerC": random.randint(10, 100)
}

# PoS: validator with highest stake
pos_validators = {
    "StakerX": random.randint(100, 1000),
    "StakerY": random.randint(100, 1000),
    "StakerZ": random.randint(100, 1000)
}

# DPoS: voters voting for delegates
delegates = ["Delegate1", "Delegate2", "Delegate3"]
voters = {
    "Voter1": random.choice(delegates),
    "Voter2": random.choice(delegates),
    "Voter3": random.choice(delegates)
}

# ---- PoW Selection Logic ----
pow_winner = max(pow_validators, key=pow_validators.get)
print("🔧 Proof of Work:")
print(f"Miner Power Ratings: {pow_validators}")
print(f"✅ Selected Validator: {pow_winner}")
print("🧠 Logic: Miner with the **highest computational power** wins the right to mine the next block.")
print("="*60)

# ---- PoS Selection Logic ----
pos_winner = max(pos_validators, key=pos_validators.get)
print("💰 Proof of Stake:")
print(f"Staker Stakes: {pos_validators}")
print(f"✅ Selected Validator: {pos_winner}")
print("🧠 Logic: Staker with the **highest stake** has the highest probability of being selected.")
print("="*60)

# ---- DPoS Selection Logic ----
# Count votes
vote_counts = {d: list(voters.values()).count(d) for d in delegates}
max_votes = max(vote_counts.values())
top_delegates = [d for d, v in vote_counts.items() if v == max_votes]
dpos_winner = random.choice(top_delegates)

print("🗳️ Delegated Proof of Stake:")
print(f"Voter Preferences: {voters}")
print(f"Vote Tally: {vote_counts}")
print(f"✅ Selected Delegate: {dpos_winner}")
print("🧠 Logic: Delegates are voted by token holders. The one with **most votes** is selected (randomly if tie).")
print("="*60)
