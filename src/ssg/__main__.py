from invoke.program import Program
from invoke.collection import Collection

from ssg import tasks


def main():
    Program(namespace=Collection.from_module(tasks)).run()


if __name__ == "__main__":
    main()
