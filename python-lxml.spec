%define		module	lxml

Summary:	A Pythonic binding for the libxml2 and libxslt libraries
Name:		python-%{module}
Version:	2.3.5
Release:	2
License:	BSD
Group:		Development/Languages/Python
Source0:	http://codespeak.net/lxml/%{module}-%{version}.tgz
# Source0-md5:	d03fb3b9139df7f182afffe72f412c87
URL:		http://codespeak.net/lxml/
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxml is a Pythonic binding for the libxml2 and libxslt libraries.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* CHANGES.txt CREDITS.txt TODO.txt
%dir %{py_sitedir}/lxml
%dir %{py_sitedir}/lxml/html
%dir %{py_sitedir}/lxml/isoschematron
%attr(755,root,root) %{py_sitedir}/lxml/*.so
%{py_sitedir}/lxml/*.h
%{py_sitedir}/lxml/*.pxd
%{py_sitedir}/lxml/*.py[co]
%{py_sitedir}/lxml/html/*.py[co]
%{py_sitedir}/lxml/isoschematron/*.py[co]
%{py_sitedir}/lxml/isoschematron/resources

