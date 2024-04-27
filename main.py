import pandas as pd
from tkinter import filedialog
import json

def excel_to_json_grouped():
    excel_file = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if not excel_file:
        print("Excel dosyası seçilmedi.")
        return

    df = pd.read_excel(excel_file)

    grouped_data = {}
    for index, row in df.iterrows():
        sondaj_no = row['SondajNo']
        if sondaj_no not in grouped_data:
            grouped_data[sondaj_no] = []
        grouped_data[sondaj_no].append(row.drop('SondajNo').to_dict())

    output_data = {}
    for sondaj_no, values in grouped_data.items():
        output_data[sondaj_no] = values

    output_file = "veriler.json"
    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=4)

    print("JSON verileri başarıyla", output_file, "adlı dosyaya yazıldı.")


excel_to_json_grouped()
