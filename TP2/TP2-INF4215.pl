%Predicates
set([], []).
set([H|T], [H|T1]) :- subtract(T, [H], T2), set(T2, T1).
%%%%%

inscrire(Etudiant, Liste):-
	getChoixValide(Etudiant, Liste),
	forall(member(C, Liste), assert(coursSuivis(Etudiant, C))).

getChoixValide(Etudiant, Liste):-
	forall(member(C, Liste), cours(C)),
	nbCreditsValide(Liste),
	forall(member(C1, Liste), getPrerequisValide(Etudiant, C1)),
	forall(member(C2, Liste), getCorequisValide(Etudiant, C2, Liste)),
	forall(member(C3, Liste), getNbCreditsValide(Etudiant, C3)).

getNbCreditsValide(Etudiant, Cours):-
	getCreditsEtudiant(Etudiant, Total),
	getNbCreditsPrealable(Cours, X),
	Total >= X .

getCorequisValide(Etudiant, Cours, Liste):-
	findall(C0, corequis(Cours, C0), C),
	findall(X0, coursSuivis(Etudiant, X0), X),
	union(X, Liste, L),
	intersection(C, L, C).


getPrerequisValide(Etudiant, Cours):-
	findall(C0, prerequis(Cours, C0), C),
	findall(X0, coursSuivis(Etudiant, X0), X),
	intersection(C, X, C).


getCreditsEtudiant(Etudiant, Total) :-
	findall(X0, coursSuivis(Etudiant, X0), X),
	totalCredits(X, Total).

getCoursSuivis(Etudiant, Result) :-
	findall(X0, coursSuivis(Etudiant, X0), Result).

nbCreditsValide(A):-
	set(A, A2),
	totalCredits(A2, Total),
	Total >= 12,
	Total =< 18.

totalCredits([], 0).
totalCredits([A|B], Total):-
	totalCredits(B, Rest),
	credits(A, C),
	Total is C + Rest.


appendProgram(Cours, Programme, Result):-
	 cheminement(Programme, ListeCheminement),	
	(
		member(Cours, ListeCheminement) -> append(Programme, [], TmpRes); 
		true
	),
	Result = TmpRes.



getProgrammeCours(Cours, Programme):-
	cours(Cours),
	(
		type_cours(Cours, _) -> Programme = [informatique, logiciel];
		(findall(P0, type_cours(Cours,_,P0,_), L1),
		findall(P1, type_cours(Cours,_,P1), L2),
		union(L1,L2,Programme))
	
	).
	%findall(P0, cheminement(P0, P), P),
	%forall(member(C3, Liste), getNbCreditsValide(Etudiant, C3)).
	%forall(member(P1, P),  appendProgram(Cours, P1, Result)),
	%Programme = Result.  
	

getCoursClasseInversee(Liste):-
	findall(C0, inverse(C0), Liste).

getCoursObligatoiresSuivis(Etudiant, Liste):-
	genie(Etudiant, Programme, Concentration),
	getCoursSuivis(Etudiant, Cours),
	getTousCoursType(obligatoire, Programme, Concentration, ListeCours),
	getCoursProjetsSuivis(Etudiant, ListeProjets),
	intersection(Cours, ListeCours, ListeTemp),
	append(ListeTemp, ListeProjets, Liste).

getCoursProjetsSuivis(Etudiant, Liste):-
	genie(Etudiant, Programme, Concentration),
	getCoursSuivis(Etudiant, Cours),
	getTousCoursType(projet, Programme, Concentration, ListeCours),
	intersection(Cours, ListeCours, Liste).

getCoursOptionnelsSuivis(Etudiant, Liste):-
	genie(Etudiant, Programme, Concentration),
	getCoursSuivis(Etudiant, Cours),
	getTousCoursType(option, Programme, Concentration, ListeCours),
	intersection(Cours, ListeCours, Liste).

getTousCoursType(Type, Programme, Concentration, Liste):-
	findall(C, type_cours(C, Type), L0),
	findall(C0, type_cours(C0,Type,Programme,Concentration), L1),
	findall(C1, type_cours(C1,Type,Programme), L2),
	union(L0, L1, L3),
	union(L3, L2, Liste).

getQualiteChoix(Etudiant, ListeCours, Result):-
	getChoixValide(Etudiant, ListeCours),
	genie(Etudiant, Programme, _),
	cheminement(Programme, ListeCheminement),
	(
		intersection(ListeCours, ListeCheminement, ListeCours) -> Result = "Good";
		Result = "Bad : some of the courses you took aren't in your program"
	).
	

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
sujetsCours(mth1006, ["transposees"," permutations"," espaces"," rang"," transformations"," hermitiennes"]).
sujetsCours(mth1102, ["integrales"," coordonnees"," curvilignes"," green"," divergence"]).
sujetsCours(mth1110, ["differentielles"," ordinaires"," oscillations"," laplace"]).
sujetsCours(mth1210, ["taylor"," euler"," runge-kutta"," differences-finies"]).
sujetsCours(mth2302, ["probabilites"," tolerance"," parametriques"," fiabilite"," previsionnelle"," tests"," intervalle-confiance"]).
sujetsCours(inf1005, ["C"," C++"," fichiers-texte"," fichiers-binaire"," classes"]).
sujetsCours(inf1010, ["C++"," objets"," pointeurs"," heritage"," stl"]).
sujetsCours(inf2010, ["listes"," piles"," files"," vecteurs"," tri"," arbre-binaire"]).
sujetsCours(log2410, ["analyse", "patrons", "uml", "diagrammes"]).
sujetsCours(log2810, ["automates", "grammaires", "langages", "recursive", "graphes", "inference", "deductions"]).
sujetsCours(inf1040, ["historique", "carrieres", "retroaction", "projection", "contraintes"]).
sujetsCours(inf1500, ["Karnaugh", "multiplexeurs", "codeurs", "registres", "compteurs", "bascules"]).
sujetsCours(log1000, ["analyse", "specifications", "tests", "prototypage", "consistance"]).
sujetsCours(inf1600, ["microprocesseur", "memoire", "bus", "alignement", "adressage"]).
sujetsCours(inf2610, ["fonctions", "services", "Interblocage", "processus", "systeme exploitation"]).
sujetsCours(inf3710, ["sql", "requetes"]).

