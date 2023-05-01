#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-nleqslv
Version  : 3.3.4
Release  : 48
URL      : https://cran.r-project.org/src/contrib/nleqslv_3.3.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/nleqslv_3.3.4.tar.gz
Summary  : Solve Systems of Nonlinear Equations
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-nleqslv-lib = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
with a choice of global strategies such as line search and trust region.
             There are options for using a numerical or user supplied Jacobian,
             for specifying a banded numerical Jacobian and for allowing
             a singular or ill-conditioned Jacobian.

%package lib
Summary: lib components for the R-nleqslv package.
Group: Libraries

%description lib
lib components for the R-nleqslv package.


%prep
%setup -q -n nleqslv
cd %{_builddir}/nleqslv

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1673896020

%install
export SOURCE_DATE_EPOCH=1673896020
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/nleqslv/DESCRIPTION
/usr/lib64/R/library/nleqslv/INDEX
/usr/lib64/R/library/nleqslv/Meta/Rd.rds
/usr/lib64/R/library/nleqslv/Meta/features.rds
/usr/lib64/R/library/nleqslv/Meta/hsearch.rds
/usr/lib64/R/library/nleqslv/Meta/links.rds
/usr/lib64/R/library/nleqslv/Meta/nsInfo.rds
/usr/lib64/R/library/nleqslv/Meta/package.rds
/usr/lib64/R/library/nleqslv/NAMESPACE
/usr/lib64/R/library/nleqslv/NEWS
/usr/lib64/R/library/nleqslv/R/nleqslv
/usr/lib64/R/library/nleqslv/R/nleqslv.rdb
/usr/lib64/R/library/nleqslv/R/nleqslv.rdx
/usr/lib64/R/library/nleqslv/help/AnIndex
/usr/lib64/R/library/nleqslv/help/aliases.rds
/usr/lib64/R/library/nleqslv/help/nleqslv.rdb
/usr/lib64/R/library/nleqslv/help/nleqslv.rdx
/usr/lib64/R/library/nleqslv/help/paths.rds
/usr/lib64/R/library/nleqslv/html/00Index.html
/usr/lib64/R/library/nleqslv/html/R.css
/usr/lib64/R/library/nleqslv/iterationreport/00readme.txt
/usr/lib64/R/library/nleqslv/iterationreport/dsdbldog.R
/usr/lib64/R/library/nleqslv/iterationreport/dsdbldog.Rout
/usr/lib64/R/library/nleqslv/iterationreport/dsdbldog.Rout.txt
/usr/lib64/R/library/nleqslv/iterationreport/dshook.R
/usr/lib64/R/library/nleqslv/iterationreport/dshook.Rout
/usr/lib64/R/library/nleqslv/iterationreport/dshook.Rout.txt
/usr/lib64/R/library/nleqslv/iterationreport/dslnsrch.R
/usr/lib64/R/library/nleqslv/iterationreport/dslnsrch.Rout
/usr/lib64/R/library/nleqslv/iterationreport/dslnsrch.Rout.txt
/usr/lib64/R/library/nleqslv/iterationreport/dspure.R
/usr/lib64/R/library/nleqslv/iterationreport/dspure.Rout
/usr/lib64/R/library/nleqslv/iterationreport/dspure.Rout.txt
/usr/lib64/R/library/nleqslv/iterationreport/dspwldog.R
/usr/lib64/R/library/nleqslv/iterationreport/dspwldog.Rout
/usr/lib64/R/library/nleqslv/iterationreport/dspwldog.Rout.txt
/usr/lib64/R/library/nleqslv/tests/brdban.R
/usr/lib64/R/library/nleqslv/tests/brdban.Rout
/usr/lib64/R/library/nleqslv/tests/brdban.Rout.save
/usr/lib64/R/library/nleqslv/tests/brdbanded.R
/usr/lib64/R/library/nleqslv/tests/brdbanded.Rout
/usr/lib64/R/library/nleqslv/tests/brdbanded.Rout.save
/usr/lib64/R/library/nleqslv/tests/brdtri.R
/usr/lib64/R/library/nleqslv/tests/brdtri.Rout
/usr/lib64/R/library/nleqslv/tests/brdtri.Rout.save
/usr/lib64/R/library/nleqslv/tests/brdtrijac.R
/usr/lib64/R/library/nleqslv/tests/brdtrijac.Rout
/usr/lib64/R/library/nleqslv/tests/brdtrijac.Rout.save
/usr/lib64/R/library/nleqslv/tests/chquad.R
/usr/lib64/R/library/nleqslv/tests/chquad.Rout
/usr/lib64/R/library/nleqslv/tests/chquad.Rout.save
/usr/lib64/R/library/nleqslv/tests/control-try.R
/usr/lib64/R/library/nleqslv/tests/control-try.Rout.save
/usr/lib64/R/library/nleqslv/tests/dslnex.R
/usr/lib64/R/library/nleqslv/tests/dslnex.Rout
/usr/lib64/R/library/nleqslv/tests/dslnex.Rout.save
/usr/lib64/R/library/nleqslv/tests/dslnexCN.R
/usr/lib64/R/library/nleqslv/tests/dslnexCN.Rout
/usr/lib64/R/library/nleqslv/tests/dslnexCN.Rout.save
/usr/lib64/R/library/nleqslv/tests/dslnexHook.R
/usr/lib64/R/library/nleqslv/tests/dslnexHook.Rout
/usr/lib64/R/library/nleqslv/tests/dslnexHook.Rout.save
/usr/lib64/R/library/nleqslv/tests/dslnexauto.R
/usr/lib64/R/library/nleqslv/tests/dslnexauto.Rout
/usr/lib64/R/library/nleqslv/tests/dslnexauto.Rout.save
/usr/lib64/R/library/nleqslv/tests/dslnexjacout.R
/usr/lib64/R/library/nleqslv/tests/dslnexjacout.Rout
/usr/lib64/R/library/nleqslv/tests/dslnexjacout.Rout.save
/usr/lib64/R/library/nleqslv/tests/dslnexscaled.R
/usr/lib64/R/library/nleqslv/tests/dslnexscaled.Rout
/usr/lib64/R/library/nleqslv/tests/dslnexscaled.Rout.save
/usr/lib64/R/library/nleqslv/tests/singular1.R
/usr/lib64/R/library/nleqslv/tests/singular1.Rout
/usr/lib64/R/library/nleqslv/tests/singular1.Rout.save
/usr/lib64/R/library/nleqslv/tests/singular2.R
/usr/lib64/R/library/nleqslv/tests/singular2.Rout
/usr/lib64/R/library/nleqslv/tests/singular2.Rout.save
/usr/lib64/R/library/nleqslv/tests/singular3.R
/usr/lib64/R/library/nleqslv/tests/singular3.Rout
/usr/lib64/R/library/nleqslv/tests/singular3.Rout.save
/usr/lib64/R/library/nleqslv/tests/trig.R
/usr/lib64/R/library/nleqslv/tests/trig.Rout
/usr/lib64/R/library/nleqslv/tests/trig.Rout.save
/usr/lib64/R/library/nleqslv/tests/tscalargrad.R
/usr/lib64/R/library/nleqslv/tests/tscalargrad.Rout.save
/usr/lib64/R/library/nleqslv/tests/xcutlip1p2.R
/usr/lib64/R/library/nleqslv/tests/xcutlip1p2.Rout
/usr/lib64/R/library/nleqslv/tests/xcutlip1p2.Rout.save
/usr/lib64/R/library/nleqslv/tests/xnames.R
/usr/lib64/R/library/nleqslv/tests/xnames.Rout
/usr/lib64/R/library/nleqslv/tests/xnames.Rout.save
/usr/lib64/R/library/nleqslv/tests/xsearchzeros.R
/usr/lib64/R/library/nleqslv/tests/xsearchzeros.Rout
/usr/lib64/R/library/nleqslv/tests/xsearchzeros.Rout.save
/usr/lib64/R/library/nleqslv/tests/xtestnslv.R
/usr/lib64/R/library/nleqslv/tests/xtestnslv.Rout
/usr/lib64/R/library/nleqslv/tests/xtestnslv.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/nleqslv/libs/nleqslv.so
/usr/lib64/R/library/nleqslv/libs/nleqslv.so.avx2
/usr/lib64/R/library/nleqslv/libs/nleqslv.so.avx512
