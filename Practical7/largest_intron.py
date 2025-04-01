seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

gt_positions = []
for i in range(len(seq) - 1):
    if seq[i] == 'G' and seq[i+1] == 'T':
        gt_positions.append(i)

max_length = 0

for i in gt_positions:
    for j in range(i + 2, len(seq) - 1):
        if seq[j] == 'A' and seq[j+1] == 'G':
            current_length = j - i + 2
            if current_length > max_length:
                max_length = current_length

print(max_length)