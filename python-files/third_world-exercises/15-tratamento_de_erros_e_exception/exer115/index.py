from lib.layout import data
from lib.data import existFile, creatFile

file = 'database.txt'

if not existFile(file):
    creatFile(file)

# Main code:
data()
