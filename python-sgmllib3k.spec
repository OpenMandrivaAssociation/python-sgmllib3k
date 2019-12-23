# Created by pyp2rpm-3.2.2
%global pypi_name sgmllib3k
%define version 1.0.0

Name:           python3-sgmllib3k
Version:        %{version}
Release:        %mkrel 4
Group:          Development/Python
Summary:        Py3k port of sgmllib

License:        BSD License
URL:            http://hg.hardcoded.net/sgmllib
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools


%description
 sgmllib3k -- Py3k port of the old stdlib module sgmllib was dropped in Python
3. For those depending on it, that's somewhat infortunate. This is a quick and
dirty port of this old module. I just ran 2to3 on it and published it. I don't
indend to maintain it, so it might be a good idea to eventually think about
finding another module to use.


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info



%build
%{__python3} setup.py build


%install
%{__python3} setup.py install --skip-build --root %{buildroot}


%files
%doc
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/sgmllib.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
