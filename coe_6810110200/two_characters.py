def alternate(s: str) -> int:
    unique_chars = list(set(s))  
    max_length = 0
    
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1 = unique_chars[i]
            char2 = unique_chars[j]
            
            filtered = [c for c in s if c == char1 or c == char2]
            
            if is_alternating(filtered):
                max_length = max(max_length, len(filtered))
    
    return max_length

def is_alternating(chars: list) -> bool:
    if len(chars) < 2:
        return True
    
    for i in range(1, len(chars)):
        if chars[i] == chars[i-1]:
            return False
    
    return True
