class A:
    def __init__(self):
        self.x = 1

    def __getitem__(self, key):
        return dir(self)[key]

a = A()

print(a["x"])

class NucleotidesChain:
    def __init__(self, A = 0, C = 0, G = 0, T = 0):
        chain = {
            'A': A,
            'C': C,
            'G': G,
            'T': T,
        }

    def __setitem__(self, key, new_val):
        self.chain[key] = new_val
    
    def __sub__(self, other):
        return NucleotidesChain(*(self.chain.values - other.chain.values))

    def __add__(self, other):
        return NucleotidesChain(*(self.chain.values + other.chain.values))

def find_impact(dna_seq):
    if 'A' in dna_seq:
        return 1
    if 'C' in dna_seq:
        return 2
    if 'G' in dna_seq:
        return 3
    else:
        return 4

def solution(S, P, Q):
    presum_list = []
    nucleotide_chain = NucleotidesChain()
    for i in range(len(S)):
        current_nucleotide = NucleotidesChain()
        current_nucleotide[S[i]] = 1
        nucleotide_chain = nucleotide_chain + current_nucleotide
        presum_list.append(nucleotide_chain)


    impact_list = []
    
    for i in range(len(P)):
        dna_seq = S[P[i]: Q[i]]
        impact_list.append(find_impact(dna_seq))
        
    return impact_list


print(solution("ATGCACCGTGGTA", [1, 4, 0], [3, 4, 12]))