#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fluidsynth
Version  : 2.2.3
Release  : 10
URL      : https://github.com/FluidSynth/fluidsynth/archive/v2.2.3/fluidsynth-2.2.3.tar.gz
Source0  : https://github.com/FluidSynth/fluidsynth/archive/v2.2.3/fluidsynth-2.2.3.tar.gz
Summary  : A Real-Time Software Synthesizer That Uses Soundfont(tm)
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: fluidsynth-bin = %{version}-%{release}
Requires: fluidsynth-filemap = %{version}-%{release}
Requires: fluidsynth-lib = %{version}-%{release}
Requires: fluidsynth-license = %{version}-%{release}
Requires: fluidsynth-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-gnome
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : doxygen
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(libpulse-simple)
BuildRequires : pkgconfig(readline)
BuildRequires : pkgconfig(sdl2)
BuildRequires : pkgconfig(sndfile)
BuildRequires : readline-dev

%description
FluidSynth (formerly IIWU Synth) is a real-time software synthesizer
based on the SoundFont(tm) 2 specifications. It can read MIDI events
from the MIDI input device and render them to the audio device. It
can also play MIDI files.

%package bin
Summary: bin components for the fluidsynth package.
Group: Binaries
Requires: fluidsynth-license = %{version}-%{release}
Requires: fluidsynth-filemap = %{version}-%{release}

%description bin
bin components for the fluidsynth package.


%package dev
Summary: dev components for the fluidsynth package.
Group: Development
Requires: fluidsynth-lib = %{version}-%{release}
Requires: fluidsynth-bin = %{version}-%{release}
Provides: fluidsynth-devel = %{version}-%{release}
Requires: fluidsynth = %{version}-%{release}

%description dev
dev components for the fluidsynth package.


%package filemap
Summary: filemap components for the fluidsynth package.
Group: Default

%description filemap
filemap components for the fluidsynth package.


%package lib
Summary: lib components for the fluidsynth package.
Group: Libraries
Requires: fluidsynth-license = %{version}-%{release}
Requires: fluidsynth-filemap = %{version}-%{release}

%description lib
lib components for the fluidsynth package.


%package license
Summary: license components for the fluidsynth package.
Group: Default

%description license
license components for the fluidsynth package.


%package man
Summary: man components for the fluidsynth package.
Group: Default

%description man
man components for the fluidsynth package.


%prep
%setup -q -n fluidsynth-2.2.3
cd %{_builddir}/fluidsynth-2.2.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633748993
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -fno-lto -march=x86-64-v3 -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -fno-lto -march=x86-64-v3 -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -fno-lto -march=x86-64-v3 -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -fno-lto -march=x86-64-v3 -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1633748993
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fluidsynth
cp %{_builddir}/fluidsynth-2.2.3/LICENSE %{buildroot}/usr/share/package-licenses/fluidsynth/731a8eff333b8f7053ab2220511b524c87a75923
pushd clr-build-avx2
%make_install_v3  || :
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fluidsynth
/usr/share/clear/optimized-elf/bin*

%files dev
%defattr(-,root,root,-)
/usr/include/fluidsynth.h
/usr/include/fluidsynth/audio.h
/usr/include/fluidsynth/event.h
/usr/include/fluidsynth/gen.h
/usr/include/fluidsynth/ladspa.h
/usr/include/fluidsynth/log.h
/usr/include/fluidsynth/midi.h
/usr/include/fluidsynth/misc.h
/usr/include/fluidsynth/mod.h
/usr/include/fluidsynth/seq.h
/usr/include/fluidsynth/seqbind.h
/usr/include/fluidsynth/settings.h
/usr/include/fluidsynth/sfont.h
/usr/include/fluidsynth/shell.h
/usr/include/fluidsynth/synth.h
/usr/include/fluidsynth/types.h
/usr/include/fluidsynth/version.h
/usr/include/fluidsynth/voice.h
/usr/lib64/libfluidsynth.so
/usr/lib64/pkgconfig/fluidsynth.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-fluidsynth

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfluidsynth.so.3
/usr/lib64/libfluidsynth.so.3.0.3
/usr/share/clear/optimized-elf/lib*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fluidsynth/731a8eff333b8f7053ab2220511b524c87a75923

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/fluidsynth.1
