import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
keywords = ["微軟", "郭台銘", "烏克麗麗"]

def generatePoem(key):
    prompt = "\nHuman: 寫一篇新詩，內容含有 \"" + key + "\"\n\nAI:"

    response = openai.Completion.create(
      model = "text-davinci-003",
      prompt = prompt,
      temperature = 0.9,
      max_tokens = 150,
      top_p = 1,
      frequency_penalty = 0.0,
      presence_penalty = 0.6,
      stop=[" Human:", " AI:"]
    )

    print(prompt + response["choices"][0]["text"] + "\n")
    
def main():
    for key in keywords:
        generatePoem(key)
        
if __name__ == '__main__':
    main()