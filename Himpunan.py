'''
A = himpunan (set) bilangan genap antara 1 dan 20.
B = himpunan (set) bilangan ganjil antara 1 dan 20.
C = himpunan (set) bilangan negatif lebih dari -10.
D = himpunan (set) bilangan prima antara 1 dan 20.
E = himpunan (set) bilangan komposit antara 1 dan 20.

a. A ∪ B ∪ C ∪ D ∪ E
b. (A ∩ B) ∪ (D ∩ E)
c. (A ∪ B) ∩ (D ∪ E)
d. (A ∪ B) - (D ∪ E)
e. (A ∪ B ∪ C) - (A ∩ E)
'''

A = {2,4,6,8,10,12,14,16,18}
B = {3,5,7,9,11,13,15,17,19}
C = {-9,-8,-7,-6,-5,-4,-3,-2,-1}
D = {2,3,5,7,11,13,17,19}
E = {4,6,8,9,10,12,14,15,16,18}

# a. A ∪ B ∪ C ∪ D ∪ E
print(A.union(B).union(C).union(D).union(E))
# b. (A ∩ B) ∪ (D ∩ E)
print(A.intersection(B).union(D.intersection(E)))
# c. (A ∪ B) ∩ (D ∪ E)
print(A.union(B).intersection(D.union(E)))
# d. (A ∪ B) - (D ∪ E)
print((A.union(B))-(D.union(E)))
# e. (A ∪ B ∪ C) - (A ∩ E)
print((A.union(B).union(C))-(A.intersection(E)))