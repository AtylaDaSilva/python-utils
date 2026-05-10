import openpyxl
import xlrd
from pathlib import Path
from typing import Callable


def read_excel(
    path: str,
    filter_fn: Callable[[dict], bool] = lambda row: True
) -> list[dict]:
    """
    Reads an Excel spreadsheet and returns filtered rows as a list of dicts.

    Args:
        path:      Path to the .xls or .xlsx file.
        filter_fn: A predicate that receives a row dict and returns True
                   to include it, False to exclude it. Defaults to
                   including all rows.

    Returns:
        A list of dicts where each key is a column header and each value
        is the corresponding cell value for that row.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError:        If the file extension is not .xls or .xlsx.
    """
    file = Path(path)

    if not file.exists():
        raise FileNotFoundError(f"File not found: {path}")

    match file.suffix.lower():
        case ".xlsx":
            return _read_xlsx(file, filter_fn)
        case ".xls":
            return _read_xls(file, filter_fn)
        case _:
            raise ValueError(f"Unsupported file type '{file.suffix}'. Expected .xls or .xlsx.")


def _read_xlsx(file: Path, filter_fn: Callable[[dict], bool]) -> list[dict]:
    wb = openpyxl.load_workbook(file, read_only=True, data_only=True)
    ws = wb.active
    rows = ws.iter_rows(values_only=True)

    headers = [cell for cell in next(rows)]
    result = [
        row_dict
        for row in rows
        if filter_fn(row_dict := dict(zip(headers, row)))
    ]

    wb.close()
    return result


def _read_xls(file: Path, filter_fn: Callable[[dict], bool]) -> list[dict]:
    wb = xlrd.open_workbook(file)
    ws = wb.sheet_by_index(0)

    headers = [ws.cell_value(0, col) for col in range(ws.ncols)]
    result = [
        row_dict
        for row_idx in range(1, ws.nrows)
        if filter_fn(row_dict := {
            headers[col]: ws.cell_value(row_idx, col)
            for col in range(ws.ncols)
        })
    ]

    return result