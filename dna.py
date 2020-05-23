import re
from operator import itemgetter

file_path = "D:\\QtProjects\\"
filename = "dna.txt"
frequency = {}
dictionary = {}
k = 3

while True:
    user_input = input("Enter DNA separator k from 1-10 (default 3): ")
    true_input = user_input.strip()
    if true_input.isdigit() and 2 <= int(true_input) <= 10:
        k = int(true_input)
        break
    elif true_input == "":
        break
    else:
        print("Wrong input.")

sequence_f = open(file_path+filename)

dna_string = sequence_f.read()
dna_string = dna_string.replace('\n', '').replace(' ', '')
dna_invalid = re.findall("([^acgt])", dna_string, re.IGNORECASE)

if not dna_invalid:
    words = [dna_string[i:i + k] for i in range(0, len(dna_string), k)]
else:
    print("File contains an invalid DNA sequence. Aborting...")
    exit(1)

sequence_f.close()

for word in words:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

freq_filename = "zipf_freq_" + str(k) + "_words.csv"
freq_file = open(freq_filename, "w")
print("DNA successfully parsed! Writing to " + freq_filename + "...")

for key, value in reversed(sorted(frequency.items(), key=itemgetter(1))):
    freq_file.write(key + "; " + str(value) + "\n")

freq_file.close()
