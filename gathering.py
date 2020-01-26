from glob import glob

# file
GENERAL_PATH = 'C:/Users/admin/Documents/Folder/'

FILE_TO_WRITE_PATH = "C:/Users/admin/Documents/MedVectors/Corpora.txt"
file_to_write = open(FILE_TO_WRITE_PATH, "a+", encoding="utf8")

i = 0
for filename in glob(GENERAL_PATH + '*.json'):
    i += 1
    print("" + i.__str__() + " " + filename)
    file_to_read = open(filename, "r", encoding="utf8")
    original_text = file_to_read.read()
    file_to_write.write(original_text)
