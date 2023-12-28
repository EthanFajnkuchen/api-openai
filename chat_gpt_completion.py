from openai import OpenAI
from dotenv import load_dotenv
import os
import subprocess  # Import subprocess module

# Load the API key from the .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

# Get the chat completion
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Python code only: Write a function that checks if a number is prime. Do not write any explanation, comments, introduction or any other text besides the python code. Also please include unit tests that check the logic of the program using 5 different inputs and expected outputs.Please print to the console the results of the unit tests. Once again, do not write any explanations, comments or introduction to this task too. "
        }
    ],
    model="gpt-3.5-turbo",
)

# Extract the generated code from the response
# Adjust the following line based on the actual structure of the ChatCompletion object
generated_code = chat_completion.choices[0].message.content

# Write the generated code to a file
with open('generatedcode.py', 'w') as file:
    file.write(generated_code)

# Run the generated Python script as a subprocess
subprocess.run(["python", "generatedcode.py"])
