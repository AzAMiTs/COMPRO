set1 = {1,2,3,4}
set2 = {3,4,5,6}

union_set = set1 | set2
print("Union:", union_set)

inter_s = set1 & set2
print("inter",inter_s)

diff_s = set1 - set2
print('diff',diff_s)

sym_diff_s = set1 ^ set2
print("symme",sym_diff_s)