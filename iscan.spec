Summary:	SANE backend for SEIKO EPSON scanners and all-in-ones
Summary(pl.UTF-8):	Backend SANE dla skanerów SEIKO EPSON i urządzeń wielofunkcyjnych
Name:		iscan
Version:	2.10.0
Release:	1
License:	GPL (with exception clauses) and EAPL
Group:		X11/Applications/Graphics
Source0:	http://lx1.avasys.jp/iscan/%{version}/%{name}_%{version}-1.tar.gz
# Source0-md5:	8e44dac50f51b4c0a2f2e60624edfedb
Source1:	%{name}.desktop
BuildRequires:	gettext-tools
BuildRequires:	gimp-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libusb-devel >= 0.1.6
BuildRequires:	pkgconfig
BuildRequires:	sane-backends-devel >= 1.0.15
Requires:	iscan-sane-epkowa
Requires:	sane-backends
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Iscan - application that enables easy scanning using SANE libraries.

The iscan program supports the following scanners:

 Seiko Epson Flatbed Scanner
 - Perfection 610
 - Perfection 640U
 - Perfection 1200S/Perfection 1200U/Perfection 1200U PHOTO
 - Perfection 1240U
 - Perfection 1660 PHOTO
 - Perfection 1640SU/Perfection 1640SU PHOTO
 - Perfection 1650/Perfection 1650 PHOTO
 - Perfection 2400 PHOTO
 - Perfection 2450 PHOTO
 - Perfection 3200 PHOTO
 - Perfection 4870 PHOTO
 - Perfection 4990 PHOTO
 - Perfection V700
 - Perfection V750
 - Expression 1600
 - Expression 1680
 - Expression 1640XL
 - Expression 10000XL
 - GT-2500
 - GT-10000/GT-10000+
 - GT-15000
 - GT-30000
 - ME200
 - Stylus CX2800/Stylus CX2900
 - Stylus CX3500/Stylus CX3600
 - Stylus CX3700/Stylus CX3800/Stylus DX3800
 - Stylus CX3900/Stylus DX4000
 - Stylus CX4100/Stylus CX4200/Stylus DX4200
 - Stylus CX4500/Stylus CX4600
 - Stylus CX4700/Stylus CX4800/Stylus DX4800
 - Stylus CX4900/Stylus CX5000/Stylus DX5000
 - Stylus CX5100/Stylus CX5200
 - Stylus CX5300/Stylus CX5400
 - Stylus CX5900/Stylus CX6000/Stylus DX6000
 - Stylus CX6300/Stylus CX6400
 - Stylus CX6500/Stylus CX6600
 - Stylus CX7300/Stylus CX7400/Stylus DX7400
 - Stylus CX7700/Stylus CX7800
 - Stylus CX8300/Stylus CX8400/Stylus DX8400
 - Stylus CX9300F/Stylus CX9400Fax/Stylus DX9400F
 - Stylus Photo RX420/Stylus Photo RX425/Stylus Photo RX430
 - Stylus Photo RX500/Stylus Photo RX510
 - Stylus Photo RX520/Stylus Photo RX530
 - Stylus Photo RX560/Stylus Photo RX580/Stylus Photo RX590
 - Stylus Photo RX600
 - Stylus Photo RX620/Stylus Photo RX630
 - Stylus Photo RX640/Stylus Photo RX650
 - Stylus Photo RX700
 - Stylus Photo RX585/Stylus Photo RX595/Stylus Photo RX610
 - Stylus Photo RX680/Stylus Photo RX685/Stylus Photo RX690
 - AcuLaser CX11
 - AcuLaser CX21

