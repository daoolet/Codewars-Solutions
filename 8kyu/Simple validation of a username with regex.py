import re

def validate_usr(username):
    return bool(re.fullmatch('[^A-Z][a-z0-9_]{3,16}', username))