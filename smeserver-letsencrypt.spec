%define name smeserver-letsencrypt
%define version 0.1
%define release 2
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
Let’s Encrypt is a free, automated, and open certificate authority

%changelog
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

echo "After install please set your db keys"
echo "Make sure you set the letsencrypt status key to test"
echo "Set the modSSL keys"
echo "Enable some domains and hosts"
echo "Then run the following"
echo "signal-event console-save"
echo "letsencrypt.sh -c create new certs"
echo "Once you are satisfied set the status key to enabled"
echo "run the letesencypt.sh file again to generate you keys"
echo "change your status back to test"

%postun
