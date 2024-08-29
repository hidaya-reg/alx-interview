#!/usr/bin/python3
"""
Log Parsing Script
"""

import sys
import re


def output(log: dict) -> None:
    """
    Helper function to display statistics
    """
    print(f"File size: {log['file_size']}")
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code] > 0:
            print(f"{code}: {log['code_frequency'][code]}")

def initialize_log() -> dict:
    """
    Initializes the log dictionary with default values
    """
    return {
        "file_size": 0,
        "code_frequency": {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    }

if __name__ == "__main__":
    log_pattern = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
    )

    log = initialize_log()
    line_count = 0

    try:
        for line in sys.stdin:
            match = log_pattern.fullmatch(line.strip())
            if match:
                line_count += 1
                code, file_size = match.groups()
                file_size = int(file_size)

                log["file_size"] += file_size
                if code in log["code_frequency"]:
                    log["code_frequency"][code] += 1

                if line_count % 10 == 0:
                    output(log)
    finally:
        output(log)
