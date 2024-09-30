from collections import deque

def is_palindrome(row):
    # Перетворюємо рядок у нижній регістр і видаляємо всі пробіли
    row = ''.join([char.lower() for char in row if char.isalnum()])
    char_deque = deque(row)

    while len(char_deque) > 1:
        print(f"processing with {char_deque}")
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True

if __name__ == "__main__":
    test_str = input("Enter row to check: ")
    
    if is_palindrome(test_str):
        print("This row is_palindrome.")
    else:
        print("This row not is_palindrome.")
