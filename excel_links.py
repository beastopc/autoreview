import os
import csv
from openpyxl import load_workbook

def check_linked_excel_files(path):
    results = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.xlsx') or filename.endswith('.xlsm'):
                file_path = os.path.join(dirpath, filename)
                wb = load_workbook(file_path, read_only=True)
                linked_files = []
                for sheet in wb.worksheets:
                    for name, link in sheet.external_links.items():
                        if link.Target.endswith('.xlsx') or link.Target.endswith('.xlsm'):
                            linked_files.append(link.Target)
                if linked_files:
                    results.append((file_path, ';'.join(linked_files)))
    return results

def save_results_to_csv(results, output_file):
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['File Path', 'Linked Excel Files'])
        writer.writerows(results)

# Example usage:
results = check_linked_excel_files('/path/to/directory')
save_results_to_csv(results, 'output.csv')
