from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY']
)

conversation = [{"role": "system", "content": "Você é o Jarvis e eu sou o Tony Stark."}]

while(True): 
    user_input = input("> ")
    conversation.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(model='gpt-4o', messages=conversation)

    conversation.append({"role": "assistant", "content": response.choices[0].message.content})
    print("\n" + response.choices[0].message.content + "\n")
