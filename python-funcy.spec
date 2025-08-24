Name:		python-funcy
Version:	2.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/f/funcy/funcy-%{version}.tar.gz
Summary:	A fancy and practical functional tools library
URL:		https://pypi.org/project/funcy/
License:	BSD
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
A fancy and practical functional tools library

%files
%{py_sitedir}/funcy
%{py_sitedir}/funcy-*.*-info
