"""
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 4
"""
def create_phone_number(n):
    n = "".join(str(num) for num in n)
    return f"({n[:3]}) {n[3:6]}-{n[6:]}"
