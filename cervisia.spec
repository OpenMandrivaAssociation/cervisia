%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	CVS frontend for KDE
Name:		cervisia
Version:	14.12.0
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
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
%{_datadir}/apps/appdata/cervisia.appdata.xml

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:14.12.0-1
- New version 14.12.0

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- Split from kdesdk4 package as upstream did
- New version 4.11.0
