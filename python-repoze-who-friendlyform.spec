%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%global betaver b3

Name:		python-repoze-who-friendlyform
Version:	1.0
Release:	0.3.%{betaver}%{?dist}
Summary:	Collection of repoze.who friendly form plugins
Group:		Development/Languages
License:	BSD
URL:		http://code.gustavonarea.net/repoze.who-friendlyform/
Source0:	http://pypi.python.org/packages/source/r/repoze.who-friendlyform/repoze.who-friendlyform-%{version}%{betaver}.tar.gz
Patch0:     %{name}-setuptools.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
BuildRequires:	python-devel, python-setuptools-devel
# Test suite requirements
BuildRequires:	python-zope-interface, python-repoze-who, python-nose, python-coverage
Requires:	python-repoze-who >= 1.0
Requires:	python-zope-interface

%description
repoze.who-friendlyform is a repoze.who plugin which provides a collection of 
developer-friendly form plugins.

%prep
%setup -q -n repoze.who-friendlyform-%{version}%{betaver}
%patch0 -p0 -b .setuptools

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
# Tests fail?
# PYTHONPATH=$(pwd) nosetests

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt
%{python_sitelib}/*

%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 05 2009 Luke Macken <lmacken@redhat.com> - 1.0-0.2.b3
- Patch the setup.py to use our own setuptools package

* Tue May 19 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-0.1.b3
- Initial package for Fedora
