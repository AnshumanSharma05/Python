Runner up Score
if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    arr.sort()
    print(arr[-2])
    # unique_arr.sort()
    # print(unique_arr)