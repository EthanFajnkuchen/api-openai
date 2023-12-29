from openai import OpenAI
from dotenv import load_dotenv
import os
import subprocess  # Import subprocess module
import random   
from colorama import Fore, Style, init
from tqdm import tqdm

init(autoreset=True)


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
        
    

def gen_code(user_input, client):
    # Initialize the OpenAI client
    prompt = "Python code only :" + user_input + " Do not write any explanation, comments, introduction or any other text besides the python code. Also please include unit tests that check the logic of the program using 5 different inputs and expected outputs.Please print to the console the results of the unit tests. Once again, do not write any explanations, comments or introduction to this task too. "
           

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

    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path for the new file
    file_path = os.path.join(current_dir, 'userCode.py')

    # Write the generated code to the file
    with open(file_path, 'w') as file:
        file.write(generated_code)

def run_and_fix_code(file_path, client, attempts=5):
    with tqdm(total=100, desc="Running and fixing code") as pbar:
        for attempt in range(attempts):
            try:
                result = subprocess.run(["python", file_path],check=True, capture_output=True, text=True)
                print(Fore.GREEN + ' Code creation completed successfully')
                pbar.update(100)  # Update progress bar to 100%

                #subprocess.call(["open", file_path]) #This line does not work, it seems that the file does not exists.
                os.startfile(file_path) #This line seems to open the file using the default app to open python code
                return
            except subprocess.CalledProcessError as e:
                print(Fore.RED + f" Error running generated code! Error: {e.stderr}")
                pbar.update(100 / attempts)  # Update progress for each attempt
                error_message = f"There was an error in the generated code: {e.stderr}. Please fix the code. Once again, i want python only! Do not write any explanations, comments or introcution. Just write a new code with the fixed error!"
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": error_message
                        }
                    ],
                    model="gpt-3.5-turbo",
                )
                fixed_code = chat_completion.choices[0].message.content
                with open(file_path, 'w') as file:
                    file.write(fixed_code)

                if attempt == attempts - 1:
                    pbar.update(100) 

        print("Code generation FAILED")




if __name__ == '__main__':

    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    user_input = get_user_task()
    gen_code(user_input,client)
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'userCode.py')
    run_and_fix_code(file_path, client)
    
    