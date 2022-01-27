






"""
포인터가 갈수 있는지 없는지 검사
갈수있으면 count
없으면 continue
"""


def solution(dirs):
    moveConst = {'U':(0,1),'D':(0,-1),'L':(-1,0),'R':(1,0)}
    visited = set()
    px,py = 0,0
    answer = 0
    visited.add((0,0,0,0))
    for move in dirs:
        x,y = moveConst[move]
        cx = px+x
        cy = py+y
        cross1 = ((cx,cy,px,py))
        cross2 = ((px,py,cx,cy))
        px, py = cx, cy
        if cross1 not in visited:
            visited.add(cross1)
            visited.add(cross2)
            answer +=1



    print(answer)



solution("RRRRRRRRRRRRRRRRRRRRRUUUUUUUUUUUUULU")