%global         __strip /bin/true
%global         debug_package %{nil}

Name:           rar
Summary:        Program to create and manage RAR archives
Version:        6.21
Release:        1%{?dist}
License:        Proprietary
URL:            https://www.rarlab.com/
ExclusiveArch:  x86_64

Source0:        https://rarlab.com/rar/rarlinux-x64-%(echo %version | tr -d '.').tar.gz

Obsoletes:      unrar < %{?epoch}:%{version}-%{release}
Provides:       unrar = %{?epoch}:%{version}-%{release}

%description
RAR is a powerful tool allowing you to manage and control archive files.
Console RAR supports archives only in RAR format, which names usually have a
".rar" extension. ZIP and other formats are not supported.

%prep
%setup -q -n %{name}

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
* Tue Feb 28 2023 Simone Caronni <negativo17@gmail.com> - 6.21-1
- Update to 6.21.

* Sat Feb 04 2023 Simone Caronni <negativo17@gmail.com> - 6.20-1
- Update to 6.20.

* Thu Jun 02 2022 Simone Caronni <negativo17@gmail.com> - 6.12-1
- Update to 6.12.

* Fri Mar 11 2022 Simone Caronni <negativo17@gmail.com> - 6.11-1
- Update to 6.11.

* Fri Feb 04 2022 Simone Caronni <negativo17@gmail.com> - 6.10-1
- Update to 6.10.
- Drop 32 bit support.

* Wed Sep 22 2021 Simone Caronni <negativo17@gmail.com> - 6.0.2-2
- Update URL and Source URLs.

* Mon Aug 09 2021 Simone Caronni <negativo17@gmail.com> - 6.0.2-1
- Update to 6.0.2.

* Thu Dec 17 2020 Simone Caronni <negativo17@gmail.com> - 6.0.0-1
- Update to 6.0.0.
- Trim changelog.

* Fri Jul 10 2020 Simone Caronni <negativo17@gmail.com> - 5.9.1-1
- Update to 5.9.1.

* Sun Mar 08 2020 Simone Caronni <negativo17@gmail.com> - 5.9.0-1
- Update to 5.9.0.

* Sat Jan 11 2020 Simone Caronni <negativo17@gmail.com> - 5.8.0-1
- Update to 5.8.0.

* Tue May 14 2019 Simone Caronni <negativo17@gmail.com> - 5.7.1-1
- Update to 5.7.1.
