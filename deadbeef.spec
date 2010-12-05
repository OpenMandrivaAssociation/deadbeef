# (tpg) do not provide plugins
%define _provides_exceptions *.so.0\\|

Summary:	Ultimate music player for GNU/Linux
Name:		deadbeef
Version:	0.3.2
Release:	%mkrel 2
License:	GPLv2+
Group:		Sound
Url:		http://deadbeef.sourceforge.net
Source0:	http://sourceforge.net/projects/deadbeef/files/%{name}-%{version}.tar.gz
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

%build
%configure2_5x \
	--disable-static

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
%doc AUTHORS ChangeLog
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/pixmaps
%{_bindir}/%{name}
%{_libdir}/%{name}/*.so.0*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/pixmaps/*.png
%{_iconsdir}/hicolor/*/apps/*.png

%files devel
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/%{name}/*.so
%{_libdir}/%{name}/*.la
