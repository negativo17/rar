%global         __strip /bin/true
%global         debug_package %{nil}

Name:           rar
Summary:        Program to create and manage RAR archives
Epoch:          1
Version:        7.21
Release:        1%{?dist}
License:        Proprietary
URL:            https://www.rarlab.com/
ExclusiveArch:  x86_64

Source0:        https://rarlab.com/rar/rarlinux-x64-%(echo %version | tr -d '.').tar.gz

Obsoletes:      unrar < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       unrar = %{?epoch:%{epoch}:}%{version}-%{release}

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
* Thu Apr 30 2026 Simone Caronni <negativo17@gmail.com> - 1:7.21-1
- Update to 7.21.
- Trim changelog.

* Thu Feb 05 2026 Simone Caronni <negativo17@gmail.com> - 1:7.20-1
- Update to 7.20.

* Thu Sep 18 2025 Simone Caronni <negativo17@gmail.com> - 1:7.12-2
- Set Epoch so it properly obsoletes unrar which has a higher version.

* Mon Jun 30 2025 Simone Caronni <negativo17@gmail.com> - 7.12-1
- Update to 7.12.

* Tue Jun 03 2025 Simone Caronni <negativo17@gmail.com> - 7.11-1
- Update to 7.11.

* Sat Feb 22 2025 Simone Caronni <negativo17@gmail.com> - 7.10-1
- Update to 7.10.
