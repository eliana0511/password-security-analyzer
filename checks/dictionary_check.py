import os

def is_common_password(pw):
    file_path = os.path.join("data", "common_passwords.txt")

    if not os.path.exists(file_path):
        return False  # fail-safe

    with open(file_path, "r") as f:
        for word in f:
            if pw.lower() == word.strip().lower():
                return True
    return False
