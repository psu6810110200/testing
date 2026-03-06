def alternatingCharacters(s: str) -> int:
    deletions = 0

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            deletions += 1 
    return deletions