%description -l pl.UTF-8
Iscan to aplikacja umożliwiająca łatwe skanowanie przy użyciu
bibliotek SANE. Program obsługuje następujące skanery:

 Seiko Epson Flatbed Scanner
 - Perfection 610
 - Perfection 640U
 - Perfection 1200S/Perfection 1200U/Perfection 1200U PHOTO
 - Perfection 1240U
 - Perfection 1660 PHOTO
 - Perfection 1640SU/Perfection 1640SU PHOTO
 - Perfection 1650/Perfection 1650 PHOTO
 - Perfection 2400 PHOTO
 - Perfection 2450 PHOTO
 - Perfection 3200 PHOTO
 - Perfection 4870 PHOTO
 - Perfection 4990 PHOTO
 - Perfection V700
 - Perfection V750
 - Expression 1600
 - Expression 1680
 - Expression 1640XL
 - Expression 10000XL
 - GT-2500
 - GT-10000/GT-10000+
 - GT-15000
 - GT-30000
 - ME200
 - Stylus CX2800/Stylus CX2900
 - Stylus CX3500/Stylus CX3600
 - Stylus CX3700/Stylus CX3800/Stylus DX3800
 - Stylus CX3900/Stylus DX4000
 - Stylus CX4100/Stylus CX4200/Stylus DX4200
 - Stylus CX4500/Stylus CX4600
 - Stylus CX4700/Stylus CX4800/Stylus DX4800
 - Stylus CX4900/Stylus CX5000/Stylus DX5000
 - Stylus CX5100/Stylus CX5200
 - Stylus CX5300/Stylus CX5400
 - Stylus CX5900/Stylus CX6000/Stylus DX6000
 - Stylus CX6300/Stylus CX6400
 - Stylus CX6500/Stylus CX6600
 - Stylus CX7300/Stylus CX7400/Stylus DX7400
 - Stylus CX7700/Stylus CX7800
 - Stylus CX8300/Stylus CX8400/Stylus DX8400
 - Stylus CX9300F/Stylus CX9400Fax/Stylus DX9400F
 - Stylus Photo RX420/Stylus Photo RX425/Stylus Photo RX430
 - Stylus Photo RX500/Stylus Photo RX510
 - Stylus Photo RX520/Stylus Photo RX530
 - Stylus Photo RX560/Stylus Photo RX580/Stylus Photo RX590
 - Stylus Photo RX600
 - Stylus Photo RX620/Stylus Photo RX630
 - Stylus Photo RX640/Stylus Photo RX650
 - Stylus Photo RX700
 - Stylus Photo RX585/Stylus Photo RX595/Stylus Photo RX610
 - Stylus Photo RX680/Stylus Photo RX685/Stylus Photo RX690
 - AcuLaser CX11
 - AcuLaser CX21

%package sane-epkowa
Summary:	An improved driver for EPSON scanners
Summary(pl.UTF-8):	Udoskonalone sterowniki dla skanerów EPSON
Group:		Libraries

%description sane-epkowa
An improved driver for EPSON scanners.

%description sane-epkowa -l pl.UTF-8
Udoskonalone sterowniki dla skanerów EPSON.

%prep
%setup -q

%build
%configure \
	--enable-jpeg \
	--enable-png \
	--enable-frontend

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_sysconfdir}{/hotplug/usb,/sane.d}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install utils/hotplug/iscan* $RPM_BUILD_ROOT%{_sysconfdir}/hotplug/usb
install backend/epkowa.conf $RPM_BUILD_ROOT%{_sysconfdir}/sane.d
ln -fs %{_libdir}/libesmod.so.1.1.0 $RPM_BUILD_ROOT%{_libdir}/libesmod.so
ln -fs %{_libdir}/libesmod.so.1.1.0 $RPM_BUILD_ROOT%{_libdir}/libesmod.so.1
ln -fs %{_libdir}/sane/libsane-epkowa.so.1.0.15 $RPM_BUILD_ROOT%{_libdir}/sane/libsane-epkowa.so.1

rm -f $RPM_BUILD_ROOT%{_libdir}/sane/libsane*.{la,a}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post sane-epkowa
dll=%{_sysconfdir}/sane.d/dll.conf
if [ -n "`grep '#[[:space:]]*epkowa' ${dll}`" ]; then
	sed -i 's,#[[:space:]]*\(epkowa\),\1,' ${dll}
elif [ -z "`grep epkowa ${dll}`" ]; then
	echo epkowa >> ${dll}
fi

%postun sane-epkowa
if [ "$1" = "0" ]; then
	dll=%{_sysconfdir}/sane.d/dll.conf
	if [ -n "`grep ^epkowa ${dll}`"]; then
		sed -i 's/^epkowa/#epkowa/' ${dll}
	fi
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iscan
%attr(755,root,root) %{_libdir}/libesmod.so.*.*.*
%{_sysconfdir}/hotplug/usb/iscan*
%{_mandir}/man*/*
%{_desktopdir}/*.desktop

%files sane-epkowa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sane/*.so.*
%{_sysconfdir}/sane.d/epkowa.conf
