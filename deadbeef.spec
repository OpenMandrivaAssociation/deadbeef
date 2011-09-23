# (tpg) do not provide plugins
%define _provides_exceptions *.so.0\\|

Summary:	Ultimate music player for GNU/Linux
Name:		deadbeef
Version:	0.5.1
Release:	%mkrel 3
License:	GPLv2+
Group:		Sound
Url:		http://deadbeef.sourceforge.net
Source0:	http://sourceforge.net/projects/deadbeef/files/%{name}-%{version}.tar.bz2
Patch0:		deadbeef-0.5.0-string_format.patch
BuildRequires:	libalsa-devel
BuildRequires:	gtk2-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libcurl-devel
BuildRequires:	libmad-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	libflac-devel
BuildRequires:	libwavpack-devel
BuildRequires:	libcdio-devel
BuildRequires:	libcddb-devel
BuildRequires:	intltool >= 0.40
BuildRequires:	libzip-devel
BuildRequires:	libstdc++-static-devel
BuildRequires:	dbus-devel
BuildRequires:	libimlib2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpulseaudio-devel
BuildRequires:	libfaad2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
DeaDBeeF is an audio player for GNU/Linux systems with X11 written in C and C++.

Features:
* minimal depends
* native GTK2 GUI
* cuesheet support
* mp3
* ogg
* flac
* ape
* chiptune formats with subtunes
* song-length databases
* small memory footprint

%package devel
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{name} = %{version}-%{release}

%description devel
Development files and headers for %{name}.

%prep
%setup -q %{name}-%{version}
%patch0 -p1

%build
%configure2_5x \
	--disable-static \
	--disable-rpath

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

rm -rf %{buildroot}%{_docdir}/%{name}

%find_lang %{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING.GPLv2 COPYING.LGPLv2.1
%doc about.txt help.txt translators.txt
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/pixmaps
%{_bindir}/%{name}
%{_libdir}/%{name}/*.so*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/pixmaps/*.png
%{_datadir}/%{name}/pixmaps/noartwork.jpg
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/deadbeef.svg
%{_libdir}/%{name}/convpresets/*.txt

%files devel
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/%{name}/*.la
