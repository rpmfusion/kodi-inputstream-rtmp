%global kodi_addon inputstream.rtmp
%global kodi_version 20
%global kodi_codename Nexus

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
Version:        20.3.0
Release:        1%{?dist}
Summary:        RTMP inputstream addon for Kodi

License:        GPL-2.0-or-later
URL:            https://github.com/xbmc/%{kodi_addon}/
Source0:        %{url}/archive/%{version}-%{kodi_codename}/%{kodi_addon}-%{version}.tar.gz
Source1:        %{name}.metainfo.xml

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(librtmp)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  zlib-devel
Requires:       kodi%{?_isa} >= %{kodi_version}
ExcludeArch:    %{power64}

%description
This is the RTMP inputstream addon for Kodi.


%prep
%autosetup -n %{kodi_addon}-%{version}-%{kodi_codename}


%build
%cmake
%cmake_build


%install
%cmake_install

# Install AppData file
install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_metainfodir}/%{name}.metainfo.xml


%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/%{name}.metainfo.xml


%files
%doc README.md
%license LICENSE.md
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/
%{_metainfodir}/%{name}.metainfo.xml


%changelog
* Sun Jan 29 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 20.3.0-1
- Initial RPM release (based on RPM Fusion package)
