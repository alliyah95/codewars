"""
Solve the horror of unstandardized keypads by providing a function that converts computer input to a number as if it was typed on a phone.

Example:
"789" -> "123"
"""
def computer_to_phone(numbers):
    x = {'0':'0','1':'7','2':'8','3':'9','4':'4','5':'5','6':'6','7':'1','8':'2','9':'3'}
    return "".join([x.get(n) for n in numbers])
