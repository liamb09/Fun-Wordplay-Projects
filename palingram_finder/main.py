import time

def is_palindrome (check_me):
    return check_me == check_me[::-1]

# Get big_dictionary
with open("words.txt") as words:
    big_dictionary = words.read().split("\n")

# Get small_dictionary
with open("popular_words.txt") as words:
    small_dictionary = words.read().split("\n")

user_choice = input("Use [b]ig or [s]mall dictionary to find palingrams? ").lower()

if user_choice == "b":
    dictionary = big_dictionary
else:
    dictionary = small_dictionary

time.sleep(1)
print("\nPalingrams:")
cnt = 0
start = time.time()
for word in dictionary:
    for i in range(len(word), 0, -1):
        if is_palindrome(word[i:]) and word[:i][::-1] in dictionary:
            print("  {} {}".format(word, word[:i][::-1]))
            cnt += 1
end = time.time()
print("\nFound {} palingrams in {} seconds".format(cnt, round((end - start)*100)/100))