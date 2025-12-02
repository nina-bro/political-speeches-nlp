import xml.etree.ElementTree as ET
import csv
import re

def extract_speeches_from_xml(xml_file, output_csv):
    """
    Extrahiert Reden aus einer Bundestags-XML-Datei und speichert sie als CSV.
    
    Args:
        xml_file: Pfad zur XML-Eingabedatei
        output_csv: Pfad zur CSV-Ausgabedatei
    """
    # XML-Datei parsen
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # CSV-Datei vorbereiten
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        
        # Header schreiben
        writer.writerow(['rede_id', 'redner_vorname', 'redner_nachname', 'fraktion', 'fliesstext'])
        
        # Alle <rede> Elemente durchgehen
        for rede in root.findall('.//rede'):
            # Rede-ID extrahieren
            rede_id = rede.get('id', '')
            
            # Redner-Informationen extrahieren
            redner = rede.find('.//redner')
            vorname = ''
            nachname = ''
            fraktion = ''
            
            if redner is not None:
                name = redner.find('.//name')
                if name is not None:
                    vorname_elem = name.find('vorname')
                    nachname_elem = name.find('nachname')
                    vorname = vorname_elem.text if vorname_elem is not None else ''
                    nachname = nachname_elem.text if nachname_elem is not None else ''
                
                fraktion_elem = redner.find('.//fraktion')
                fraktion = fraktion_elem.text if fraktion_elem is not None else ''
            
            # Alle Paragraphen sammeln (nur <p> Elemente, keine Kommentare)
            paragraphs = []
            for p in rede.findall('.//p'):
                # Nur Paragraphen mit klasse != "kommentar" nehmen
                klasse = p.get('klasse', '')
                if 'kommentar' not in klasse.lower() and klasse != 'redner' and klasse != "J_1":
                    # Text aus dem Paragraph extrahieren
                    text = ''.join(p.itertext()).strip()
                    # Überflüssige Whitespaces entfernen
                    text = re.sub(r'\s+', ' ', text)
                    if text:
                        paragraphs.append(text)
            
            # Fließtext zusammensetzen
            fliesstext = ' '.join(paragraphs)
            
            # Zeile in CSV schreiben
            writer.writerow([rede_id, vorname, nachname, fraktion, fliesstext])
    
    print(f"Erfolgreich {len(root.findall('.//rede'))} Reden extrahiert und in {output_csv} gespeichert.")

# Beispielaufruf
if __name__ == "__main__":
    extract_speeches_from_xml('plenarprotokoll.xml', 'reden.csv')
