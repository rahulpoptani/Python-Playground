# A DNA sequence can be represented as a string consisting of the letters A, C, G and T
# Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively.
# For example, consider string S = CAGCCTA and arrays P, Q such that:
#     P[0] = 2    Q[0] = 4
#     P[1] = 5    Q[1] = 5
#     P[2] = 0    Q[2] = 6

# 1. The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
# 2. The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
# 3. The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.

def solution (S, P, Q):
    result = [None] * len(P)
    gen = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    for x in range(len(P)):
        first_element = P[x]
        last_element = Q[x]
        min_chr = 'Z'
        for y in range(first_element, last_element+1):
            min_chr = min(min_chr, S[y])
        result[x] = gen[min_chr]
    print (result)

solution('CAGCCTA', [2, 5, 0], [4, 5, 6])
