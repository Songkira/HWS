import re
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = "hit"

def many(a):

    ra = re.sub("[^ \w]","",a.lower())
    sa = ra.split()
    dic_sa = {}
    for i in sa:
        banned = "hit"
        if i in dic_sa:
            dic_sa[i] += 1
        elif i == banned:
            continue
        elif i not in dic_sa:
            dic_sa[i] = 1
    return max(dic_sa, key=dic_sa.get)

print(many(paragraph))


