def funnyString(s: str) -> str:

    original_diffs = []
    for i in range(len(s) - 1):
        diff = abs(ord(s[i]) - ord(s[i + 1]))
        original_diffs.append(diff)
    
    reversed_s = s[::-1]
    reversed_diffs = []
    for i in range(len(reversed_s) - 1):
        diff = abs(ord(reversed_s[i]) - ord(reversed_s[i + 1]))
        reversed_diffs.append(diff)
    
    if original_diffs == reversed_diffs:
        return "Funny"
    else:
        return "Not Funny"
