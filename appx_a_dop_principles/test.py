import json
from pprint import pprint

import pytest

from dop.appx_a_dop_principles.good_ex import (
    AuthorData,
    NameCalculator,
    create_author_data,
)


class TestAuthor:
    fields: str = "first_name," + "last_name," + "nb_books"
    values: list[tuple[str, str, int]] = [
        ("Luffy", "Uzumaki", 5),
        ("Mhmd", "Jouni", 101),
    ]


@pytest.mark.parametrize(TestAuthor.fields, TestAuthor.values)
def test_full_name(first_name, last_name, nb_books):
    print()

    author_data = AuthorData(
        first_name=first_name, last_name=last_name, nb_books=nb_books
    )
    assert (
        NameCalculator.full_name(data=author_data)
        == first_name + " " + last_name
    )

    print(f"Tested Author:\n"
          f"\t{author_data}")

    print(
        "COMMENTARY:\n"
        "\tHere, the code is tested in isolation without having to load\n"
        "\tunused methods like is_prolific()."
    )


@pytest.mark.parametrize(TestAuthor.fields, TestAuthor.values)
def test_create_author_data(first_name, last_name, nb_books):
    print()

    author_data = create_author_data(
        first_name=first_name, last_name=last_name, nb_books=nb_books
    )

    assert type(author_data) == dict
    assert (
        author_data["first_name"] == first_name
        and author_data["last_name"] == last_name
        and author_data["nb_books"] == nb_books
    )

    print(f"Tested Author:\n"
          f"\t{author_data}")

    print(
        "COMMENTARY:\n"
        "\tTesting the representation of data using generic data structures."
    )


def test_add_author_request_schema():
    print()

    with open('add_author_request_schema.json') as schema_file:
        author_schema = json.load(schema_file)

    pprint(author_schema)
