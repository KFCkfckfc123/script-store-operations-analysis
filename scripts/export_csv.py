"""Export workbook tables to CSV, using header names (not column indices).

Reads the published workbook's Raw Data and Script List sheets and writes
data/raw_data.csv and data/script_list.csv. This gives reviewers a plain-text
copy of the same fixture without needing Excel.
"""
import csv
from pathlib import Path
import openpyxl

ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / 'workbook/Script_Store_Operations_Synthetic_Compatible.xlsx'
OUT = ROOT / 'data'
OUT.mkdir(exist_ok=True)

w = openpyxl.load_workbook(FILE, data_only=True)
for sheet, name in [('Raw Data', 'raw_data.csv'), ('Script List', 'script_list.csv')]:
    rows = list(w[sheet].values)
    header = [str(c) if c is not None else '' for c in rows[0]]
    body = [r for r in rows[1:] if r[0] is not None]
    with open(OUT / name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(body)
    print(f'{name}: {len(body)} rows, {len(header)} columns')
