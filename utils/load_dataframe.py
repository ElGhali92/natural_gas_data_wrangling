from pathlib import Path

SAVE_DICT = {
    ".csv": "to_csv",
    ".xlsx": "to_excel",
    ".parquet": "to_parquet",
    ".json": "to_json",
}


def save_pd(data, file_path):
    extension = Path(file_path).suffix
    assert extension in SAVE_DICT, f"Only support export in {list(SAVE_DICT.keys())}"
    if extension != ".json":
        exec(f"data.{SAVE_DICT[extension]}('{file_path}', index = False)")
    else:
        exec(f"data.{SAVE_DICT[extension]}('{file_path}')")
