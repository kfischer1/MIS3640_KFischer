import dbm
import random                           #database demo
ROSTER = ("Beshansky",
          "Collins",
          "Fischer",
          "Giovanucci",
          "Jain",
          "Kim",
          "Lauture",
          "Lee",
          "Maddox",
          "Martinez",
          "Mendez",
          "Oh",
          "Petrone",
          "Posada",
          "Rule",
          "Schilb",
          "Tariq",
          "Wang",
          "Wolf")
# GRADES = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-']
visits = ['0']
db = dbm.open('db_student', 'c')                # c = combo of r/w (is reads and writes)
for student in ROSTER:
    db[student] = random.choice(visits)             #everything is stored as a 'bite' because it is not a .txt file
db(close)
return db

def call(db_name):
    ''' among all names called least times,
    return one randomly.
    
    update database after each call'''

    db = dbm.open(db_name, 'c')


def display_all(db_name):
    '''
    display all names and values
    '''
    db = dbm.open(db_name, 'r')
    for student in 
db.close()