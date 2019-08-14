import re
'''Este script foi desenvolvido para extrair os tweets já rotulados
   pelos membros do grupo.
   Parte da extração e pré-processamento para treinamento de um Naïve Bayes.
'''

def extract_labeled(data,file):
	'''Esta função realiza a extração retornando a lista de documentos
	rotulado do total de exemplos no documento passado.'''
	new_list=[]
	c_1 = 0
	c_0 = 0
	for tweet in data:
	    words = re.findall(r"\t[0-1]",tweet)
	    if len(words)>0:
	        new_list.append(tweet)
	        if tweet.endswith('\t1'):
	        	c_1 += 1
	        elif tweet.endswith('\t0'):
	        	c_0 += 1
	        #Para debugar
	        #else:
	        #	print(tweet[-20:])

	print(f'\nQuantidade de exemplos rotulados:', len(new_list))
	print(f'Documento: {file}')
	print(f'Quantidade contra (0) - {c_0} e a favor (1) - {c_1}.')
	return new_list


arquivos = ['twitter_lava_joa.data','twitter_vaza_joa.data',
'twitter_lava_Pedro.data','twitter_vaza_Pedro.data','twitter_lava_du.data','twitter_vaza_du.data']

#Adiciona-se a lista t1 a lista referente a cada um
# dos documentos processados

t1 = []
c_0 = []
c_1 = []
for i in arquivos:
	data_file = i
	with open(data_file,"r",encoding="utf8") as f_open:
	    keys = f_open.read().splitlines()

	t1.append(extract_labeled(keys,i))



