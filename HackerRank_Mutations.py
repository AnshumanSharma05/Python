def mutate_string(string, position, character):
    # l=list(string)
    # l[position]=character
    # stri="".join(l)
    # return stri 
    return string[:position]+character+string[position+1:]

if __name__ == '__main__':