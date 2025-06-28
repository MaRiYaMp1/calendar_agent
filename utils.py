# backend/utils.py

from datetime import datetime, timezone
from dateutil import parser

def parse_datetime(user_str):
    """
    Try to parse a datetime string from user input into a timezone-aware datetime.
    """
    try:
        dt = parser.parse(user_str)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except (ValueError, OverflowError):
        raise ValueError(f"Could not parse datetime from: {user_str}")

def is_time_range(msg):
    """
    Detect if message includes a time range like '3-5 PM'.
    """
    return '-' in msg and any(p in msg.lower() for p in ['am', 'pm'])

def extract_range(msg):
    """
    Extract start and end from a range string.
    Return (start_str, end_str).
    """
    parts = msg.split('-')
    return parts[0].strip(), parts[1].strip()
