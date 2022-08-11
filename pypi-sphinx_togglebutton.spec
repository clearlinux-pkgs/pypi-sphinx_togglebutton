#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-sphinx_togglebutton
Version  : 0.3.2
Release  : 8
URL      : https://files.pythonhosted.org/packages/f0/df/d151dfbbe588116e450ca7e898750cb218dca6b2e557ced8de6f9bd7242b/sphinx-togglebutton-0.3.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/f0/df/d151dfbbe588116e450ca7e898750cb218dca6b2e557ced8de6f9bd7242b/sphinx-togglebutton-0.3.2.tar.gz
Summary  : Toggle page content and collapse admonitions in Sphinx.
Group    : Development/Tools
License  : MIT
Requires: pypi-sphinx_togglebutton-license = %{version}-%{release}
Requires: pypi-sphinx_togglebutton-python = %{version}-%{release}
Requires: pypi-sphinx_togglebutton-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(docutils)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(sphinx)
BuildRequires : pypi(wheel)

%description
# sphinx-togglebutton
A small sphinx extension to make it possible to add a "toggle button" to
sections of your page. This allows you to:

%package license
Summary: license components for the pypi-sphinx_togglebutton package.
Group: Default

%description license
license components for the pypi-sphinx_togglebutton package.


%package python
Summary: python components for the pypi-sphinx_togglebutton package.
Group: Default
Requires: pypi-sphinx_togglebutton-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinx_togglebutton package.


%package python3
Summary: python3 components for the pypi-sphinx_togglebutton package.
Group: Default
Requires: python3-core
Provides: pypi(sphinx_togglebutton)
Requires: pypi(docutils)
Requires: pypi(setuptools)
Requires: pypi(sphinx)
Requires: pypi(wheel)

%description python3
python3 components for the pypi-sphinx_togglebutton package.


%prep
%setup -q -n sphinx-togglebutton-0.3.2
cd %{_builddir}/sphinx-togglebutton-0.3.2
pushd ..
cp -a sphinx-togglebutton-0.3.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1658959151
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sphinx_togglebutton
cp %{_builddir}/sphinx-togglebutton-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sphinx_togglebutton/04f302f55e177936c00dce6b36ca9cf0c4e007ff
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sphinx_togglebutton/04f302f55e177936c00dce6b36ca9cf0c4e007ff

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
