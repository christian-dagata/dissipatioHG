import string

try:
    file1 = open("/Users/chris/Documents/Articoli/Morselli/Diario - Guido Morselli.txt")
    file2 = open("/Users/chris/Documents/Articoli/Morselli/Dissipatio H.G_ - Guido Morselli.txt")
except FileNotFoundError:
    print("Sorry that file doesn't exist")
    exit()
 
punteggiatura = '''!@#$%^&*(){}[]|._-`/?:;"’'\,~«»'''

file1 = file1.read().translate(str.maketrans(punteggiatura, ' '*len(punteggiatura)))
file2 = file2.read().translate(str.maketrans(punteggiatura, ' '*len(punteggiatura)))
file1_words = set()
file2_words = set()

for word in file1.split():

    file1_words.add(word.lower())

for word in file2.split():

    file2_words.add(word.lower())


common_words = file1_words.intersection(file2_words)


merge_file = open("/Users/chris/Documents/Articoli/Morselli/merge.txt", mode="w")

for word in sorted(common_words):
    word = word + ", "
    merge_file.write(word)

merge_file.close()
