import os
import calendar
import locale
import shutil
import glob


def create_year_month_folders(year):
    folders = ['Belege', 'Kontrolle Monate']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
    
    # Setze die Sprache auf Deutsch, damit calendar.month_name[month] Deutsche Monatsnamen ausgibt
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

def copy_excel_files(year):
    # Finde Excel-Dateien im aktuellen Verzeichnis
    excel_files = glob.glob("Vorlage*.xlsx") + glob.glob("Vorlage*.xls")
    
    for excel_file in excel_files:
        # Zielverzeichnis für Belege und Kontrolle
        destination_kontrolle = os.path.join("Kontrolle Monate", str(year))

        # Überprüfe, ob die Datei bereits im Zielordner vorhanden ist
        #file_exists_belege = os.path.exists(os.path.join(destination_belege, excel_file.replace('Vorlage', '')))
        file_exists_kontrolle = os.path.exists(os.path.join(destination_kontrolle, excel_file.replace('Vorlage ', '')))


        # Kopiere Excel-Datei in das Kontrolle-Verzeichnis
        if not file_exists_kontrolle:
            if not os.path.exists(destination_kontrolle):
                os.makedirs(destination_kontrolle)
            new_name = os.path.join(destination_kontrolle, excel_file.replace('Vorlage ', ''))
            shutil.copy(excel_file, new_name)
            print(f"Excel-Dateien {new_name} wurde in den Jahresordner für Kontrolle kopiert.")

def main():
    try:
        year = int(input("Bitte geben Sie das gewünschte Jahr ein: "))
        create_year_month_folders(year)
        print(f"Ordnerstruktur für das Jahr {year} wurde erstellt.")
        copy_excel_files(year)
    except ValueError:
        print("Ungültige Eingabe für das Jahr. Bitte geben Sie eine gültige Jahreszahl ein.")

if __name__ == "__main__":
    main()
