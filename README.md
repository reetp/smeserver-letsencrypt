# smeserver-letsencrypt
A contrib to use letsencrypt certificates on Koozali SME Server

yum --enablerepo=reetp install smeserver-letsencrypt

To make sure the httpd template is expanded run

signal-event post-upgrade;signal-event reboot

Set the letsencrypt service

This can have one of 3 states. Make sure you set to test until you are sure of you have everything correct to avoid overloading the service
config setprop letsencypt status disabled | enabled | test

First set it to test
config setprop letsencrypt status test

Optional keys - (not required)

config setprop letsencypt email (defaults to empty)  
config setprop letsencypt keysize (defaults to 4096)  

You need to enable a domain and a host on the domain

Per domain 
db domains setprop mydomain.com letsencryptSSLcert enabled

Per host (domain has to be enabled first)
db hosts setprop www.mydomain.com letsencryptSSLcert enabled

If you want a hook script to push changes remotely (not required)

db configuration setprop letsencrypt hookScript enabled  
db configuration setprop letsencrypt user someuser  
db configuration setprop letsencrypt host 1.2.3.4
db configuration setprop letsencrypt path //some/remote/local/path  

Then run

signal-event console-save

Create or test create certificates (file is in the path so should be OK)

letsencrypt.sh -c

Once you are satisfied with your test

config setprop letsencrypt status test

signal-event console-save

and

letsencrypt.sh -c
  
ToDo

