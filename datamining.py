# entropy of a set:
# e(set) = - \sum_i (P(value_i) \times log_2(P(value_i)))
# for more information: https://en.wikipedia.org/wiki/Entropy_(information_theory)
import math 
def entropy(dataset):
    ent = 0
    all_len = len(dataset)
    lables = {}
    for i in dataset:
        if i in lables:
            lables[i] += 1
        else:
            lables[i] = 1
    number_of_symbols = len(lables)
    for i in lables:
        p = float(lables[i])/all_len
        ent += -p * math.log(p,number_of_symbols)
    return ent
