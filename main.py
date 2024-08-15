from groq_ai import check_spell_request
from text_replacer import replace_words, get_text
import os

def main():
    path_file = str(input("Enter the path of the file: "))
    text = get_text(path_file)   
    incorrect_words = {item['incorrect_word']: item['correct_word'] for item in check_spell_request(text)}
    new_text = replace_words(text, incorrect_words)
    
    with open(f"{os.curdir}/{path_file}_corrected.txt", 'w') as file:
        file.write(new_text)



if '__main__' == __name__:
    main()