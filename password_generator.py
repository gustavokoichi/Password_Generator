import argparse
import random
import string
import sys


def read_user_cli_args():
    """ 
    Handle user CLI interations

    "length": Argument to password's length
    "-u": Argument to upper
    "-n": Argument to Number
    "-s": Argument to special character
    """

    parser = argparse.ArgumentParser(description="Generates a random password.")

    parser.add_argument(
        "length",
        type=int,
        help="Enter length between 8 and 16 characters",
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


def build_random_password(length=int, upper=False, numbers=False, special=False):
    if 8 <= length <= 16:
        if upper is numbers is special is False: #LOWERCASE
            all_lower = string.ascii_lowercase
            result = "".join(random.choice(all_lower) for i in range(length))
        elif upper is True and numbers is special is False: #with UPPER
            with_upper = string.ascii_letters
            result = "".join(random.choice(with_upper) for i in range(length))
        elif numbers is True and upper is special is False: #with NUMBERS
            with_numbers = string.ascii_lowercase + string.digits
            result = "".join(random.choice(with_numbers) for i in range(length))
        elif upper is numbers is True and special is False: #UPPER + NUMBERS
            with_upper_numbers = string.ascii_letters + string.digits
            result = "".join(random.choice(with_upper_numbers) for i in range(length))
        elif numbers is special is True and upper is False:
            with_numbers_special = string.digits + string.punctuation
            result = "".join(random.choice(with_numbers_special) for i in range(length))
        elif special is True and upper is numbers is False: #with SPECIAL
            with_special = string.ascii_lowercase + string.punctuation
            result = "".join(random.choice(with_special) for i in range(length))
        elif upper is special is True and numbers is False: #UPPER + SPECIAL
            with_upper_special = string.ascii_letters + string.punctuation
            result = "".join(random.choice(with_upper_special) for i in range(length))
        elif upper is numbers is special is True:
            all_included = string.ascii_letters + string.digits + string.punctuation
            result = "".join(random.choice(all_included) for i in range(length))
    else:
        result = sys.exit("Password needs to be between 8 and 16 characters. Finishing program!")
    return result


if __name__ == "__main__":
    user_args = read_user_cli_args()
    random_password = build_random_password(user_args.length, user_args.upper, user_args.numbers, user_args.special)
    print(random_password)
    