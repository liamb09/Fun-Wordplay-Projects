with open("10000words.txt") as dictionary:
    words = dictionary.read().split("\n")

user_word = input("Enter word to find anagrams for: ").lower()
print("Anagrams:")

letter_count = {i: user_word.count(i) for i in set(user_word)}
for word in words:
    is_anagram = True
    for letter in word:
        if letter not in letter_count.keys() or word.count(letter) > letter_count[letter]:
            is_anagram = False
            break
    if is_anagram and word != user_word:
        print("  " + word)