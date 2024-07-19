def solve_cryptarithmetic(puzzle):
    # Extract unique letters from the puzzle
    letters = set([char for word in puzzle for char in word if char.isalpha()])
    letters = list(letters)
    n = len(letters)
    used_digits = [False] * 10
    letter_to_digit = {}

    def is_valid_solution():
        # Check if all words are valid with the current letter_to_digit mapping
        return all(word_to_number(word) != 0 for word in puzzle)

    def word_to_number(word):
        # Convert a word to its corresponding number using letter_to_digit mapping
        return int("".join(str(letter_to_digit[char]) for char in word))

    def solve(index):
        # Recursive function to try assigning digits to letters
        if index == n:
            # If all letters are assigned, check if the solution is valid
            if is_valid_solution():
                return True
            return False
        
        letter = letters[index]
        for digit in range(10):
            if not used_digits[digit]:
                used_digits[digit] = True
                letter_to_digit[letter] = digit
                if solve(index + 1):
                    return True
                # Backtrack
                used_digits[digit] = False
        
        return False

    # Start solving from the first letter
    if solve(0):
        # Print the letter_to_digit mapping
        for letter in letters:
            print(f"{letter}: {letter_to_digit[letter]}")
    else:
        print("No solution found.")

# Example usage:
if __name__ == "__main__":
    puzzle = ["SEND", "MORE", "MONEY"]
    #puzzle = []
    #while True:
     #   word = input().strip().upper()
      #  if word == "DONE":
       #     break
        #puzzle.append(word)
    
    #solve_cryptarithmetic(puzzle)
    solve_cryptarithmetic(puzzle)
