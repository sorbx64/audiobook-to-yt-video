import os
import argparse
from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup

def epub_to_text(epub_path, output_path):
    # Load the EPUB file
    book = epub.read_epub(epub_path)

    # Create a new text file
    with open(output_path, 'w', encoding='utf-8') as text_file:
        for item in book.get_items():
            # We are interested in HTML content
            if item.get_type() == ITEM_DOCUMENT:
                # Parse the HTML content with BeautifulSoup
                soup = BeautifulSoup(item.get_content(), 'html.parser')
                # Extract and write the text content to the file
                text_file.write(soup.get_text())
                text_file.write('\n\n')  # Add a new line for better readability

    print(f'Text content has been written to {output_path}')

def main():
    parser = argparse.ArgumentParser(description="Extract all text content of epub file into plain text.")
    parser.add_argument("epub", type=str, help="Path to epub file whose text is to be extracted.")
    parser.add_argument("output", type=str, help="Path to output extracted text file.")
    args = parser.parse_args()
    epub_to_text(args.epub, args.output)

if __name__ == "__main__":
    main()