%global         __strip /bin/true
%global         debug_package %{nil}

Name:           rar
Summary:        Program to create and manage RAR archives
Version:        7.10
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
%autosetup -n %{name}

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
* Sat Feb 22 2025 Simone Caronni <negativo17@gmail.com> - 7.10-1
- Update to 7.10.

* Fri May 24 2024 Simone Caronni <negativo17@gmail.com> - 7.0.1-1
- Update to 7.0.1.

* Tue Mar 19 2024 Simone Caronni <negativo17@gmail.com> - 7.0.0-1
- Update to 7.0.0.
- Trim changelog.

* Thu Feb 08 2024 Simone Caronni <negativo17@gmail.com> - 6.24-1
- Update to 6.24.

* Wed Aug 23 2023 Simone Caronni <negativo17@gmail.com> - 6.23-1
- Update to 6.23.

* Thu Jun 08 2023 Simone Caronni <negativo17@gmail.com> - 6.22-1
- Update to 6.22.

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
