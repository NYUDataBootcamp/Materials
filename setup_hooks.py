import os
from shutil import copyfile

if __name__ == '__main__':
    copyfile("./pre-commit.py", ".git/hooks/pre-commit")
