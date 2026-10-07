Name:           ooln
Version:        0.1.0
Release:        1%{?dist}
Summary:        Creates atomic hard links and relative symbolic links with cycle detection.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooln
Source0:        ooln-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooln is a sovereign, capability-bounded LINK CREATOR written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooln
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooln-uninstall

%files
/usr/bin/ooln
/usr/bin/ooln-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
