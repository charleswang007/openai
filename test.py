import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

question = "Who is the highest scorer of all time in NBA history?"

prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\n\nAI: I am an AI created by OpenAI. How can I help you today?\n\nHuman: " + question + "\n\nAI:"

response = openai.Completion.create(
  model = "text-davinci-003",
  prompt = prompt,
  temperature = 0.9,
  max_tokens = 150,
  top_p = 1,
  frequency_penalty = 0.0,
  presence_penalty = 0.6,
  stop = [" Human:", " AI:"]
)
print("\n===== OpenAI Prompt =====\n")
print(prompt + response["choices"][0]["text"] + "\n")