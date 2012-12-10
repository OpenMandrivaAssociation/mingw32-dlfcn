%define __strip %{_mingw32_strip}
%define __objdump %{_mingw32_objdump}
%define _use_internal_dependency_generator 0
%define __find_requires %{_mingw32_findrequires}
%define __find_provides %{_mingw32_findprovides}

%define realname dlfcn-win32

%define alphatag r11

Name:          mingw32-dlfcn
Version:       0
Release:       %{alphatag}.%mkrel 3
Summary:       Implements a wrapper for dlfcn (dlopen dlclose dlsym dlerror)

License:       LGPLv2+
Group:         Development/Other
URL:           http://code.google.com/p/dlfcn-win32/
Source0:       http://dlfcn-win32.googlecode.com/files/%{realname}-%{alphatag}.tar.bz2
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch:     noarch

BuildRequires: mingw32-filesystem >= 40
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils
#BuildRequires: dos2unix

Patch1:        dlfcn_configure.patch


%description
This library implements a wrapper for dlfcn, as specified in POSIX and SUS,
around the dynamic link library functions found in the Windows API.


%prep
%setup -q -n %{realname}-%{alphatag}

%{__sed} -i 's/\r//' configure
%{__sed} -i 's/\r//' README
%{__sed} -i 's/\r//' COPYING

%patch1 -p1


%build
%{_mingw32_configure} \
  --incdir=%{_mingw32_includedir} \
  --cc=i586-pc-mingw32-gcc \
  --enable-shared=yes \
  --enable-static=no \
  --enable-strip=i586-pc-mingw32-strip
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc README COPYING
%{_mingw32_bindir}/libdl.dll
%{_mingw32_libdir}/libdl.dll.a
%{_mingw32_includedir}/dlfcn.h


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0-r11.3mdv2011.0
+ Revision: 620345
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0-r11.2mdv2010.0
+ Revision: 439813
- rebuild

* Fri Feb 06 2009 Jérôme Soyer <saispo@mandriva.org> 0-r11.1mdv2009.1
+ Revision: 338152
- Fix compiler
- import mingw32-dlfcn


