# Question 2
import re

def check_password(passwd: str) -> bool:
    """A strong password has a length greater than or equal to 6, contains at
    least one lowercase letter, at least one uppercase letter, and at least
    one digit.  Return True iff passwd is considered strong.

    example:
    >>> check_password('I<3ece1779')
    True
    """
    if len(passwd) >= 6:
        if re.search(r'[A-Z]', passwd) and re.search(r'[a-z]', passwd) and re.search(r'[0-9]', passwd):
            return True
        else:
            return False
    else:
        return False

print(check_password('I<3ece1779'))

print(check_password('I<3ECE1779'))