
from collections import Counter

words = ["playing", "played", "player"]

# Step 1: Initialize vocabulary
vocab = [list(word) for word in words]

# Step 2: Calculate frequency and score
for step in range(5):

    token_freq = Counter()
    pair_freq = Counter()

    for word in vocab:
        for token in word:
            token_freq[token] += 1

        for i in range(len(word)-1):
            pair_freq[(word[i], word[i+1])] += 1

    if not pair_freq:
        break

    scores = {}

    for pair, freq in pair_freq.items():
        a, b = pair
        scores[pair] = freq / (token_freq[a] * token_freq[b])

    # Step 3: Find highest score
    best_pair = max(scores, key=scores.get)

    print("\nToken Frequencies:", token_freq)
    print("Pair Frequencies:", pair_freq)
    print("Scores:", scores)
    print("Best Pair:", best_pair)

    # Step 4: Merge best pair
    for i in range(len(vocab)):
        new_word = []
        j = 0

        while j < len(vocab[i]):
            if (j < len(vocab[i])-1 and
                (vocab[i][j], vocab[i][j+1]) == best_pair):
                new_word.append(vocab[i][j] + vocab[i][j+1])
                j += 2
            else:
                new_word.append(vocab[i][j])
                j += 1

        vocab[i] = new_word

# Step 5: Display final tokens
print("\nFinal WordPiece Vocabulary:")
for word in vocab:
    print(word)
