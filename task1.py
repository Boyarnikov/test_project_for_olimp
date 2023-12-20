import csv


def find_res(name: str, filename: str) -> str:
    """
    returns the result of the user as:
    Ты получил: <ОЦЕНКА>, за проект - <id>
    :param name:
    :return:
    """

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, ["id", "name", "titleProject_id", "class", "score"])
        for human in reader:
            if name in human["name"]:
                return f"{human['score']}, за проект - {human['titleProject_id']}"
