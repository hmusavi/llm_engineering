import json
from pathlib import Path
from pydantic import BaseModel, Field

TEST_FILE = str(Path(__file__).parent / "tests.jsonl")


class TestQuestion(BaseModel):
    """A test question with expected keywords and reference answer."""

    question: str = Field(description="The question to ask the RAG system")
    keywords: list[str] = Field(description="Keywords that must appear in retrieved context")
    reference_answer: str = Field(description="The reference answer for this question")
    category: str = Field(description="Question category (e.g., direct_fact, spanning, temporal)")


def load_tests() -> list[TestQuestion]:
    """
    Load test questions from a JSONL file.
    Reads a JSONL (JSON Lines) file where each line contains a JSON object representing
    a test question. Each JSON object is parsed and unpacked into a TestQuestion instance
    using the dictionary unpacking operator (**data).
    The **data syntax is used for dictionary unpacking, which passes the key-value pairs
    from the 'data' dictionary as keyword arguments to the TestQuestion constructor.
    For example, if data = {"question": "What?", "answer": "42"}, then TestQuestion(**data)
    is equivalent to TestQuestion(question="What?", answer="42").
    Returns:
        list[TestQuestion]: A list of TestQuestion objects loaded from the JSONL file.
    Raises:
        FileNotFoundError: If TEST_FILE does not exist.
        json.JSONDecodeError: If a line in the file contains invalid JSON.
        TypeError: If the JSON data cannot be unpacked into TestQuestion parameters.
    """
    """Load test questions from JSONL file."""
    tests = []
    with open(TEST_FILE, "r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line.strip())
            tests.append(TestQuestion(**data))
    return tests
