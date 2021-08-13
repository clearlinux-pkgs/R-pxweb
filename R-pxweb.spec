#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pxweb
Version  : 0.11.0
Release  : 38
URL      : https://cran.r-project.org/src/contrib/pxweb_0.11.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pxweb_0.11.0.tar.gz
Summary  : R Interface to PXWEB APIs
Group    : Development/Tools
License  : BSD-2-Clause
Requires: R-checkmate
Requires: R-httr
Requires: R-jsonlite
BuildRequires : R-checkmate
BuildRequires : R-data.table
BuildRequires : R-httr
BuildRequires : R-jsonlite
BuildRequires : buildreq-R

%description
API is used by organizations such as Statistics Sweden and Statistics
    Finland to disseminate data. The R package can interact with all
    PX-Web/PC-Axis APIs to fetch information about the data hierarchy, extract
    metadata and extract and parse statistics to R data.frame format. PX-Web is
    a solution to disseminate PC-Axis data files in dynamic tables on the web.
    Since 2013 PX-Web contains an API to disseminate PC-Axis files.

%prep
%setup -q -c -n pxweb
cd %{_builddir}/pxweb

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1625758190

%install
export SOURCE_DATE_EPOCH=1625758190
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc pxweb || :


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
/usr/lib64/R/library/pxweb/NEWS.md
/usr/lib64/R/library/pxweb/R/pxweb
/usr/lib64/R/library/pxweb/R/pxweb.rdb
/usr/lib64/R/library/pxweb/R/pxweb.rdx
/usr/lib64/R/library/pxweb/doc/index.html
/usr/lib64/R/library/pxweb/doc/pxweb.R
/usr/lib64/R/library/pxweb/doc/pxweb.Rmd
/usr/lib64/R/library/pxweb/doc/pxweb.html
/usr/lib64/R/library/pxweb/examples/ex_data_mining.R
/usr/lib64/R/library/pxweb/examples/ex_dimension_mining.R
/usr/lib64/R/library/pxweb/examples/ex_get_data.R
/usr/lib64/R/library/pxweb/examples/ex_statfi_getdata.R
/usr/lib64/R/library/pxweb/examples/ex_time_tracking_graphs.R
/usr/lib64/R/library/pxweb/examples/hierarchy.RData
/usr/lib64/R/library/pxweb/extdata/api.json
/usr/lib64/R/library/pxweb/extdata/examples/json-stat_query_example.json
/usr/lib64/R/library/pxweb/extdata/examples/json_big_query_example.json
/usr/lib64/R/library/pxweb/extdata/examples/json_query_agg_example.json
/usr/lib64/R/library/pxweb/extdata/examples/json_query_example.json
/usr/lib64/R/library/pxweb/extdata/examples/json_query_last_names.json
/usr/lib64/R/library/pxweb/extdata/examples/json_query_variables_example.json
/usr/lib64/R/library/pxweb/extdata/test_files/json_queries/json_full_test_query.json
/usr/lib64/R/library/pxweb/extdata/test_files/json_queries/json_single_query_test.json
/usr/lib64/R/library/pxweb/extdata/test_files/responseTest.Rdata
/usr/lib64/R/library/pxweb/extdata/test_files/testFiles.Rdata
/usr/lib64/R/library/pxweb/extras/build.cran.sh
/usr/lib64/R/library/pxweb/extras/cheatsheet_pxweb.pptx
/usr/lib64/R/library/pxweb/extras/document.R
/usr/lib64/R/library/pxweb/help/AnIndex
/usr/lib64/R/library/pxweb/help/aliases.rds
/usr/lib64/R/library/pxweb/help/paths.rds
/usr/lib64/R/library/pxweb/help/pxweb.rdb
/usr/lib64/R/library/pxweb/help/pxweb.rdx
/usr/lib64/R/library/pxweb/html/00Index.html
/usr/lib64/R/library/pxweb/html/R.css
/usr/lib64/R/library/pxweb/tests/testthat.R
/usr/lib64/R/library/pxweb/tests/testthat/log_pxweb_api_http_calls.txt
/usr/lib64/R/library/pxweb/tests/testthat/test-README.R
/usr/lib64/R/library/pxweb/tests/testthat/test-defunct.R
/usr/lib64/R/library/pxweb/tests/testthat/test-pxweb_api_catalogue.R
/usr/lib64/R/library/pxweb/tests/testthat/test-pxweb_api_paths.R
/usr/lib64/R/library/pxweb/tests/testthat/test-pxweb_as_dataframe.R
/usr/lib64/R/library/pxweb/tests/testthat/test-pxweb_constructor.R
/usr/lib64/R/library/pxweb/tests/testthat/test-pxweb_data_comments.R
/usr/lib64/R/library/pxweb/tests/testthat/test-pxweb_get.R
/usr/lib64/R/library/pxweb/tests/testthat/test-pxweb_interactive.R
/usr/lib64/R/library/pxweb/tests/testthat/test-pxweb_query.R
/usr/lib64/R/library/pxweb/tests/testthat/test-pxweb_test_api.R
/usr/lib64/R/library/pxweb/tests/testthat/test_data/filter_query.json
/usr/lib64/R/library/pxweb/tests/testthat/test_data/pxm1_test.rda
