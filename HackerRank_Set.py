def average(array):
    # your code goes here
    sett=set(array)
    summ=0
    for i in sett:
        summ+=i
    return summ/len(sett)    

if __name__ == '__main__':