import csv


def find_res(name: str, filename: str) -> str:
    """
    returns the result of the user as:
    Ты получил: <ОЦЕНКА>, за проект - <id>
    :param name:
    :return:
    """

    with open(filename, "r") as f:
        csv.DictReader()
