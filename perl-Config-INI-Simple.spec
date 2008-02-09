%define realname   Config-INI-Simple

Name:		perl-%{realname}
Version:    0.02
Release:    %mkrel 1
License:	Artistic and GPL
Group:		Development/Perl
Summary:    Simple reading and writing from an INI file--with preserved comments
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Config/Config-INI-Simple-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel

BuildArch: noarch

%description
Config::INI::Simple is for very simplistic reading and writing of INI files. 
A new object must be created for each INI file (an object keeps all the data 
read in from an INI which is used on the write method to write to the INI).

It also keeps all your comments and original order intact.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%{perl_vendorlib}/Config/
%{_mandir}/man3/*

