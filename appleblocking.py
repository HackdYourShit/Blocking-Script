from subprocess import *

#***********(suixido)*************

var=input("Enter Domain Name:")


#In domain name field we should start by typing: domain="domain name"
#Example: domain=pasteyourdomainname
#and press enter

call(["http", "--form", "POST", "http://128.199.154.155/api/setting/get_setting.php",var] )


#***********16shop blocking script latest 2020*************
