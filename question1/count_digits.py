"""
Write a function, "count_digits," that declares a parameter for a filename. 
The function should count the number of times the digits 0-9 appear in the
file and print the tally for each digit, e.g.:

0 - 791
1 - 758
2 - 813
3 - 791
4 - 774
5 - 775
6 - 825
7 - 768
8 - 815
9 - 790

Your function should gracefully handle errors including file not found and
(print an error message) and non-numeric data (skip it).

Correct answers:
data/digits_1.txt
0 - 9
1 - 8
2 - 4
3 - 9
4 - 6
5 - 6
6 - 11
7 - 11
8 - 10
9 - 5

data/digits_10.txt
0 - 74
1 - 78
2 - 78
3 - 82
4 - 93
5 - 67
6 - 78
7 - 69
8 - 87
9 - 84

data/digits_100.txt
0 - 791
1 - 758
2 - 813
3 - 791
4 - 774
5 - 775
6 - 825
7 - 768
8 - 815
9 - 790

data/digits_100_bad.txt
0 - 761
1 - 755
2 - 799
3 - 778
4 - 771
5 - 734
6 - 758
7 - 719
8 - 749
9 - 732

File not found: data/not_a_file.txt


"""


def count_digits(filename):
    """
    Write a function, "count_digits," that declares a parameter for a filename. 
    The function should count the number of times the digits 0-9 appear in the
    file and print the tally for each digit.
    """
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0

    try:
        with open(filename) as file:
            for line in file:
                for letter in line:
                    if letter == '0':
                        zero += 1
                    elif letter == '1':
                        one += 1
                    elif letter == '2':
                        two += 1
                    elif letter == '3':
                        three += 1
                    elif letter == '4':
                        four += 1
                    elif letter == '5':
                        five += 1
                    elif letter == '6':
                        six += 1
                    elif letter == '7':
                        seven += 1
                    elif letter == '8':
                        eight += 1
                    elif letter == '9':
                        nine += 1

                print("0 - ",zero,"\n1 - ",one, "\n2 - ", two, "\n3 - ", three,
                          "\n4 - ", four, "\n5 - ", five, "\n6 - ", six, "\n7 - ", seven,
                          "\n8 - ", eight, "\n9 - ", nine)

    except FileNotFoundError:
        print("file wasn't found")


def main():
    count_digits("data/digits_1.txt")
    """ Additional Test Cases """
    # count_digits ("data/digits_10.txt")
    # count_digits ("data/digits_100.txt")
    # count_digits ("data/digits_100_bad.txt")
    # count_digits ("data/not_a_file.txt")


if __name__ == "__main__":
    main()
