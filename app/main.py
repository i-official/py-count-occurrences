def count_occurrences(phrase: str, letter: str) -> int:
    result = phrase.lower()
    counter = 0
    for phase in result:
        if phase == letter.lower():
            counter += 1
    return counter
print(count_occurrences("letter", "t"))
print(count_occurrences("abc", "a"))
print(count_occurrences("abc", "d"))
print(count_occurrences("ABC", "a"))
