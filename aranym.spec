%define _disable_lto 1

Name: aranym
Version: 1.0.2
Release: 2
Summary: Atari ST/TT/Falcon emulator
Source0: http://downloads.sourceforge.net/project/aranym/aranym/%{version}/aranym_%{version}.orig.tar.gz
License: GPLv2
Group: Emulators
BuildRequires: pkgconfig(x11) pkgconfig(sdl) pkgconfig(SDL_image)

%description
Atari ST/TT/Falcon emulator

%prep
%setup -q
%configure --disable-sdl2

%build
%make

%install
%makeinstall_std

%files
%_bindir/*
%_datadir/%name
%_mandir/man1/*
%doc %_docdir/%name
