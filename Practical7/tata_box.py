import re
import textwrap

tata_pattern = re.compile(r"TATA[AT]A[AT]")

input_file = "D:\\IBI\\IBI1_2024-25\\Practical7\\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "D:\\IBI\\IBI1_2024-25\\Practical7\\tata_genes.fa"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    gene_name = ""
    sequence = ""

    for line in infile:
        line = line.strip()
        if line.startswith(">"):  # face a new gene
            if sequence and tata_pattern.search(sequence):
                # if include TATA box，write to output file
                outfile.write(f">{gene_name}\n")
                for wrapped_line in textwrap.wrap(sequence, 80):  # each 80 characters change line
                    outfile.write(f"{wrapped_line}\n")
                outfile.write("\n")  # change line for separation

            # deal with the new gene
            gene_name = line.split()[0][1:]  # delete '>'
            sequence = ""
        else:
            sequence += line  # connect the sequence

    # deal with the last gene
    if sequence and tata_pattern.search(sequence):
        outfile.write(f">{gene_name}\n")
        for wrapped_line in textwrap.wrap(sequence, 80):  # each 80 characters change line
            outfile.write(f"{wrapped_line}\n")
        outfile.write("\n")  # additional newline for separation

print(f"save as {output_file}")