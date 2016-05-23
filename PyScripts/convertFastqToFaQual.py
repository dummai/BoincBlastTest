import sys
from Bio import SeqIO


def convertFastqToFasta(fastq_file):
    fasta_filename = '%s.fa' % fastq_file
    record = SeqIO.convert(fastq_file, "fastq", fasta_filename, "fasta")
    print 'Number of converted reads to fasta =', record

def convertFastqToQual(fastq_file):
    qual_filename = '%s.qual' % fastq_file
    record = SeqIO.convert(fastq_file, "fastq", qual_filename, "qual")
    print 'Number of converted reads to qual =', record

def main():
    fastq_file = sys.argv[1]
    convert_type = sys.argv[2]
    if convert_type == 'fasta':
        convertFastqToFasta(fastq_file)
    elif convert_type == 'qual':
        convertFastqToQual(fastq_file)
    else:
        print 'Error convert type %s' % convert_type

if __name__ == '__main__':
    main()
