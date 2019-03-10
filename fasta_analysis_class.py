#! /usr/bin/python3
#-*-coding: utf-8-*-
#no shebang required to launch in conda environnement, write python in front of the :
# ./fasta_analysis
# Louison Fresnais M2BB


import sys
# import modules from the class files
from utils_class import *
from parameter_parsing import *
#Argparse initialisation
args = vars(argument_parsing())
print(args)


#####################################################################
#   						INPUT	 								#
#####################################################################

###Fasta file(s) reading or request a fasta file name to the user if failure.
try:
	datas = list()
	for fic in args.get("file"):
		fasta_data = fasta_dic()
		datas.append(fasta_data.read_fasta(fic))


except TypeError:
	fic = str(input("Entrez un nom de fichier fasta s'il vous plait "))
	fasta_data = fasta_dic()
	datas.append(fasta_data.read_fasta(fic))

###If the argument for the minimal score is missing, ask a minimal score to the user
try:
	score = int(args.get("score"))
	print(score)

except TypeError:
	score = int(input("Entrez une valeur de score minimal requise pour l'intégration dans le graph "))

###If  the graph name is missing, ask a graphic name to the user
try:
	names = list()
	for current_name in args.get("name"):
		names.append(current_name)

except TypeError:
	names.append(str(input("Entrez le nom que vous désirez donner à votre graphique ")))


#####################################################################
#   						EXECUTION	 							#
#####################################################################
#name_pos is a counter made to avoid identical output filename during one execution.
name_pos = 0
for data in datas:
	#Fasta file reading
	graph = fasta_graph()
	#graph buiding on the previously submitted data
	graph.build_graph(data,score)
	#Plot the graph with matplotlib
	graph.plot_graph(names[name_pos],score)
	name_pos+=1
