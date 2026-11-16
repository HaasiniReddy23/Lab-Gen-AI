from collections import Counter

words = ["low", "lower", "lowest", "low"]

# Convert words into characters
vocab = [list(word) for word in words]

for step in range(5):
    pairs = Counter()

    for word in vocab:
        for i in range(len(word)-1):
            pairs[(word[i], word[i+1])] += 1

    if not pairs:
        break

    # Find most frequent pair
    best = max(pairs, key=pairs.get)
    print("Merging:", best)

    # Merge the pair
    for i in range(len(vocab)):
        new_word = []
        j = 0

        while j < len(vocab[i]):
            if (j < len(vocab[i])-1 and
                (vocab[i][j], vocab[i][j+1]) == best):
                new_word.append(vocab[i][j] + vocab[i][j+1])
                j += 2
            else:
                new_word.append(vocab[i][j])
                j += 1

        vocab[i] = new_word

print("\nFinal BPE Tokens:")
for word in vocab:
    print(word)