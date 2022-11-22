#!/usr/bin/env python3
# Created By: Jessah
# Date: Nov 22, 2022
# This program lists double digit numbers that sum to 60
# and have a difference of 14
# altered to have user input


def main():
    # get sum and difference from the user
    sum = input("Enter a sum: ")
    diff = input("Enter a difference: ")

    try:  # change str to int
        sum_int = int(sum)
        diff_int = int(diff)
    except Exception:
        print("Invalid input")

    else:
        if sum_int and diff_int >= 0:
            for counter1 in range(10, sum_int):  # for integer one
                for counter2 in range(10, sum_int):  # for integer two
                    if (
                        counter1 + counter2 == sum_int
                        and abs(counter1 - counter2) == diff_int
                    ):
                        print("{} {} ".format(counter1, counter2))
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
