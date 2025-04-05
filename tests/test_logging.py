import sys
import os
import pytest
import logging
from modules.logger import get_logger

# Add the project directory to sys.path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)


@pytest.fixture
def logger_test():
    """
    Fixture to create a logger instance for testing.
    """
    test_logger = get_logger("test_logging")
    return test_logger


def test_logger_output(caplog, logger_test):
    """
    Test that the logger outputs messages to the console and log file.
    """
    with caplog.at_level(logging.DEBUG):
        logger_test.debug("This is a debug message")
        logger_test.info("This is an info message")
        logger_test.warning("This is a warning message")
        logger_test.error("This is an error message")
        logger_test.critical("This is a critical message")

    # Verify that all log messages are captured
    assert "This is a debug message" in caplog.text
    assert "This is an info message" in caplog.text
    assert "This is a warning message" in caplog.text
    assert "This is an error message" in caplog.text
    assert "This is a critical message" in caplog.text
