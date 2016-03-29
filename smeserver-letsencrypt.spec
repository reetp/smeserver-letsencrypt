%define name smeserver-letsencrypt
%define version 0.1
<<<<<<< HEAD
%define release 17
=======
%define release 20
>>>>>>> cd009772435e33e240a4e3aa23f0b189b5a40f52
Summary: Plugin to enable letsencrypt certificates
Name: %{name}
Version: %{version}
Release: %{release}
License: GNU GPL version 2
URL: http://libreswan.org/
Group: SMEserver/addon
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
Requires:  e-smith-release >= 8.0
AutoReqProv: no

%description
Lets Encrypt is a free, automated, and open certificate authority
https://letsencrypt.org/

%changelog
<<<<<<< HEAD
* Tue Mar 29 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-17
- modify hook script templates as per Dan Browd contribution
=======
* Thu Mar 17 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-20
- updated letsencrypt.sh
- https://github.com/lukas2511/letsencrypt.sh/commit/429c5250ede7ff4af3b6f37b39925cfa5afee278
- Add "" to wellknown path in config.sh

* Fri Feb 05 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-19
- updated letsencrypt.sh
- https://github.com/lukas2511/letsencrypt.sh/commit/21c18dd3b8c2572b894d9ec2e5c3fc2589f56f32

* Tue Jan 26 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-18
- updated letsencrypt.sh
- https://github.com/lukas2511/letsencrypt.sh/commit/79ff846e267c30d85988f79f58b81bc7bd91790c

* Sat Jan 23 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-17
- Fix typos in hook-script
- Add latest letsencrypt.sh script
>>>>>>> cd009772435e33e240a4e3aa23f0b189b5a40f52

* Wed Jan 20 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-16
- Minor fixes including typo in cron.daily

* Tue Jan 19 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-15
- Missed a "
- remove ' from Let's encrypt and add URL

* Tue Jan 19 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-14
- Updated readme and install notes
- Allow either domains or hosts

* Mon Jan 18 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-13
- Add missing templates.metadata file
- modify spec file wording

* Mon Jan 18 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-12
- Set hookscript to always run unless letsencrypt is disabled
- Add cron.daily script to console-save action and set perms

* Sun Jan 17 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-11
- Fix hook-script.sh perms using templates.metadata

* Sun Jan 17 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-10
- Add latest revision of letsencrypt.sh
- add hookscript.sh templates and various fixes

* Sat Jan 16 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-9
- Add latest revision of letsencrypt.sh

* Fri Jan 15 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-8
- set +x on hook-script and correct file name in config

* Fri Jan 15 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-7
- Add missing curly brace
- Move Status check line up so we can generate empty file if disabled

* Fri Jan 15 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-6
- Add hookScript key

* Fri Jan 15 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-5
- Modify spec file to add paths and set permisssions

* Thu Jan 14 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-4
- Modify file paths and cron script

* Thu Jan 14 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-3
- updated bash script in spec file
- updated file locations in README.MD

* Wed Jan 13 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-2
- Moved config.sh file location
- added cron.daily template - only works if letsencrypt is enabled
- added check to create /etc/letsencrypt.sh directory if it does not exist
- added latest letsencrypt.sh script

* Thu Jan 07 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-1
- initial release

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING" >> %{name}-%{version}-filelist


%clean
cd ..
rm -rf %{name}-%{version}

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%pre

%preun

%post
if [[ ! -e /etc/letsencrypt.sh ]];
then mkdir /etc/letsencrypt.sh;
fi

if [[ ! -e /home/e-smith/files/ibays/Primary/html/.well-known/acme-challenge ]];
then mkdir -p /home/e-smith/files/ibays/Primary/html/.well-known/acme-challenge;
fi

chmod -R 0775  /home/e-smith/files/ibays/Primary/html/.well-known
chown -R apache:shared /home/e-smith/files/ibays/Primary/html/.well-known


echo "###################################################################"
echo "# After install please set your db keys"
echo "# Make sure you set the letsencrypt status key to test"
echo "# Enable some domains or hosts"
echo "# Then run the following"
echo "# signal-event console-save"
echo "# letsencrypt.sh -c"
echo "# Once you are satisfied set the letsencrypt status key to enabled"
echo "# mv /etc/letsencrypt.sh/private_key.pem /etc/letsencrypt.sh/private_key.test"
echo "# Run the letesencypt.sh file again to generate your keys"
echo "# signal-event console-save"
echo "# letsencrypt.sh -c -x"
echo "# Thereafter only use"
echo "# letsencrypt.sh -c"
echo "# If you make any key changes run console-save first"
echo "###################################################################"

%postun
