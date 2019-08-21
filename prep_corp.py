import re
import time
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer
import sys

stopwords = set(stopwords.words('portuguese'))
stemmer = RSLPStemmer()

def clean(file,name):

	with open(file,"r",encoding="utf-8") as f_open:
	    keys = f_open.read().splitlines()

	l = []
	w = []
	for k in keys:
		#first cleanse
		text = re.sub(r"([^\s]+:\/\/[^\s]+)|(@[^\s]+)|(#[^\s]+)|(\n)", "",k,flags=re.MULTILINE)
		
		#patterns of words and classes to find
		words = re.findall(r"([-'a-zA-ZÀ-ÖØ-öø-ÿ]+)",text)
		labels = re.findall(r"\t[\d]",text)
		labels = [lab.replace("\t","") for lab in labels]
		
		#stemming
		words = [stemmer.stem(word) for word in words if word not in stopwords]

		#joining the words back into one unique string
		phrase = ' '.join(words)[10:]
		w.append(phrase)
		l.append(labels)
	
	#format: 'tweet \t label \n'
	with open(name,"w") as f:
		for tweet,lab in zip(w,l):
			f.write(tweet)
			f.write('\t')
			f.write(lab[0])
			f.write('\n')
	f.close()

if __name__ == '__main__':
	fileNameTrain = sys.argv[1]  
	fileNameTest  = sys.argv[2]

	clean(fileNameTrain,'treino70.txt')
	clean(fileNameTest,'test30.txt')
