import itertools

def get_words():
    words = []
    for i in range(10):
        word = input(f"Enter word {i+1} (5 letters): ").strip()
        while len(word) != 5:
            print("Word must be exactly 5 letters.")
            word = input(f"Enter word {i+1} (5 letters): ").strip()
        words.append(word)
    return words

def is_valid_crossword(across_words, down_words):
    # Initialize a 5x5 grid with empty strings
    grid = [['' for _ in range(5)] for _ in range(5)]

    # Place across words in the grid
    for i, word in enumerate(across_words):
        for j, letter in enumerate(word):
            grid[i][j] = letter

    # Check and place down words in the grid
    for j, word in enumerate(down_words):
        for i, letter in enumerate(word):
            if grid[i][j] == '' or grid[i][j] == letter:
                grid[i][j] = letter
            else:
                return False

    return True

def find_valid_crossword(words):
    for perm in itertools.permutations(words, 10):
        across_words = perm[:5]
        down_words = perm[5:]
        if is_valid_crossword(across_words, down_words):
            return across_words, down_words
    return None, None

def print_crossword(across_words, down_words):
    grid = [['' for _ in range(5)] for _ in range(5)]
    for i, word in enumerate(across_words):
        for j, letter in enumerate(word):
            grid[i][j] = letter
    for j, word in enumerate(down_words):
        for i, letter in enumerate(word):
            grid[i][j] = letter
    for row in grid:
        print(' '.join(row))

def main():
    words = get_words()
    across_words, down_words = find_valid_crossword(words)
    if across_words and down_words:
        print("Valid crossword found:")
        print_crossword(across_words, down_words)
    else:
        print("No valid crossword configuration found.")

if __name__ == "__main__":
    main()