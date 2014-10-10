%define realname   Config-INI-Simple

Name:		perl-%{realname}
Version:    0.02
Release:    6
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



%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.02-5mdv2011.0
+ Revision: 680841
- mass rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.02-4mdv2011.0
+ Revision: 430337
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.02-3mdv2009.0
+ Revision: 256090
- rebuild

* Sat Feb 09 2008 Funda Wang <fwang@mandriva.org> 0.02-1mdv2008.1
+ Revision: 164418
- update to new version 0.02

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 07 2007 Michael Scherer <misc@mandriva.org> 0.01-2mdv2008.0
+ Revision: 81738
- rebuild


* Wed Aug 09 2006 Michael Scherer <misc@mandriva.org> 0.01-1mdv2007.0
- First Mandriva package

