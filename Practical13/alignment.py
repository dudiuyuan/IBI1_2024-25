from scoring_matrices import ScoringMatrix

def read_fasta(file_path):
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
   
    seq = ''.join(line.strip().upper() for line in lines[1:])
    return seq

def calculate_alignment(seq1, seq2, matrix):

    if len(seq1) != len(seq2):
        raise ValueError("Sequences must be of equal length for non-gapped alignment")
    
    score = 0
    matches = 0
    for a, b in zip(seq1, seq2):
        try:
            
            score += matrix[a, b]
        except KeyError:
            
            score += matrix.default  
        if a == b:
            matches += 1
    identity = (matches / len(seq1)) * 100
    return score, identity


if __name__ == "__main__":
   
    blosum62 = ScoringMatrix.from_name("BLOSUM62")
    
  
    human_seq = read_fasta("D:/IBI/IBI1_2024-25/Practical13/P04179.fasta")
    mouse_seq = read_fasta("D:/IBI/IBI1_2024-25/Practical13/P09671.fasta")
    random_seq = read_fasta("D:/IBI/IBI1_2024-25/Practical13/random.fasta")
    
  
    score_hm, identity_hm = calculate_alignment(human_seq, mouse_seq, blosum62)
    score_hr, identity_hr = calculate_alignment(human_seq, random_seq, blosum62)
    score_mr, identity_mr = calculate_alignment(mouse_seq, random_seq, blosum62)
    

    print(f"Human-Mouse Alignment:")
    print(f"  BLOSUM62 Score: {score_hm}")
    print(f"  Percentage Identity: {identity_hm:.1f}%\n")
    
    print(f"Human-Random Alignment:")
    print(f"  BLOSUM62 Score: {score_hr}")
    print(f"  Percentage Identity: {identity_hr:.1f}%\n")
    
    print(f"Mouse-Random Alignment:")
    print(f"  BLOSUM62 Score: {score_mr}")
    print(f"  Percentage Identity: {identity_mr:.1f}%")