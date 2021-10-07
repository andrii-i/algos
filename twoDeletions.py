def twoDeletions(str):
    if len(str) <= 2:
        return 0
    
    enumArr = []
    s = 0
    for i in range(1, len(str)):
        if str[i] != str[s]:
            enumArr.append([i - s, str[s]])
            s = i
        elif i == len(str) - 1:
            enumArr.append([i - s + 1, str[s]])
    
    largestSeqArr = sorted(enumArr, key=lambda el: el[0], reverse=True)

    maxThreeSeq = 0
    if len(enumArr) > 2:
        s = 0
        e = 2
        while e < len(enumArr):
            if enumArr[s][1] == enumArr[e][1]:
                maxThreeSeq = max(maxThreeSeq, enumArr[s][0] + enumArr[s + 1][0] + enumArr[e][0])
            s += 1
            e += 1

    return len(str) - max(largestSeqArr[0][0] + largestSeqArr[1][0], maxThreeSeq)
