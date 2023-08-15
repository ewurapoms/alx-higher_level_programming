#!/usr/bin/python3
""" script reads stdin line by line and computes metrics"""


def read_stdin(size, status_codes):
    """Displays computed metrics"""

    print("File size: {}".format(size))
    for element in sorted(status_codes):
        print("{}: {}".format(element, status_codes[element]))


if __name__ == "__main__":
    import sys

    size = 0
    total = 0
    status_codes = {}
    possibilities = ['200', '301', '400', '401', '403', '404', '405', '500']

    try:
        for row in sys.stdin:
            if total == 10:
                read_stdin(size, status_codes)
                total = 1
            else:
                total = total + 1

            row = row.split()

            try:
                size += int(row[-1])
            except (IndexError, ValueError):
                pass

            try:
                if row[-2] in possibilities:
                    if status_codes.get(row[-2], -1) == -1:
                        status_codes[row[-2]] = 1
                    else:
                        status_codes[row[-2]] += 1
            except IndexError:
                pass

        read_stdin(size, status_codes)

    except KeyboardInterrupt:
        read_stdin(size, status_codes)
        raise
