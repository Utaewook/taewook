def solution(s):
    answer = 0
    L = []
    for i in s:
        if len(L)==0:
            L.append(i)
        else:
            if L[-1] == i:
                L.pop()
            else:
                L.append(i)
    if len(L)==0:
        answer = 1
    return answer


print(solution("baabaa"))
print(solution("cdcd"))