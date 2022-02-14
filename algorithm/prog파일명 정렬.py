


import re

def solution(files):
    answer = []
    tups = []
    for char in files:
        p = re.compile('\d')
        i = p.search(char).start()
        head = char[:i]
        number = char[i:i+5]
        tail = char[i+5:]

        if not number.isalnum():
            np = re.compile('\D')
            n = np.search(number).start()
            tail = char[i + n:]
            number = number[:n]

        tups.append([head,number,tail])

    tups.sort(key= lambda x: (x[0].lower(),x[1].zfill(5)))

    for word in tups:
        word = ''.join(word)
        answer.append(word)
    print(answer)
    return answer




solution(["img000012345", "img1.png","img2","IMG02"])

