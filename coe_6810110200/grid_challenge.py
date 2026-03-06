def gridChallenge(grid):
    """
    Determine if a square grid can be rearranged such that both rows and columns
    are in lexicographical (alphabetical) order.
    
    Args:
        grid: List of strings representing the grid
        
    Returns:
        "YES" if the grid can be rearranged to meet the condition, "NO" otherwise
    """
    if not grid:
        return "YES"
    
    n = len(grid)
    
    # Sort each row alphabetically
    sorted_rows = []
    for row in grid:
        sorted_row = ''.join(sorted(row))
        sorted_rows.append(sorted_row)
    
    # Check if columns are in alphabetical order
    for col in range(len(sorted_rows[0])):  # assuming all rows have same length
        for row in range(1, n):
            if sorted_rows[row][col] < sorted_rows[row-1][col]:
                return "NO"
    
    return "YES"
