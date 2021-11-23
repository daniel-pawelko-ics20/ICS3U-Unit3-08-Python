#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Nov 2021
# Leap Years


def main():
    # main function for determining leap years

    # asking for input
    try:
        year = input("Please enter the year: ")
        year = int(year)

        # process/output
        if year % 400 == 0:
            print(f"{year} is a Leap Year")
        elif year % 100 == 0:
            print(f"{year} is not a Leap Year")
        elif year % 4 == 0:
            print(f"{year} is a Leap Year")
        else:
            print(f"{year} is not a Leap Year")
    except ValueError:
        print("Input has to be integer")

    # done
    print("\nDone.")


if __name__ == "__main__":
    main()
