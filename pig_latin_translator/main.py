vowels = ["a", "e", "i", "o", "u"]

def to_pig_latin (str):
    words = str.split(" ")
    ret = ""
    for word in words:
        if word[0] in vowels:
            ret += word + "way"
        else:
            consonant_cluster_end = 0
            for letter in word:
                if letter in vowels:
                    break
                consonant_cluster_end += 1
            ret += word[consonant_cluster_end:] + word[:consonant_cluster_end] + "ay"
        ret += " "
    return ret[:len(ret)-1]

phrase = input("").lower()
translated_phrase = to_pig_latin(phrase)
print(translated_phrase)