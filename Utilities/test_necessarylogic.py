import random

from faker import Faker

fakename = Faker()























def randomemail():
    male = fakename.first_name_male()
    no = random.randint(1, 1000)
    email = f"{male}{no}@gmail.com"
    return email






