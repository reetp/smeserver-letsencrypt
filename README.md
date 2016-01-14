# smeserver-letsencrypt
A contrib to use letsencrypt certificates on Koozali SME Server

yum --enablerepo=reetp install smeserver-letsencrypt

This should not need a reboot so :

config set UnsavedChanges no

Set the letsencrypt service
This can have one of 3 states. Make sure you set to test until you are sure of you have everything correct to avoid overloading the service

config set letsencrypt service status disabled

config setprop letsencypt status disabled | enabled | test 
config setprop letsencypt email (defaults to empty) 
config setprop letsencypt keysize (defaults to 4096) 


Set these keys to your primary domain
db configuration setprop modSSL crt /etc/letsencrypt.sh/certs/{mydomain.com}/cert.pem
db configuration setprop modSSL key /etc/letsencrypt.sh/certs/{mydomain.com}/privkey.pem
db configuration setprop modSSL CertificateChainFile /etc/letsencrypt.sh/certs/{mydomain.com}/fullchain.pem

Per domain 
db domains setprop mydomain.com letsencryptSSLcert enabled

Per host
db hosts setprop www.mydomain.com letsencryptSSLcert enabled

Expanding templates
expand-template expand-template /etc/letsencrypt.sh/domains.txt
cat /etc/letsencrypt.sh/domains.txt

expand-template /etc/letsencrypt.sh/config.sh
cat /etc/letsencrypt.sh/config.sh

Create or test create certificates (files is in the path so should be OK)
config show 

ToDo

