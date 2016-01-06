#!/bin/bash
# config.sh

WELLKNOWN=/home/e-smith/files/ibays/Primary/html/.well-known/acme-challenge

# Use staging directory
CA="https://acme-staging.api.letsencrypt.org/directory"

# Base directory for account key, generated certificates and list of domains (default: $SCRIPTDIR -- uses config directory if undefined)
#BASEDIR=$SCRIPTDIR
BASEDIR="/etc/letsencrypt"

# Location of private account key (default: $BASEDIR/private_key.pem)
#PRIVATE_KEY="${BASEDIR}/private_key.pem"

# Default keysize for private keys (default: 4096)
#KEYSIZE="4096"

# E-mail to use during the registration (default: <unset>)
#CONTACT_EMAIL=
