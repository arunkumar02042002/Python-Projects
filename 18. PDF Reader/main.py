'''
PDF Reader is a Python script that extracts text from a PDF file, counts word frequencies,
displays the top five most common words, count alphabet frequency and display the frequency table.
'''

# Import necessary libraries
import regex as re
from collections import Counter
from PyPDF2 import PdfReader
import string

# Define a function to extract text from a PDF file
def extract_text_from_pdf(pdf_file_name: str) -> list[str]:
    with open(pdf_file_name, 'rb') as pdf:
        # Create a PdfReader object
        reader = PdfReader(pdf, strict=False)

        # Print the number of pages in the PDF
        print('-----------------------------------------')
        print(f'Your PDF has {len(reader.pages)} pages.')
        print('=========================================')

        # Extract text from each page
        pdf_text: list[str] = [page.extract_text() for page in reader.pages]

        return pdf_text

# Define a function to extract words
def extract_word(text_list: list[str]) -> list[str]:
    all_words: list[str] = []

    for text in text_list:
        # Split text into words using regular expressions
        split_text: list[str] = re.split(r'\s+|[,;?!.-]\s*', text.lower())

    # Filter out empty strings and append words to the list
    all_words += [word for word in split_text if word]

    return all_words

# Define a function to count words in a list of text
def count_words(text_list: list[str]) -> Counter:
    all_words: list[str] = extract_word(text_list)

    return Counter(all_words)

# Define a function to count alphabets in a list of text
def count_alphabets(text_list: list[str]) -> Counter:

    all_words: list[str] = extract_word(text_list)

    all_alphabets: list[str] = []
    for i in all_words:
        # Add characters to the list
        all_alphabets += [j for j in i]

    return Counter(all_alphabets)
    
# Main program
def main():
    # Extract text from a PDF file
    extracted_text: list[str] = extract_text_from_pdf('sample.pdf')

    # Count word frequencies
    counter: Counter = count_words(extracted_text)

    print('Top five common words.')
    print('-----------------------------------------')
    # Print the top five most common words and their frequencies
    for word, frequency in counter.most_common(5):
        print(f'{word:10}: {frequency:3} times')
    print('=========================================')

    # Count alphabet frequencies
    char_counter: Counter = count_alphabets(extracted_text)

    print('Alpabet   : Frequency')
    print('-----------------------------------------')
    # Print the top five most common words and their frequencies
    for i in string.ascii_lowercase:
        print(f'{i:10}: {char_counter.get(i, 0):3} times')
    print('-----------------------------------------')


if __name__ == '__main__':
    main()