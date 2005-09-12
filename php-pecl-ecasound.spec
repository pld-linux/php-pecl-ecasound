%define		_modname	ecasound
%define		_modname_c	Ecasound
%define		_status		beta
Summary:	%{_modname} - audio recording and processing functions
Summary(pl):	%{_modname} - funkcje do nagrywania i przetwarzania d¼wiêku
Name:		php-pecl-%{_modname}
Version:	0.2
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname_c}-%{version}.tgz
# Source0-md5:	002e7bb8c0f018bb41cefc71e5f9f54b
Patch0:		%{name}-search_path.patch
URL:		http://pecl.php.net/package/ecasound/
BuildRequires:	ecasound-devel
BuildRequires:	libtool
BuildRequires:	php-devel
Requires:	php-common
Obsoletes:	php-Ecasound
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
This extension wraps the Ecasound libraries to provide advanced audio
processing capabilities.

In PECL status of this package is: %{_status}.

%description -l pl
To rozszerzenie opakowuje biblioteki Ecasound, aby dostarczyæ
zaawansowane mo¿liwo¶ci przetwarzania d¼wiêku.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c
%patch0 -p0

%build
cd %{_modname_c}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname_c}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
