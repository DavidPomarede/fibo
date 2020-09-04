def xo(s):
        numX = 0
        numO = 0
        for x in range(len(s)) :
            if s[x].lower()=='x' :
                numX+=1
            elif s[x].lower()=='o' :
                numO+=1
            else :
                pass
                                                                                                
            if numX==numO :
                return True
            else :
                return False
