from tinydb import TinyDB, Query
from datetime import date

db = TinyDB('db.json')
today = date.today()

User = Query()

weight = input('What is your todays weight? ')
db.insert({'weight': float(weight), 'date': str(today)})

currentWeight = float(500)

for key in db.search(User.weight):
    print(f"-----------{key['date']}-----------\n")
    whatToPrint = '     ⇩' if (key['weight'] < currentWeight) else '     ⇧'
    print(key['weight'], whatToPrint, '\n\n')
    currentWeight = key['weight']
