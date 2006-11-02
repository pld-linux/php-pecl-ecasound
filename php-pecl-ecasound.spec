# TODO
# - doesn't build
#./configure[3441]: cannot open /home/builder/rpm/pecl/BUILD/php-pecl-ecasound-0.2/Ecasound-0.2/Makefile.in: No such file or directory
%define		_modname	ecasound
%define		_modname_c	Ecasound
%define		_status		beta
%define		_sysconfdir	/etc/php
%define		extensionsdir	%(php-config --extension-dir 2>/dev/null)
Summary:	%{_modname} - audio recording and processing functions
Summary(pl):	%{_modname} - funkcje do nagrywania i przetwarzania d�wi�ku
Name:		php-pecl-%{_modname}
Version:	0.2
Release:	1.1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname_c}-%{version}.tgz
# Source0-md5:	002e7bb8c0f018bb41cefc71e5f9f54b
Patch0:		%{name}-search_path.patch
URL:		http://pecl.php.net/package/ecasound/
BuildRequires:	ecasound-devel
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.322
%{?requires_php_extension}
Requires:	%{_sysconfdir}/conf.d
Obsoletes:	php-Ecasound
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This extension wraps the Ecasound libraries to provide advanced audio
processing capabilities.

In PECL status of this package is: %{_status}.

%description -l pl
To rozszerzenie opakowuje biblioteki Ecasound, aby dostarczy�
zaawansowane mo�liwo�ci przetwarzania d�wi�ku.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c
%patch0 -p0

%build
cd %{_modname_c}-%{version}
phpize
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/conf.d,%{extensionsdir}}

install %{_modname_c}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}
cat <<'EOF' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -f /etc/apache/conf.d/??_mod_php.conf ] || %service -q apache restart
[ ! -f /etc/httpd/httpd.conf/??_mod_php.conf ] || %service -q httpd restart

%postun
if [ "$1" = 0 ]; then
	[ ! -f /etc/apache/conf.d/??_mod_php.conf ] || %service -q apache restart
	[ ! -f /etc/httpd/httpd.conf/??_mod_php.conf ] || %service -q httpd restart
fi

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
