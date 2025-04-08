def find_restriction_sites(dna_sequence, enzyme_sequence):
    # examing if ACGT is in the sequence
    valid_nucleotides = {'A', 'C', 'G', 'T'}
    for seq in [dna_sequence, enzyme_sequence]:
        if not set(seq).issubset(valid_nucleotides):
            raise ValueError("Invalid nucleotide in sequence")
    
    # examing the length of the sequence
    enzyme_len = len(enzyme_sequence)
    if enzyme_len == 0 or enzyme_len > len(dna_sequence):
        return []
    
    # searching for the restriction enzyme cut sites
    cut_sites = []
    for i in range(len(dna_sequence) - enzyme_len + 1):
        if dna_sequence[i:i+enzyme_len] == enzyme_sequence:
            cut_sites.append(i)
    
    return cut_sites

# for example
print(find_restriction_sites("AGCTGATCGA", "GAT"))  # output [3]
print(find_restriction_sites("ACGTACGT", "AC"))     # output [0, 4]