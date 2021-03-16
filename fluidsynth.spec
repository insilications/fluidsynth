#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fluidsynth
Version  : 2.1.8
Release  : 5
URL      : https://github.com/FluidSynth/fluidsynth/archive/v2.1.8/fluidsynth-2.1.8.tar.gz
Source0  : https://github.com/FluidSynth/fluidsynth/archive/v2.1.8/fluidsynth-2.1.8.tar.gz
Summary  : Software SoundFont synth
Group    : Development/Tools
License  : LGPL-2.1
Requires: fluidsynth-bin = %{version}-%{release}
Requires: fluidsynth-lib = %{version}-%{release}
Requires: fluidsynth-license = %{version}-%{release}
Requires: fluidsynth-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-gnome
BuildRequires : buildreq-kde
BuildRequires : doxygen
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(libpulse-simple)
BuildRequires : pkgconfig(readline)
BuildRequires : pkgconfig(sdl2)
BuildRequires : pkgconfig(sndfile)
BuildRequires : readline-dev

%description
To build FluidSynth API reference documentation, make sure you have Doxygen
installed.

%package bin
Summary: bin components for the fluidsynth package.
Group: Binaries
Requires: fluidsynth-license = %{version}-%{release}

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


%package lib
Summary: lib components for the fluidsynth package.
Group: Libraries
Requires: fluidsynth-license = %{version}-%{release}

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
%setup -q -n fluidsynth-2.1.8
cd %{_builddir}/fluidsynth-2.1.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615935660
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
export CFLAGS="$CFLAGS -O3 -fno-lto -march=haswell "
export FCFLAGS="$FFLAGS -O3 -fno-lto -march=haswell "
export FFLAGS="$FFLAGS -O3 -fno-lto -march=haswell "
export CXXFLAGS="$CXXFLAGS -O3 -fno-lto -march=haswell "
export CFLAGS="$CFLAGS -march=haswell -m64"
export CXXFLAGS="$CXXFLAGS -march=haswell -m64"
export FFLAGS="$FFLAGS -march=haswell -m64"
export FCFLAGS="$FCFLAGS -march=haswell -m64"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1615935660
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fluidsynth
cp %{_builddir}/fluidsynth-2.1.8/LICENSE %{buildroot}/usr/share/package-licenses/fluidsynth/731a8eff333b8f7053ab2220511b524c87a75923
pushd clr-build-avx2
%make_install_avx2  || :
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fluidsynth
/usr/bin/haswell/fluidsynth

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
/usr/lib64/haswell/libfluidsynth.so
/usr/lib64/libfluidsynth.so
/usr/lib64/pkgconfig/fluidsynth.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libfluidsynth.so.2
/usr/lib64/haswell/libfluidsynth.so.2.3.8
/usr/lib64/libfluidsynth.so.2
/usr/lib64/libfluidsynth.so.2.3.8

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fluidsynth/731a8eff333b8f7053ab2220511b524c87a75923

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/fluidsynth.1
