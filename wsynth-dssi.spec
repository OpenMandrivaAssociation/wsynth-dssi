Name:       wsynth-dssi
Summary:    A Xsynth DSSI wavetable version plugin
Version:    0.1.3
Release:    7

Source:     http://static.nekosynth.co.uk/releases/wsynth-dssi-%{version}.tar.gz
URL:        https://www.nekosynth.co.uk/wiki/wsynt
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



%changelog
* Fri Apr 27 2012 Frank Kober <emuse@mandriva.org> 0.1.3-6
+ Revision: 794047
- fixer GUI binary installation path

* Fri Apr 27 2012 Frank Kober <emuse@mandriva.org> 0.1.3-5
+ Revision: 793824
- rebuild, spec cleanup

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.1.3-4mdv2009.0
+ Revision: 262176
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.1.3-3mdv2009.0
+ Revision: 256427
- rebuild

* Thu Jan 03 2008 Olivier Blin <blino@mandriva.org> 0.1.3-1mdv2008.1
+ Revision: 140933
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 08 2007 Helio Chissini de Castro <helio@mandriva.com> 0.1.3-1mdv2008.0
+ Revision: 24974
- DISABLE
- Missing build requires
- import wsynth-dssi-0.1.3-1mdv2008.0


* Mon May 07 2007 Helio Chissini de Castro <helio@mandriva.com> 0.1.2-1mdv2008.0
- First package release for Mandriva Linux

