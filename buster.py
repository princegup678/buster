#This is a directory busting  tool which mainly takes two arguments i.e. url of the target and the wordlist.
#This can be also used for finding files of any any type present in that directory by passing additional parameters.
#More details are available on https://github.com/princegup678/buster

import requests
import sys
from multiprocessing.pool import ThreadPool as Pool
#here prCyan,prYellow and prGreen are the functions defined for the printing the text in cyan , yellow and green colour respectively.
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def thread_requests():
  s=""
  s=url+i
  s=s[:-1]
  #print(s)
  r=requests.get(s)
  if r.status_code == 200: #checking whether the requested url is 200 or not
   print (s)
   r.close
  for i in range(3,length):
    k=s+"."+str(sys.argv[i])
    #print(k)
    r=requests.get(k)   #checking for the file types
    if r.status_code == 200:
      print (k)
      r.close


banner_me='''  
                ██████╗     ██╗   ██╗    ███████╗    ████████╗    ███████╗    ██████╗ 
                ██╔══██╗    ██║   ██║    ██╔════╝    ╚══██╔══╝    ██╔════╝    ██╔══██╗
                ██████╔╝    ██║   ██║    ███████╗       ██║       █████╗      ██████╔╝
                ██╔══██╗    ██║   ██║    ╚════██║       ██║       ██╔══╝      ██╔══██╗
                ██████╔╝    ╚██████╔╝    ███████║       ██║       ███████╗    ██║  ██║
                ╚═════╝      ╚═════╝     ╚══════╝       ╚═╝       ╚══════╝    ╚═╝  ╚═╝                                             
 '''
aut=''' Author : Prince Kumar https://github.com/princegup678 '''
sep="*************************************************"
print("\n\n")
prYellow(sep)
print("\n\n\n\n")

prCyan(banner_me)
print("\n\n\n\n")


prGreen(aut)

prYellow(sep)
pool_size = 5  # For "parallelness"
pool = Pool(pool_size)
c=str(sys.argv[2])
url=str(sys.argv[1])
length=len(sys.argv)
#ext=str(sys.argv[3])
#print (ext)
#print (url)
#print (c)

print("")
print("")

stinfo="Starting directory on " + url+"   using the wordlist  "+c +" .\n This will show only successful attempts .\n\n"
prYellow(stinfo)
prYellow(sep)
f=open(c,"r")  #opening the wordlist file using given path
for i in f:
    pool.apply_async(thread_requests, (i,))
f.close()
pool.close()
pool.join()


prGreen("\nDirectory Busting is completed")
prYellow(sep)
