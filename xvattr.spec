%define debug_package %{nil}

Name:	xvattr
Version: 1.3
Release: 12
Summary: Attribute editor for Xv extensions
License: GPL
Group:	 Video
URL:	http://www.dtek.chalmers.se/groups/dvd/
Source:	 http://www.dtek.chalmers.se/~dvd/dist/%{name}-%{version}.tar.bz2
# (gentoo) use gtk+2.0:
Patch0:  xvattr-1.3-gtk.patch
Patch1:  xvattr-1.3-encoding.patch
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(xv)


%description
Xvattr lets you list the available attributes associated with the Xv
extension to Xorg. It also allows you to change the values of the
attributes. This can be used to change brightness and so on for
programs that use Xv overlays.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
%configure2_5x
%make

%install
%makeinstall


%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README xvattr.html
%{_bindir}/%{name}
%{_bindir}/gxvattr
%{_mandir}/man1/%{name}.1*


