def count_occurrences(phrase: str, letter: str) -> int:
    result = phrase.lower()
    return result.count(letter.lower())
print(count_occurrences("letter", "t"))
print(count_occurrences("abc", "a"))
print(count_occurrences("abc", "d"))
print(count_occurrences("ABC", "a"))
