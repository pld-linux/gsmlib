Summary:	Library to access GSM mobile phones through GSM modems
Summary(pl):	Bibliteka dostÍpu do telefonÛw GSM poprzez modem GSM
Name:		gsmlib
Version:	1.5
Release:	1
License:	LGPL
Vendor:		Peter Hofmann <software@pxh.de>
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
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
Pakiet zawiera bibliotekÍ umoøliwiaj±c± dostÍp do mobilnych telefonÛw
GSM poprzez modemy GSM. Moøliwo∂ci to m.in.:
 - modyfikacja ksi±øek adresowych zawartych w telefonie lub na karcie
   SIM
 - czytanie i pisanie wiadomo∂ci SMS zapisanych w telefonie
 - wysy≥anie i odbieranie wiadomo∂ci SMS

Dodatkowo dostÍpnych jest kilka prostych poleceÒ do korzystania z tych
funkcji.

%package devel
Summary:	Development tools for programs which will use the gsmlib library
Summary(pl):	Pliki nag≥Ûwkowe do pisania programÛw wykorzystuj±cych gsmlib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
The gsmlib-devel package includes the header files necessary for
developing programs which use the gsmlib library.

%description -l pl devel
Pliki nag≥Ûwkowe wymagane do rozwoju programÛw wykorzystuj±cych
gsmlib.

%package static
Summary:	Static gmslib library.
Summary(pl):	Statyczna biblioteka gsmlib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
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
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
