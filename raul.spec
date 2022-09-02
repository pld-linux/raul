Summary:	C++ library for realtime audio applications
Summary(pl.UTF-8):	Biblioteka C++ do aplikacji dźwiękowych czasu rzeczywistego
Name:		raul
Version:	2.0.0
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.xz
# Source0-md5:	4660c4a468bca2106d7d57c37ccd1ace
URL:		http://drobilla.net/software/raul/
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	meson >= 0.49.2
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
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
Requires:	libstdc++-devel >= 6:7
Obsoletes:	raul < 2

%description devel
Header files for raul library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki raul.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# make package noarch
install -d $RPM_BUILD_ROOT%{_npkgconfigdir}
%{__mv} $RPM_BUILD_ROOT{%{_pkgconfigdir},%{_npkgconfigdir}}/raul-2.pc

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc NEWS README.md
%{_includedir}/raul-2
%{_npkgconfigdir}/raul-2.pc
