"""While Loop Examples"""

while True and False:
    print("Text")

running = False
while running:
    running = True
    if running:
        print("Das Programm wird ausgeführt.")
    else:
        print("Das Programm wird nicht ausgeführt.")

running = True
while running:
    running = input("Weitermachen? ")
    if running != False:
        running = True
