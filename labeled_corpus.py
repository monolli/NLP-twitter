import re
'''Este script foi desenvolvido para extrair os tweets já rotulados
   pelos membros do grupo.
   Parte da extração e pré-processamento para treinamento de um Naïve Bayes.
'''

data_file = 'twitter_lava_Pedro.data'
with open(data_file,"r",encoding="utf8") as f_open:
    keys = f_open.read().splitlines()

#print(keys[-2:0])

new_list=[]
for s in keys:
    words = re.findall(r"\t[0-1]",s)
    if len(words)>0:
        print(s)
        new_list.append(s)

print(len(new_list))
