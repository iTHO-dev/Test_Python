import os
import calendar
import locale


def create_year_month_folders(year):
    folders = ['Belege', 'Kontrolle Monate']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
    
        # Setze die Sprache auf Deutsch
    locale.setlocale(locale.LC_TIME, "de_DE.UTF-8")

    for folder in folders:
        year_folder_path = os.path.join(folder, str(year))
        if not os.path.exists(year_folder_path):
            os.makedirs(year_folder_path)
        
        for month in range(1, 13):
            month_name = f'{month:02d}'  # Formatierung für zweistellige Monatsnummern (z.B. 01, 02, ..., 12)
            month_name = month_name + ' ' + calendar.month_name[month]
            month_folder_path = os.path.join(year_folder_path, month_name)
            if not os.path.exists(month_folder_path):
                os.makedirs(month_folder_path)
                print(f"Monatsordner {month_folder_path} wurde erstellt.")

def main():
    try:
        year = int(input("Bitte geben Sie das gewünschte Jahr ein: "))
        create_year_month_folders(year)
        print(f"Ordnerstruktur für das Jahr {year} wurde erstellt.")
    except ValueError:
        print("Ungültige Eingabe für das Jahr. Bitte geben Sie eine gültige Jahreszahl ein.")

if __name__ == "__main__":
    main()
