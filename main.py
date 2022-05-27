class Student:
    # [assignment] Skeleton class. Add your code here

    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self):
        print(f"I am {self.name}")

    def change_age(self):
        print(f"I am {self.age}")

    def change_tracks(self):
        print(f"I am now enrolled in {self.tracks}")

    def get_score(self):
        print(f"This is my score {self.score}")


Bob = Student("Bob", 26, ["FE", "BE"], 20.90)
Bob.change_name()
Bob.change_age()
Bob.change_tracks()
Bob.get_score()


Peter = Student("Peter", 34, ["UI/IX", "PHP"], 10.89)
Peter.change_name()
Peter.change_age()
Peter.change_tracks()
Peter.get_score()


# Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# # Expected methods
# Bob.change_name("Peter")
# Bob.change_age(34)
# Bob.add_track("UI/UX")
# Bob.get_score()
