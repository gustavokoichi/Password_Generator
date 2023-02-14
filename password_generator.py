import argparse


def read_user_cli_args():
    """ """

    parser = argparse.ArgumentParser(
        description="Generates a random password."
    )

    parser.add_argument(
        "lenght",
        type=int,
        help="Enter lenght between 8 and 16 characters",
    )

    parser.add_argument(
        "-u",
        "--upper",
        action="store_true",
        help="Add upper letters",
    )

    parser.add_argument(
        "-n",
        "--numbers",
        action="store_true",
        help="Add numbers",
    )

    parser.add_argument(
        "-s",
        "--special",
        action="store_true",
        help="Add 1 special character",
    )
    return parser.parse_args()


if __name__ == "__main__":
    user_args = read_user_cli_args()
    print(user_args.lenght, user_args.upper, user_args.numbers, user_args.special)