%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	CVS frontend for KDE
Name:		cervisia
Version:	22.08.3
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5DBusAddons)
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

%files -f %{name}.lang -f cvsservice.lang
%{_bindir}/cervisia
%{_bindir}/cvsaskpass
%{_bindir}/cvsservice5
%{_libdir}/libkdeinit5_cervisia.so
%{_libdir}/libkdeinit5_cvsaskpass.so
%{_libdir}/libkdeinit5_cvsservice.so
%{_libdir}/qt5/plugins/cervisiapart5.so
%{_datadir}/applications/org.kde.cervisia.desktop
%{_datadir}/config.kcfg/cervisiapart.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.cervisia5.*
%{_datadir}/knotifications5/cervisia.notifyrc
%{_datadir}/kservices5/org.kde.cervisiapart5.desktop
%{_datadir}/kservices5/org.kde.cvsservice5.desktop
%{_datadir}/kxmlgui5/cervisia
%{_datadir}/kxmlgui5/cervisiapart
%{_datadir}/metainfo/org.kde.cervisia.appdata.xml
%{_datadir}/icons/*/*/*/vcs-*.*
%{_datadir}/icons/*/*/*/cervisia.*
%{_mandir}/man1/cervisia.1*

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-man --with-html
%find_lang cvsservice
