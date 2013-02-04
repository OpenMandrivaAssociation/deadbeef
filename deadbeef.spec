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
Version:	0.5.6
Release:	2%{?extrarelsuffix}
Summary:	Ultimate music player for GNU/Linux
License:	GPLv2+
Group:		Sound
Url:		http://deadbeef.sourceforge.net
Source0:	http://sourceforge.net/projects/deadbeef/files/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gtk+-3.0)
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
	--enable-gtk3 \
	--disable-gtk2 \
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

%changelog
* Thu Apr 12 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.5.2-1mdv2012.0
- New version 0.5.2
- Add PLF-related parts in spec
- Build only PLF-featured version with faad2 support

* Sat Feb 25 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.2-0.beta1.1mdv2012.0
+ Revision: 780738
- update to new version 0.5.2-beta1
- add buildrequires on yasm and bison
- drop patch 0, applied by upstream

  + Götz Waschk <waschk@mandriva.org>
    - rebuild for new libcdio

* Fri Sep 23 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.1-3
+ Revision: 701114
- rebuild

* Fri Sep 23 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.1-2
+ Revision: 701086
- nuke rpath
- add missing buildrequires on libzip-devel dbus-devel libimlib2-devel libjpeg-devel libpulseaudio-devel libfaad2-devel

* Tue Jun 14 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.1-1
+ Revision: 685144
- update to version 0.5.1

* Fri May 20 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.0-2
+ Revision: 676348
- new version 0.5.0

* Sun Dec 19 2010 Shlomi Fish <shlomif@mandriva.org> 0.4.4-2mdv2011.0
+ Revision: 622922
- Add a dependency on intltool - it was missing
- update to version 0.4.4
- fix plugin loading by moving *.so files from devel package to main
- fix help menu by packaging doc files
- contributed by BALATON Zoltan.

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-2mdv2011.0
+ Revision: 610220
- rebuild

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - add source and spec files
    - Created package structure for deadbeef.

