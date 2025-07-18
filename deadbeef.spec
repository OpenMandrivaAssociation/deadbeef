# (tpg) Do not provide plugins
%if %{_use_internal_dependency_generator}
%define	__noautoprov '(.*)\\.so\\.0'
%else
%define	_provides_exceptions *.so.0\\|
%endif

####################
# Hardcore PLF build
%define build_plf 0
####################

%if %{build_plf}
%define	distsuffix plf
%define	with_faad 1
# Make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define	extrarelsuffix plf
%else
%define	with_faad 0
%endif

%global	_disable_rebuild_configure 1

Summary:	Ultimate music player for GNU/Linux
Name:		deadbeef
Version:	1.10.0
Release:	1%{?extrarelsuffix}
License:	zlib
Group:	Sound
Url:		https://deadbeef.sourceforge.net
Source0:	https://sourceforge.net/projects/deadbeef/files/travis/linux/%{version}/%{name}-%{version}.tar.bz2
# remove objc code built on mac only causing libtool to get confused
# something like this has already been done upstream
#Patch1:		deadbeef-0.7.2-libtool.patch
#Patch0:		https://patch-diff.githubusercontent.com/raw/DeaDBeeF-Player/deadbeef/pull/3101.patch
BuildRequires:	bison
BuildRequires:	gettext
BuildRequires:	intltool >= 0.40
BuildRequires:	%{_lib}BlocksRuntime0
BuildRequires:	locales-extra-charsets
BuildRequires:	yasm
BuildRequires:	libdispatch-devel
BuildRequires:	libstdc++-static-devel
BuildRequires:	pkgconfig(adplug)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(dbus-1)
%if %{with_faad}
BuildRequires:	pkgconfig(faad2)
%endif
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:	pkgconfig(jansson)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(imlib2)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libavutil)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libgme)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(libpipewire-0.3)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libsidplayfp)
BuildRequires:	pkgconfig(libzip)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(soundtouch)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(wavpack)
BuildRequires:	pkgconfig(wildmidi)
BuildRequires:	pkgconfig(x11)
Requires:	%{_lib}flac

%description
DeaDBeeF is an audio player for GNU/Linux systems written in C and C++.
Features:
* minimal depends;
* native GTK3 GUI;
* cuesheet support;
* mp3, ogg, flac, ape and other popular formats;
* chiptune formats with subtunes;
* song-length databases;
* small memory footprint-
%if %{build_plf}
This package is in restricted repo because it uses the patented faad codec.
%endif

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING.GPLv2 COPYING.LGPLv2.1
%doc about.txt help.txt translators.txt
%{_bindir}/%{name}
%{_libdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/pixmaps
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/pixmaps/*.png
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg

#-----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{name} = %{version}-%{release}

%description devel
Development files and headers for %{name}.

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h

#-----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
export LDFLAGS="%{ldflags} -lm -logg"
%configure	--disable-static \
	--disable-oss \
	--disable-gtk2 \
	--enable-gtk3 \
	--enable-ffmpeg \
	--disable-lfm \
	--disable-notify \
    --disable-rpath \
%if !%{with_faad}
	--disable-aac \
%endif

%make_build


%install
%make_install

rm -rf %{buildroot}%{_docdir}/%{name}

%find_lang %{name}
