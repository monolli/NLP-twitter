import re
'''Este script foi desenvolvido para extrair os tweets já rotulados
   pelos membros do grupo.
   Parte da extração e pré-processamento para treinamento de um Naïve Bayes.
'''

def extract_labeled(data):
	'''Esta função realiza a extração retornando a lista de documentos
	rotulado do total de exemplos no documento passado.'''
	new_list=[]
	for tweet in data:
	    words = re.findall(r"\t[0-1]",tweet)
	    if len(words)>0:
	        new_list.append(tweet)

	print(f'Quantidade de exemplos rotulados:', len(new_list))
	return new_list


arquivos = ['twitter_lava_joa.data','twitter_vaza_joa.data',
'twitter_lava_Pedro.data','twitter_vaza_Pedro.data']

#Adiciona-se a lista t1 a lista referente a cada um
# dos documentos processados

t1 = []
for i in arquivos:
	data_file = i
	with open(data_file,"r",encoding="utf8") as f_open:
	    keys = f_open.read().splitlines()
	t1.append(extract_labeled(keys))

<<<<<<< HEAD
=======
def extract_labeled(data):
	new_list=[]
	for tweet in data:
	    words = re.findall(r"\t[0-1]",tweet)
	    if len(words)>0:
	        new_list.append(tweet)

	print(len(new_list))
	return new_list

extract_labeled(data_file)
>>>>>>> e4d2e1ff283d3c1153ced04f41bd32632d185c37

