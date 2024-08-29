#!/usr/bin/python3

"""
    reads stdin line by line and computes metrics
"""

import sys
import signal


def print_stats(total_size, status_counts):
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

def process_line(line, total_size, status_counts):
    try:
        parts = line.split()
        if len(parts) < 7:
            return total_size, status_counts

        file_size = int(parts[-1])
        status_code = int(parts[-2])

        if status_code in status_counts:
            status_counts[status_code] += 1
        total_size += file_size
    except (ValueError, IndexError):
        pass
    return total_size, status_counts

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    def handle_interrupt(signal, frame):
        print_stats(total_size, status_counts)
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_interrupt)

    try:
        for line in sys.stdin:
            total_size, status_counts = process_line(line, total_size, status_counts)
            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
    except BrokenPipeError:
        pass

    print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
