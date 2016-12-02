%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	CVS frontend for KDE
Name:		cervisia
Version:	16.08.3
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Init)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5Su)
Requires:	cvs
Conflicts:	kdesdk4-core < 1:4.11.0
Conflicts:	kdesdk4-devel < 1:4.11.0

%description
CVS frontend for KDE.

%files
%{_kde_bindir}/cvsaskpass
%{_kde_bindir}/cvsservice
%{_kde_bindir}/cervisia
%{_kde_applicationsdir}/cervisia.desktop
%{_kde_appsdir}/cervisia/cervisia.notifyrc
%{_kde_appsdir}/cervisia/cervisiashellui.rc
%{_kde_appsdir}/cervisiapart/cervisiaui.rc
%{_kde_datadir}/config.kcfg/cervisiapart.kcfg
%{_kde_iconsdir}/*/*/*/*cervisia*
%{_kde_libdir}/libkdeinit4_cvsaskpass.so
%{_kde_libdir}/libkdeinit4_cvsservice.so
%{_kde_libdir}/libkdeinit4_cervisia.so
%{_kde_libdir}/kde4/cervisiapart.so
%{_kde_services}/cervisiapart.desktop
%{_kde_services}/cvsservice.desktop
%{_kde_docdir}/*/*/cervisia
%{_kde_mandir}/man1/cervisia.1.*
%{_datadir}/dbus-1/interfaces/org.kde.cervisia.*.xml
%{_datadir}/apps/appdata/cervisia.appdata.xml

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
