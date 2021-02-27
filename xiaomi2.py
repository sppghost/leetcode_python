import sys
import collections
lst = []
dct = collections.OrderedDict()
for line in sys.stdin:
    ele = line.split('\\')[-1].strip('\n')
    if ele not in lst:
        lst.append(ele)
    if ele in dct:
        dct[ele] = dct[ele] + 1
    else:
        dct[ele] = 1
lstTuple = sorted(dct.items(), key=lambda d: d[1], reverse=True)
count = 0
for key in lstTuple:
    if count > 7:
        break
    count = count + 1
    if len(key[0].split(' ')[0]) > 16:
        print(key[0].split(' ')[0][-16:], key[0].split(' ')[1], key[1])
    else:
        print(key[0].split(' ')[0], key[0].split(' ')[1], key[1])
