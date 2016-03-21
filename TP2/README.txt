Etudiants existants:
	- slimane, informatique, classique
	- houcine, informatique, securite
	- fazil, logiciel, classique
	- dago, logiciel, multimedia
	- maiky, logiciel, multimedia

Requêtes utiles:
	- getCoursSuivis(Etudiant, X). --> retourne la liste de tous les cours suivis par Etudiant
	- inscrire(Etudiant, [Cours, ...]). --> ajoute des cours à Etudiant
		cette requête demande de rentrer une liste de cours, tel qu'on inscrirait un choix de cours (+/- 5 cours)
	- getProgrammeCours(Cours, X). --> retourne la liste des programmes proposant Cours
	- getCoursObligatoiresSuivis(Etudiant, X). --> retourne la liste des cours obligatoires suivis par Etudiant + la liste des projets suivis (considérés comme obligatoires)
	- getCoursOptionnelsSuivis(Etudiant, X). --> retourne la liste des cours optionnels suivis par Etudiant
	- getCoursProjetsSuivis(Etudiant, X). --> retourne la liste des projets suivis par Etudiant
	- getCoursNonAccessibleEchange(Cours). --> retourne la liste des cours non-accessibles aux étudiants en échange
	- inverse(X). --> retourne la liste des cours se donnant en classe inversée
	- getCoursLangage("L", X). --> retourne la liste des cours dans lesquels le langage de programmation "L" est utilisé
	- getEquivalenceValide(Cours, [Liste "sujets" vus, ...]). --> retourne True si la liste des sujets vus contient tous les sujets abordés dans Cours
	- cheminement(Programme, X). --> retourne la liste des cours à suivre dans Programme
	- getQualiteChoix(Etudiant, ListeCours). --> retourne "bon" ou "mauvais" selon la ListeCours donnée pour Etudiant. Ceci est évalué selon si les cours choisis font partie de son cheminement ou non, si un cours a déjà été pris, et si le nombre de crédits est approprié.