import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from checks.entropy import calculate_entropy
from checks.patterns import detect_patterns
from checks.dictionary_check import is_common_password

def evaluate_password(pw):
    entropy = calculate_entropy(pw)
    patterns = detect_patterns(pw)
    dictionary_flag = is_common_password(pw)

    score = 0

    if entropy >= 50:
        score += 1
    if len(patterns) == 0:
        score += 1
    if not dictionary_flag:
        score += 1
    if len(pw) >= 12:
        score += 1

    if score <= 1:
        strength = "WEAK"
    elif score == 2:
        strength = "MODERATE"
    elif score == 3:
        strength = "STRONG"
    else:
        strength = "MILITARY GRADE"

    return {
        "password": pw,
        "entropy_bits": entropy,
        "patterns_found": patterns,
        "is_common_password": dictionary_flag,
        "score": score,
        "strength": strength
    }

def print_results(results):
    print("\n=== PASSWORD SECURITY REPORT ===")
    print(f"Password: {results['password']}")
    print(f"Entropy: {results['entropy_bits']} bits")
    print(f"Strength: {results['strength']}")

    print("\nPatterns detected:")
    if results["patterns_found"]:
        for p in results["patterns_found"]:
            print(f"- {p}")
    else:
        print("None found ✓")

    print("\nDictionary Check:")
    if results["is_common_password"]:
        print("⚠️ Password appears in common-password list! DO NOT USE.")
    else:
        print("✓ Password not found in common-password list.")

    print("\n=================================\n")

if __name__ == "__main__":
    pw = input("Enter a password to analyze: ")
    results = evaluate_password(pw)
    print_results(results)
