# Created by pyp2rpm-3.2.2
%global pypi_name sgmllib3k

Name:           python-sgmllib3k
Version:        1.0.0
Release:        3
Group:          Development/Python
Summary:        Py3k port of sgmllib

License:        BSD License
URL:            http://hg.hardcoded.net/sgmllib
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools

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
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%doc
%{python_sitelib}/sgmllib.py
%{python_sitelib}/%{pypi_name}-%{version}-py*.*.egg-info
