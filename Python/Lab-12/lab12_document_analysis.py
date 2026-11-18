sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in sentence:

    if ch.lower() in "aeiou":
        vowels = vowels + 1

    elif ch.isalpha():
        consonants = consonants + 1

    elif ch.isdigit():
        digits = digits + 1

    elif ch == " ":
        spaces = spaces + 1

    else:
        special = special + 1

words = len(sentence.split())
total_characters = len(sentence)
total_letters = vowels + consonants

if total_letters > 0:
    percentage = (vowels / total_letters) * 100
else:
    percentage = 0

print()
print("=" * 42)
print("          DOCUMENT ANALYSIS REPORT")
print("=" * 42)

print("Sentence:", sentence)
print("Total characters:", total_characters)

print()
print("--- Character Breakdown ---")

print(f"Words:{words}")
print(f"Vowels:{vowels}")
print(f"Consonants:{consonants}")
print(f"Digits:{digits}")
print(f"Spaces:{spaces}")
print(f"Special characters:{special}")

print()
print("--- Summary ---")

print(f"Total letters:{total_letters}")
print(f"Vowel percentage:{percentage:.1f}" "+" "%")

print()
print("=" * 42)
print("Analysis Complete!")
print("=" * 42)
