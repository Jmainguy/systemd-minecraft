%if 0%{?rhel} == 7
  %define dist .el7
%endif
%define _unpackaged_files_terminate_build 0
Name:	systemd-minecraft
Version: 0.1
Release: 1%{?dist}
Summary: A rpm for minecraft and systemd

License: GPLv2
URL: https://github.com/Jmainguy/systemd-minecraft
Source0: systemd-minecraft.tar.gz
Requires(pre): shadow-utils
Requires: java-1.8.0-openjdk


%description
A systemd solution for minecraft

%prep
%setup -q -n systemd-minecraft
%install
mkdir -p $RPM_BUILD_ROOT/opt/minecraft
mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/system
install -m 0644 $RPM_BUILD_DIR/systemd-minecraft/service/minecraft.service %{buildroot}/usr/lib/systemd/system
install -m 0644 $RPM_BUILD_DIR/systemd-minecraft/minecraft_server.jar %{buildroot}/opt/minecraft
install -m 0644 $RPM_BUILD_DIR/systemd-minecraft/eula.txt %{buildroot}/opt/minecraft


%files
/opt/minecraft/minecraft_server.jar
/opt/minecraft/eula.txt
/usr/lib/systemd/system/minecraft.service
%dir /opt/minecraft
%doc

%pre
getent group systemd-minecraft >/dev/null || groupadd -r systemd-minecraft
getent passwd systemd-minecraft >/dev/null || \
    useradd -r -g systemd-minecraft -d /opt/minecraft -s /sbin/nologin \
    -c "User to run minecraft service" systemd-minecraft
exit 0
%post
chown -R systemd-minecraft:systemd-minecraft /opt/minecraft
systemctl daemon-reload

%changelog
