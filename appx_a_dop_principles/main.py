from dop.appx_a_dop_principles.bad_ex import Author
from dop.appx_a_dop_principles.good_ex import AuthorData, NameCalculator, UserData


def main():
    print("Executing bad example from main:")
    bad_author = Author(first_name="Isaac", last_name="Asimov", nb_books=500)
    print(bad_author.full_name)

    print()

    print("Executing good example from main:")
    good_author = AuthorData(
        first_name="Isaac", last_name="Asimov", nb_books=500
    )
    print(NameCalculator.full_name(good_author))

    good_user = UserData(
        first_name="Luffy",
        last_name="Uzumaki",
        email_address="luffy.uzumaki@ani.me",
    )
    print(NameCalculator.full_name(good_user))


if __name__ == "__main__":
    main()
