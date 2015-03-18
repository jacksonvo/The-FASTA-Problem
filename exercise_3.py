file = open("seqcombined.fasta")
#could not do only sequence in lower case so everything was in lower case
for dna in file:
    print(dna.lower())
