# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Create script called getngrams.py. 

#Your script should define the following function:

#processSentence(text1, text2)

#- The parameters of this function are a piece of text (text1), another text (text2). 

#- The function should return the number of 2-grams that appear in both texts and have the following structure.                                                    

#<Adjective> <Noun>, write loop to find them independently, count the number of word. 

 

#Notes:

#Don't change the names or the parameters of the function
#Don't forget to convert the texts into sentences using sent_tokenize()
#Make sure that your script imports all the libraries needed by the function
#Ignore case #B and b are the same thing, ignore it 

from nltk.tokenize import sent_tokenize
from nltk import load
import nltk,re

def process(text1, text2):

    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'#local path
    tagger = load(_POS_TAGGER)

    #read the input
    
    sentences=sent_tokenize(text1)
    #print ('NUMBER OF SENTENCES: ',len(sentences))
    
    nounAfterAdj=[]

    # for each sentence
    for sentence in sentences:
        
        terms = nltk.word_tokenize(sentence)   #tokenize the sentence, using the word_tokenize to make the parsing more accurate and flextible. For
        # for example, i have dinner, it was great. Because they are not in th order adjafteradv. But word_tokenize make it possible. 
        
        #print(terms)
        tagged_terms=tagger.tag(terms)#do POS tagging on the tokenized sentence
        #print(tagged_terms)
       
        for i in range(len(tagged_terms)-1):# for every tagged term, the -1 is to avoid the loop hit the last word, then loop blow up. Check on the last two words. 
            term1=tagged_terms[i] #current term
            term2=tagged_terms[i+1] # following term
        
            if re.match('JJ',term1[1]) and re.match('NN',term2[1]): # current term is an adverb, next one is an adjective, using match function to find every tag that started with JJ, such as JJR, J
                nounAfterAdj.append((term1[0],term2[0]))# add the adverb-adj pair to the list
        
   

    sentences2=sent_tokenize(text2)
    #print ('NUMBER OF SENTENCES: ',len(sentences2))
    
    nounAfterAdj2=[]

    # for each sentence
    for sentence in sentences2:
        
        terms2 = nltk.word_tokenize(sentence)   #tokenize the sentence, using the word_tokenize to make the parsing more accurate and flextible. For
        # for example, i have dinner, it was great. Because they are not in th order adjafteradv. But word_tokenize make it possible. 
        
        #print(terms2)
        tagged_terms2=tagger.tag(terms2)#do POS tagging on the tokenized sentence
        #print(tagged_terms2)
       
        for i in range(len(tagged_terms2)-1):# for every tagged term, the -1 is to avoid the loop hit the last word, then loop blow up. Check on the last two words. 
            term3=tagged_terms2[i] #current term
            term4=tagged_terms2[i+1] # following term
        
            if re.match('JJ',term3[1]) and re.match('NN',term4[1]): # current term is an adverb, next one is an adjective, using match function to find every tag that started with JJ, such as JJR, J
                nounAfterAdj2.append((term3[0],term4[0]))# add the adverb-adj pair to the list
        
    set1=set(nounAfterAdj)
    set2=set(nounAfterAdj2)

    print (len(set1.intersection(set2)))
    
if __name__=='__main__':
    process('I went to a park today, I saw a very cute dogs and beautiful flowers. I had a great time there and great food',
        'My family went out for a nice meal last night, the restaurant had great food and beautiful flowers on the table.')