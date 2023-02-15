import os
import sys
import glob
import pypff

eml_folder = ''

# Überprüfen, ob ein Ordnerpfad als Argument übergeben wurde
if len(sys.argv) > 1:
    eml_folder = sys.argv[1]

# Überprüfen, ob ein Ordner per Drag and Drop auf das Skript gezogen wurde
elif len(sys.argv) == 1 and os.path.isdir(sys.argv[0]):
    eml_folder = sys.argv[0]

# Aufforderung zur Eingabe des Ordnerpfads, falls kein Argument und kein Drag and Drop erfolgt ist
while not eml_folder or not os.path.isdir(eml_folder):
    eml_folder = input("Bitte geben Sie den Pfad zum EML-Ordner ein: ")

pst_file = os.path.join(eml_folder, 'sonderimport.pst')

pst = pypff.file(pst_file, 'w')

# Schleife durch alle EML-Dateien im Ordner
for eml_file in glob.glob(os.path.join(eml_folder, '*.eml')):
    try:
        with open(eml_file, 'rb') as f:
            eml_data = f.read()
        message = pst.message_add(eml_data)
    except Exception as e:
        with open(os.path.join(eml_folder, 'sonderimport-fehler.log'), 'a') as f:
            f.write(f"Fehler beim Importieren von {eml_file}: {str(e)}\n")

# Speichern und Schließen der PST-Datei
pst.close()