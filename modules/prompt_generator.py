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

    def prompt_list_size(self) -> int:
        return len(self.prompt_list)

    def promptlist(self) -> list:
        return self.prompt_list


if __name__ == "__main__":
    prompts = prompt_generator()
    print(f'prompts.prompt_list_size(): {prompts.prompt_list_size()}')
    prompts.load_prompt_list()
    print(f'prompts.prompt_list_size(): {prompts.prompt_list_size()}')
    for i in range(0, prompts.prompt_list_size()):
        print(f'{i+1:<3} {prompts.prompt_text()}')

    prompts.load_prompt_list()
    list_of_prompts = prompts.promptlist()
    print(f'\nlist_of_prompts: {list_of_prompts[0]}')
