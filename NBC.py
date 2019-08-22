import sys
import re
import math
from random import randrange

regex = r"[-'a-zA-ZÀ-ÖØ-öø-ÿ]+" 

class NBClassifier:

    def __init__(self, training_file=None):
        self.Data          = []
        self.Classes       = dict([])
        self.V             = set([])
        self.bigdoc        = dict([])

        self.logprior      = dict([])
        self.loglikelihood = dict([])

        if training_file is not None:
            self.load_data(training_file)

    def load_data(self, training_file):
        training_document = open(training_file,'r')

        for line in training_document.readlines():
            d, c = tuple(line.strip().split("\t"))
            self.Data.append((c,d))

            if c not in self.Classes:
                self.Classes[c] = 0
                self.bigdoc[c] = []
            self.Classes[c] += 1
            
            for w in re.findall(regex, d):
                self.V.add(w)
                self.bigdoc[c].append(w)
            
        print("Total: classes={} documentos={} vocabulario={}".format(len(self.Classes), len(self.Data), len(self.V) ) )

    def train(self):
        for c in self.Classes:
            Ndoc = len(self.Data)
            Nc   = self.Classes[c]

            self.logprior[c] = math.log(Nc/Ndoc)

            count_wc = 0
            for w in self.V:
                count_wc += self.bigdoc[c].count(w)

            for w in self.V:
                self.loglikelihood[(w,c)] = math.log( (self.bigdoc[c].count(w) + 1) / (count_wc + len(self.V) )  ) 

        print("\n", self.logprior)

    def test(self, testdoc):
        s = dict([])
        for c in self.Classes.keys():
            s[c] = self.logprior[c]
            for w in re.findall(regex, testdoc):
                if w in self.V:
                    s[c] += self.loglikelihood[(w,c)]
        return max(s, key=s.get)
 
    def test_batch(self, testing_file):
        testing_document = open(testing_file,'r')
        correct = 0
        total   = 0
        (tp, tn, fp, fn) = (0,0,0,0)

        for line in testing_document.readlines():
            total += 1
            d, c   = tuple(line.strip().split("\t"))
            result = NBC.test(d)
            print ("Classe_Verdadeira={} Classe_Identificada={}:\t{}".format(c, result, d))
            if c==result:
                correct += 1
            if c=='1' and result=='1':
                tp += 1
            if c=='0' and result=='1':
                fp += 1
            if c=='1' and result=='0':
                fn += 1
            if c=='0' and result=='0':
                tn += 1

        print ("\nCorrects = {}/{}\t\t\tAccuracy = {:.3f}".format(correct, total, correct/float(total) ))
        print ("Precision  = {:.3f}\t\t\tRecall = {:.3f}".format((tp)/(tp+fp),(tp)/(tp+fn)))
        print ("Negative Predictive Value = {:.3f}\tSpecificity = {:.3f}".format((tn)/(tn+fn),(tn)/(tn+fp)))
        print ('\n-Confusion matrix-')
        print (f' {tp}\t{fp}')
        print (f' {fn}\t{tn}')

    def classify(self,testing_file):
        testing_document = open(testing_file,'r')
        total = 0
        (c_1,c_0) = (0,0)
        for line in testing_document.readlines():
            total += 1
            d = line.strip()
            result = NBC.test(d)
            print(result)
            print ("Classe_Identificada={}:\t{}".format(result, d))
            if result=='1':
                c_1 += 1
            elif result=='0':
                c_0 += 1

        print(f'Total de Tweets a favor: {c_1}\nTotal de Tweets Contra: {c_0}')

        
if __name__ == '__main__':
    fileNameTrain = sys.argv[1]   # datasets/all_datasets-train.txt
    fileNameTest  = sys.argv[2]   # datasets/all_datasets-test.txt

    NBC = NBClassifier(fileNameTrain)
    NBC.train()
    #NBC.test_batch(fileNameTest)
    NBC.classify(fileNameTest)