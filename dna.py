import re
from operator import itemgetter
from PyQt5.QtWidgets import QMessageBox, QApplication

# Message box literals
MSG_SUCCESS = 0
MSG_INPUT_FILE_ERROR = 1
MSG_OUTPUT_FILE_ERROR = 2


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

    frequency = {}
    words = [dna_string[i:i + k] for i in range(0, len(dna_string), k)]

    for word in words:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    freq_file = open(freq_filename, "w")
    print("DNA successfully parsed! Writing to " + freq_filename + "...")

    for key, value in reversed(sorted(frequency.items(), key=itemgetter(1))):
        freq_file.write(key + "; " + str(value) + "\n")

    freq_file.close()


def displayMessage(msgCode):
    msg = QMessageBox()

    if msgCode == MSG_INPUT_FILE_ERROR:
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

    elif msgCode == MSG_SUCCESS:
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Zapis pomyślny")
        msg.setText("Zapisano wyniki generacji do pliku!")

    QApplication.beep()
    msg.exec_()
