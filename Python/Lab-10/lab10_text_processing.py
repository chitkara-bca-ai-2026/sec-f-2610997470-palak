print("=" * 40)
print("          TEXT PROCESSING TOOL")
print("=" * 40)

sentence = input("Enter a sentence: ")

print("\n--- Processing Results ---")

position = int(input("Enter position for indexing: "))
print(f"Character at position {position} : '{sentence[position]}'")

start = int(input("Enter start index for slicing : "))
end = int(input("Enter end index for slicing : "))

print(f"Sliced string [{start}:{end}]       : '{sentence[start:end]}'")

print(f"Uppercase                       : {sentence.upper()}")
print(f"Lowercase                       : {sentence.lower()}")

word = input("Enter word to replace : ")
replacement = input("Enter replacement word : ")

new_sentence = sentence.replace(word, replacement)

print(f"After replace                   : {new_sentence}")
print(f"Length of sentence              : {len(sentence)}")

print("\n" + "=" * 40)
print("Analysis Complete!")
print("=" * 40)
