"""While Loop Examples"""

# Schleife 1: Keine Endlosschleife, Bedingung ist nie erfüllt
while True and False:
    print("Text")

# Schleife 2: Keine Endlosschleife, Bedingung ist nie erfüllt
running = False
while running:
    running = True
    if running:
        print("Das Programm wird ausgeführt.")
    else:
        print("Das Programm wird nicht ausgeführt.")

# Schleife 3: Endlosschleife, input() gibt immer einen String zurück, keinen Boolean
running = True
while running:
    running = input("Weitermachen? ")
    if running != False:
        running = True
