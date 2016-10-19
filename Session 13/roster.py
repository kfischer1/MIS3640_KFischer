import random

ROSTER = {"Beshansky": 0,
          "Collins": 0,
          "Fischer": 1,
          "Giovanucci": 0,
          "Jain": 0,
          "Kim": 0,
          "Lauture": 0,
          "Lee": 0,
          "Maddox": 0,
          "Martinez": 0,
          "Mendez": 0,
          "Oh": 0,
          "Petrone": 1,
          "Posada": 0,
          "Rule": 1,
          "Schilb": 0,
          "Tariq": 0,
          "Wang": 0,
          "Wolf": 0}


def call(roster):
    """
    Among the names that are called least times,
    print one name
    roster: a dict of names and integers
    TO-DO: update dict after every call
    TO-DO: save dict to files
    """
    value_list = roster.values()                # makes list of values as the roster values (0 and 1)
    min_value = min(value_list)                 # minimum value of roster values (0)
    
    names = []                                  # creates name list because that is all we need printed
    for name, number in roster.items():
        if number == min_value:
            names.append(name)      # if number is associated with min value (0), the name is added to the list
    return random.choice(names)

print(call(ROSTER))