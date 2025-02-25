
import re

def count_words(text):
    """Function to count the number of words in a given text."""
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def main():
    """Main function to run the Word Counter program."""
    print("Welcome to the Word Counter!\n")
    
    while True:
        # Get user input
        text = input("Enter a sentence or paragraph (or type 'exit' to quit): ").strip()
        
        # Exit condition
        if text.lower() == 'exit':
            print("Thank you for using the Word Counter. Goodbye!")
            break
        
        # Error handling for empty input
        if not text:
            print("Error: No text entered. Please provide valid input.")
            continue
        
        # Count words
        word_count = count_words(text)
        
        # Display output
        print(f"\nWord Count: {word_count}\n")

if __name__ == "__main__":
    main()
