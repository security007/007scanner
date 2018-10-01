#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import BeautifulSoup 
import time
import re
import sys
import urllib
import os
judul = """
++++++++++++++++++++++++++++++++++++++++++
++          WELCOME TO 007scan!         ++
++ Author : security007                 ++
++ Email  : defacementsec007@gmail.com  ++
++ Greets : Allah, ProblemCyberTeam     ++
++++++++++++++++++++++++++++++++++++++++++"""
print judul+"\n"
if (len(sys.argv) == 2):
	url = sys.argv[1]
else:
	print "[!] Usage : python "+sys.argv[0]+" http://domain.com"
	sys.exit()

if (url.startswith("https://")==True):
	print "[!] Please use http:// only"
	sys.exit()
print "\n"
print "[+] Checking "+url
try:
	page = requests.request('get',url=url)
	print "Status Code :",page.status_code
except:
	print "[x] Failed to connect "+url
time.sleep(2)
print "\n[+] Crawling"
htmlcode_page = page.text
dump_isihtml = BeautifulSoup.BeautifulSoup(htmlcode_page)

Links = dump_isihtml.findAll("a",{"href":True})
leng = len(Links)  
count = 0  
while count < leng:    
	lk = "[*] "
	pp = Links[count]["href"] 
	print lk+pp
	a=open("link.txt","ab")
	a.writelines(pp+"\n")	
	time.sleep(0.2)
	count += 1  
time.sleep(2)
print "\n[+] Checking Robots"
cek = requests.get(url+"/robots.txt")
if (cek.status_code == 200):
	print "[*] Found [200] /robots.txt"
	print cek.text
else:
	print "[-] Not Found"
time.sleep(2)
print "\n[+]Checking sitemap"
cek = requests.get(url+"/sitemap.xml")
if (cek.status_code == 200):
	print "[*] Found [200] /sitemap.xml"
	print "[ "+cek.text+" ]"
else:
	print "[-] Not found"
time.sleep(2)
print "\n[+] Grabbing form"
c=urllib.urlopen(url).read()
b=re.findall("<form(.+?)>",c)
bb=re.findall("<input(.+?)>",c)
for a in b:
	print ">>>>>>>>>>"*5
	print "<form"+a+">"
	for b in bb:	
		print "<input"+b+">"
	print "</form>"
	print ">>>>>>>>>>"*5
	print ""
time.sleep(1)
print "\n[+] Scanning hidden directory"
dir =["KCFinder","files","file","tmp","admin","Admin","image","images","img","a","in","upload","uploads","photos","photo","js","css","backup","backend","downloads","download","temp","panel","pages","slider","php","kcfinder","home","ujian","pdf",".well-knows","documents","Document","document","Documents","plugins","plugin","wp-admin","asset","assets","php","server","backup","component","components","webalizer","A","wp-content","upload","uploaded","wp","wp-includes","wp-login","wp-register","admin/gallery/","admin/photos/","admin/upload/","dashboard","file_upload","About","AboutUs","Administration","Archive","Articles","Dashboard","Login","login","misc","XML","_admin","_images","_mem_bin","_pages","_vti_aut","_vti_bin","_vti_cnf","_vti_log","_vti_pvt","_vti_rpc","sitemaps","sitemap","include","includes","category","content","contents","gallery",".git"]
for file in dir:
	cek = requests.get(url+"/"+file)
	if (cek.status_code == 200):
		print "[*] Found [200] "+"/"+file
	elif (cek.status_code == 403):
		print "[*] Found [403] "+"/"+file
	elif (cek.status_code == 302):
		print "[*] Found [302] "+"/"+file
