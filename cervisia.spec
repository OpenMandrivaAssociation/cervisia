Summary:	CVS frontend for KDE
Name:		cervisia
Version:	4.11.0
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
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

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- Split from kdesdk4 package as upstream did
- New version 4.11.0
