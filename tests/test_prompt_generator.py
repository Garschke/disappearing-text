import sys
import os
import pytest
import modules.prompt_generator as generator

# Add the project root directory to sys.path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)


@pytest.fixture
def setup_prompts():
    """
    Fixture to set up the prompt list before each test.
    """
    # Instantiate the PromptGenerator class
    test_prompts = generator.prompt_generator()
    return test_prompts


def test_load_prompt_list(setup_prompts):
    """
    Test that prompts are loaded correctly into the prompt_list.
    """
    # Verify the prompt list is initially empty
    test = "Prompt list should initially be empty."
    assert len(setup_prompts.prompt_list) == 0, test
    # Load the prompt list
    setup_prompts.load_prompt_list()
    # Verify the prompt list is not empty after loading
    test = "Prompt list should not be empty after loading."
    assert len(setup_prompts.prompt_list) > 0, test
    # Verify the prompt list is a list
    test = "Prompt list should be a list."
    assert isinstance(setup_prompts.prompt_list, list), test
    # Verify all prompts are strings
    test = "All prompts should be strings."
    assert all(
        isinstance(prompt, str) for prompt in setup_prompts.prompt_list
    ), test


def test_prompt_text(setup_prompts):
    """
    Test that prompt_text returns a valid prompt.
    """
    # Load the prompt list
    setup_prompts.load_prompt_list()
    # Make a copy of the prompt_list before calling prompt_text
    pre_popped_list = setup_prompts.prompt_list.copy()
    # Call prompt_text to get a prompt
    prompt = setup_prompts.prompt_text()
    test = "Generated prompt should be a string."
    assert isinstance(prompt, str), test
    test = "Generated prompt should be from the pre-popped prompt list."
    assert prompt in pre_popped_list, test


def test_prompt_list_is_unique(setup_prompts):
    """
    Test that all prompts in the prompt list are unique.
    """
    test = "Prompt list should not contain duplicates."
    assert len(
        setup_prompts.prompt_list) == len(set(setup_prompts.prompt_list)), test
