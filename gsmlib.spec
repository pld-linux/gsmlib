Summary:	Library to access GSM mobile phones through GSM modems
Summary(pl):	Bibliteka dostêpu do telefonów GSM poprzez modem GSM
Name:		gsmlib
Version:	1.5
Release:	1
License:	LGPL
Vendor:		Peter Hofmann <software@pxh.de>
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://www.pxh.de/fs/gsmlib/download/%{name}-%{version}.tar.gz
URL:		http://www.pxh.de/fs/gsmlib/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This distribution contains a library to access GSM mobile phones
through GSM modems. Features include:
 - modification of phonebooks stored in the mobile phone or on the SIM
   card
 - reading and writing of SMS messages stored in the mobile phone
 - sending and reception of SMS messages Additionally, some simple
   command line programs are provided to use these functionalities.

%description -l pl
Pakiet zawiera bibliotekê umo¿liwiaj±c± dostêp do mobilnych telefonów
GSM poprzez modemy GSM. Mo¿liwo¶ci to m.in.:
 - modyfikacja ksi±¿ek adresowych zawartych w telefonie lub na karcie
   SIM
 - czytanie i pisanie wiadomo¶ci SMS zapisanych w telefonie
 - wiele innych

%package devel
Summary:	Development tools for programs which will use the gsmlib library
Summary(pl):	Pliki nag³ówkowe do pisania programów wykorzystuj±cych gsmlib
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description devel
The gsmlib-devel package includes the header files necessary for
developing programs which use the gsmlib library.

%description -l pl devel
Pliki nag³ówkowe wymagane do rozwoju programów wykorzystuj±cych
gsmlib.

%package static
Summary:	Static gmslib library.
Summary(pl):	Statyczna biblioteka gsmlib
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static gmslib library.

%description -l pl static
Statyczna biblioteka gsmlib.

%prep
%setup -q

%build
aclocal
autoconf
%configure \
	--enable-nls
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

gzip -9nf doc/FAQ NEWS README TODO

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man*/*

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
