from random import randint
import os

prompt_list = []


def load_prompt_list():
    global prompt_list
    # Example: Load prompts from a file
    file_path = os.path.join(os.path.dirname(__file__), 'prompts.txt')
    try:
        with open(file_path, 'r') as file:
            prompt_list.extend(line.strip() for line in file if line.strip())
    except FileNotFoundError:
        print("Error: prompts.txt file not found.")


def prompt_text():
    global prompt_list
    if len(prompt_list) == 0:
        prompt_list = load_prompt_list()
    selection = randint(0, len(prompt_list)-1)
    prompt_text = prompt_list.pop(selection)
    return prompt_text


if __name__ == "__main__":
    prompt_list.clear
    print(f'len(prompt_list): {len(prompt_list)}')
    load_prompt_list()
    print(f'len(prompt_list): {len(prompt_list)}')
    for i in range(1, 251):
        print(f'{i:<3} {prompt_text()}')
