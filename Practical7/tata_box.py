# import re

# input_filename = 'Saccharomyces_cerevsizae.R64-1-1.cdna.all.fa'
# output_filename = 'tata_genes.fa'

# with open(input_filename, 'r') as f_in, open(output_filename, 'w') as f_out:
#     current_gene_name = None
#     current_sequence = []
#     for line in f_in:
#         line = line.strip()
#         if line.startswith('>'):
#             if current_gene_name is not None:
#                 full_seq = ''.join(current_sequence)
#                 if 'TATA' in full_seq:
#                     f_out.write(f'>{current_gene_name}\n{full_seq}\n')
#             match = re.search(r'gene:(\S+)', line)
#             current_gene_name = match.group(1) if match else None
#             current_sequence = []
#         else:
#             current_sequence.append(line)
#     if current_gene_name is not None:
#         full_seq = ''.join(current_sequence)
#         if 'TATA' in full_seq:
#             f_out.write(f'>{current_gene_name}\n{full_seq}\n')

import re

# 定义 TATA box 的正则表达式
tata_pattern = re.compile(r"TATA[AT]A[AT]")

# 读取 FASTA 文件
input_file = "D:\\IBI\\IBI1_2024-25\\Practical7\\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "D:\\IBI\\IBI1_2024-25\\Practical7\\tata_genes.fa"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    gene_name = ""
    sequence = ""

    for line in infile:
        line = line.strip()
        if line.startswith(">"):  # 遇到新的基因
            if sequence and tata_pattern.search(sequence):
                # 如果上一个基因序列包含 TATA box，写入到文件
                outfile.write(f">{gene_name}\n{sequence}\n")

            # 提取基因名称（假设基因名称是 '>' 后的第一个单词）
            gene_name = line.split()[0][1:]  # 去掉 '>'
            sequence = ""
        else:
            sequence += line  # 累积基因序列

    # 处理最后一个基因
    if sequence and tata_pattern.search(sequence):
        outfile.write(f">{gene_name}\n{sequence}\n")

print(f"包含 TATA box 的基因已保存到 {output_file}")
