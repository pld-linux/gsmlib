Summary:	Library to access GSM mobile phones through GSM modems
Summary(pl):	Biblioteka dostępu do telefonów GSM poprzez modem GSM
Name:		gsmlib
Version:	1.9
Release:	1
License:	LGPL
Vendor:		Peter Hofmann <software@pxh.de>
Group:		Libraries
Source0:	http://www.pxh.de/fs/gsmlib/download/%{name}-%{version}.tar.gz
URL:		http://www.pxh.de/fs/gsmlib/
BuildRequires:	autoconf
BuildRequires:	automake
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This distribution contains a library to access GSM mobile phones
through GSM modems. Features include:
 - modification of phonebooks stored in the mobile phone or on the SIM
   card
 - reading and writing of SMS messages stored in the mobile phone
 - sending and reception of SMS messages

Additionally, some simple command line programs are provided to use
these functionalities.

%description -l pl
Pakiet zawiera bibliotekę umożliwiającą dostęp do mobilnych telefonów
GSM poprzez modemy GSM. Możliwości to m.in.:
 - modyfikacja książek adresowych zawartych w telefonie lub na karcie
   SIM
 - czytanie i pisanie wiadomości SMS zapisanych w telefonie
 - wysyłanie i odbieranie wiadomości SMS

Dodatkowo dostępnych jest kilka prostych poleceń do korzystania z tych
funkcji.

%package devel
Summary:	Development tools for programs which will use the gsmlib library
Summary(pl):	Pliki nagłówkowe do pisania programów wykorzystujących gsmlib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
The gsmlib-devel package includes the header files necessary for
developing programs which use the gsmlib library.

%description devel -l pl
Pliki nagłówkowe wymagane do rozwoju programów wykorzystujących
gsmlib.

%package static
Summary:	Static gmslib library.
Summary(pl):	Statyczna biblioteka gsmlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static gmslib library.

%description static -l pl
Statyczna biblioteka gsmlib.

%prep
%setup -q

%build
#aclocal
#autoconf
%configure2_13 \
	--enable-nls
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

gzip -9nf doc/FAQ NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man*/*

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
