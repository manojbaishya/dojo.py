import os


def general_os_functions():
    get_environment_variables()

    for path in get_environment_path():
        print(path)


def get_environment_variables():
    for key in os.environ:
        print(f"{key}: {os.environ[key]}")


def get_environment_path():
    return os.environ["PATH"].split(";")
