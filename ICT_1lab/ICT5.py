sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = set(words)

print(f"Number of unique words: {len(unique_words)}")
