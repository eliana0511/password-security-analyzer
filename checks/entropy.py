import math

def calculate_entropy(password):
    """Shannon entropy calculation."""
    if not password:
        return 0

    # Count frequency of each character
    freq = {}
    for char in password:
        freq[char] = freq.get(char, 0) + 1

    entropy = 0
    length = len(password)

    for count in freq.values():
        p = count / length
        entropy += -p * math.log2(p)

    # Multiply by length to get total bits of entropy
    return round(entropy * length, 2)
