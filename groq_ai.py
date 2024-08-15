from groq import Groq
from pydantic import BaseModel
import json

client = Groq()

# SpellChecker model
class SpellChecker(BaseModel):
    incorrect_word: str
    correct_word: str


def check_spell_request(user_text: str):
    """ 
    Function to check the spelling of the words in the user_text
    Args:
        user_text: str: The text to be spell checked
    Returns:
        list: A list of dictionaries with the incorrect and correct words
    """
    
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are english words database that outputs in JSON format. Please provide the JSON Object with the incorrect words."
                f"The JSON Object must use the schema: {json.dumps(SpellChecker.model_json_schema(), indent=2)}"
            },
            {
                "role": "user",
                "content": f'fetch, there might be more that one incorrect word.: {user_text}'
            }
        ],
        temperature=0,
        stream=False,
        response_format={"type": "json_object"},
        )
    return json.loads(completion.choices[0].message.content)['data']
