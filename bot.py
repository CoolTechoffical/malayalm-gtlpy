from pyrogram import Client, filters
import openai

# Your Pyrogram API ID and API hash
api_id = "your_api_id"
api_hash = "your_api_hash"

# Your bot token
bot_token = "your_bot_token"

# Your OpenAI API key
openai.api_key = 'your_openai_api_key'

# Create Pyrogram client
app = Client("malayalam_chatgpt_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

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
