def count_vowels(input_text):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in input_text if char in vowels)
    return count

def main():
    user_input = input("Enter a sentence or word: ")
    num_vowels = count_vowels(user_input)
    print(f"The number of vowels in the input is: {num_vowels}")

if __name__ == "__main__":
    main()