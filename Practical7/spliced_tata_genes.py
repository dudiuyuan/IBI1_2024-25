import re
# This script counts the number of TATA boxes in spliced genes and outputs the results to a new FASTA file.
# It prompts the user to select a splice donor/acceptor combination from a predefined list.
#define a function to count TATA boxes in spliced genes
import re

def extract_gene_name(header):
    """Extract gene name from FASTA header"""
    match = re.search(r'gene:(\S+)', header)
    if match:
        return match.group(1)
    return header.split(' ')[0][1:]  # Fallback: use the first word after >

def count_tata_boxes(sequence):
    """Count occurrences of TATA box (TATAWAW where W is A or T)"""
    return len(re.findall(r'TATA[AT]A[AT]', sequence))

def process_fasta(input_file, output_file, splice_site):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        current_gene = None
        current_sequence = []
        
        for line in infile:
            if line.startswith('>'):
                # Process previous gene if we have one
                if current_gene and current_sequence:
                    full_sequence = ''.join(current_sequence)
                    if splice_site in full_sequence:
                        tata_count = count_tata_boxes(full_sequence)
                        if tata_count > 0:
                            gene_name = extract_gene_name(current_gene)
                            outfile.write(f'>{gene_name} TATA_count:{tata_count}\n{full_sequence}\n')
                
                # Start new gene
                current_gene = line.strip()
                current_sequence = []
            else:
                current_sequence.append(line.strip())
        
        # Process the last gene in the file
        if current_gene and current_sequence:
            full_sequence = ''.join(current_sequence)
            if splice_site in full_sequence:
                tata_count = count_tata_boxes(full_sequence)
                if tata_count > 0:
                    gene_name = extract_gene_name(current_gene)
                    outfile.write(f'>{gene_name} TATA_count:{tata_count}\n{full_sequence}\n')

def main():
    while True:
        splice_site = input("Enter splice donor/acceptor combination (GTAG, GCAG, or ATAC): ").upper()
        if splice_site in ['GTAG', 'GCAG', 'ATAC']:
            break
        print("Invalid input. Please enter GTAG, GCAG, or ATAC.")
    
    input_file = 'D:\\IBI\\IBI1_2024-25\\Practical7\\tata_genes.fa'
    output_file = f'D:\\IBI\\IBI1_2024-25\\Practical7\\{splice_site}_spliced_genes.fa'
   
    process_fasta(input_file, output_file, splice_site)
    print(f"Results written to {output_file}")

if __name__ == '__main__':
    main()





