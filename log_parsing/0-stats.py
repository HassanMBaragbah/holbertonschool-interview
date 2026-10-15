#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics:
- Total file size
- Number of lines by status code
"""

import sys


def print_statistics(total_file_size, status_counts):
    """Prints the accumulated metrics."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    total_file_size = 0
    status_counts = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    valid_codes = list(status_counts.keys())
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 2:
                try:
                    file_size = int(parts[-1])
                    status_code = parts[-2]

                    total_file_size += file_size

                    if status_code in valid_codes:
                        status_counts[status_code] += 1
                except (ValueError, IndexError):
                    pass

            line_count += 1

            if line_count % 10 == 0:
                print_statistics(total_file_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_counts)
        raise

    if line_count % 10 != 0:
        print_statistics(total_file_size, status_counts)
