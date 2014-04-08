'''
Created on Apr 7, 2012

@author: Scott Brown

Command line tool used to create an EDL

'''

import sys
from EDLManager import EDLManager
import filter

def main():
    args = sys.argv
    if len(args) < 4:
        print "Usage: movieFile srtFile filterFile"
        sys.exit()

    categories = filter.parse_file(args[3])
    profanity = filter.get_all_words(categories)
    worker = EDLManager(args[2], args[1], profanity);
    
    if len(args) == 5:
        worker.setEDLName(args[4])
        
    worker.updateEDL()
    
    print "EDL file %s created / or updated" % worker.edlLoc
    
if __name__ == '__main__':
    main()

