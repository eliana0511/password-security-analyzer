def detect_patterns(pw):
    patterns = []

    # Sequential patterns like 12345, abcde, qwerty
    sequences = ["12345", "qwerty", "asdf", "password", "abc"]
    for seq in sequences:
        if seq in pw.lower():
            patterns.append(f"Contains common sequence: {seq}")

    # Repeated characters
    if len(set(pw)) <= len(pw) // 2:
        patterns.append("Too many repeated characters")

    # Looks like email
    if "@" in pw and "." in pw:
        patterns.append("Contains email-like pattern")

    # Only numbers
    if pw.isdigit():
        patterns.append("Contains only digits")

    return patterns
