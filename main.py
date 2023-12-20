from Names import names
import random

print(names)
# im.mcko.ru/mo.php

d = dict()

d["test1"] = 10


# https://github.com/Boyarnikov/test_project_for_olimp
# shorturl.at/nqDG1

def generate_dataset(names_):
    n = len(names_)
    data = list()
    project_ids = [i for i in range(n)]
    random.shuffle(project_ids)
    print(project_ids)
    class_letters = "аибыжв"
    class_numbers = ["10", "11"]

    for i in range(n):
        human = dict()
        human["id"] = i
        human["name"] = names_[i]
        human["titleProject_id"] = project_ids[i]
        human["class"] = random.choice(class_numbers) + random.choice(class_letters)
        human["score"] = random.randint(20, 100)
        if random.random() < 0.2:
            human["score"] = "None"
        print(human)

generate_dataset(names)

# id, Name(в формате ФИО), titleProject_id(номер проекта, целое число), class(класс, в
# формате цифра+буква), score(оценки, в формате целого числа или None).
