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

If the licence changes before this script is updated you can specify a new licence URL:
config setprop letsencrypt licence https://letsencrypt.org/documents/LE-SA-v1.0.1-July-27-2015.pdf

You can enable just a domain or just a host on a domain

Per domain 
db domains setprop mydomain.com letsencryptSSLcert enabled

Per host 
db hosts setprop www.mydomain.com letsencryptSSLcert enabled

If you want a hook script to push changes remotely (not required)

db configuration setprop letsencrypt hookScript enabled  
db configuration setprop letsencrypt user someuser  
db configuration setprop letsencrypt host 1.2.3.4
db configuration setprop letsencrypt path //some/remote/local/path  

Then run

signal-event console-save

Create test certificates (file is in the path so should be OK)

letsencrypt.sh -c

Once you are satisfied with your test

config setprop letsencrypt status enabled

signal-event console-save

and

mv /etc/letsencrypt.sh/private_key.pem /etc/letsencrypt.sh/private_key.test

letsencrypt.sh -c -x

Note thereafter you ONLY need to run

letsencrypt.sh -c

If you make any db key changes run console-save to regenerate your config files

You can now set any public ibays to SSL only using the server manager, or set the following key:

db accounts setprop {accountname} SSL enabled

You cannot set the Primary ibay to SSL from the panel:

db accounts setprop Primary SSL enabled

signal-event console-save 

or

signal-event ibay-modify Primary

You can now use a db entry to set all domains or hosts regardless of status

config setprop letsencrypt configure none| all | domains | hosts

default is none

If you set to domains it will enable ALL domains regardless of individual settings. Hosts will be per host as normal.
If you set to hosts it will enable ALL hosts regardless of individual settings. Domains will be per domain as normal
If you set to all it will enable ALL hosts AND domains regardless of individual settings.


ToDo

