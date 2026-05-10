import pytest
from dotenv import load_dotenv, dotenv_values


@pytest.fixture
def env():
    load_dotenv(dotenv_path='.env')
    return dotenv_values('.env')
