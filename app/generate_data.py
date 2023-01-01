from faker import Faker
import random
import string
from classes import AppUsers, AppSecert

fake = Faker()

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for _ in range(length))
    return result_str


def generate_users(count):
    for _ in range(count):
        user = AppUsers(name=fake.name(), login=fake.user_name(), password=get_random_string(32))
        print(user.create_user())
    return None

def generate_secrets(count):
    for _ in range(count):
        secret = AppSecert(name=fake.domain_word(), user_id=random.randint(1, 50), sycret_type=1)
        print(secret.create_secert())
    return None


if __name__ == "__main__":
    generate_users(50)
    #INSERT INTO secret_type(name, sycret_store_type) VALUES (login_password, 1);
    generate_secrets(50)
    pass
