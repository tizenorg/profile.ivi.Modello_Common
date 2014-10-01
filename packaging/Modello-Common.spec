Name:       Modello-Common
Summary:    Pure html5 UI
Version:    0.0.2
Release:    0
Group:      Automotive/Modello
License:    Apache-2.0
URL:        http://www.tizen.org
Source0:    %{name}-%{version}.tar.bz2
Source1001: Modello-Common.manifest

BuildRequires:  fdupes

BuildArchitectures: noarch

%description
A proof of concept pure html5 UI

%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1001} .

%build
#empty

%install
mkdir -p %{buildroot}%{_datadir}/Modello/Common/
cp -r css %{buildroot}%{_datadir}/Modello/Common/
cp -r js %{buildroot}%{_datadir}/Modello/Common/

%fdupes %{buildroot}%{_datadir}

%files
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_datadir}/Modello/Common/js
%{_datadir}/Modello/Common/css
