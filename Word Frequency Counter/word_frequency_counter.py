def count_words(sentence):
    words = sentence.lower().split()
    frequency = {}

    for word in words:
        word = word.strip(".,!?")
        if word:
            frequency[word] = frequency.get(word, 0) + 1

    print("\nWORD FREQUENCY")
    for word, count in frequency.items():
        print(word, ":", count)


print("WORD FREQUENCY COUNTER")
text = input("Enter a sentence: ")

count_words(text)
