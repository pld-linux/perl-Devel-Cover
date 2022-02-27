#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define	pdir	Devel
%define	pnam	Cover
Summary:	Devel::Cover - Code coverage metrics for Perl
Summary(pl.UTF-8):	Devel::Cover - metryki pokrycia kodu dla Perla
Name:		perl-Devel-Cover
Version:	1.36
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3430734551004b6b7e46505d1d9578a0
URL:		https://metacpan.org/release/Devel-Cover
BuildRequires:	perl-devel >= 1:5.10.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-B-Debug
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-HTML-Parser >= 3.69
BuildRequires:	perl-JSON-MaybeXS
BuildRequires:	perl-Moo
BuildRequires:	perl-Sereal-Decoder
BuildRequires:	perl-Sereal-Encoder
BuildRequires:	perl-Storable
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Test-Warn
%endif
Requires:	perl-modules >= 1:5.8.2
Suggests:	perl-Browser-Open
Suggests:	perl-JSON-PP
Suggests:	perl-PPI-HTML >= 1.07
Suggests:	perl-Pod-Coverage >= 0.06
Suggests:	perl-Template-Toolkit >= 2.00
Suggests:	perl-Test-Differences
Suggests:	perltidy >= 20060719
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides code coverage metrics for Perl. Code coverage
metrics describe how thoroughly tests exercise code. By using
Devel::Cover you can find areas of code not exercised by your tests
and find out which tests to create to increase coverage. Code coverage
can be considered as an indirect measure of quality.

%description -l pl.UTF-8
Ten moduł udostępnia metryki pokrycia kodu dla Perla. Metryki te
opisują jak dokładnie testy sprawdzają kod. Dzięki użyciu Devel::Cover
można odnaleźć obszary kodu nie sprawdzane przez testy i określić,
jakie testy należy stworzyć, aby zwiększyć pokrycie. Pokrycie kodu
można uznać jako niebezpośrednią miarę jakości.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/cover
%attr(755,root,root) %{_bindir}/cpancover
%attr(755,root,root) %{_bindir}/gcov2perl
%{perl_vendorarch}/Devel/Cover.pm
%dir %{perl_vendorarch}/Devel/Cover
%{perl_vendorarch}/Devel/Cover/*.pm
%dir %{perl_vendorarch}/Devel/Cover/Annotation
%{perl_vendorarch}/Devel/Cover/Annotation/*.pm
%dir %{perl_vendorarch}/Devel/Cover/DB
%{perl_vendorarch}/Devel/Cover/DB/*.pm
%dir %{perl_vendorarch}/Devel/Cover/DB/IO
%{perl_vendorarch}/Devel/Cover/DB/IO/*.pm
%dir %{perl_vendorarch}/Devel/Cover/Report
%{perl_vendorarch}/Devel/Cover/Report/*.pm
# Some people may appreciate Tutorial in pod form
# or move to subpackage?
%{perl_vendorarch}/Devel/Cover/Tutorial.pod
%dir %{perl_vendorarch}/auto/Devel/Cover
%attr(755,root,root) %{perl_vendorarch}/auto/Devel/Cover/*.so
%{_mandir}/man3/Devel::Cover*.3pm*
%{_mandir}/man1/cover.1p*
%{_mandir}/man1/cpancover.1p*
%{_mandir}/man1/gcov2perl.1p*
