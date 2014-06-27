'''
Created on 23 juin 2014

@author: Charly 
'''
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk import downloader
from nltk.chunk import ne_chunk
from nltk.tag.util import str2tuple

exemples = ["And now, you don't do something completely different.",'San Francisco is foggy']
#asgjklsfsdjkl

def printExemple(sentence):
    
    print('\t---sentence:')
    print(sentence)
    
    print('\n\t---word_tokenize:')
    words = word_tokenize(sentence)
    print(words)
    
    print('\n\t---pos_tag:')
    print(pos_tag(words))
    
    print('\n\t---ne_chunk pos_tag:')
    print(ne_chunk(pos_tag(words)))
    
    print('\n\n')
    pass

def main():
    
    exempleNumber = 0
    for sentence in exemples:
        print('\nExemple' + `++exempleNumber`)
        printExemple(sentence)
    
    pass

def prepareTagsData():
    
    'download tagging'
    #downloader.download()
    #===========================================================================
    # print('download all tags')
    # downloader.download('all',"D:\\nltk_data",True)
    #===========================================================================
    
    pass

if __name__ == '__main__':
    
    prepareTagsData()
    
    #===========================================================================
     main()
    #===========================================================================

