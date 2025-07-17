G = [3, 2, 3, 0, 0, 1, 2, 2, 3, 0]
k = [i for i in range(len(G))]

def calculate_dg(G):
    DG = []
    for i, e in enumerate(G):
        if i == 0:
            DG.append(e)
        else:
            value = e * (1 / (math.log2(i + 1)))
            DG.append(value)
    return DG

def calculate_dcg(DG):
    return sum(DG)

import math

print('k:', k[1:])
print("G: ", G)

DG1 = calculate_dg(G)
DCG = calculate_dcg(DG1)
print("DG: ", DG1)
print("DCG@10: ", DCG)
print("________________________________")

iG = sorted(G, reverse=True)
print("iG: ", iG)
iDG = calculate_dg(iG)
print("iDG: ", iDG)
iDCG = calculate_dcg(iDG)
print("iDCG@10: ", iDCG)
print("________________________________")

CalculatenDCG = DCG / iDCG if iDCG != 0 else 0
print("normalization(nDCG@k)", CalculatenDCG)