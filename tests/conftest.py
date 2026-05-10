from dotenv import load_dotenv, dotenv_values
from pathlib import Path
import pytest


@pytest.fixture
def env():
    """
    Loads environment variables from the project's .env file and returns them
    as a dict. Ensures variables are available both via os.environ (side effect
    of load_dotenv) and as an explicit mapping for direct assertions in tests.
    """
    load_dotenv(dotenv_path='.env')
    return dotenv_values('.env')


@pytest.fixture
def sample_xlsx_file_path() -> Path:
    """
    Returns the Path to the sample .xlsx fixture file used in tests that
    exercise the modern Excel format reader.
    """
    return Path("templates/spreadsheets/sample_xlsx_spreadsheet.xlsx")


@pytest.fixture
def sample_xls_file_path() -> Path:
    """
    Returns the Path to the sample .xls fixture file used in tests that
    exercise the legacy Excel format reader.
    """
    return Path("templates/spreadsheets/sample_xls_spreadsheet.xls")