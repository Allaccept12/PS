






def dailyTempatures(days):

    result = []

    #브루투 포스
    for i,n in enumerate(days):
        for j in range(i+1,len(days)):
            print(n,n > days[j],j >= len(days),days[j],i,j,len(days))
            if n < days[j]:
                result.append(j - i)
                break
            elif n >= days[j] and j==len(days)-1:
                result.append(0)
                break
    result.append(0)
    return result


#[1,0,0,0,1,0,0,0,0,0]

if __name__ == "__main__":
    print(dailyTempatures([34,80,80,80,34,80,80,80,34,20,34,40,20]))