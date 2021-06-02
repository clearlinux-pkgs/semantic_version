#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : semantic_version
Version  : 2.8.5
Release  : 43
URL      : https://files.pythonhosted.org/packages/d4/52/3be868c7ed1f408cb822bc92ce17ffe4e97d11c42caafce0589f05844dd0/semantic_version-2.8.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/d4/52/3be868c7ed1f408cb822bc92ce17ffe4e97d11c42caafce0589f05844dd0/semantic_version-2.8.5.tar.gz
Summary  : A library implementing the 'SemVer' scheme.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: semantic_version-license = %{version}-%{release}
Requires: semantic_version-python = %{version}-%{release}
Requires: semantic_version-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
python-semanticversion
======================
This small python library provides a few tools to handle `SemVer`_ in Python.
It follows strictly the 2.0.0 version of the SemVer scheme.

%package license
Summary: license components for the semantic_version package.
Group: Default

%description license
license components for the semantic_version package.


%package python
Summary: python components for the semantic_version package.
Group: Default
Requires: semantic_version-python3 = %{version}-%{release}

%description python
python components for the semantic_version package.


%package python3
Summary: python3 components for the semantic_version package.
Group: Default
Requires: python3-core
Provides: pypi(semantic_version)

%description python3
python3 components for the semantic_version package.


%prep
%setup -q -n semantic_version-2.8.5
cd %{_builddir}/semantic_version-2.8.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588191346
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/semantic_version
cp %{_builddir}/semantic_version-2.8.5/LICENSE %{buildroot}/usr/share/package-licenses/semantic_version/a70ef24806317169e4539b723cad891e08cf1783
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/semantic_version/a70ef24806317169e4539b723cad891e08cf1783

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
