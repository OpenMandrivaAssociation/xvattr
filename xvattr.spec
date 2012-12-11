%define name	xvattr
%define version	1.3
%define release	%mkrel 9

Name:	%{name}
Version: %{version}
Release: %{release}
Summary: Attribute editor for Xv extensions
License: GPL
Group:	 Video
Source:	 http://www.dtek.chalmers.se/~dvd/dist/%{name}-%{version}.tar.bz2
# (gentoo) use gtk+2.0:
Patch0:  xvattr-1.3-gtk.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: gtk+2-devel
BuildRequires: libxv-devel
URL:	http://www.dtek.chalmers.se/groups/dvd/

%description
Xvattr lets you list the available attributes associated with the Xv
extension to Xorg. It also allows you to change the values of the
attributes. This can be used to change brightness and so on for
programs that use Xv overlays.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README xvattr.html
%{_bindir}/%name
%{_bindir}/gxvattr
%{_mandir}/man1/%name.1*




%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3-9mdv2011.0
+ Revision: 615753
- the mass rebuild of 2010.1 packages

* Thu Dec 03 2009 Thierry Vignaud <tv@mandriva.org> 1.3-8mdv2010.1
+ Revision: 472978
- patch 0: use gtk+2.0 (from gentoo)

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 1.3-7mdv2010.0
+ Revision: 435322
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 1.3-6mdv2009.0
+ Revision: 262740
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.3-5mdv2009.0
+ Revision: 257847
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.3-3mdv2008.1
+ Revision: 130604
- kill re-definition of %%buildroot on Pixel's request


* Fri Jan 12 2007 Götz Waschk <waschk@mandriva.org> 1.3-3mdv2007.0
+ Revision: 108136
- fix buildrequires
- Import xvattr

* Fri Jan 12 2007 Götz Waschk <waschk@mandriva.org> 1.3-3mdv2007.1
- use the right configure macro

* Fri Jun 03 2005 Sebastien savarin <plouf@mandriva.org> 1.3-3mdk
- Rebuild for new gcc

* Wed Sep 08 2004 Spencer Anderson <sdander@oberon.ark.com> 1.3-2mdk
- rebuild
- change description

