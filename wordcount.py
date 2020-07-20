#import sys
def readfile (filepath):
    count = 0    
    infile = open(filepath)
    for line in infile:
        
        print('you had '+ str(count) +' characters.')
        count = count+1
        print(line, end = '')

    infile.close

import sys
name = sys.argv[1]
readfile(name)
