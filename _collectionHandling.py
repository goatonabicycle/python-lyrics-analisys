from collections import Counter
import re

class collectionHandling(object):    
    def stringToCountedCollection(self, stringItem, exclusionList):                
        stringAsListOfWords = re.findall(r'\w+', stringItem)         
        collectionOfIndividualItems = Counter(stringAsListOfWords)

        for word in exclusionList:
            if word in collectionOfIndividualItems:
                del collectionOfIndividualItems[word]
                
        return collectionOfIndividualItems