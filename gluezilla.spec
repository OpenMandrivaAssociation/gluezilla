%define name gluezilla
%define major 0
%define libname %mklibname %name %major
Name:           %name
Version:        1.2.6.1
Release:        %mkrel 2
License:        GPL
URL:            http://www.go-mono.com
Source0:        http://go-mono.com/sources/gluezilla/%{name}-%{version}.tar.bz2
Summary:        Glue library for Winforms Web Control
Group:          System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  mozilla-firefox-devel >= 2.0.0.11-3mdv
BuildRequires:  mono-devel
BuildRequires:  gtk2-devel

%description
This is a glue library for Winforms Web control. It wraps Mozilla
Firefox to be used by mono.

%package -n %libname
Group:System/Libraries
Summary: Glue library for Winforms Web Control
Provides: gluezilla = %version-%release
#gw this is opened dynamically, LD_LIBRARY_PATH should be set to the
# firefox dir
Requires: libmozilla-firefox


%description -n %libname
This is a glue library for Winforms Web control. It wraps Mozilla
Firefox to be used by mono.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std

# Unwanted files:
rm -f $RPM_BUILD_ROOT/%_libdir/libgluezilla.la
rm -f $RPM_BUILD_ROOT/%_libdir/libgluezilla.so

%clean
rm -rf "$RPM_BUILD_ROOT"

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-, root, root)
%_libdir/libgluezilla.so.%{major}*
%doc AUTHORS README TODO
