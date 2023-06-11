import pytest
from src.preprocessing import preprocess_text

@pytest.fixture
def example_text():
    return "During my vacation, I visited beautiful beaches, explored ancient temples, tasted delicious local cuisine, and captured breathtaking photographs."

def test_preprocess_text(example_text):
    # Set up: 
    # The example_text fixture provides a sample text that represents a vacation experience.

    # The preprocess_text function is called with the example_text as input to preprocess the text.
    processed_text = preprocess_text(example_text)

    # Verify:
    # The processed_text is compared to the expected output.
    assert processed_text == "vacation visited beautiful beach explored ancient temple tasted delicious local cuisine captured breathtaking photograph"
