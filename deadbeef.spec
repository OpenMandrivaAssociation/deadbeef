# (tpg) do not provide plugins
%if %{_use_internal_dependency_generator}
%define __noautoprov '(.*)\\.so\\.0'
%else
%define _provides_exceptions *.so.0\\|
%endif

%define with_faad 0

####################
# Hardcore PLF build
%define build_plf 0
####################

%if %{build_plf}
%define distsuffix plf
%define with_faad 1
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%endif

Name:		deadbeef
Version:	0.5.5
Release:	1%{?extrarelsuffix}
Summary:	Ultimate music player for GNU/Linux
License:	GPLv2+
Group:		Sound
Url:		http://deadbeef.sourceforge.net
Source0:	http://sourceforge.net/projects/deadbeef/files/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(wavpack)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	intltool >= 0.40
BuildRequires:	pkgconfig(libzip)
BuildRequires:	libstdc++-static-devel
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(imlib2)
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libpulse)
%if %{with_faad}
BuildRequires:	libfaad2-devel
%endif
BuildRequires:	bison
BuildRequires:	yasm

%description
DeaDBeeF is an audio player for GNU/Linux systems with
X11 written in C and C++.

Features:
* minimal depends
* native GTK2 GUI
* cuesheet support
* mp3, ogg, flac, ape and other popular formats
* chiptune formats with subtunes
* song-length databases
* small memory footprint

%if %{build_plf}
This package is in restricted repository because it uses patented codecs.
%endif

%package devel
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{name} = %{version}-%{release}

%description devel
Development files and headers for %{name}.

%prep
%setup -q

%build
# ffmpeg >= 0.11.x support is dropped in upstream:
# http://code.google.com/p/ddb/issues/detail?id=812
# So no wma and alac support for a while
%configure2_5x \
	--disable-static \
	--disable-ffmpeg \
%if !%{with_faad}
	--disable-aac \
%endif
	--disable-rpath

%make

%install
%makeinstall_std

%__rm -rf %{buildroot}%{_docdir}/%{name}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING.GPLv2 COPYING.LGPLv2.1
%doc about.txt help.txt translators.txt
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/pixmaps
%{_bindir}/%{name}
%{_libdir}/%{name}/*.so*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/pixmaps/*.png
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/deadbeef.svg
%{_libdir}/%{name}/convpresets/*.txt

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h

