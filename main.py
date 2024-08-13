from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY']
)

deployment = "gpt-4o"

prompt = "Quem nasceu primeiro, o ovo ou a galinha?"
messages = [{"role": "user", "content": prompt}]

completion = client.chat.completions.create(model=deployment, messages=messages)

print(completion.choices[0].message.content)