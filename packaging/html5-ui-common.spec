Name:       html5_UI_Common
Summary:    A proof of concept pure html5 UI
Version:    0.0.1
Release:    1
Group:      Applications/System
License:    Apache 2.0
URL:        http://www.tizen.org
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  zip
Requires:   wrt-installer
Requires:   wrt-plugins-ivi

%description
A proof of concept pure html5 UI

%prep
%setup -q -n %{name}-%{version}

%build

#make wgtPkg

%install
rm -rf %{buildroot}
%make_install

%post
    #wrt-installer -i /opt/usr/apps/.preinstallWidgets/html5_UI_Common.wgt;

%postun
    #TODO: Delete the common files
    #wrt-installer -un html5POC01.html5_UI_Common

%files
%defattr(-,root,root,-)
/opt/usr/apps/_common/*
