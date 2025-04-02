import re

valid_options = {'GTAG', 'GCAG', 'ATAG'}
user_input = input("Enter splice donor/acceptor combination (GTAG, GCAG, ATAG): ").strip().upper()
if user_input not in valid_options:
    print("Invalid option. Please choose from GTAG, GCAG, ATAG.")
    exit()

donor = user_input[:2]
acceptor = user_input[2:]
output_filename = f"{user_input}_spliced_genes.fa"
input_filename = 'Saccharomyces_cerevsizae.R64-1-1.cdna.all.fa'

def is_spliced(seq, donor, acceptor):
    pattern = re.escape(donor) + r'.+' + re.escape(acceptor)
    return re.search(pattern, seq) is not None

with open(input_filename, 'r') as f_in, open(output_filename, 'w') as f_out:
    current_gene_name = None
    current_sequence = []
    for line in f_in:
        line = line.strip()
        if line.startswith('>'):
            if current_gene_name is not None:
                full_seq = ''.join(current_sequence)
                if is_spliced(full_seq, donor, acceptor) and 'TATA' in full_seq:
                    tata_count = full_seq.count('TATA')
                    f_out.write(f'>{current_gene_name} {tata_count}\n{full_seq}\n')
            match = re.search(r'gene:(\S+)', line)
            current_gene_name = match.group(1) if match else None
            current_sequence = []
        else:
            current_sequence.append(line)
    if current_gene_name is not None:
        full_seq = ''.join(current_sequence)
        if is_spliced(full_seq, donor, acceptor) and 'TATA' in full_seq:
            tata_count = full_seq.count('TATA')
            f_out.write(f'>{current_gene_name} {tata_count}\n{full_seq}\n')






#


import re

# 让用户输入剪切供体/受体组合
valid_splice_sites = ["GTAG", "GCAG", "ATAC"]
splice_site = input(f"请输入剪切供体/受体组合 {valid_splice_sites}: ").strip().upper()

# 确保输入合法
if splice_site not in valid_splice_sites:
    print("输入无效，请输入 GTAG, GCAG 或 ATAC")
    exit()

# 读取 FASTA 文件
input_file = r"D:\IBI\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = f"{splice_site}_spliced_genes.fa"

# TATA box 的正则表达式
tata_pattern = re.compile(r"TATA[AT]A[AT]")

# 解析 FASTA 文件
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    gene_name = ""
    sequence = ""

    for line in infile:
        line = line.strip()
        if line.startswith(">"):  # 遇到新的基因
            if sequence:
                # 处理上一个基因的序列
                introns = re.findall(f"{splice_site[0:2]}(.*?){splice_site[2:4]}", sequence)
                for intron in introns:
                    if tata_pattern.search(intron):
                        tata_count = len(tata_pattern.findall(intron))
                        outfile.write(f">{gene_name} | TATA_count={tata_count}\n{intron}\n")

            # 提取基因名称
            gene_name = line.split()[0][1:]  # 去掉 '>'
            sequence = ""
        else:
            sequence += line  # 继续拼接序列

    # 处理最后一个基因
    introns = re.findall(f"{splice_site[0:2]}(.*?){splice_site[2:4]}", sequence)
    for intron in introns:
        if tata_pattern.search(intron):
            tata_count = len(tata_pattern.findall(intron))
            outfile.write(f">{gene_name} | TATA_count={tata_count}\n{intron}\n")

print(f"剪切基因已保存到 {output_file}")
