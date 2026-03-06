def caesarCipher(s: str, k: int) -> str:
    """
    Encrypt a string using Caesar cipher by rotating each letter by k positions.
    
    Args:
        s: Input string to encrypt
        k: Number of positions to rotate the alphabet
        
    Returns:
        Encrypted string where letters are rotated by k positions,
        non-alphabetic characters remain unchanged
    """
    result = []
    
    # Normalize k to be within 0-25 (26 letters in alphabet)
    k = k % 26
    
    for char in s:
        if 'a' <= char <= 'z':
            # Handle lowercase letters
            original_pos = ord(char) - ord('a')
            new_pos = (original_pos + k) % 26
            new_char = chr(new_pos + ord('a'))
            result.append(new_char)
        elif 'A' <= char <= 'Z':
            # Handle uppercase letters
            original_pos = ord(char) - ord('A')
            new_pos = (original_pos + k) % 26
            new_char = chr(new_pos + ord('A'))
            result.append(new_char)
        else:
            # Non-alphabetic characters remain unchanged
            result.append(char)
    
    return ''.join(result)
