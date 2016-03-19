	cours(mth1101).
	cours(mth1006).
	cours(mth1102).
	cours(mth1110).
	cours(mth1210).
	cours(mth2302).
	cours(inf1005).
	cours(inf1010).
	cours(inf2010).
	cours(log2410).
	cours(log2810).
	cours(inf1040).
	cours(inf1500).
	cours(log1000).
	cours(inf1600).
	cours(inf2610).
	cours(inf3710).
	cours(inf1995).
	cours(inf2990).
	cours(log2420).
	cours(ssh5100).
	cours(inf3405).
	cours(phs1101).
	cours(ssh5201).
	cours(inf4705).
	cours(ssh5501).
	cours(inf2705).
	cours(inf4215).
	cours(inf3500).
	cours(ele2302).
	cours(inf3610).
	cours(log3000).
	cours(inf3990).
	cours(log3900).
	cours(inf4990).
	cours(log4900).
	cours(inf3005).
	cours(log3005).

	sujetsCours(mth1101, ["suites"," series"," taylor"," gradient"," lagrange"]).
	sujetsCours(mth1006, ["transposées"," permutations"," espaces"," rang"," transformations"," hermitiennes"]).
	sujetsCours(mth1102, ["integrales"," coordonnées"," curvilignes"," green"," divergence"]).
	sujetsCours(mth1110, ["différentielles"," ordinaires"," oscillations"," laplace"]).
	sujetsCours(mth1210, ["taylor"," euler"," runge-kutta"," différences-finies"]).
	sujetsCours(mth2302, ["probabilités"," tolérance"," paramétriques"," fiabilité"," prévisionnelle"," tests"," intervalle-confiance"]).
	sujetsCours(inf1005, ["C"," C++"," fichiers-texte"," fichiers-binaire"," classes"]).
	sujetsCours(inf1010, ["C++"," objets"," pointeurs"," heritage"," stl"]).
	sujetsCours(inf2010, ["listes"," piles"," files"," vecteurs"," tri"," arbre-binaire"]).
	sujetsCours(log2410, ["analyse", "patrons", "uml", "diagrammes"]).
	sujetsCours(log2810, ["automates", "grammaires", "langages", "recursive", "graphes", "inférence", "déductions"]).
	sujetsCours(inf1040, ["historique", "carrieres", "rétroaction", "projection", "contraintes"]).
	sujetsCours(inf1500, ["Karnaugh", "multiplexeurs", "codeurs", "registres", "compteurs", "bascules"]).
	sujetsCours(log1000, ["analyse", "spécifications", "tests", "prototypage", "consistance"]).
	sujetsCours(inf1600, ["microprocesseur", "mémoire", "bus", "alignement", "adressage"]).
	sujetsCours(inf2610, ["fonctions", "services", "Interblocage", "processus", "systeme exploitation"]).
	sujetsCours(inf3710, ["sql", "requetes"]).

	credits(mth1101, 2).
	credits(mth1006, 2).
	credits(mth1102, 2).
	credits(mth1110, 2).
	credits(mth1210, 1).	
	credits(inf1995, 4).
	credits(inf2990, 4).	
	credits(ssh5501, 2).
	credits(inf3990, 4).
	credits(log3900, 4).
	credits(inf4990, 4).
	credits(log4900, 4).
	credits(inf3005, 1).
	credits(log3005, 1).
 
    inverse(inf4215).
	inverse(inf3500).

	langage("C++", [inf1005, inf1010, inf2410, inf2610, inf2810, inf3405, inf4710]).
	langage("C", [inf1005, inf2610, inf3990, inf4990, inf4705]).
	langage("Java", [inf2010, inf2420, inf4705]).
	langage("Python", [inf4215]).

	prerequis(mth1102, mth1101).
	prerequis(mth1110, mth1101).
	prerequis(mth1110, mth1006).
	prerequis(inf1010, inf1005).
	prerequis(inf2010, inf1010).
	prerequis(log2410, log1000).
	prerequis(log2410, inf1010).
	prerequis(log1000, inf1005).
	prerequis(inf1600, inf1005).
	prerequis(inf1600, inf1500).
	prerequis(inf2610, inf1010).
	prerequis(inf2610, inf1600).
	prerequis(inf3710, inf2010).
	prerequis(inf1995, inf1040).
	prerequis(inf2990, inf2010).
	prerequis(inf2990, log2410).
	prerequis(inf3405, mth2302).
	prerequis(inf4705, inf2010).
	prerequis(inf4705, log2810).
	prerequis(inf2705, mth1006).
	prerequis(inf2705, inf2010).
	prerequis(inf4215, log2810).
	prerequis(inf4215, mth2302).
	prerequis(inf3500, inf1600).
	prerequis(ele2302, mth1110).
	prerequis(inf3610, inf2610).
	prerequis(inf3610, inf3500).
	prerequis(log3000, inf2990).
	prerequis(inf3990, inf3405).
	prerequis(inf3990, inf3500).
	prerequis(log3900, inf2990).
	prerequis(inf4990, inf3990).
	prerequis(log4900, log3900).

	corequis(mth1102, mth1006).
	corequis(mth1210, mth1110).
	corequis(mth2302, mth1101).
	corequis(inf2010, log2810).
	corequis(inf3710, inf2610).
	corequis(inf1995, inf1600).
	corequis(inf1995, log1000).
	corequis(log2420, inf2010).
	corequis(inf2705, inf2990).
	corequis(inf3500, ele2302).
	corequis(inf3610, inf3990).
	corequis(log3000, log3900).
	corequis(inf3990, inf3005).
	corequis(log3900, log3005).
	
	type_cours(mth1101, obligatoire, tous).
	type_cours(mth1006, obligatoire, tous).
	type_cours(mth1102, obligatoire, tous).
	type_cours(mth1110, obligatoire, tous).
	type_cours(mth1210, obligatoire, tous).
	type_cours(mth2302, obligatoire, tous).
	type_cours(inf1005, obligatoire, infolog).
	type_cours(inf1010, obligatoire, infolog).
	type_cours(inf2010, obligatoire, infolog).
	type_cours(log2410, obligatoire, infolog).
	type_cours(log2810, obligatoire, infolog).
	type_cours(inf1040, obligatoire, infolog).
	type_cours(inf1500, obligatoire, infolog).
	type_cours(log1000, obligatoire, infolog).
	type_cours(inf1600, obligatoire, infolog).
	type_cours(inf2610, obligatoire, infolog).
	type_cours(inf3710, obligatoire, infolog).
	type_cours(inf1995, projet, infolog).
	type_cours(inf2990, projet, infolog).
	type_cours(log2420, obligatoire, logiciel).
	type_cours(ssh5100, obligatoire, tous).
	type_cours(inf3405, obligatoire, infolog).
	type_cours(inf3405, option, biomedical).
	type_cours(phs1101, obligatoire, tous).
	type_cours(ssh5201, obligatoire, tous).
	type_cours(inf4705, obligatoire, informatique).
	type_cours(inf4705, obligatoire, logiciel, classique).
	type_cours(inf4705, option, logiciel, multimedia).
	type_cours(ssh5501, obligatoire, tous).
	type_cours(inf2705, obligatoire, informatique).
	type_cours(inf2705, obligatoire, logiciel, multimedia).
	type_cours(inf4215, option, informatique).
	type_cours(inf4215, option, logiciel, classique).
	type_cours(inf4215, obligatoire, logiciel, multimedia).
	type_cours(inf3500, obligatoire, informatique).
	type_cours(ele2302, obligatoire, informatique).
	type_cours(inf3610, obligatoire, informatique).
	type_cours(log3000, obligatoire, logiciel).
	type_cours(inf3990, projet, informatique).
	type_cours(log3900, projet, logiciel).
	type_cours(inf4990, projet, informatique).
	type_cours(log4900, projet, logiciel).
	type_cours(inf3005, obligatoire, informatique).
	type_cours(log3005, obligatoire, logiciel).

	genie(logiciel).
	genie(informatique).
	genie(infolog).
	genie(biomedical).
	genie(electrique).
	genie(tous).

	concentration(multimedia).
	concentration(classique).

	cheminement(tous, [mth1101, mth1006, mth1102, mth1110, mth1210, mth2302, ssh5100, phs1101, ssh5201, ssh5501]).
	cheminement(biomedical, [inf3405, inf1005]).
	cheminement(electrique, [inf1005, inf1010]).
	cheminement(infolog, [inf1005, inf1010, inf2010, log2410, log2810, inf1040, inf1500, log1000, 
		inf1600, inf2610, inf3710, inf1995, inf2990, inf3405, inf4705, inf2705, inf4215]).
	cheminement(logiciel, [log2420, log3000, log3900, log3005]).
	cheminement(informatique, [inf3500, ele2302, inf3610, inf3990, inf4990, inf3005]).

	type(obligatoire).
	type(projet).
	type(option).
