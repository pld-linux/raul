Summary:	C++ library for realtime audio applications
Summary(pl.UTF-8):	Biblioteka C++ do aplikacji dźwiękowych czasu rzeczywistego
Name:		raul
Version:	0.8.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.bz2
# Source0-md5:	8fa71a20db81fbed5fb6516dea383ea8
URL:		http://drobilla.net/software/raul/
BuildRequires:	boost-devel
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	python
Requires:	glib2 >= 1:2.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Raul (Realtime Audio Utility Library) is a C++ utility library
primarily aimed at audio/musical applications.

%description -l pl.UTF-8
Raul (Realtime Audio Utility Library) to biblioteka narzędziowa C++
przeznaczona głównie dla aplikacji dźwiękowych/muzycznych czasu
rzeczywistego.

%package devel
Summary:	Header files for raul library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki raul
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	boost-devel
Requires:	glib2-devel >= 1:2.14.0

%description devel
Header files for raul library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki raul.

%prep
%setup -q

%build
CXX="%{__cxx}" \
CXXFLAGS="%{rpmcxxflags}" \
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--strict

./waf -v

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

# let rpm autogenerate dependencies
chmod 755 $RPM_BUILD_ROOT%{_libdir}/lib*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libraul.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libraul.so.10

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libraul.so
%{_includedir}/raul
%{_pkgconfigdir}/raul.pc
