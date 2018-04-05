#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pxweb
Version  : 0.6.3
Release  : 2
URL      : https://cran.r-project.org/src/contrib/pxweb_0.6.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pxweb_0.6.3.tar.gz
Summary  : R Interface to the PX-Web/PC-Axis API
Group    : Development/Tools
License  : BSD-2-Clause
Requires: R-RJSONIO
Requires: R-httr
Requires: R-plyr
BuildRequires : R-RJSONIO
BuildRequires : R-data.table
BuildRequires : R-httr
BuildRequires : R-plyr
BuildRequires : clr-R-helpers

%description
API is used by organizations such as Statistics Sweden and Statistics
    Finland to disseminate data. The R package can interact with all
    PX-Web/PC-Axis APIs to fetch information about the data hierarchy, extract
    metadata and extract and parse statistics to R data.frame format. PX-Web is
    a solution to disseminate PC-Axis data files in dynamic tables on the web.
    Since 2013 PX-Web contains an API to disseminate PC-Axis files.

%prep
%setup -q -c -n pxweb

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521178415

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521178415
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pxweb
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pxweb
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pxweb
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library pxweb|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pxweb/CITATION
/usr/lib64/R/library/pxweb/DESCRIPTION
/usr/lib64/R/library/pxweb/INDEX
/usr/lib64/R/library/pxweb/LICENSE
/usr/lib64/R/library/pxweb/Meta/Rd.rds
/usr/lib64/R/library/pxweb/Meta/features.rds
/usr/lib64/R/library/pxweb/Meta/hsearch.rds
/usr/lib64/R/library/pxweb/Meta/links.rds
/usr/lib64/R/library/pxweb/Meta/nsInfo.rds
/usr/lib64/R/library/pxweb/Meta/package.rds
/usr/lib64/R/library/pxweb/Meta/vignette.rds
/usr/lib64/R/library/pxweb/NAMESPACE
/usr/lib64/R/library/pxweb/R/pxweb
/usr/lib64/R/library/pxweb/R/pxweb.rdb
/usr/lib64/R/library/pxweb/R/pxweb.rdx
/usr/lib64/R/library/pxweb/doc/index.html
/usr/lib64/R/library/pxweb/doc/pxweb.R
/usr/lib64/R/library/pxweb/doc/pxweb.Rmd
/usr/lib64/R/library/pxweb/doc/pxweb.html
/usr/lib64/R/library/pxweb/doc/pxweb.md
/usr/lib64/R/library/pxweb/examples/ex_data_mining.R
/usr/lib64/R/library/pxweb/examples/ex_dimension_mining.R
/usr/lib64/R/library/pxweb/examples/ex_get_data.R
/usr/lib64/R/library/pxweb/examples/ex_statfi_getdata.R
/usr/lib64/R/library/pxweb/examples/ex_time_tracking_graphs.R
/usr/lib64/R/library/pxweb/examples/hierarchy.RData
/usr/lib64/R/library/pxweb/extdata/api.json
/usr/lib64/R/library/pxweb/extdata/test_files/responseTest.Rdata
/usr/lib64/R/library/pxweb/extdata/test_files/testFiles.Rdata
/usr/lib64/R/library/pxweb/extras/build.cran.sh
/usr/lib64/R/library/pxweb/extras/document.R
/usr/lib64/R/library/pxweb/help/AnIndex
/usr/lib64/R/library/pxweb/help/aliases.rds
/usr/lib64/R/library/pxweb/help/paths.rds
/usr/lib64/R/library/pxweb/help/pxweb.rdb
/usr/lib64/R/library/pxweb/help/pxweb.rdx
/usr/lib64/R/library/pxweb/html/00Index.html
/usr/lib64/R/library/pxweb/html/R.css
