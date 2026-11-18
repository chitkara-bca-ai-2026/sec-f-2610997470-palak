username = input("Enter your username: ")
password = input("Enter your password: ")

length = len(password) >= 8
digit = False
uppercase = False

for ch in password:
    if ch >= '0' and ch <= '9':
        digit = True

    if ch >= 'A' and ch <= 'Z':
        uppercase = True

print()
print("=" * 40)
print("       PASSWORD VALIDATION REPORT")
print("=" * 40)

print("Username:", username)
print("Password:", "*" * len(password))
print()
print("--- Validation Rules ---")

if length:
    print("[PASS] Minimum 8 characters (10 characters)")
else:
    print("[FAIL] Minimum 8 characters (10 characters)")

if digit:
    print("[PASS] At least one digit")
else:
    print("[FAIL] At least one digit")

if uppercase:
    print("[PASS] At least one uppercase letter")
else:
    print("[FAIL] At least one uppercase letter")

print()
print("--- Result ---")

if length and digit and uppercase:
    print("Password is VALID!")
    print("Account created successfully for", username + "!")
else:
    print("Password is INVALID.")

print("=" * 40)
