def find_restriction_sites(dna_sequence, enzyme_sequence):
    # examing if ACGT is in the sequence
    valid_nucleotides = {'A', 'C', 'G', 'T'}
    for seq in [dna_sequence, enzyme_sequence]:
        if not set(seq).issubset(valid_nucleotides):
            print("Invalid nucleotide in sequence")
        else:

    # examing the length of the sequence
            enzyme_len = len(enzyme_sequence)
            if enzyme_len == 0 or enzyme_len > len(dna_sequence):
                return []
    
    # searching for the restriction enzyme cut sites
            cut_sites = []
            for i in range(len(dna_sequence) - enzyme_len + 1):
                if dna_sequence[i:i+enzyme_len] == enzyme_sequence:
                    cut_sites.append(i+1)
    
            return cut_sites
        

# for example
print(f"For example, restriction enzyme cut sites:{find_restriction_sites("AGCTGATCGA", "GAT")}")  # output [5]

input_dna_sequence = input("Enter the DNA sequence: ")  # input DNA sequence
input_enzyme_sequence = input("Enter the restriction enzyme sequence: ")  # input enzyme sequence
print(f"Restriction enzyme cut sites: {find_restriction_sites(input_dna_sequence, input_enzyme_sequence)}")  # output the cut sites

