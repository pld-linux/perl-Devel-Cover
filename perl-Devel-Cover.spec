#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	Cover
Summary:	Devel::Cover - Code coverage metrics for Perl
Summary(pl.UTF-8):	Devel::Cover - metryki pokrycia kodu dla Perla
Name:		perl-Devel-Cover
Version:	0.79
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
#Source0:	http://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
Source0:	http://sunsite.icm.edu.pl/pub/CPAN//modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	476037bb7dc7b075de355832de16f2ca
URL:		http://search.cpan.org/dist/Devel-Cover/
BuildRequires:	perl-devel >= 1:5.8.0
%{?with_tests:BuildRequires:	perl-Test-Warn}
BuildRequires:	rpm-perlprov >= 4.1-13
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
%doc README
%{perl_vendorarch}/Devel/*.pm
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
%{perl_vendorarch}/auto/Devel/Cover/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Devel/Cover/*.so
%{_mandir}/man3/*
%attr(755,root,root) %{_bindir}/cover
%attr(755,root,root) %{_bindir}/cpancover
%attr(755,root,root) %{_bindir}/gcov2perl
%{_mandir}/man1/*
