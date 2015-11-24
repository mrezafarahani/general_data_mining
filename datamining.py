# entropy of a set:
# e(set) = - \sum_i (P(value_i) \times log_2(P(value_i)))
# for more information: https://en.wikipedia.org/wiki/Entropy_(information_theory)
import math 
def entropy(dataset):
    ent = 0
    all_len = len(dataset)
    lable = {}
    for i in dataset:
        if i in lable:
            lable[i] += 1
        else:
            lable[i] = 1
    for i in lable:
        p = float(lable[i])/all_len
        ent += -p * math.log(p,2)
    return ent
