%define		_modname	ecasound
Summary:	PHP wrapper to the Ecasound Library
Summary(pl):	PHP-owy wrapper do biblioteki Ecasound
Name:		php-pecl-%{_modname}
Version:	0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/Ecasound-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	libecasound-devel
BuildRequires:	php-devel
Obsoletes:	php-Ecasound
Requires:	php-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
PHP wrapper to the Ecasound Library.

%description -l pl
PHP-owy wrapper do biblioteki Ecasound.

%prep
%setup -q -c

%build
cd Ecasound-%{version}
phpize
%{__aclocal}
%configure \
	--with-ecasound

%{__make} CPPFLAGS="-DHAVE_CONFIG_H -I/usr/X11R6/include/X11/"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install Ecasound-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/php-module-install install %{_modname} %{_sysconfdir}/php.ini

%preun
if [ "$1" = "0" ]; then
	/usr/sbin/php-module-install remove %{_modname} %{_sysconfdir}/php.ini
fi

%files
%defattr(644,root,root,755)
%doc Ecasound-%{version}/{CREDITS,EXPERIMENTAL,*.php}
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
