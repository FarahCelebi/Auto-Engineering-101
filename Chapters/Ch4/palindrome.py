import re

def is_palindrome(word):
    # Remove any non-alphanumeric characters and convert the word to lowercase
    cleaned_word = re.sub(r'[^A-Za-z0-9]', '', word).lower()
    # Check if the cleaned word is equal to its reverse
    return cleaned_word == cleaned_word[::-1]

def main():
    user_input = input("Enter a word: ")
    if is_palindrome(user_input):
        print("The word is a palindrome.")
    else:
        print("The word is not a palindrome.")

if __name__ == "__main__":
    main()