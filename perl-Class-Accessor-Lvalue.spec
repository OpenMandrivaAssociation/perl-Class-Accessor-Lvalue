%define upstream_name    Class-Accessor-Lvalue
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Class-Accessor-Lvalue module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/R/RC/RCLAMP/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Want)
BuildRequires:	perl(Class::Accessor)
BuildArch:	noarch
# README says this is a dependency and automatic rpm dependencies
# are not catching this
Requires:	perl(Class::Accessor)

%description
This module subclasses Class::Accessor in order to provide lvalue
accessor makers.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Class/Accessor/Lvalue.pm
%{perl_vendorlib}/Class/Accessor/Lvalue
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 680778
- mass rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 402279
- update to 0.56
- update to 0.56

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.11-4mdv2009.0
+ Revision: 241171
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-2mdv2008.0
+ Revision: 86070
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.11-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.11-1mdk
- initial Mandriva package

