# import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# stemming process
sentence = 'Saya Bangga jadi warga nahdlatul ulama'
output   = stemmer.stem(sentence)

print(output)
# Saya
#Bangga
#jadi
#warga
#nahdlatul
#ulama

print(stemmer.stem('Mereka meniru-nirukannya'))
# mereka tiru
