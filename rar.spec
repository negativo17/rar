%global         __strip /bin/true
%global         debug_package %{nil}

Name:           rar
Summary:        Program to create and manage RAR archives
Version:        5.4.0
Release:        2%{?dist}
License:        Proprietary
URL:            http://www.rarlabs.com/

Source0:        http://rarlab.com/rar/rarlinux-%{version}.tar.gz
Source1:        http://rarlab.com/rar/rarlinux-x64-%{version}.tar.gz
ExclusiveArch:  %{ix86} x86_64

Obsoletes:      unrar < %{?epoch}:%{version}-%{release}
Provides:       unrar = %{?epoch}:%{version}-%{release}

%description
RAR is a powerful tool allowing you to manage and control archive files.
Console RAR supports archives only in RAR format, which names usually have a
".rar" extension. ZIP and other formats are not supported.

%prep
%ifarch %{ix86}
%setup -qn %{name}
%endif

%ifarch x86_64
%setup -T -b 1 -n %{name}
%endif

%build
# Nothing to build

%install
install -D -p -m0755 rar %{buildroot}%{_bindir}/rar
install -D -p -m0755 unrar %{buildroot}%{_bindir}/unrar
install -D -p -m0644 rarfiles.lst %{buildroot}%{_sysconfdir}/rarfiles.lst
install -D -p -m0755 default.sfx %{buildroot}%{_libdir}/default.sfx

%files
%license license.txt
%doc acknow.txt order.htm rar.txt readme.txt whatsnew.txt
%config(noreplace) %{_sysconfdir}/rarfiles.lst
%{_bindir}/rar
%{_bindir}/unrar
%{_libdir}/default.sfx

%changelog
* Mon Feb 13 2017 Simone Caronni <negativo17@gmail.com> - 5.4.0-2
- Remove RHEL/CentOS 5 support.

* Wed Aug 17 2016 Simone Caronni <negativo17@gmail.com> - 5.4.0-1
- Update to 5.4.0.

* Mon Dec 21 2015 Simone Caronni <negativo17@gmail.com> - 5.3.0-1
- Update to 5.3.0.
- Add license macro.
- Add unrar binary, obsolete unrar package in RPMFusion to enable 5.x archive
  extraction.

* Wed Apr 01 2015 Simone Caronni <negativo17@gmail.com> - 5.2.1-1
- Update to 5.2.1.

* Fri Dec 19 2014 Simone Caronni <negativo17@gmail.com> - 5.2.0-1
- Update to 5.2.0 (5.20).

* Fri Sep 05 2014 Simone Caronni <negativo17@gmail.com> - 5.1.1-1
- Update to 5.1.1.

* Mon Jul 07 2014 Simone Caronni <negativo17@gmail.com> - 5.1.0-1
- Update to 5.1.0.

* Sat Dec 14 2013 Simone Caronni <negativo17@gmail.com> - 5.0.1-1
- Update to 5.0.1.

* Fri Oct 04 2013 Simone Caronni <negativo17@gmail.com> - 5.0.0-1
- Update to version 5.0.0.

* Fri Aug 03 2012 Simone Caronni <negativo17@gmail.com> - 4.2.0-2
- Small spec file changes.

* Mon Jun 25 2012 Simone Caronni <negativo17@gmail.com> - 4.2.0-1
- Updated.
