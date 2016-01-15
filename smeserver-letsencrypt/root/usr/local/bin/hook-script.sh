#!/bin/bash

# Hook script for letsencrypt.sh for testing with SME Server 9.x

# deploy_cert hook will set config database entries to put to cert files
# and restart appropriate services

# deploy_challenge hook will create challenge file on public-facing server.
# This requires ssh access via public key to the public-facing server.
# This assumes that $REMOTE_PATH already exists on the public-facing server,
# and that its permissions are appropriate (i.e., writable by $USER, and readable
# by the web server).  $REMOTE_PATH should appear to the outside world as
# /.well-known/acme-challenge/

# clean_challenge hook will delete challenge file from public-facing server
# Again, it requires ssh access via public key to that server

if [ $1 = "deploy_cert" ]; then
  KEY=$3
  CERT=$4
  CHAIN=${5/fullchain.pem/chain.pem}
  /sbin/e-smith/db configuration setprop modSSL key $KEY
  /sbin/e-smith/db configuration setprop modSSL crt $CERT
  /sbin/e-smith/db configuration setprop modSSL CertificateChainFile $CHAIN
  /sbin/e-smith/signal-event domain-modify
  /sbin/e-smith/signal-event email-update
  /sbin/e-smith/signal-event ibay-modify
fi

if [ $1 = "deploy_challenge" ]; then
  CHALLENGE_FILE=$3
  CHALLENGE_CONTENT=$4
  HOST="192.168.1.1" # FQDN or IP of public-facing server
  USER="root" # username on public-facing server
  REMOTE_PATH="/home/e-smith/files/ibays/Primary/html/.well-known/acme-challenge"
  if scp $WELLKNOWN/$CHALLENGE_FILE $USER@$HOST:$REMOTE_PATH/$CHALLENGE_FILE ; then
    exit 0
  else
    echo "Failed to deploy challenge!"
    exit 1
  fi    
fi  

if [ $1 = "clean_challenge" ]; then
  CHALLENGE_FILE=$3
  HOST="192.168.1.1" # FQDN or IP of public-facing server
  USER="root" # username on public-facing server
  REMOTE_PATH="/home/e-smith/files/ibays/Primary/html/.well-known/acme-challenge"
  if ssh $USER@$HOST "rm $REMOTE_PATH/$CHALLENGE_FILE" ; then
    exit 0
  else
    echo "Failed to clean challenge!"
    exit 1
  fi    
fi  
