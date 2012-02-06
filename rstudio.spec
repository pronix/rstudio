Summary:	IDE for R
Summary(pl.UTF-8):	IDE dla R
Name:		rstudio
Version:	0.95.258
Release:	1
License:	AGPLv3
Group:		Applications
Source0:	https://github.com/rstudio/rstudio/tarball/v0.95.258/%{name}-%{version}.tar.gz
# Source0-md5:	89d540c607361314b6e73a1ab75293d4
Source1:	https://s3.amazonaws.com/rstudio-buildtools/gwt-2.4.0.zip
# Source1-md5:	f071dee835b402b36517e2c0a777ff34
Source2:	https://s3.amazonaws.com/rstudio-buildtools/gin-1.5.zip
# Source2-md5:	2409168cc18bf5f341e107e6887fe359
URL:		http://rstudio.org/
BuildRequires:	QtWebKit-devel
BuildRequires:	QtXmlPatterns-devel
BuildRequires:	R >= 2.11.1
BuildRequires:	cmake >= 2.8.0
BuildRequires:	java-junit
BuildRequires:	openssl-devel
BuildRequires:	pam-devel
BuildRequires:	pango-devel
Requires:	R >= 2.11.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RStudio(tm) is a free and open source integrated development
environment (IDE) for R. You can run it on your desktop (Windows, Mac,
or Linux) or even over the web using RStudio Server.

%prep
%setup -q -n %{name}-%{name}-13a7f41
mkdir -p src/gwt/lib/gwt
mkdir -p src/gwt/lib/gin/1.5
unzip -qq %{SOURCE1} -d src/gwt/lib/gwt
unzip -qq %{SOURCE2} -d src/gwt/lib/gin/1.5
mv src/gwt/lib/gwt/gwt-2.4.0 src/gwt/lib/gwt/2.4.0

%build
install -d build
cd build
%cmake \
	-DRSTUDIO_TARGET=Desktop \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_PREFIX=%{_libdir}/%{name} \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} -C build install/fast \
	DESTDIR=$RPM_BUILD_ROOT

ln -s %{_libdir}/%{name}/bin/rstudio $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NOTICE README.md
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/R
%dir %{_libdir}/%{name}/bin
%attr(755,root,root) %{_libdir}/%{name}/bin/r*
%dir %{_libdir}/%{name}/bin/postback
%attr(755,root,root) %{_libdir}/%{name}/bin/postback/*
%{_libdir}/%{name}/resources
%{_libdir}/%{name}/www
%{_libdir}/%{name}/rstudio.png
%{_desktopdir}/rstudio.desktop
%{_iconsdir}/hicolor/*x*/apps/*
%{_iconsdir}/hicolor/*x*/mimetypes/*
%{_datadir}/mime/packages/*.xml
%{_pixmapsdir}/rstudio.png