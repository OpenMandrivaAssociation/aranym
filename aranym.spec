%define _disable_lto 1

Name: aranym
Version: 1.1.0
Release: 1
Summary: Atari ST/TT/Falcon emulator
Source0: https://github.com/aranym/aranym/archive/ARANYM_1_1_0/aranym-ARANYM_1_1_0.tar.gz.tar.gz
License: GPLv2
Group: Emulators
BuildRequires: pkgconfig(x11) 
BuildRequires: pkgconfig(sdl) 
BuildRequires: pkgconfig(SDL_image)

%description
Atari ST/TT/Falcon emulator

%prep
%setup -qn ARANYM_1_1_0/aranym-ARANYM_1_1_0

%build
autoreconf -vfi
%configure2_5x
make depend
%make_build

%install
%make_install

install -Dm 0644 contrib/icon-48.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
install -Dm 0644 contrib/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc %{_docdir}/%{name}
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/pixmaps/%{name}*.png
%{_iconsdir}/*/*/*/%{name}*.png
%{_mandir}/man?/*.*.*
