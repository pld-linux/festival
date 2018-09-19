# TODO: kill ELF binary from %{_datadir}, see files
Summary:	The Festival speech sythesis system
Summary(pl.UTF-8):	System syntezy mowy Festival
Name:		festival
Version:	2.4
Release:	2
License:	BSD-like (except for festival.el, which is on GPL)
Group:		Applications/Sound
Source0:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/%{name}-%{version}-release.tar.gz
# Source0-md5:	49707d2f6744d5a67f81a96c36f7cb59
Patch0:		%{name}-config.patch
Patch1:		%{name}-pulse.patch
URL:		http://www.cstr.ed.ac.uk/projects/festival/
BuildRequires:	automake
BuildRequires:	speech_tools-devel >= 2.4
Requires:	festival-voice
Requires:	speech_tools >= 2.4
Suggests:	festival-voice-english-slt-cg
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

%description -l pl.UTF-8
Festival jest platformą przeznaczoną do budowania systemów syntezy
mowy oraz do łatwego testowania różnych modułów składających się na
syntezator mowy. Można też używać programu jako maszynki czytającej
pliki tekstowe. Festival jest wielojęzyczny, lecz język angielski jest
najbardziej zaawansowany.

%package devel
Summary:	Festival developement environment
Summary(pl.UTF-8):	Festival - środowidko rozwojowe
Group:		Applications/Sound

%description devel
Festival developement environment.

%description devel -l pl.UTF-8
Festival - środowisko rozwojowe.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

ln -s %{_libdir}/speech_tools/base_class src/modules/MultiSyn
ln -s %{_libdir}/speech_tools/config/modules/pulse_audio.mak config/modules

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r rm -v

%build
cp -f /usr/share/automake/config.* .
%{__perl} -pi -e 's,^EST=.*,EST=%{_libdir}/speech_tools,' config/config.in
%configure2_13
%{__make} -j1 \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	ECHO_N='printf "%%s"' \
	OPTIMISE_CCFLAGS="%{rpmcflags}" \
	OPTIMISE_CXXFLAGS="%{rpmcflags}" \
	OPTIMISE_LINK="%{rpmldflags}" \
	REQUIRED_LIBDEPS=
# REQUIRED_LIBDEPS is workaround not to need static speech_tools libraries

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/lib/{voices/english,dicts},%{_libdir},%{_includedir}/%{name},%{_mandir}/man1}

# bin
install -p bin/festival_server* bin/text2wave $RPM_BUILD_ROOT%{_bindir}
install -p src/main/festival{,_client} $RPM_BUILD_ROOT%{_bindir}
cp -p doc/festival*.1 $RPM_BUILD_ROOT%{_mandir}/man1

# devel
cp -p src/lib/libFestival.a $RPM_BUILD_ROOT%{_libdir}
cp -p src/include/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}

# data
cp -a lib config examples $RPM_BUILD_ROOT%{_datadir}/%{name}
%{__rm} $RPM_BUILD_ROOT%{_datadir}/festival/lib/etc/unknown_Linux/.made
find $RPM_BUILD_ROOT%{_datadir}/%{name} -name Makefile | xargs rm -v

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGMENTS COPYING NEWS README
%attr(755,root,root) %{_bindir}/festival
%attr(755,root,root) %{_bindir}/festival_client
%attr(755,root,root) %{_bindir}/festival_server
%attr(755,root,root) %{_bindir}/festival_server_control
%attr(755,root,root) %{_bindir}/text2wave
%{_mandir}/man1/festival.1*
%{_mandir}/man1/festival_client.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/examples
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/VCLocalRules
%{_datadir}/%{name}/lib/festival.el
%{_datadir}/%{name}/lib/sable-latin.ent
%{_datadir}/%{name}/lib/scfg_wsj_wp20.gram
%{_datadir}/%{name}/lib/sec.*.ngrambin
%{_datadir}/%{name}/lib/speech.properties
%{_datadir}/%{name}/lib/*.dtd
%{_datadir}/%{name}/lib/*.scm
%dir %{_datadir}/%{name}/lib/etc
%{_datadir}/%{name}/lib/etc/email_filter
%dir %{_datadir}/%{name}/lib/etc/%{fostype}
# XXX: ELF binary, fix it!
%attr(755,root,root) %{_datadir}/%{name}/lib/etc/%{fostype}/audsp
%dir %{_datadir}/%{name}/lib/multisyn
%{_datadir}/%{name}/lib/multisyn/*.scm
# directories for festival data
%dir %{_datadir}/%{name}/lib/dicts

%files devel
%defattr(644,root,root,755)
%{_libdir}/libFestival.a
%{_includedir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/config
