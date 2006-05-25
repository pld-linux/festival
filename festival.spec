# TODO: kill ELF binary from %{_datadir}, see files
Summary:	The Festival speech sythesis system
Summary(pl):	System syntezy mowy Festival
Name:		festival
Version:	1.4.4
%define		_snap	20030803
Release:	0.%{_snap}.4
License:	BSD-like (except for festival.el, which is on GPL)
Group:		Applications/Sound
#Source0:	http://www.cstr.ed.ac.uk/download/festival/%{version}/%{name}-%{version}-release.tar.gz
Source0:	http://www.festvox.org/packed/festival/latest/festival-%{version}-current%{_snap}.tar.gz
# Source0-md5:	ffaa7533b3f50791aabfbf1cee09ca85
Source1:	http://www.cstr.ed.ac.uk/download/festival/%{version}/festvox_us1.tar.gz
# Source1-md5:	d0c3e727003e715a65daf01003101813
Source2:	http://www.cstr.ed.ac.uk/download/festival/%{version}/festvox_us2.tar.gz
# Source2-md5:	fbcc8baacbff3aa2aaaf5a93701bb5e0
Source3:	http://www.cstr.ed.ac.uk/download/festival/%{version}/festvox_us3.tar.gz
# Source3-md5:	06dbfe2edaab6ffa31deeaf522e0c33e
Source4:	http://www.cstr.ed.ac.uk/download/festival/%{version}/festvox_en1.tar.gz
# Source4-md5:	66e3bc07751d7e31826185649c5ada5a
Patch0:		%{name}-config.patch
Patch1:		%{name}-asterisk.patch
Patch2:		%{name}-gcc4.patch
URL:		http://www.cstr.ed.ac.uk/projects/festival/
BuildRequires:	automake
BuildRequires:	speech_tools-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%ifarch alpha
%define		fostype	alpha_Linux
%else
%define		fostype	unknown_Linux
%endif

%description
Festival offers a general framework for building speech synthesis
systems as well as including examples of various modules. As a whole
it offers full text to speech through a number APIs: from shell level,
though a Scheme command interpreter, as a C++ library, from Java, and
an Emacs interface. Festival is multi-lingual, though English is the
most advanced.

%description -l pl
Festival jest platform± przeznaczon± do budowania systemów syntezy
mowy oraz do ³atwego testowania ró¿nych modu³ów sk³adaj±cych siê na
syntezator mowy. Mo¿na te¿ u¿ywaæ programu jako maszynki czytaj±cej
pliki tekstowe. Festival jest wielojêzyczny, lecz jêzyk angielski jest
najbardziej zaawansowany.

%package devel
Summary:	Festival developement enviroment
Summary(pl):	Festival - ¶rodowidko rozwojowe
Group:		Applications/Sound

%description devel
Festival developement enviroment.

%description devel -l pl
Festival - ¶rodowisko rozwojowe.

%package voices-english-mbrola-us
Summary:	Festival's files for voices us1, us2, us3
Summary(pl):	Pliki Festival do g³osów us1, us2, us3
Group:		Applications/Sound
Requires:	mbrola

%description voices-english-mbrola-us
Files needed to use us1, us2, us3 voices from mbrola packages.

%description voices-english-mbrola-us -l pl
Pliki potrzebne do u¿ycia g³osów us1, us2, us3 z pakietu mbrola.

%package voices-english-mbrola-en
Summary:	Festival's files for voice en1
Summary(pl):	Pliki Festival do g³osu en1
Group:		Applications/Sound
Requires:	mbrola

%description voices-english-mbrola-en
Files needed to use en1 voice from mbrola packages.

%description voices-english-mbrola-en -l pl
Pliki potrzebne do u¿ycia g³osu en1 z pakietu mbrola.

%prep
%setup -q -n %{name} -b1 -b2 -b3 -b4
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cp -f /usr/share/automake/config.* .
%{__perl} -pi -e 's,^EST=.*,EST=%{_libdir}/speech_tools,' config/config.in
%configure2_13
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	ECHO_N='printf "%%s"' \
	OPTIMISE_CCFLAGS="%{rpmcflags}" \
	OPTIMISE_CXXFLAGS="%{rpmcflags}" \
	OPTIMISE_LINK="%{rpmldflags}" \
	REQUIRED_LIBDEPS= 
# REQUIRED_LIBDPES is workaround not to need static speech_tools libraries

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/lib/{voices/english,dicts},%{_libdir},%{_includedir}/%{name},%{_mandir}/man1}

# bin
install bin/festival_server* bin/text2wave $RPM_BUILD_ROOT%{_bindir}
install src/main/festival{,_client} $RPM_BUILD_ROOT%{_bindir}

# devel
install src/lib/libFestival.a $RPM_BUILD_ROOT%{_libdir}
install src/include/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}

# data
cp -r lib config examples $RPM_BUILD_ROOT%{_datadir}/%{name}
find $RPM_BUILD_ROOT%{_datadir}/%{name} -name Makefile -exec rm \{\} \;

install doc/festival{,_client}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGMENTS COPYING NEWS README
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lib
%dir %{_datadir}/%{name}/lib/dicts
%dir %{_datadir}/%{name}/lib/voices
%dir %{_datadir}/%{name}/lib/voices/english
%dir %{_datadir}/%{name}/lib/etc
%dir %{_datadir}/%{name}/lib/etc/%{fostype}
# XXX: ELF binary, fix it!
%attr(755,root,root) %{_datadir}/%{name}/lib/etc/%{fostype}/audsp
%{_datadir}/%{name}/lib/etc/email_filter
%{_datadir}/%{name}/lib/*.scm
%{_datadir}/%{name}/lib/Sable.v0_2.dtd
%{_datadir}/%{name}/lib/festival.el
%{_datadir}/%{name}/lib/sable-latin.ent
%{_datadir}/%{name}/lib/scfg_wsj_wp20.gram
%{_datadir}/%{name}/lib/sec.*.ngrambin
%{_datadir}/%{name}/lib/speech.properties
%{_datadir}/%{name}/examples

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_libdir}/libFestival.a
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/config

# no mbrola on amd64
%ifarch %{ix86} ppc alpha sparc
%files voices-english-mbrola-us
%defattr(644,root,root,755)
%{_datadir}/%{name}/lib/voices/english/us1_mbrola
%{_datadir}/%{name}/lib/voices/english/us2_mbrola
%{_datadir}/%{name}/lib/voices/english/us3_mbrola

%files voices-english-mbrola-en
%defattr(644,root,root,755)
%{_datadir}/%{name}/lib/voices/english/en1_mbrola
%endif
