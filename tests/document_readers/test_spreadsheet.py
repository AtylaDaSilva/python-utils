from src.document_readers.spreadsheet import read_excel


class TestSpreadsheetReaders:
    def test_read_excel_basic_usage(self):
        sheet_path = "templates/spreadsheets/sample_xlsx_spreadsheet.xlsx"
        sheet_data = read_excel(sheet_path)
        assert isinstance(sheet_data, list) and len(sheet_data) > 0


    def test_read_excel_xls_file(self):
        sheet_path = "templates/spreadsheets/sample_xls_spreadsheet.xls"
        sheet_data = read_excel(sheet_path)
        assert isinstance(sheet_data, list) and len(sheet_data) > 0
