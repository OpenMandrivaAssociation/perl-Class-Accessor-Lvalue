%define upstream_name    Class-Accessor-Lvalue
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_name}
Release:	%mkrel 1

Summary:	Class-Accessor-Lvalue module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires: perl-Want
BuildRequires: perl-Class-Accessor
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
# README says this is a dependency and automatic rpm dependencies
# are not catching this
Requires:	perl-Class-Accessor

%description
This module subclasses Class::Accessor in order to provide lvalue
accessor makers.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class/Accessor/Lvalue.pm
%{perl_vendorlib}/Class/Accessor/Lvalue
%{_mandir}/*/*
