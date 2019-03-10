#! /usr/bin/python3
#-*-coding: utf-8-*-
#no shebang required to launch in conda environnement, write python in front of the :
# ./fasta_analysis
# Louison Fresnais M2BB

#####################################################################
#   This function is required for the parsing process       		#
#####################################################################

def argument_parsing():

    import argparse #https://docs.python.org/3/library/argparse.html

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Fasta analysis",
        epilog="""This program is going to provide a graph representing the alignment scores between all the sequences provided in a fasta file. You need to take in consideration the impact of the sequence length on the alignement score in order to have the most accurate graphic.
            There is two kind of outputs:
            -Alignment scores in text, on your terminal.
            -A gexf graphic and a png graphic

            The parameters are the following:
            -1: name(s) of the fasta file
            -2: minimum score needed for the edge intergration in the final graph
            -3: name of the graphic
            If you do not enter the parameters, the script will ask you to give the missing parameters in the terminal.

            Contact: fresnaislouison@gmail.com""")
    #The add_argument method add a parameters to the command line and describe how to use the parameter when help is requested by the user.
    parser.add_argument('-f','--file', nargs='+', type=str, help='template to enter more than one file: -f "file1.fa file2.fa filex.fa"')
    parser.add_argument('-s','--score', type=int, help='enter a number for a score value')
    parser.add_argument('-n','--name', nargs='+', type=str, help='enter a name for the output graphic')
    args = parser.parse_args()

    return args
