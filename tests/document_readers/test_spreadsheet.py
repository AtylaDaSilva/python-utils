from src.document_readers.spreadsheet import read_excel
from pathlib import Path


class TestSpreadsheetReaders:
    def test_read_excel_basic_usage(self, sample_xlsx_file_path: Path):
        sheet_data = read_excel(sample_xlsx_file_path)
        assert isinstance(sheet_data, list) and len(sheet_data) > 0


    def test_read_excel_xls_file(self, sample_xls_file_path: Path):
        sheet_data = read_excel(sample_xls_file_path)
        assert isinstance(sheet_data, list) and len(sheet_data) > 0


    def test_read_excel_include_first_row(self):
        sheet_path = "templates/spreadsheets/sample_xls_spreadsheet.xls"
        sheet_data = read_excel(sheet_path, skip_first_row=False)
        first_row_sheet = sheet_data[0]
        first_row_test = {0: 0.0, 1: 'First Name', 2: 'Last Name', 3: 'Gender', 4: 'Country', 5: 'Age', 6: 'Date', 7: 'Id'}
        assert isinstance(sheet_data, list) and len(sheet_data) > 0 and (first_row_sheet == first_row_test)