#!/usr/bin/env python3
# Created by: Alex OBrien
# Created on: October 10, 2026
# This program uses an  if..then..elseif..else statement to
# tell the user in they should share, keep, or take
# cookies depending how many they have


def main():
    # Prompt user for the number of cookies and convert input to int
    cookies = int(input("<< How many cookies do you have? : "))

    # Print response to user depending on number given.
    if cookies == 3:
        print(">> Keep your cookies for yourself!")

    elif cookies > 3:
        print(">> Share your cookies with someone else with less than 3 cookies!")

    elif cookies > 0:
        print(">> Find someone with more than 3 cookies who will share with you!")


if __name__ == "__main__":
    main()
