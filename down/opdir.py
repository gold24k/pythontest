import sys
import os
#os.makedirs("bbb")
#os.makedirs("a\\gg\\d") 
aa = 'asfs\\asfsd\\sdfa\\345'
cc = aa.index('\\')
bb = aa.rindex('\\')
print(cc)
print(bb)
print(aa[cc+1:bb])
os.makedirs(aa[cc+1:bb])