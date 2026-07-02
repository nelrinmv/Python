strs = ["flower","flow","flight"]

if len(strs) >=2 :
    maxlength = max(strs)
    for i in range(0,len(maxlength)):
        if strs[0][i:i+1] == strs[1][i:i+1] == strs[2][i:i+1]:
            print(str(strs[0][0:i+2]))
            break
        else:
            print(str(""))
            break
    else:
        print(str(""))
else:
    print(str(""))