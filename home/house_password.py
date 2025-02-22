def checkio(data: str) -> bool:
    if len(data) < 10:
        return False
    if data.islower():
        return False
    if data.isupper():
        return False
    if data.isdigit():
        return False
    if data.isalpha():
        return False
    else:
        return True

'''
def checkio(data: str) -> bool:
    return not (len(data) < 10 or data.islower() or data.isupper() or data.isdigit() or data.isalpha())
'''

if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
