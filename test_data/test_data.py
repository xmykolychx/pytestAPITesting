from faker import Faker

FAKE = Faker()


class TestData:
    board_name = FAKE.company()
    list_name = FAKE.name()
    label_name = FAKE.job()
    label_colors = ['yellow', 'purple', 'blue', 'red', 'green', 'orange', 'black', 'sky', 'pink', 'lime']
