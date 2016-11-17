import csv
import pandas as pd

def read_csv(filepath):
    df = pd.read_csv(filepath, encoding='Shift_JIS')
    return df.columns.tolist(), df.values

def write_csv(header, data, filepath):
    with open(filepath, 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(data)