import string
from collections import Counter

def read_file(file_path):
    """Reads the content of a text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

def clean_text(text):
    """Cleans the text by removing punctuation and converting to lowercase."""
    return text.translate(str.maketrans('', '', string.punctuation)).lower()

def analyze_text(text):
    """Analyzes the text and returns word count, unique word count, and most common words."""
    words = text.split()
    word_count = len(words)
    unique_words = set(words)
    unique_word_count = len(unique_words)
    most_common_words = Counter(words).most_common(10)
    return word_count, unique_word_count, most_common_words

def display_results(word_count, unique_word_count, most_common_words):
    """Displays the analysis results."""
    print(f"Total Words: {word_count}")
    print(f"Unique Words: {unique_word_count}")
    print("\nMost Common Words:")
    for word, count in most_common_words:
        print(f"{word}: {count}")

def main():
    """Main function to run the Bookbot program."""
    print("Welcome to Bookbot!")
    file_path = input("Enter the path to the text file you want to analyze: ")
    text = read_file(file_path)
    if text:
        cleaned_text = clean_text(text)
        word_count, unique_word_count, most_common_words = analyze_text(cleaned_text)
        display_results(word_count, unique_word_count, most_common_words)

if __name__ == "__main__":
    main()