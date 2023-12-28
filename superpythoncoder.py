from openai import OpenAI
from dotenv import load_dotenv
import os
import subprocess  # Import subprocess module
import random   

# Load the API key from the .env file
load_dotenv()

PROGRAMS_LIST = [
    '''Given two strings str1 and str2, prints all interleavings of the given
        two strings. You may assume that all characters in both strings are
        different.Input: str1 = "AB", str2 = "CD"
        Output:
        ABCD
        ACBD
        ACDB
        CABD
        CADB
        CDAB
        Input: str1 = "AB", str2 = "C"
        Output:
        ABC
        ACB
        CAB "''',
        "A program that checks if a number is a palindrome",
        "A program that finds the kth smallest element in a given binary search tree."
    ]

def get_user_task(): 
    user_input = input("Tell me, which program would you like me to code for you? If you don't have an idea,just press enter and I will choose a random program to code: ")
    if user_input.strip() == "":
        return random.choice(PROGRAMS_LIST)
    else :
        return user_input
        
    

def gen_code(user_input):
    # Initialize the OpenAI client
    prompt = "Python code only :" + user_input + " Do not write any explanation, comments, introduction or any other text besides the python code. Also please include unit tests that check the logic of the program using 5 different inputs and expected outputs.Please print to the console the results of the unit tests. Once again, do not write any explanations, comments or introduction to this task too. "
           
    client = OpenAI(
        api_key=os.getenv('OPENAI_API_KEY')
    )

    # Get the chat completion
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="gpt-3.5-turbo",
    )

    # Extract the generated code from the response
    # Adjust the following line based on the actual structure of the ChatCompletion object
    generated_code = chat_completion.choices[0].message.content

    with open('userCode.py', 'w') as file:
        file.write(generated_code)


if __name__ == '__main__':
    user_input = get_user_task()
    print(user_input)
    gen_code(user_input)
    subprocess.run(["python", "userCode.py"])

    