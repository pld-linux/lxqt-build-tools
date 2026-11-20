Summary:	Packaging tools for LXQt
Summary(pl.UTF-8):	Narzędzia do budowania pakietów dla LXQt
Name:		lxqt-build-tools
Version:	2.5.0
Release:	1
License:	BSD-3-Clause
URL:		https://lxqt-project.org/
Source0:	https://github.com/lxqt/lxqt-build-tools/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	17dbc7ec0714c8c930fa2105f9d1cf11
BuildRequires:	Qt6Core-devel
BuildRequires:	cmake
BuildRequires:	rpmbuild(macros) >= 1.742
BuildArch:	noarch

%description
Various packaging tools and scripts for LXQt applications.

%description -l pl.UTF-8
Różne narzędzia i skrypty pomocne przy budowaniu aplikacji LXQt.

%prep
%setup -q

%build
%cmake -B build \
	-DLXQT_ETC_XDG_DIR="/etc/xdg"

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BSD-3-Clause
%doc CHANGELOG README.md
%{_datadir}/cmake/lxqt2-build-tools
%attr(755,root,root) %{_bindir}/lxqt2-transupdate

%clean
rm -rf $RPM_BUILD_ROOT
