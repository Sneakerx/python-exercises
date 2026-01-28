"""What is the output of the following code?"""


class Tier:
    def __init__(self, name):
        self.name = name
        self.tierart = "Tier"

    def __str__(self):
        return f"{self.name} ist ein {self.tierart}."

    def reden(self):
        print("...")


class Hund(Tier):
    def __init__(self, name):
        self.name = name
        self.tierart = "Hund"

    def reden(self):
        print("Wuff, wuff!")


class Ente(Tier):
    pass


class Robbe(Tier):
    def __init__(self, name):
        super().__init__(name)
        self.tierart = "Robbe"

    def reden(self):
        print("Ow, ow!")


benni = Tier("Benni")
maya = Hund("Maya")
robin = Robbe("Robin")
darkwing = Ente("Darkwing")

print(benni)
print(maya)
print(robin)
print(darkwing)
benni.reden()
robin.reden()
darkwing.reden()
maya.reden()
