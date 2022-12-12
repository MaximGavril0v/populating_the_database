from random import *
from faker import Faker
from collections import defaultdict

fake = Faker()


def acting():
    fake_data = defaultdict(list)
    fkey_set = set(tuple())
    for i in range(3000):
        fkey_set.add((randint(0, 99), randint(0, 99)))
    for _ in range(len(fkey_set)):
        pair = fkey_set.pop()
        fake_data["mov_id"].append(pair[0])
        fake_data["act_id"].append(pair[1])
    return fake_data


def use():
    fake_data = defaultdict(list)
    fkey_set = set(tuple())
    for i in range(1000):
        fkey_set.add((randint(0, 99), randint(0, 99)))
    for _ in range(100):
        fake_data["user_id"].append(fkey_set.pop()[0])
        fake_data["lang_id"].append(fkey_set.pop()[1])
    return fake_data


def watch():
    fake_data = defaultdict(list)
    fkey_set = set(tuple())
    for i in range(3000):
        fkey_set.add((randint(0, 99), randint(0, 99)))
    for _ in range(len(fkey_set)):
        pair = fkey_set.pop()
        fake_data["user_id"].append(pair[0])
        fake_data["mov_id"].append(pair[1])
    return fake_data



def chose():
    fake_data = defaultdict(list)
    fkey_set = set(tuple())
    for i in range(1000):
        fkey_set.add((randint(0, 99), randint(0, 99)))
    for _ in range(100):
        fake_data["cur_id"].append(fkey_set.pop()[0])
        fake_data["sub_id"].append(fkey_set.pop()[1])
    return fake_data


def create1():
    fake_data = defaultdict(list)
    fkey_set = set(tuple())
    for i in range(3000):
        fkey_set.add((randint(0, 99), randint(0, 99)))
    for _ in range(len(fkey_set)):
        pair = fkey_set.pop()
        fake_data["prod_id"].append(pair[0])
        fake_data["mov_id"].append(pair[1])
    return fake_data


def create2_():
    fake_data = defaultdict(list)
    fkey_set = set(tuple())
    for i in range(1000):
        fkey_set.add((randint(0, 99), randint(0, 99)))
    for _ in range(100):
        fake_data["pc_id"].append(fkey_set.pop()[0])
        fake_data["mov_id"].append(fkey_set.pop()[1])
    return fake_data


def dubbed():
    fake_data = defaultdict(list)
    fkey_set = set(tuple())
    for i in range(1000):
        fkey_set.add((randint(0, 99), randint(0, 99)))
    for _ in range(100):
        a = fake.boolean()
        b = fake.boolean()
        if (a == False and b == False):
            continue
        fake_data["subtitles"].append(a)
        fake_data["audio"].append(b)
        fake_data["lang_id"].append(fkey_set.pop()[0])
        fake_data["mov_id"].append(fkey_set.pop()[1])
    return fake_data


def get_():
    fake_data = defaultdict(list)
    fkey_set = set(tuple())
    for i in range(1000):
        fkey_set.add((randint(0, 99), randint(0, 99)))
    for _ in range(100):
        fake_data["start_date"].append(fake.date())
        fake_data["way_of_payment"].append(choice(["Qiwi", "PayPal", "Card"]))
        fake_data["auto_renewal"].append(fake.boolean())
        fake_data["end_date"].append(fake.date())
        fake_data["user_id"].append(fkey_set.pop()[0])
        fake_data["sub_id"].append(fkey_set.pop()[1])
    return fake_data


def having_():
    fake_data = defaultdict(list)
    fkey_set = set(tuple())
    for i in range(1000):
        fkey_set.add((randint(0, 99), randint(0, 99)))
    for _ in range(100):
        fake_data["year_"].append(randint(1975, 2021))
        fake_data["prod_id"].append(fkey_set.pop()[0])
        fake_data["awards_id"].append(fkey_set.pop()[1])
    return fake_data


def include_():
    fake_data = defaultdict(list)
    fkey_set = set(tuple())
    for i in range(1000):
        fkey_set.add((randint(0, 99), randint(0, 99)))
    for _ in range(100):
        fake_data["sub_id"].append(fkey_set.pop()[0])
        fake_data["mov_id"].append(fkey_set.pop()[1])
    return fake_data


def play():
    fake_data = defaultdict(list)
    fkey_set = set(tuple())
    for i in range(1000):
        fkey_set.add((randint(0, 99), randint(0, 99)))
    for _ in range(100):
        fake_data["vr_id"].append(choice([0, 1, 2, 3]))
        fake_data["mov_id"].append(fkey_set.pop()[1])
    return fake_data


def add_():
    fake_data = defaultdict(list)
    fkey_set = set(tuple())
    for i in range(3000):
        fkey_set.add((randint(0, 99), randint(0, 99)))
    for _ in range(1000):
        fake_data["listname"].append(fake.word())
        fake_data["mov_id"].append(fkey_set.pop()[0])
        fake_data["user_id"].append(fkey_set.pop()[1])
    return fake_data

