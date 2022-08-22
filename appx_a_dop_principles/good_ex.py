import json
from abc import ABC
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol, Optional, Union


# Python's Protocols are meant only for type checking. They do not function
#   exactly as what is known as "Interfaces"
class IFirstLastName(Protocol):
    first_name: str
    last_name: str


# Interfaces, as known from other languages, is more like ABCs in Python, than
#   Protocols. To make an ABC behave exactly like an interface, we just have to
#   override all of its components by the classes implementing / subclassing
#   it, which is what @abstractmethod's are for.
# Data classes contain only data. Separate code from data (principle 1)
# We set "frozen=True" to make sure the data is immutable (principle 3)
@dataclass(frozen=True)
class AbcPersonData(ABC):
    first_name: str
    last_name: str


@dataclass(frozen=True)
class AuthorData(AbcPersonData):
    nb_books: Optional[int]


@dataclass(frozen=True)
class UserData(AbcPersonData):
    email_address: Optional[str]


class NameCalculator:
    @staticmethod
    def full_name(data: IFirstLastName):
        return data.first_name + " " + data.last_name


class AuthorRater:
    @staticmethod
    def is_prolific(author_data: AuthorData):
        return author_data.nb_books > 100


# Represent data using generic data structures (dict, etc.) (principle 2)
def create_author_data(
    first_name: str, last_name: str, nb_books: Optional[int]
):
    # I don't like it though, as I prefer to have a data Class that enforces
    #   a kind of structure to what the class should have as data fields. Or,
    #   maybe, we can use this to generate data Classes through a factory?
    #
    # From the book:
    #   When using generic data structures, the data model is flexible, and
    #   data is not forced into a specific shape. Data can be created with no
    #   predefined shape, and its shape can be modified at will.
    return {
        "first_name": first_name,
        "last_name": last_name,
        "nb_books": nb_books,
    }


# Separate data schema from data representation (principle 4)
# Here, we should insert a schema validation code, but I think Pydantic does
#   this kind of thing (data validators) in Python.
def json_schema_to_dict(schema_file_path: Union[str, Path]):
    with open(schema_file_path) as schema_file:
        return json.load(schema_file)
