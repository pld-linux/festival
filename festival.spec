Summary:	The Festival speech sythesis system
Summary(pl):	System syntezy g³osu Festival
Name:		festival
Version:	1.4.2
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://www.cstr.ed.ac.uk/download/festival/%{version}/%{name}-%{version}-release.tar.gz
#Source1:	ftp://voruta.ek.univ.gda.pl:21/emacspeak/festival_polish_voice.tgz
Patch0:		%{name}-config.patch
URL:		http://www.cstr.ed.ac.uk/projects/festival/
BuildRequires:	speech_tools-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%configure2_13
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_libdir},%{_includedir}/%{name},%{_mandir}/man1}

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
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/examples

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_libdir}/*
%{_datadir}/%{name}/config
