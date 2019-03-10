#! /usr/bin/python3
#-*-coding: utf-8-*-
#no shebang required to launch in conda environnement, write python in front of the :
# ./fasta_analysis
# Louison Fresnais M2BB


class fasta_dic():
	"""This class is used to read a fasta file and store the datas in a dictionnary.
       The only method is read_fasta.
	"""
	def __init__(self):
		super(fasta_dic, self).__init__()
		self.fastas = {}

#####################################################################
#   This method read a fasta file given in parameters and then store#
#   these datas in a dictionnary where the fasta identifier is the  #
#   key and the sequence the value.								    #
#####################################################################

	def read_fasta(self, file):

	    nameHandle = open(file,'r')

	    for line in nameHandle:
	        if line[0] == '>':
	            header = line[1:]
	            self.fastas[header] = ''
	        else:
	            self.fastas[header] += line
	    nameHandle.close()
	    return self.fastas




class fasta_graph():
	"""This class is used to draw a graph of pairwise alignment scores.
	   There is two methods:
	   -build_graph is going to build a graph with the datas from a dictionnary
	   made by the read_fasta function.
	   -plot_graph will draw the graph with specified properties. At the moment, these properties are in the code but they could be given as parameter in the future.
	"""
	def __init__(self):
		super(fasta_graph, self).__init__()
		self.graph = ""

########################################################################
#   This method is performing a paiwise alignment over datas in the    #
#   dictionnary provided by the get_fasta method.                	   #
#   The parameters are the dictionnary and the minimum score required  #
#   to integrate the edge in the graph.                                #
########################################################################

	def build_graph(self,data,score):

		# import biopython, that is needed for the pairwise alignment
		# http://biopython.org/DIST/docs/api/Bio.pairwise2-module.html

		from Bio import pairwise2

		# import a library required to produce gexf graphs
		# https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.readwrite.gexf.write_gexf.html#networkx.readwrite.gexf.write_gexf

		from networkx import nx

		###Similarity graph
		self.graph = nx.Graph()

		### pairwise alignement with biopython
		k = 0
		for key in data: #These loops are made in order to avoid redundant alignement
			k += 1
			for i in range(k, len(data.keys())):
				key_2 = list(data.keys())
				if key != key_2[i]:  # Check with we don't align two identical sequences.
					print(key_2[i])
					seq1 = data.get(key)
					seq2 = data.get(key_2[i])
					pairwise_result = pairwise2.align.globalxx(seq1, seq2)
					# Add the edge if score is greater than minimal score
					#We take only the first ten characters of the identifier.
					#It could need to be adjusted regarding the identifier length.
					if pairwise_result[0][2] > score:
						self.graph.add_edge(key[0:10],key_2[i][0:10],weight = int(pairwise_result[0][2]))
						# Alignement score display
						print("score = ", pairwise_result[0][2])

		return self.graph

########################################################################
#   This method produce a graph representing the paiwise alignement    #
#   scores between fasta sequences   								   #
#   The parameters are a dictionnary, the title of the graph    #
#   and the minimal score. Each edge have a score.  				   #
########################################################################

	def plot_graph(self,name,score):

		#Import matplotlib, a library used to produce graphic in python.
		import matplotlib.pyplot as plt
		from networkx import nx
		
		plt.figure(figsize=(7, 7))  # Adjust the window size
		plt.margins(.2, .2)  # Adjust margins
		#We determine the node position: https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.drawing.layout.spring_layout.html
		position = nx.spring_layout(self.graph)
		nx.draw_networkx(self.graph, with_labels=True,pos = position)
		plt.axis('off')  # Removing axis
		#Weights on edges : solution found on stackoverflow
		#https://stackoverflow.com/questions/28372127/add-edge-weights-to-plot-output-in-networkx

		labels = nx.get_edge_attributes(self.graph, 'weight')
		nx.draw_networkx_edge_labels(self.graph, pos=position, edge_labels=labels)
		plt.title("fasta alignment graph according to a minimum alignment score of " + str(score))
		plt.savefig(name + ".png") # Produce a png file with the graph annotated by default
		plt.show()

		nx.write_gexf(self.graph, name + ".gexf") # Produce a gexf file that can be annotated with gephi.

		return None
