def swap_case(s):
    sentence=""
    for letter in s:
        if letter==letter.upper():
            sentence+=letter.lower()
        else:
            sentence+=letter.upper()    
    return sentence        
if __name__ == '__main__':