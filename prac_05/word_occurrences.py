def main():
    user_input = input("Text: ")
    words = user_input.split()
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    longest_word_length = max(len(word) for word in word_counts.keys())
    for word in sorted(word_counts.keys()):
        print(f"{word:{longest_word_length}} : {word_counts[word]}")


main()
