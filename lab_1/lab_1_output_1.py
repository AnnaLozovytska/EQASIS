class User:
    def __init__(self, name, age, gender, height, weight, scores):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.scores = scores

def calculate_score(user):
    total_score = sum(user.scores)
    is_adult = user.age >= 18

    print(f"Name: {user.name}")
    print(f"Age: {user.age}, Adult: {is_adult}")
    print(f"Gender: {user.gender}")
    print(f"Height: {user.height} cm, Weight: {user.weight} kg")
    print(f"Total Score: {total_score}")

# Приклад використання
user = User("John", 25, "Male", 175, 70, [85, 90, 75, 88, 92])
calculate_score(user)
