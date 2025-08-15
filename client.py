from openai import OpenAI
 
# pip install openai 
# Add your OpenAI API key below
client = OpenAI(
  api_key="",  # Add your OpenAI API key here
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)