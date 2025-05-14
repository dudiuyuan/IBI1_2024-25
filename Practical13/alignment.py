def read_fasta(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    seq = ''.join(line.strip() for line in lines[1:])
    return seq

blosum62 = {
    ('A', 'A'): 4, ('A', 'R'): -1, ...,  # 实际需完整填充矩阵
}

# 计算比对得分和百分比同一性
def calculate_alignment(seq1, seq2, matrix):
    score = 0
    matches = 0
    for a, b in zip(seq1, seq2):
        score += matrix.get((a, b), 0)  # 假设矩阵键为元组
        if a == b:
            matches += 1
    identity = (matches / len(seq1)) * 100
    return score, identity

# 主程序
human_seq = read_fasta("human_sod2.fasta")
mouse_seq = read_fasta("mouse_sod2.fasta")
random_seq = read_fasta("random.fasta")

# 三组比对
score_hm, identity_hm = calculate_alignment(human_seq, mouse_seq, blosum62)
score_hr, identity_hr = calculate_alignment(human_seq, random_seq, blosum62)
score_mr, identity_mr = calculate_alignment(mouse_seq, random_seq, blosum62)

print(f"Human-Mouse: Score={score_hm}, Identity={identity_hm:.1f}%")
print(f"Human-Random: Score={score_hr}, Identity={identity_hr:.1f}%")
print(f"Mouse-Random: Score={score_mr}, Identity={identity_mr:.1f}%")