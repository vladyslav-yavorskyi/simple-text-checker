import os
import re

def get_text(filename: str):
    # Read the text from the file
    with open(f"{os.curdir}/{filename}", 'r') as file:
        return file.read()
    

def replace_words(text, corrections):
    """
    Function to replace the incorrect words in the text with the correct words
    Args:
        text: str: The text to be corrected
        corrections: dict: A dictionary of incorrect words and their correct words
    Returns:
        str: The corrected text
    """
    pattern = re.compile(r'\b(' + '|'.join(re.escape(key) for key in corrections.keys()) + r')\b')
    
    def replace(match):
        return corrections[match.group(0)]
    
    return pattern.sub(replace, text)