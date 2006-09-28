Summary:	Library to access GSM mobile phones through GSM modems
Summary(pl):	Biblioteka dost�pu do telefon�w GSM poprzez modem GSM
Name:		gsmlib
Version:	1.10
Release:	6
License:	LGPL
Group:		Libraries
Source0:	http://www.pxh.de/fs/gsmlib/download/%{name}-%{version}.tar.gz
# Source0-md5:	deea4ce2e4f5f1965d32d576597d3ff4
URL:		http://www.pxh.de/fs/gsmlib/
Patch0:		%{name}-assert.patch
Patch1:		%{name}-template.patch
Patch2:		%{name}-qual.patch
Patch3:		%{name}-gcc-4.1.patch
Patch4:		%{name}-include.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Pakiet zawiera bibliotek� umo�liwiaj�c� dost�p do mobilnych telefon�w
GSM poprzez modemy GSM. Mo�liwo�ci to m.in.:
 - modyfikacja ksi��ek adresowych zawartych w telefonie lub na karcie
   SIM
 - czytanie i pisanie wiadomo�ci SMS zapisanych w telefonie
 - wysy�anie i odbieranie wiadomo�ci SMS

Dodatkowo dost�pnych jest kilka prostych polece� do korzystania z tych
funkcji.

%package devel
Summary:	Development tools for programs which will use the gsmlib library
Summary(pl):	Pliki nag��wkowe do pisania program�w wykorzystuj�cych gsmlib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
The gsmlib-devel package includes the header files necessary for
developing programs which use the gsmlib library.

%description devel -l pl
Pliki nag��wkowe wymagane do rozwoju program�w wykorzystuj�cych
gsmlib.

%package static
Summary:	Static gmslib library
Summary(pl):	Statyczna biblioteka gsmlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gmslib library.

%description static -l pl
Statyczna biblioteka gsmlib.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p0

%build
# supplied libtool is broken (C++ library linking)
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-nls
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/FAQ NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man*/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a