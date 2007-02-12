#
# Conditional build:
%bcond_without	static_libs # don't build static libraries
#
Summary:	vdkodbc - data-access objects for developing database applications using VDK and unixODBC
Summary(pl.UTF-8):	vdkodbc - obiekty dostępu do danych do tworzenia aplikacji bazodanowych przy użyciu VDK i unixODBC
Name:		vdkodbc
Version:	2.4.2
Release:	0.1
License:	LGPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/vdklib/%{name}-%{version}.tar.gz
# Source0-md5:	a54b9e611b1cb1590fcf4f8008669eed
URL:		http://www.mariomotta.it/vdklib/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	unixODBC >= 2.2.1
BuildRequires:	vdk-devel >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VDKODBC is a set of data-access and data-aware objects made to build
database applications using VDK and unixODBC libraries.

%description -l pl.UTF-8
VDKODBC jest zbiorem obiektów dostępu do danych przeznaczonym do
budowania aplikacji bazodanowych w oparciu o biblioteki vdk i
unixODBC.

%package devel
Summary:	Header files for VDKODBC library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki VDKODBC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for VDKODBC library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki VDKODBC.

%package static
Summary:	Static VDKODBC library
Summary(pl.UTF-8):	Statyczna biblioteka VDKODBC
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static VDKODBC library.

%description static -l pl.UTF-8
Statyczna biblioteka VDKODBC.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static=%{?with_static_libs:yes}%{!?with_static_libs:no}
%{__make}
%{__make} docs

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/doxy/html/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
