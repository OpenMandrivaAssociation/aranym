Name: aranym
Version: 0.9.13
Release: 1
Summary: Atari ST/TT/Falcon emulator
Source: http://switch.dl.sourceforge.net/project/aranym/aranym/%version/aranym_%version.orig.tar.gz
License: GPLv2
Group: Emulators
BuildRequires: pkgconfig(x11) pkgconfig(sdl) pkgconfig(SDL_image)

%description
Atari ST/TT/Falcon emulator

%prep
%setup -q
%configure

%build
%make

%install
%makeinstall_std

%files
%_bindir/*
%_datadir/%name
%_mandir/man1/*
%doc %_docdir/%name
