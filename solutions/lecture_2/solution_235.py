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

# Schleife 3: Endlosschleife, input() gibt immer einen String zurück.
# In Python wird jeder nicht-leere String als True evaluiert, auch "False".
# Wird ein leerer String eingegeben, evaluiert running zu False, ...
# ... aber wird danach wieder auf True gesetzt.
running = True
while running:
    running = input("Weitermachen? ")  # string
    if running != False:  # string != bool
        running = True
