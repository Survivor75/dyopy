import os
from contextlib import contextmanager


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir('Dir-One'):
    print(os.listdir())

with change_dir('Dir-Two'):
    print(os.listdir())
