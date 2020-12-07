if __name__ == '__main__':
    marksheet=[]
    scores=set()
    names=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.add(score)
        marksheet.append([name,score])
    second_lowest=sorted(scores)[1]   
    for name, marks in marksheet:
            if marks==second_lowest:
                names.append(name)
    names.sort()            
    for name in names:
        print(name)   