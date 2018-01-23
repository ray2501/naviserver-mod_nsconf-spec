#
# spec file for package naviserver nsconf module
#

Summary:        NaviServer nsconf module
Name:           naviserver-mod_nsconf
Version:        1.0
Release:        0
License:        MPL-1.1
Group:          Productivity/Networking/Web/Servers
Url:            http://bitbucket.org/naviserver/nsconf
BuildRequires:  naviserver
Requires:       naviserver
Requires:       tcl
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Simple config viewer and generator Module for NaviServer.

%prep
%setup -q %{name}-%{version}

%build

%install
mkdir -p %buildroot/var/lib/naviserver/pages/
cp nsconf.tcl %buildroot/var/lib/naviserver/pages/

%clean
rm -rf %buildroot

%files
%defattr(-,nsadmin,nsadmin,-)
/var/lib/naviserver/pages/nsconf.tcl

%changelog

