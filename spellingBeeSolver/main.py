def sort_by_length(lst):
    lst.sort(key=len)
    lst.reverse()
    return lst

with open("words.txt") as dictionary:
    words = dictionary.read().split("\n")

main_letter = input("Enter main letter: ").lower()
other_letters = input("Enter other letters: ").lower()

valid_words = []
for word in words:
    if len(word) > 3:
        if main_letter in word:
            is_valid = True
            for letter in word:
                if letter != main_letter and letter not in other_letters:
                    is_valid = False
                    break
            if is_valid:
                valid_words.append(word)
final_words = sort_by_length(valid_words)
super_words = [] # super_words is the list of words that has all the letters
for word in final_words:
    has_every_letter = main_letter in word
    for letter in other_letters:
        if letter not in word:
            has_every_letter = False
            break
    if has_every_letter:
        final_words.remove(word)
        super_words.append(word)

print("\nSuper Words:\n  ", end="")
print(*super_words, sep="\n  ")

print("\nWords:\n  ", end="")
print(*final_words, sep="\n  ")