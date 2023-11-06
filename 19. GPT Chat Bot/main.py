import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Use your API key
# Visit: https://platform.openai.com/account/api-keys
API_KEY = os.getenv('OPENAI_API_KEY')
print(API_KEY)

openai.api_key = API_KEY

def get_response(promt: str) -> str | None:
    text: str | None = None
    try:
        response: dict = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "user",
            "content": promt
            }
        ],

        # Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.
        temperature=0.5,

        # The maximum number of tokens to generate shared between the prompt and completion. The exact limit varies by model. (One token is roughly 4 characters for standard English text)
        max_tokens=120,

        # Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered.
        top_p=1,

        # How much to penalize new tokens based on their existing frequency in the text so far. Decreases the model's likelihood to repeat the same line verbatim.
        frequency_penalty=0,

        # How much to penalize new tokens based on whether they appear in the text so far. Increases the model's likelihood to talk about new topics.
        presence_penalty=0,

        stop = [' Human', ' AI']
        )
        print(response)
    except Exception as e:
        print(f'Error: {e}')