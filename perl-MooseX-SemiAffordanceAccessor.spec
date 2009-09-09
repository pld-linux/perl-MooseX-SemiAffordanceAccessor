#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MooseX
%define	pnam	SemiAffordanceAccessor
Summary:	MooseX::SemiAffordanceAccessor - Name your accessors foo() and set_foo()
Summary(pl.UTF-8):	MooseX::SemiAffordanceAccessor - nazywa metody dostępowe foo() i set_foo()
Name:		perl-MooseX-SemiAffordanceAccessor
Version:	0.05
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4e917185d50a0de2dc9942a643eb76bd
URL:		http://search.cpan.org/dist/MooseX-SemiAffordanceAccessor/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Moose >= 0.55_04
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module does not provide any methods. Simply loading it changes
the default naming policy for the loading class so that accessors are
separated into get and set methods. The get methods have the same name
as the accessor, while set methods are prefixed with "set_".

If you define an attribute with a leading underscore, then the set
method will start with "_set_".

If you explicitly set a "reader" or "writer" name when creating an
attribute, then that attribute's naming scheme is left unchanged.

The name "semi-affordance" comes from David Wheeler's Class::Meta
module.

%description -l pl.UTF-8
Moduł ten nie dostarcza żanych metod. Załadowanie go zmienia domyślną
politykę nazywania dla ładowanych klas, tak że metody dostępowe są
rozdzielone na metody get i set.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MooseX/*.pm
%dir %{perl_vendorlib}/MooseX/SemiAffordanceAccessor/
%dir %{perl_vendorlib}/MooseX/SemiAffordanceAccessor/Role
%{perl_vendorlib}/MooseX/SemiAffordanceAccessor/Role/Attribute.pm
%{_mandir}/man3/*
