#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : keyring
Version  : 9.3.1
Release  : 29
URL      : http://pypi.debian.net/keyring/keyring-9.3.1.tar.gz
Source0  : http://pypi.debian.net/keyring/keyring-9.3.1.tar.gz
Summary  : Store and access your passwords safely.
Group    : Development/Tools
License  : MIT Python-2.0
Requires: keyring-bin
Requires: keyring-python
Requires: pytest
Requires: secretstorage
BuildRequires : fs-python
BuildRequires : hgtools-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pycrypto-python
BuildRequires : pytest-runner-python
BuildRequires : python-dev
BuildRequires : python-keyczar-python
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : secretstorage
BuildRequires : setuptools
BuildRequires : setuptools_scm

%description
=======================================
Installing and Using Python Keyring Lib
=======================================

%package bin
Summary: bin components for the keyring package.
Group: Binaries

%description bin
bin components for the keyring package.


%package python
Summary: python components for the keyring package.
Group: Default

%description python
python components for the keyring package.


%prep
%setup -q -n keyring-9.3.1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487876663
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python setup.py ptr || :
%install
export SOURCE_DATE_EPOCH=1487876663
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/keyring

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
