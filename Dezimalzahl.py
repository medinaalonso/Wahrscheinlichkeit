# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 09:42:48 2019

@author: DiBot
"""
from collections import Counter 
import matplotlib.pyplot as plt
def calcPi(limit):  # Generator function
    """
    Prints out the digits of PI
    until it reaches the given limit
    """

    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

    decimal = limit
    counter = 0
    result=[]
    result2=[]
    while counter != decimal + 1:
            if 4 * q + r - t < n * t:
                    # yield digit
                    #result.append(n)
                    #print("resultado",result)
                    #return n 
                    yield n
                    # insert period after first digit
                    if counter == 0:
                            #result2.append('.')
                            #print("result2",result2)
                            #return result2     
                            yield '.'
                    # end
                    if decimal == counter:
                            print('')
                            break
                    counter += 1
                    nr = 10 * (r - n * t)
                    n = ((10 * (3 * q + r)) // t) - 10 * n
                    q *= 10
                    r = nr
            else:
                    nr = (2 * q + r) * l
                    nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
                    q *= k
                    t *= l
                    l += 2
                    k += 1
                    n = nn
                    r = nr


def main():  # Wrapper function

    # Calls CalcPi with the given limit
    pi_digits = calcPi(int(input(
        "Enter the number of decimals to calculate to: ")))

    i = 0
  #  print("pii",pi_digits)
    # Prints the output of calcPi generator function
    # Inserts a newline after every 40th number
    papas=[]
    for d in pi_digits:
            print(d, end='')
            papas.append(d)
            
            
            i += 1
            if i == 40:
                print("")
                i = 0
                
    print("dd",papas)
    papas=str(papas)
    print(papas)
   # split_list =[i.split() for i in papas]
    papas2=papas.split('.')
    
    for i in papas2:
       
        print(i)
   # print(sin)
    nms=Counter(papas)
    print(nms)
    x=sorted(nms.items())

    key=[lis[0] for lis in x]
    res=[lis[1] for lis in x]
    
    #print("keys,res",key,res)
   # key=[lis[0] for lis in nms]
    #res=[lis[1] for lis in nms]
    
    plt.bar(key,res)
    plt.show()
   
            
            
if __name__ == '__main__':
    main()