#This code reads alphabet characters from certain files and fills up an array so
#it can be used for generating test images

import os

def combine(frest,fc,fpresv,fpostsv):
    """ Creates all possible combinations of consonant+vowel"""
    all_comb=[]
    
    for c in fc:
        c=c.strip() #remove special characters
        c1=c+" "
        all_comb.append(c1)
        for postv in fpostsv: # combine vowel sign+consonant
            txt=c+postv.strip()
            txt=txt+" "
            all_comb.append(txt)
    count=0
    for a in all_comb:
        #print count,
        count+=1
        print a
    print all_comb
    return all_comb



def read_file(alphabet_dir):
    """Reads input alphabet files from alphabet_dir"""
    print "in file.py"
    #file containing vowels
    if(os.path.exists(alphabet_dir+"consonants")):
        f=open(alphabet_dir+"consonants",'r')
        fc=f.readlines()
        f.close()
    else:
        fc=[]
        
    
    fpresv=[]
        

    #file containing semivowels of the form semivowel+consonant_conjunct
    if(os.path.exists(alphabet_dir+"post_semivowels")):
        f=open(alphabet_dir+"post_semivowels",'r')
        fpostsv=f.readlines()
        f.close()
    else:
        fpostsv=[]
    
    frest=[]
    return combine(frest,fc,fpresv,fpostsv)
