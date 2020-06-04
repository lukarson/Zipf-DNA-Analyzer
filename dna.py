from PyQt5.QtWidgets import QMessageBox, QApplication
from operator import itemgetter
import re
import os

# Message box literals
MSG_SUCCESS = 0
MSG_INPUT_FILE_ERROR = 1
MSG_OUTPUT_FILE_ERROR = 2
MSG_INVALID_PATH = 3
MSG_ILLEGAL_CHARS = 4
MSG_FILE_EXISTS = 5


def parseFile(file_path):
    sequence_f = open(file_path)

    dna_string = sequence_f.read()
    dna_string = dna_string.replace('\n', '').replace(' ', '')
    dna_invalid = re.findall("([^acgt])", dna_string, re.IGNORECASE)

    if dna_invalid:
        return None

    sequence_f.close()
    return dna_string


def generateZipfDistribution(dna_string, freq_filename, k):
    frequency, zipfRanks = {}, {}
    rank = 0
    words = [dna_string[i:i + k] for i in range(0, len(dna_string), k)]

    for word in words:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    freq_file = open(freq_filename, "w")
    print("DNA successfully parsed! Writing to " + freq_filename + "...")

    for key, value in reversed(sorted(frequency.items(), key=itemgetter(1))):
        if len(key) != k:
            continue
        rank += 1
        zipfRanks[rank] = value
        freq_file.write(key + "; " + str(value) + "\n")

    freq_file.close()

    return zipfRanks


def isOutputFileValid(filepath):
    illegalChars = [":", "<", ">", "?", "*", "|", "\""]

    # Check if field is empty
    if filepath.replace(' ', '') == "":
        displayMessage(MSG_INVALID_PATH)
        return False

    path = "/".join(filepath.split("/")[0:-1])
    path_exists = os.path.exists(path)
    file_exists = os.path.isfile(filepath)

    # Check if given path exists
    if not path_exists:
        displayMessage(MSG_INVALID_PATH)
        return False

    # The file doesn't exist
    if not file_exists:
        filename = filepath.split(path + "/")[-1]

        # If only dir path given or a file with no csv extension
        if filename.split(".")[-1] != "csv":
            displayMessage(MSG_OUTPUT_FILE_ERROR)
            return False

        # Check for illegal characters:
        for char in illegalChars:
            if char in filename:
                displayMessage(MSG_ILLEGAL_CHARS)
                return False

    # The file exists
    else:
        if not displayMessage(MSG_FILE_EXISTS):
            return False

    return True

def displayMessage(msgCode):
    msg = QMessageBox()

    if msgCode == MSG_SUCCESS:
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Zapis pomyślny")
        msg.setText("Zapisano wyniki generacji do pliku!")

    elif msgCode == MSG_INPUT_FILE_ERROR:
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Plik zawiera nieprawidłową sekwencję DNA. "
                    "Sprawdź poprawność podanego pliku.")
        msg.setInformativeText('Dopuszczalne małe/duże litery A,C,G,T oraz białe znaki.')
        msg.setWindowTitle("Błąd pliku z sekwencją")

    elif msgCode == MSG_OUTPUT_FILE_ERROR:
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Niepoprawne rozszerzenie pliku wyjściowego.")
        msg.setInformativeText("Plik musi mieć nazwę i być w formacie .csv.")
        msg.setWindowTitle("Błąd pliku wyjściowego")

    elif msgCode == MSG_INVALID_PATH:
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Błąd zapisu")
        msg.setText("Podana ścieżka nie istnieje!")

    elif msgCode == MSG_ILLEGAL_CHARS:
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Błąd zapisu")
        msg.setText("Nazwa pliku nie może zawierać znaków < > : ? * | \"")

    elif msgCode == MSG_FILE_EXISTS:
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle("Plik istnieje")
        msg.setText("Plik o podanej ścieżce i nazwie już istnieje. Nadpisać?")
        msg.setStandardButtons(msg.Yes | msg.No)
        buttonY = msg.button(msg.Yes)
        buttonY.setText("Tak")
        buttonN = msg.button(msg.No)
        buttonN.setText("Nie")
        QApplication.beep()
        msg.exec_()

        if msg.clickedButton() == buttonY:
            return True
        else:
            return False

    QApplication.beep()
    msg.exec_()
