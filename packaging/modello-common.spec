Name:       Modello_Common
Summary:    A proof of concept pure html5 UI
Version:    0.0.2
Release:    1
Group:      Applications/System
License:    Apache 2.0
URL:        http://www.tizen.org
Source0:    %{name}-%{version}.tar.bz2
BuildRequires: pkgconfig(libtzplatform-config)

%description
A proof of concept pure html5 UI

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/Modello/Common/
cp -r css %{buildroot}%{_datadir}/Modello/Common/
cp -r js %{buildroot}%{_datadir}/Modello/Common/

%files
%defattr(-,root,root,-)
%{_datadir}/Modello/Common/js
%{_datadir}/Modello/Common/css
