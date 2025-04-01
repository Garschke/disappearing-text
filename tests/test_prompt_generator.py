import sys
import os
import pytest
from modules.prompt_generator import load_prompt_list, prompt_text, prompt_list


# Add the project root directory to sys.path
sys.path.append(
    os.path.abspath(
        "/Users/andrew/Documents/_Development_Learning/Programming/Python/" +
        "100-Days-of-Code-Python/day0090_Professional_Portfolio_Project-" +
        "Python_GUI-Desktop-App_Disapearing_Text_Writing_App/disappearing-text"
    )
)


@pytest.fixture
def setup_prompts():
    """
    Fixture to set up the prompt list before each test.
    """
    # Clear the prompt list and reload it
    prompt_list.clear()
    load_prompt_list()


def test_load_prompt_list(setup_prompts):
    """
    Test that prompts are loaded correctly into the prompt_list.
    """
    test = "Prompt list should not be empty after loading."
    assert len(prompt_list) > 0, test
    test = "Prompt list should be a list."
    assert isinstance(prompt_list, list), test
    test = "All prompts should be strings."
    assert all(isinstance(prompt, str) for prompt in prompt_list), test


def test_prompt_text(setup_prompts):
    """
    Test that prompt_text returns a valid prompt.
    """
    # Make a copy of the prompt_list before calling prompt_text
    pre_popped_list = prompt_list.copy()
    # Call prompt_text to get a prompt
    prompt = prompt_text()
    test = "Generated prompt should be a string."
    assert isinstance(prompt, str), test
    test = "Generated prompt should be from the pre-popped prompt list."
    assert prompt in pre_popped_list, test


def test_prompt_list_is_unique(setup_prompts):
    """
    Test that all prompts in the prompt list are unique.
    """
    test = "Prompt list should not contain duplicates."
    assert len(prompt_list) == len(set(prompt_list)), test
