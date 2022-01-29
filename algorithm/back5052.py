import sys







tc = int(sys.stdin.readline())
for i in range(tc):
    check = True
    phonNumCount = int(sys.stdin.readline())
    temp = list(sys.stdin.readline().rstrip() for _ in range(phonNumCount))
    temp.sort()

    for j in range(phonNumCount-1):
        if temp[j+1].startswith(temp[j]):
            check = False
            print("No")
            break
    if check:
        print("Yes")




