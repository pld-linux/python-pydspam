Summary:	Python interface for dspam library
Summary(pl.UTF-8):	Interfejs Pythona do biblioteki dspam
%define	module	pydspam
Name:		python-%{module}
Version:	1.1.9
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pymilter/%{module}-%{version}.tar.gz
# Source0-md5:	1caff10d2fa3968ed8e0def126f74b40
Patch0:		%{name}-setup.patch
URL:		http://www.bmsi.com/python/dspam.html
BuildRequires:	dspam-devel
BuildRequires:	python-devel >= 2.2.1
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python interface for dspam library.

%description -l pl.UTF-8
Interfejs Pythona do biblioteki dspam.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS dspam.html
%attr(755,root,root) %{py_sitedir}/*.so