print "\n[+] Scanning admin login"
adm = ["administrator","webadmin","wp-login.php","painel","cmsadmin","aadmin","login.htm","login.html","login/","adm/","admin/account.html","login.html","admin/login.htm","admin/controlpanel.html","admin/controlpanel.htm","admin/adminLogin.html","admin","adminLogin.htm","admin.htm","admin.html","adminitem","adminitems","administration/","adminLogin/","admin_area/ ","manager/","letmein/","superuser/","access/","sysadm/","superman/","supervisor/","control/","member/","members/ ","user/","cp/","uvpanel/","manage/","management/ ","signin/ ","log-in/ ","log_in/ ","sign_in/ ","sign-in/ ","users/","accounts/","login_userasp","vmailadmin/","globes_admin/","fileadmin/","login_out.php","admin4_colon/","super.php","admin/ vorud.asp","admin_login.php","manager.php","admin/account.asp","admin_area.asp","admin.html ","usr/ ","administr8.php ","SysAdmin2/ ","adminitem.php","login.php ","management/ ","project-admins/","typo3/","admin.htm","admin","home.asp","vorud.php","admins/","accounts/","super_loginphp","super_indexphp","adminpanel.php","memberadmin/","access.asp","superuserphp","systemadministration/","pagesadminadminlogin.asp","paneladministracionlogin.asp","sign_in.php","super_loginasp","moderator.html","log_in/","autologin.php","ysadmin.asp","supermanasp","adminitems.php","admincp.asp","acceso.php","loginredirect/","auth.php","login.asp","Database_Administration/","webadmin.asp","modelsearchlogin.asp","cmsadmin/","admincplogin.asp","phpSQLiteAdmin/","login_admin/","ServerAdministrator/","adminlogin.asp","letmein.asp","member/","acct_login/","loginsuperasp","manage.asp","sign_in/","LiveUser_Admin/","administratoraccounts/","utility_login/","administrator.php","secure/","administratorlogin.asp","checklogin.asp","admin_arealogin.php","authentication.php","UserLogin/","webadmin/","rcLogin/","sub-login","authenticate.asp","login.html","adminadminlogin.php","ss_vms_admin_sm/","SysAdmin/","secret/","login1php","fileadmin.php","controlpanel.php","members.asp","login1asp","irectadmin/","adminlogin.asp","affiliate.asp","adminhome.php","admin.asp","superuser/","Server.php","cpanel/","cp.php","customer_login/","access.php","administratie/","control.asp","autologin/","wplogin/","administratorlogin.php","adminadminlogin.asp","openvpnadmin/","checklogin.php","admin1.html","siteadmin.php","yonetim.asp","supervise","Loginasp","adminitem/","admincontrolpanel.php","authuser.php","modelsearchlogin.php","uradmin.asp","showlogin/","webmaster.php","letmein.php","adminlogin.php","sign_in.asp","sshadmin/","loginasp","checkadmin.php","letmein/","panel.php","simpleLogin/","control/","login/","moderator/","adminlogin.asp","members/","admin_area.php","logoutphp","account.php","bbadmin/","administr8/","relogin.asp","cmsadmin.asp","member.php","adminadminLogin.html","adminpanel/","supermanagerphp","paneladministracion/","relogin.html","signin.asp","adm_auth.php","ezsqliteadmin/","adm.asp","member.asp","admin1.php","radmind/","login_outasp","admin2.php","admin_area/","sqladmin/","administratorlogin/","adminlogin.php","admincontrolpanel.htm","processlogin.asp","administrators.asp","admincp/","SuperAdmin/","kpanel/","log_in.asp","webadmin.php","accounts.asp","checkuser.php","ccp14admin/","newsadmin/","check.asp","manuallogin/","phpmyadmin/","administrators/","autologin.asp","checkuser.asp","acceso.asp","adminitems.asp","auth.asp","super.asp","login_user.php","PSUser/","siteadmin.asp","admin_arealogin.asp","wizmysqladmin/","memberadmin.php","userlogin.asp","siteadmin/","adminarea/","adm/","users.php","superviseLoginphp","manager.asp","users.asp","login.htm","cmsadmin.php","administration.asp","signin/","admin_areaadmin.php","admincontrol.asp","supervise/","adminpanel.asp","super1asp","login_adminphp","webmaster/","signin/","bbadmin/","authadmin.asp","adminadminLogin.asp ","hpwebjetadmin/","super1/","support_login/","login_out/","yonetici.html","administratorlogin.asp","bbadminlogin.php","management.php","administer/","yonetici.php","sysadmin/","Lotus_Domino_Admin/","members.php","administrivia/","authenticate.php"]
for brute in adm:
	try:
		src = requests.get(url+"/"+brute,timeout=20)
		if (src.status_code != 404):
			print "[*] Found ==> "+url+"/"+brute
	except:
		print "[-] Request Time out X==X> "+url+"/"+brute
time.sleep(1)
print ""
print "[+] Reverse Ip"
if (url.startswith("http://")):
	domain = url.replace("http://","").replace("/","")
	cek = requests.get("http://api.hackertarget.com/reverseiplookup/",params={'q':domain}).text
	print cek
time.sleep(1)
print "\n[+] SQL INJECTION check from crawler method"
buka=open("link.txt","rb")
baca=buka.readlines()
for cek in baca:
	if re.search("p?(.*?)=",cek)!=None:
		print "[*] Injection point found ==> "+url+cek
		time.sleep(0.5)
time.sleep(1)
os.system("rm link.txt")
print "[++] Scanning complete"