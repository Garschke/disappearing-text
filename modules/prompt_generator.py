from random import randint
import os


class prompt_generator():

    def __init__(self):
        self.prompt_list = []

    def load_prompt_list(self) -> None:
        # Example: Load prompts from a file
        file_path = os.path.join(
            os.path.dirname(__file__), 'prompts.txt'
        )
        try:
            with open(file_path, 'r') as file:
                self.prompt_list.extend(
                    line.strip() for line in file if line.strip()
                )
        except FileNotFoundError:
            print("Error: prompts.txt file not found.")

    def prompt_text(self) -> str:
        if (not self.prompt_list):
            self.load_prompt_list
        selection = randint(0, len(self.prompt_list)-1)
        prompt_text = self.prompt_list.pop(selection)
        return prompt_text


if __name__ == "__main__":
    prompts = prompt_generator()
    print(f'len(prompts.prompt_list): {len(prompts.prompt_list)}')
    prompts.load_prompt_list()
    print(f'len(prompts.prompt_list): {len(prompts.prompt_list)}')
    for i in range(1, 251):
        print(f'{i:<3} {prompts.prompt_text()}')
