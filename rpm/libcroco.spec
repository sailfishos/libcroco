Name:             libcroco
Summary:          A CSS2 parsing library
Version:          0.6.13
Release:          1
License:          LGPLv2
Source:           http://download.gnome.org/sources/libcroco/0.6/%{name}-%{version}.tar.xz

Patch1:           0001-Disable-gtkdoc.patch
Patch2:           0002-multilib.patch

BuildRequires:    pkgconfig
BuildRequires:    glib2-devel
BuildRequires:    libxml2-devel

%description
CSS2 parsing and manipulation library for GNOME

%package devel
Summary:          Libraries and include files for developing with libcroco
Requires:         %{name} = %{version}-%{release}

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with libcroco.

%prep
%autosetup -n %{name}-%{version}/%{name} -p1

%build
./autogen.sh --disable-static --prefix=%{_prefix} --libdir=%{_libdir}
make %{?_smp_mflags} CFLAGS="$CFLAGS -fno-strict-aliasing"

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING COPYING.LIB
%doc AUTHORS NEWS README
%{_bindir}/csslint-0.6
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/libcroco-0.6
%{_bindir}/croco-0.6-config
%{_libdir}/pkgconfig/libcroco-0.6.pc
