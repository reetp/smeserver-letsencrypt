# smeserver-letsencrypt

A contrib to use letsencrypt certificates on Koozali SME Server

Note that we call this contrib 'smeserver-letsencrypt because it installs letsencrypt support

Also note that due to either ignorance or stupidity by people or peoples unknown at LE, the script that this plugin uses has had to be renamed from letsencrypt.sh to dehydrated.

I can only presume that money talks and LE enforced some copyright madness on the script name.

Whatever next ? I can't use feckbook.sh to remove feckbook crap out of a system for instance ? I digress.

yum --enablerepo=reetp install smeserver-letsencrypt

To make sure the httpd template is expanded run

signal-event post-upgrade;signal-event reboot

Set the letsencrypt service

This can have one of 3 states. Make sure you set to test until you are sure of you have everything correct to avoid overloading the service

config setprop letsencrypt status disabled | enabled | test

First set it to test
config setprop letsencrypt status test

Optional keys - (not required)

config setprop letsencrypt email (defaults to empty)  
config setprop letsencrypt keysize (defaults to 4096)

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

dehydrated -c

Once you are satisfied with your test

config setprop letsencrypt status enabled

signal-event console-save

and

mv /etc/dehydrated/private_key.pem /etc/dehydrated/private_key.test

dehydrated -c -x

Note thereafter you ONLY need to run

dehydrated -c

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

Errors

If you see:

 ERROR: Problem connecting to server (get for https://acme-v01.api.letsencrypt.org/directory; curl returned with 6)

Try this:

 curl https://acme-v01.api.letsencrypt.org/directory

It should show something like this:

 [root@test ~]# curl https://acme-v01.api.letsencrypt.org/directory
 {
   "new-authz": "https://acme-v01.api.letsencrypt.org/acme/new-authz",
   "new-cert": "https://acme-v01.api.letsencrypt.org/acme/new-cert",
   "new-reg": "https://acme-v01.api.letsencrypt.org/acme/new-reg",
   "revoke-cert": "https://acme-v01.api.letsencrypt.org/acme/revoke-cert"
 }


 warning:    erase unlink of /usr/local/bin/config.sh failed: No such file or directory
 
This is due to the original config.sh file being renamed/moved and the rpm cannot find it during package update/replacement
It is log noise and can safely be ignored.

ToDo

