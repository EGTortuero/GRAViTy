from Bio import Entrez
import os

def DownloadGenBankFile (GenomeSeqFile, SeqIDLists):
	if not os.path.exists("/".join(GenomeSeqFile.split("/")[:-1])):
		os.makedirs("/".join(GenomeSeqFile.split("/")[:-1]))
	
	Entrez.email = input("To download GenBank file(s), please provide your email: ")
	search_results = Entrez.read(Entrez.epost(db = "nucleotide", id=", ".join(map(lambda x:", ".join(x), SeqIDLists))))
	handle = Entrez.efetch(db = "nucleotide", rettype="gb", retmode="text", webenv = search_results["WebEnv"], query_key = search_results["QueryKey"])
	with open(GenomeSeqFile, "w") as GenomeSeqFile_handle:
		GenomeSeqFile_handle.write(handle.read())
	
	handle.close()
