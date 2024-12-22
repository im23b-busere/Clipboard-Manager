
# Clipboard Manager

## Bist du müde, deine kopierten Texte zu verlieren?

Hast du schon einmal einen wichtigen Text kopiert und ihn dann verloren, weil du etwas anderes kopiert hast? Verabschiede dich vom Chaos in deiner Zwischenablage mit dem **Clipboard Manager**! Diese einfache Anwendung hilft dir, deine Zwischenablage zu verwalten, indem sie kopierte Texte speichert und dir ermöglicht, diese schnell wiederzuverwenden.

<img src="https://github.com/user-attachments/assets/14a2ce2b-96dc-42f2-91d6-71d67eaaf75a" alt="Clipboard Manager Screenshot" width="500"/>

---

## Inhaltsverzeichnis

- [Features](#features)
- [Anforderungen](#anforderungen)
- [Installation](#installation)
- [Verwendung](#verwendung)
- [Autor](#autor)

---

## Features

- **Zwischenablage-Überwachung**: Automatisches Protokollieren neuer Einträge in der Zwischenablage.
- **Verlauf-Anzeige**: Zeigt den neuesten kopierten Text in einem scrollbaren Textfeld an.
- **Einträge kopieren**: Kopiere jeden Eintrag im Verlauf bequem zurück in die Zwischenablage.
- **Alle Einträge löschen**: Lösche die gesamte Verlaufsanzeige mit einem Klick.

---

## Anforderungen

Falls du die Python-Version verwenden möchtest, benötigst du:
- Python 3.x
- Die Bibliotheken aus der `requirements.txt`:
  - `customtkinter`
  - `pyperclip`
  - `keyboard`

---

## Installation

### Option 1: Verwende die ausführbare Datei (`main.exe`)

1. Lade die neueste Version von [Releases](https://github.com/im23b-busere/Clipboard-Manager/releases) herunter.
2. Öffne die Datei `main.exe`, um die Anwendung zu starten – keine Installation notwendig!

### Option 2: Starte das Python-Skript

1. Klone das Repository:
   ```bash
   git clone https://github.com/dein-benutzername/clipboard-manager.git
   cd clipboard-manager
   ```

2. Installiere die benötigten Pakete:
   ```bash
   pip install -r requirements.txt
   ```

3. Starte die Anwendung:
   ```bash
   python main.py
   ```

---

## Verwendung

1. Starte die Anwendung (entweder `main.exe` oder `python main.py`).
2. Die Anwendung überwacht automatisch deine Zwischenablage:
   - Kopiere Text mit `Ctrl + C`, um ihn zu speichern.
   - Der Verlauf wird in der Anwendung angezeigt.
3. Klicke auf **"Copy"**, um einen Eintrag zurück in die Zwischenablage zu kopieren.
4. Klicke auf **"Clear All"**, um den gesamten Verlauf zu löschen.
5. Beende die Anwendung mit der Taste `Esc`.

---

## Autor

**[im23b-busere](https://github.com/im23b-busere)**  
Feedback oder Vorschläge? Öffne ein Issue oder erstelle einen Pull-Request!
