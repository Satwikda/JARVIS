from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)