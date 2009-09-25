%define name gluezilla
%define major 0
%define libname %mklibname %name %major
Name:           %name
Version:        2.4.2
Release:        %mkrel 2
License:        GPL
URL:            http://www.go-mono.com
Source0:        http://go-mono.com/sources/gluezilla/%{name}-%{version}.tar.bz2
Patch:		gluezilla-2.4-fix-linking.patch
Summary:        Glue library for Winforms Web Control
Group:          System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  xulrunner-devel
%ifnarch %arm %mips
BuildRequires:  mono-devel
%endif
BuildRequires:  gtk2-devel

%description
This is a glue library for Winforms Web control. It wraps Mozilla
Firefox to be used by mono.

%package -n %libname
Group:System/Libraries
Summary: Glue library for Winforms Web Control
Provides: gluezilla = %version-%release
Requires: libxulrunner


%description -n %libname
This is a glue library for Winforms Web control. It wraps Mozilla
Firefox to be used by mono.

%prep
%setup -q
%patch -p1
autoconf

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

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-, root, root)
%_libdir/libgluezilla.so.%{major}*
%doc AUTHORS README TODO