getEquivalenceValide(Cours, Liste):-
	sujetsCours(Cours, Sujets),
	intersection(Sujets, Liste , Sujets).
	

credits(X, Y) :-
	(
		member(X, [mth1101, mth1006, mth1102, mth1110, ssh5501]) ->	Y is 2;
		(
			member(X, [mth1210, inf3005, log3005]) -> Y is 1;
			(
				member(X, [inf1995, inf2990, inf3990, log3900, inf4990, log4900]) -> Y is 4;
				Y is 3
			)
		)
	).


inverse(inf4215).
inverse(inf3500).

langage(1, [inf1005, inf1010, inf2410, inf2610, inf2810, inf3405, inf4710]).
langage(2, [inf1005, inf2610, inf3990, inf4990, inf4705]).
langage(3, [inf2010, inf2420, inf4705]).
langage(4, [inf4215]).

getCoursLangage(Langage, Cours) :-
	(
		Langage == "C++" ->	langage(1, Cours);
		(
			Langage == "C" ->	langage(2, Cours);
			(
				Langage == "Python" ->	langage(3, Cours);
				(
					Langage == "Java" ->	langage(4, Cours);
					Cours = [])
			)
		)
	).

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
corequis(log2810, inf2010).
corequis(inf3710, inf2610).
corequis(inf1995, inf1600).
corequis(inf1995, log1000).
corequis(log2420, inf2010).
corequis(inf2705, inf2990).
corequis(inf2990, inf2705).
corequis(inf3500, ele2302).
corequis(inf3610, inf3990).
corequis(inf3990, inf3610).
corequis(log3000, log3900).
corequis(log3900, log3000).
corequis(inf3990, inf3005).
corequis(inf3005, inf3990).
corequis(log3900, log3005).
corequis(log3005, log3900).

credit_prealable(ssh5201, 27).
credit_prealable(ssh5501, 27).
credit_prealable(ssh5100, 30).
credit_prealable(inf4990, 85).
credit_prealable(log4900, 85).

getNbCreditsPrealable(Cours, Result):-
(
	credit_prealable(Cours,X) -> Result is X;
	Result is 0
).


type_cours(mth1101, obligatoire).
type_cours(mth1006, obligatoire).
type_cours(mth1102, obligatoire).
type_cours(mth1110, obligatoire).
type_cours(mth1210, obligatoire).
type_cours(mth2302, obligatoire).
type_cours(inf1005, obligatoire).
type_cours(inf1010, obligatoire).
type_cours(inf2010, obligatoire).
type_cours(log2410, obligatoire).
type_cours(log2810, obligatoire).
type_cours(inf1040, obligatoire).
type_cours(inf1500, obligatoire).
type_cours(log1000, obligatoire).
type_cours(inf1600, obligatoire).
type_cours(inf2610, obligatoire).
type_cours(inf3710, obligatoire).
type_cours(ssh5100, obligatoire).
type_cours(phs1101, obligatoire).
type_cours(ssh5201, obligatoire).
type_cours(inf3405, obligatoire).
type_cours(ssh5501, obligatoire).
type_cours(inf1995, projet).
type_cours(inf2990, projet).
type_cours(log2420, obligatoire, logiciel).
type_cours(inf4705, obligatoire, informatique).
type_cours(inf2705, obligatoire, informatique).
type_cours(inf4215, option, informatique).
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
type_cours(inf4705, obligatoire, logiciel, classique).
type_cours(inf4215, obligatoire, logiciel, multimedia).
type_cours(inf2705, obligatoire, logiciel, multimedia).
type_cours(inf4705, option, logiciel, multimedia).
type_cours(inf4215, option, logiciel, classique).

concentration(multimedia).
concentration(classique).

infolog(Result):-
	commun(X),
	append(X, [inf1005, inf1010, inf2010, log2410, log2810, inf1040, inf1500, log1000,
	inf1600, inf2610, inf3710, inf1995, inf2990, inf3405, inf4705, inf2705, inf4215], Result).

commun( [mth1101, mth1006, mth1102, mth1110, mth1210, mth2302, ssh5100, phs1101, ssh5201, ssh5501]).


cheminement(logiciel, Result):-
	infolog(X),
	append(X,[log2420, log3000, log3900, log3005], Result).
	
cheminement(informatique, Result):-
	infolog(X),
	append(X,[inf3500, ele2302, inf3610, inf3990, inf4990, inf3005], Result).

type(obligatoire).
type(projet).
type(option).

non_accessible(ssh5501).
non_accessible(inf3005).
non_accessible(log3005).

getCoursNonAccessibleEchange(Cours):-
    findall(X0, non_accessible(X0), C0),
    findall(X1, type_cours(X1, projet, _), C1),
    union(C0, C1, Cours).

etudiant(slimane).
etudiant(houcine).
etudiant(fazil).
etudiant(maiky).
etudiant(dago).

genie(maiky, logiciel, multimedia).
genie(fazil, logiciel, classique).
genie(dago, logiciel, multimedia).
genie(slimane, informatique, classique).
genie(houcine, informatique, securite).

