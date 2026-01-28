"""Create class Person and subclass Student with specific methods and attributes.
A person can celebrate a birthday to change their age. A student has an additional
attribute matrikelnummer and a method to study, which checks if the student is
below a certain age limit."""


class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def geburtstag_feiern(self):
        self.alter += 1
        print(f"Herzlichen Glückwunsch zum {self.alter}. Geburtstag, {self.name}!")

    def ausweis_faelschen(self, neues_alter):
        self.alter += neues_alter
        print(f"Herzlichen Glückwunsch zum {self.alter}. Geburtstag, {self.name}!")


class Student(Person):
    altersgrenze = 40

    def __init__(self, name, alter, matrikelnummer):
        super().__init__(name, alter)
        self.matrikelnummer = matrikelnummer

    def studieren(self):
        if self.alter <= self.altersgrenze:
            print(
                f"Student {self.name} mit Matrikelnummer {self.matrikelnummer} studiert."
            )
        else:
            print(f"Student {self.name} ist zu alt zum studieren.")


peter = Person("Peter", 25)
lisa = Student("Lisa", 39, "A12345")
hans = Student(matrikelnummer="1234", name="Hans", alter=41)

peter.geburtstag_feiern()
lisa.geburtstag_feiern()
lisa.studieren()
lisa.geburtstag_feiern()
lisa.studieren()
hans.studieren()
hans.ausweis_faelschen(-10)
hans.studieren()
