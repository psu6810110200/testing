def cat_and_mouse(x: int, y: int, z: int) -> str:
    """
    Cat and Mouse function that determines which cat reaches the mouse first.
    
    Args:
        x: Position of Cat A
        y: Position of Cat B  
        z: Position of Mouse C
        
    Returns:
        "Cat A" if Cat A reaches the mouse first
        "Cat B" if Cat B reaches the mouse first
        "Mouse C" if both cats reach at the same time (mouse escapes)
    """
    distance_a = abs(z - x)
    distance_b = abs(z - y)
    
    if distance_a < distance_b:
        return "Cat A"
    elif distance_b < distance_a:
        return "Cat B"
    else:
        return "Mouse C"

if __name__ == "__main__":
    line = list(map(int, input("Enter A B C: ").split()))
    result = cat_and_mouse(*line)
    print("Result:", result)
