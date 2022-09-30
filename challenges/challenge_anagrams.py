def aux(word, anagram):
    for letter in word:
        if letter in anagram:
            anagram = anagram.replace(letter, "", 1)
        else:
            return False

    return True


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    elif not first_string or not second_string:
        return False

    word, anagram = first_string.lower(), second_string.lower()
    return aux(word, anagram)
