#!/usr/bin/env python3
"""
Filtered logger
"""
import re
import logging
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(field + "=.*?" + separator,
                         field + "=" + redaction + separator, message)
    return message


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        constructor method for RedactingFormatter class
        """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        format method for RedactingFormatter class
        """
        return filter_datum(
            self.fields,
            self.REDACTION,
            super(RedactingFormatter, self).format(record),
            self.SEPARATOR
        )