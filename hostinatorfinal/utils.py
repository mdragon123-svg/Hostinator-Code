"""
Utility functions for the application
"""
from datetime import datetime

def str_to_datetime(date_str):
    """Convert string to datetime object with fallback"""
    if isinstance(date_str, str):
        try:
            return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            try:
                return datetime.strptime(date_str, '%Y-%m-%d %H:%M')
            except ValueError:
                return datetime.now()
    return date_str
