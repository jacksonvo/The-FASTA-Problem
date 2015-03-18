import os
import glob

path = 'fasta_problem' #takes us into the folder
for infile in glob.glob( os.path.join(path, '*.seq') ):
    print infile #prints the names of all files in folder
