def TaxoLabel_Constructor (SeqIDLists, FamilyList, GenusList, VirusNameList):
	return list(map("_".join,list(zip(["/".join(SeqIDList) if len(SeqIDList)<=3 else "/".join(SeqIDList[0:3])+"/..." for SeqIDList in SeqIDLists],
				list(map(lambda Family: Family.replace(" ", "-"), FamilyList)),
				list(map(lambda Genus: Genus.replace(" ", "-"), GenusList)),
				list(map(lambda VirusName: VirusName.replace(" ", "-"), VirusNameList)),
				))
			))

