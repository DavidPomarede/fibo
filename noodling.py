import string

alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
arr = alphabet.split(',')
print(arr)
# pangramTrue = True
# check = 0

def is_pangram(s):
        check = 0
            for x in range(26) :
                        for y in s.lower() :
                                        if y == arr[x] :
                                                            check += 1
                                                                            if check == 26 :
                                                                                #                     print('true')
                                                                                #                     pangramTrue = True
                                                                                                    return True
                                                                                                                else :
                                                                                                                                        pass
                                                                                                                                    #                     pangramTrue = False

                                                                                                                                        
                                                                                                                                        #     return pangramTrue
                                                                                                                                                        
                                                                                                                                                                    
                                                                                                                                                                        
                                                                                                                                                                            #     for x in s.lower() :
                                                                                                                                                                            #         print(x)
                                                                                                                                                                            #         if x == alphabet(x)
                                                                                                                                                                            #             print('yes')
                                                                                                                                                                            #         for y in alphabet :
                                                                                                                                                                            #             if y != x :
                                                                                                                                                                            #                 return True
                                                                                                                                                                            #             else :
                                                                                                                                                                            #                 return False
                                                                                                                                                                                return False
