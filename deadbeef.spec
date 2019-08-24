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

%define _disable_rebuild_configure 1

Summary:	Ultimate music player for GNU/Linux
Name:		deadbeef
Version:	1.8.2
Release:	1%{?extrarelsuffix}
License:	GPLv2+
Group:		Sound
Url:		http://deadbeef.sourceforge.net
Source0:	https://sourceforge.net/projects/deadbeef/files/travis/linux/%{version}/%{name}-%{version}.tar.bz2
# remove objc code built on mac only causing libtool to get confused
# something like this has already been done upstream
#Patch1:		deadbeef-0.7.2-libtool.patch

BuildRequires:	bison
BuildRequires:	intltool >= 0.40
BuildRequires:	yasm
BuildRequires:	jpeg-devel
BuildRequires:	libstdc++-static-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(imlib2)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libzip)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(wavpack)
BuildRequires:	pkgconfig(jansson)
%if %{with_faad}
BuildRequires:	libfaad2-devel
%endif

%description
DeaDBeeF is an audio player for GNU/Linux systems with
X11 written in C and C++.

Features:
* minimal depends
* native GTK3 GUI
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
%autopatch -p1
#autoreconf -fiv


%build
# ffmpeg >= 0.11.x support is dropped in upstream:
# http://code.google.com/p/ddb/issues/detail?id=812
# So no wma and alac support for a while

#./autogen.sh
%configure \
	--disable-gtk2 \
	--enable-gtk3 \
	--disable-static \
	--enable-ffmpeg \
    --disable-rpath \
%if !%{with_faad}
	--disable-aac \
%endif
    LIBS='-logg -lm'

%make_build

%install
%make_install
rm -rf %{buildroot}%{_docdir}/%{name}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING.GPLv2 COPYING.LGPLv2.1
%doc about.txt help.txt translators.txt
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/pixmaps
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/pixmaps/*.png
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/deadbeef.svg

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
