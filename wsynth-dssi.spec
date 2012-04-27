Name:       wsynth-dssi
Summary:    A Xsynth DSSI wavetable version plugin
Version:    0.1.3
Release:    6

Source:     http://static.nekosynth.co.uk/releases/wsynth-dssi-%{version}.tar.gz
URL:        http://www.nekosynth.co.uk/wiki/wsynt
License:    GPL
Group:      Sound

BuildRequires:  pkgconfig(dssi)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(sndfile)

%description
A Xsynth DSSI wavetable version plugin

%prep
%setup -q

%build
%configure2_5x --with-dssi-dir=%{buildroot}%{_libdir}/dssi

%make bindir=%{_libdir}/dssi/%name

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall bindir=%{buildroot}%{_libdir}/dssi/%name

%files
%defattr(-,root,root)
%doc COPYING README
%_libdir/dssi/*

