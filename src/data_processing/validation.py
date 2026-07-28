"""
Data validation functions.
"""

def validate_isbn(isbn):
    if isbn is None:
        return None

    cleaned = str(isbn).replace("-", "")

    if not cleaned.isdigit():
        return None

    if len(cleaned) != 13:
        return None

    digits = []
    for character in cleaned:
        digits.append(int(character))

    total = 0
    for i in range(12):
        digit = digits[i]
        if i % 2 == 0:
            total += digit * 1
        else:
            total += digit * 3

    check_digit = (10 - (total % 10)) % 10

    if check_digit != digits[12]:
        return None

    return cleaned

# Example function to implement:
# def validate_isbn(isbn):
#     """Clean and validate an ISBN-13 value.

#     Args:
#         isbn: Raw ISBN value (may be a hyphenated string, a number, or None)

#     Returns:
#         The cleaned ISBN-13 string if valid, or None if invalid.

#     TODO: Implement check-digit validation and formatting cleanup.
#     """

#     isbn_new = isbn

#     if isbn_new is None:
#         return False

#     # Convert to string and remove hyphens
#     isbn_new = str(isbn_new).replace("-", "")

#     # Must be exactly 13 digits
#     if len(isbn_new) != 13:
#         return False

#     # All characters must be digits
#     if not isbn_new.isdigit():
#         return False

#     # Calculate check digit from first 12 digits
#     total = 0
#     for i in range(12):
#         digit = int(isbn_new[i])
#         total += digit * (1 if i % 2 == 0 else 3)

#     check_digit = (10 - (total % 10)) % 10

#     # Compare with 13th digit
#     return check_digit == int(isbn_new[12])

#     #return isbn
