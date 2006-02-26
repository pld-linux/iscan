Summary:	SANE backend for SEIKO EPSON scanners and all-in-ones
Summary(pl):	Nak³adka na SANE dla skanerów SEIKO EPSON i urz±dzeñ wielofunkcyjnych
Name:		iscan
Version:	2.0.0
Release:	1
License:	GPL (with exception clauses) and EAPL
Group:		X11/Applications/Graphics
Source0:	http://lx1.avasys.jp/iscan/%{version}/%{name}-%{version}-0.tar.gz
# Source0-md5:	a9fd56f754eeac51fcc403f09b1d606d
Source1:	%{name}.desktop
BuildRequires:	gimp-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libusb >= 0.1.6
BuildRequires:	sane-backends-devel
Requires:	iscan-sane-epkowa
Requires:	sane-backends
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Iscab - application that enables easy scanning using SANE libraries.
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
            - Expression 1600
            - Expression 1680
            - Expression 1640XL
            - Expression 10000XL
            - GT-10000/GT-10000+
            - GT-15000
            - GT-30000
            - Stylus CX3500/Stylus CX3600
            - Stylus CX3700/Stylus CX3800/Stylus DX3800
            - Stylus CX4500/Stylus CX4600
            - Stylus CX5100/Stylus CX5200
            - Stylus CX5300/Stylus CX5400
            - Stylus CX6300/Stylus CX6400
            - Stylus CX6500/Stylus CX6600
            - Stylus CX7700/Stylus CX7800
            - Stylus Photo RX420/Stylus Photo RX425/Stylus Photo RX430
            - Stylus Photo RX500/Stylus Photo RX510
            - Stylus Photo RX520/Stylus Photo RX530
            - Stylus Photo RX600/Stylus Photo RX610
            - Stylus Photo RX620/Stylus Photo RX630
            - Stylus Photo RX700
            - AcuLaser CX11


%description -l pl
Iscan to aplikacja umo¿liwiaj±ca ³atwe skanowanie przy u¿yciu
bibliotek SANE. Program obs³uguje nastêpuj±ce skanery:

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
            - Expression 1600
            - Expression 1680
            - Expression 1640XL
            - Expression 10000XL
            - GT-10000/GT-10000+
            - GT-15000
            - GT-30000
            - Stylus CX3500/Stylus CX3600
            - Stylus CX3700/Stylus CX3800/Stylus DX3800
            - Stylus CX4500/Stylus CX4600
            - Stylus CX5100/Stylus CX5200
            - Stylus CX5300/Stylus CX5400
            - Stylus CX6300/Stylus CX6400
            - Stylus CX6500/Stylus CX6600
            - Stylus CX7700/Stylus CX7800
            - Stylus Photo RX420/Stylus Photo RX425/Stylus Photo RX430
            - Stylus Photo RX500/Stylus Photo RX510
            - Stylus Photo RX520/Stylus Photo RX530
            - Stylus Photo RX600/Stylus Photo RX610
            - Stylus Photo RX620/Stylus Photo RX630
            - Stylus Photo RX700
	    - AcuLaser CX11

%package sane-epkowa
Summary:	An improved driver for EPSON scanners
Summary(pl):	Udoskonalone sterowniki dla skanerów EPSON
Group:		X11/Development/Libraries

%description sane-epkowa
An improved driver for EPSON scanners.

%description sane-epkowa -l pl
Udoskonalone sterowniki dla skanerów EPSON

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

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
dll=%{_sysconfdir}/sane.d/dll.conf
if [ -n "`grep '#[[:space:]]*epkowa' ${dll}`" ]
then                            # uncomment existing entry
    sed -i 's,#[[:space:]]*\(epkowa\),\1,' ${dll}
elif [ -z "`grep epkowa ${dll}`" ]
then                            # append brand new entry
    echo epkowa >> ${dll}
fi

%postun
dll=%{_sysconfdir}/sane.d/dll.conf
if [ -n "`grep ^epkowa ${dll}`"]
then
    sed -i 's/^epkowa/#epkowa/' ${dll}
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iscan
%attr(755,root,root) %{_libdir}/libesmod.*
%{_sysconfdir}/hotplug/usb/iscan*
%{_sysconfdir}/sane.d/epkowa.conf
%{_mandir}/man*/*
%{_desktopdir}/*

%files sane-epkowa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sane/*.so.*
%{_libdir}/sane/*.la
%{_libdir}/sane/*.a
