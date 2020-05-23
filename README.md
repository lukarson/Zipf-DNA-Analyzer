# Zipf-DNA-Analyzer
Small Qt app for analyzing the Zipf distribution for k-length words of random DNA sequences.

## Szybki how to uruchomić i testować

Teoretycznie wystarczy sam Python3 i biblioteki pyqt5 + pyqt5-tools, ale polecam Qt Designer i oprócz tego jakiś edytor typu Sublime Text czy Pycharm (lub Qt Creator, który zawiera Qt Designer i od razu pythonowy edytor kodu, ale wsparcie póki co takie sobie).

Czasami może Windows nie widzieć pythona lub bibliotek przy odpalaniu w konsoli cmd, to wystarczy dodać odpowiednią ścieżkę do systemowej PATH.

Instalacja bibliotek: `pip3 install pyqt5 pyqt5-tools`
Uruchomienie: `py main.py`

## Konwersja UI na kod (do testów)

Qt Designer wyrzuca stworzony UI w pliku .ui, żeby przekonwertować na .py wpisujemy:
`pyuic5 -x moje_ui.ui -o kod_w_python.py`