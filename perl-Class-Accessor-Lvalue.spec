%define real_name Class-Accessor-Lvalue

Summary:	Class-Accessor-Lvalue module for perl 
Name:		perl-%{real_name}
Version:	0.11
Release:	%mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel, perl-Want, perl-Class-Accessor
# README says this is a dependency and automatic rpm dependencies
# are not catching this
Requires:	perl-Class-Accessor
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module subclasses Class::Accessor in order to provide lvalue
accessor makers.

%prep
%setup -q -n %{real_name}-%{version} 

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


