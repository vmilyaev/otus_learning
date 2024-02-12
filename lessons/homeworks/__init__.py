import os.path


def get_path(filename):
    work_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(work_folder, filename)


BOOKS_CSV = get_path(filename="books.csv")
USERS_JSON = get_path(filename="users.json")
