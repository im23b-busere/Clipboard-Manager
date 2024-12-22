
# Clipboard Manager

## Bist du müde, deine kopierten Texte zu verlieren?

Hast du schon einmal einen wichtigen Text kopiert und ihn dann verloren, weil du etwas anderes kopiert hast? Verabschiede dich vom Chaos in deiner Zwischenablage mit dem **Clipboard Manager**! Diese simple Python-Anwendung hilft dir, deine Zwischenablage zu verwalten, indem sie kopierte Texte speichert und dir ermöglicht, diese schnell wiederzuverwenden.


<img src="https://github.com/user-attachments/assets/14a2ce2b-96dc-42f2-91d6-71d67eaaf75a" alt="Clipboard Manager Screenshot" width="500"/>




## Inhaltsverzeichnis

- [Features](#features)
- [Anforderungen](#anforderungen)
- [Installation](#installation)
- [Verwendung](#verwendung)
- [Autor](#autor)

## Features

- **Zwischenablage-Überwachung**: Automatisches Protokollieren neuer Einträge in der Zwischenablage.
- **Verlauf-Anzeige**: Zeigt den neuesten kopierten Text in einem scrollbaren Textfeld an.

## Anforderungen

Zum Ausführen dieses Projekts benötigst du:

- Python 3.x
- Die **customtkinter**-Bibliothek für die grafische Benutzeroberfläche
- Die **pyperclip**-Bibliothek für die Zwischenablage-Operationen
- **keyboard** für Tastenkombinationen

## Installation

1. Klone das Repository:
   ```bash
   git clone https://github.com/dein-benutzername/clipboard-manager.git
   cd clipboard-manager
   ```

2. Installiere die benötigten Pakete:
   ```bash
   pip install -r requirements.txt
   ```

## Verwendung

1. Führe das Skript im Terminal oder der Kommandozeile aus:
   ```bash
   python main.py
   ```

2. Die Anwendung startet und überwacht deine Zwischenablage.
3. Verwende `Ctrl + C`, um die Zwischenablage zu aktivieren und Text zu speichern.
4. Der Verlauf wird in der Anwendung angezeigt, und du kannst Einträge zurück in die Zwischenablage kopieren.

## Autor

**[im23b-busere](https://github.com/im23b-busere)**  
Feedback oder Vorschläge? Öffne ein Issue oder erstelle einen Pull-Request!