def related1():
    fake_data = defaultdict(list)
    fkey_set = set(tuple())
    for i in range(1000):
        fkey_set.add((choice(range(1, 9)), randint(0, 99)))
    for _ in range(100):
        fake_data["g_id"].append(fkey_set.pop()[0])
        fake_data["mov_id"].append(fkey_set.pop()[1])
    return fake_data


def related2():
    fake_data = defaultdict(list)
    fkey_set = set(tuple())
    for i in range(1000):
        fkey_set.add((choice(range(0, 3)), randint(0, 99)))
    for _ in range(100):
        fake_data["c_id"].append(fkey_set.pop()[0])
        fake_data["mov_id"].append(fkey_set.pop()[1])
    return fake_data


def category():
    fake_data = defaultdict(list)
    fake_data["c_name"].append("feature film")
    fake_data["c_name"].append("short film")
    fake_data["c_name"].append("series")
    return fake_data


def currency():
    fake_data = defaultdict(list)
    for _ in range(100):
        fake_data["cur_name"].append(fake.currency()[0])
    return fake_data


def director():
    fake_data = defaultdict(list)
    for _ in range(100):
        fake_data["dir_name"].append(fake.name())
    return fake_data


def director_awards():
    fake_data = defaultdict(list)
    for i in range(1975, 2022):
        fake_data["award_year"].append(i)
        fake_data["award_year"].append(i)
        fake_data["award_year"].append(i)
        fake_data["awards_name"].append("Oscar")
        fake_data["awards_name"].append("BAFTA")
        fake_data["awards_name"].append("Golden Globe")
    return fake_data


def film():
    fake_data = defaultdict(list)
    for _ in range(100):
        fake_data["rate"].append(randint(10, 100) / 10)
        fake_data["film_name"].append(fake.word())
        fake_data["storyline"].append(fake.text())
        fake_data["age_limit"].append(choice(["G", "PG", "PG-13", "R"]))
        fake_data["released_data"].append(fake.date())
        fake_data["country_of_origin"].append(fake.country())
        fake_data["trailer"].append(fake.url())
    return fake_data


def genre():
    fake_data = defaultdict(list)
    fake_data["g_name"].append("Action")
    fake_data["g_name"].append("Comedy")
    fake_data["g_name"].append("Drama")
    fake_data["g_name"].append("Fantasy")
    fake_data["g_name"].append("Horror")
    fake_data["g_name"].append("Mystery")
    fake_data["g_name"].append("Romance")
    fake_data["g_name"].append("Thriller")
    fake_data["g_name"].append("Western")
    return fake_data


def languages():
    fake_data = defaultdict(list)
    languages_set = set()
    for _ in range(10000):
        languages_set.add(fake.language_name())
    for i in range(len(languages_set)):
        fake_data["lang_name"].append(languages_set.pop())
    return fake_data


def production_company():
    fake_data = defaultdict(list)
    for _ in range(100):
        a = fake.words(2)
        b = a[0]
        c = a[1]
        fake_data["pc_name"].append(b + ' ' + c)
    return fake_data


def sub():
    fake_data = defaultdict(list)
    for _ in range(100):
        fake_data["sub_last"].append(fake.time())
        fake_data["sub_name"].append(fake.word())
    return fake_data


def user_():
    fake_data = defaultdict(list)
    for _ in range(100):
        fake_data["user_password"].append(fake.word() + fake.word())
        fake_data["login"].append(fake.word())
        fake_data["country"].append(fake.country())
        fake_data["cur_id"].append(randint(0, 100))
    return fake_data


def review():
    fake_data = defaultdict(list)
    fkey_set = set(tuple())
    for i in range(1000):
        fkey_set.add((randint(0, 99), randint(0, 99)))
    for _ in range(100):
        fake_data["summary"].append(fake.text())
        fake_data["rate"].append(randint(1, 10))
        fake_data["date"].append(fake.date())
        fake_data["mov_id"].append(fkey_set.pop()[0])
        fake_data["user_id"].append(fkey_set.pop()[1])
    return fake_data


def rate_review():
    fake_data = defaultdict(list)
    fkey_set = set(tuple())
    for i in range(1000):
        fkey_set.add((randint(0, 99), randint(0, 99)))
    for _ in range(100):
        fake_data["rrate"].append(randint(1, 10))
        fake_data["rev_id"].append(fkey_set.pop()[0])
        fake_data["user_id"].append(fkey_set.pop()[1])
    return fake_data


def video_resolution():
    fake_data = defaultdict(list)
    fake_data["vr_name"].append("4K")
    fake_data["vr_name"].append("2K")
    fake_data["vr_name"].append("FULL HD")
    fake_data["vr_name"].append("HD")
    return fake_data
