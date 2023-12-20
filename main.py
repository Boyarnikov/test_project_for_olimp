from Names import names
import random
import csv
import Names
import generate
import task1

generate.generate_dataset(Names.names)
print(task1.find_res("Ефимов Григорий", "students.csv"))