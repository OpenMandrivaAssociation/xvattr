%define name	xvattr
%define version	1.3
%define release	%mkrel 3

Name:	%{name}
Version: %{version}
Release: %{release}
Summary: Attribute editor for Xv extensions
License: GPL
Group:	 Video
Source:	 http://www.dtek.chalmers.se/~dvd/dist/%{name}-%{version}.tar.bz2
BuildRequires: gtk+-devel
BuildRequires: libxv-devel
URL:	http://www.dtek.chalmers.se/groups/dvd/

%description
Xvattr lets you list the available attributes associated with the Xv
extension to Xorg. It also allows you to change the values of the
attributes. This can be used to change brightness and so on for
programs that use Xv overlays.

%prep
%setup -q

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


