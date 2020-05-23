import re
from operator import itemgetter


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
