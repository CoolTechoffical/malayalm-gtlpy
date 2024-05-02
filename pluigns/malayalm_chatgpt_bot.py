from pyrogram import Client, filters
import openai

# Your OpenAI API key
openai.api_key = 'sk-proj-YbIcYTflSunu6Tr9io9tT3BlbkFJ7mRBegKdBmogebwc8a2B'

# Create Pyrogram client
app = Client("malayalam_chatgpt_bot")

# Function to generate Malayalam text using GPT
def generate_malayalam_text(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Define command /malayalam
@app.on_message(filters.command("malayalam", prefixes="/"))
def malayalam_chatgpt(_, message):
    # Extract the text after the command
    text = message.text.split("/malayalam", 1)[-1].strip()
    
    # Generate Malayalam text using GPT
    generated_text = generate_malayalam_text(text)
    
    # Send the generated text as a reply
    message.reply(generated_text)

# Start the bot
app.run()
