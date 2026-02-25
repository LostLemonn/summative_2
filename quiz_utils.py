import re  # used to ensure that the name does not contain any numerical values


def clean_name(name):
    """
    Pure function
    """
    return name.strip().title()

def presence_check(name: str) -> bool:
    
    """
    Checks that a name has been provided.
    Also a pure function. Returns True if the name is not empty.
    """
    return bool(name)

def length_check(name: str) -> bool:
    
    """
    Checks that the name length is within an acceptable range.
    Another pure function. Returns True if the name length is between 2 and 50 characters.
    """
    return 2 <= len(name) <= 50

def character_check(name: str) -> bool:
    
    """
    Checks that the name contains only valid characters.
    Again, this is also a pure function. Returns True if the name has no numbers.
    """
    return not re.search(r"\d", name)
