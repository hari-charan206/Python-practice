def check_anagram(word1, word2):
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")

    if sorted(word1) == sorted(word2):
        print("They are anagrams!")
    else:
        print("They are not anagrams.")

print("ANAGRAM CHECKER")
first = input("Enter first word: ")
second = input("Enter second word: ")

check_anagram(first, second)
