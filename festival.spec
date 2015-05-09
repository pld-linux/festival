# TODO: kill ELF binary from %{_datadir}, see files
Summary:	The Festival speech sythesis system
Summary(pl.UTF-8):	System syntezy mowy Festival
Name:		festival
Version:	2.1
Release:	2
License:	BSD-like (except for festival.el, which is on GPL)
Group:		Applications/Sound
Source0:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/%{name}-%{version}-release.tar.gz
# Source0-md5:	c93eb3e389ed171ab9abd46afe8897a8
Source1:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/festvox_cmu_us_awb_cg.tar.gz
# Source1-md5:	2c14269587ad018ee93176bb44f4c38b
Source2:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/festvox_cmu_us_rms_cg.tar.gz
# Source2-md5:	a9514a9df32401774c074abec42ffb22
Source3:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/festvox_cmu_us_slt_arctic_hts.tar.gz
# Source3-md5:	a9b53441968f6bc612b85c04bbc4cf0f
Source4:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/festvox_kallpc16k.tar.gz
# Source4-md5:	3869af78f473b616601cac3fa83cc14e
Source5:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/festvox_rablpc16k.tar.gz
# Source5-md5:	34cb2478f5b8fa1ed02f5cbb496c1dcd
Patch0:		%{name}-config.patch
Patch1:		%{name}-pulse.patch
URL:		http://www.cstr.ed.ac.uk/projects/festival/
BuildRequires:	automake
BuildRequires:	speech_tools-devel >= 2.1-3
Requires:	festival-voice
Suggests:	festival-voice-english-slt-arctic-hts
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

%package voice-english-kal-diphone
Summary:	American English male speaker "Kevin" for Festival
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	festival-voice

%description voice-english-kal-diphone
American English male speaker ("Kevin") for Festival.

This voice provides an American English male voice using a residual
excited LPC diphone synthesis method. It uses the CMU Lexicon
pronunciations. Prosodic phrasing is provided by a statistically
trained model using part of speech and local distribution of breaks.
Intonation is provided by a CART tree predicting ToBI accents and an
F0 contour generated from a model trained from natural speech. The
duration model is also trained from data using a CART tree.

%package voice-english-rab-diphone
Summary:	British RP English male speaker "Roger" for Festival
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	festival-voice

%description voice-english-rab-diphone
British RP English male speaker ("Roger") for Festival.

This voice provides a British RP English male voice using a residual
excited LPC diphone synthesis method. It uses a modified Oxford
Advanced Learners' Dictionary for pronunciations. Prosodic phrasing is
provided by a statistically trained model using part of speech and
local distribution of breaks. Intonation is provided by a CART tree
predicting ToBI accents and an F0 contour generated from a model
trained from natural speech. The duration model is also trained from
data using a CART tree.

%package voice-english-awb-cg
Summary:	Scottish-accent US English male speaker "AWB" for Festival
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	festival-voice

%description voice-english-awb-cg
US English male speaker ("AWB") for Festival. AWB is a native Scottish
English speaker, but the voice uses the US English front end.

This is a HMM-based Speech Synthesis System (HTS) voice from the
Nagoya Institute of Technology, trained using the CMU ARCTIC database.
This voice is based on 1138 utterances spoken by a Scottish English
male speaker. The speaker is very experienced in building synthetic
voices and matched prompted US English, though his vowels are very
different from US English vowels. Scottish English speakers will
probably find synthesizers based on this voice strange. Unlike the
other CMU_ARCTIC databases this was recorded in 16 bit 16KHz mono
without EGG, on a Dell Laptop in a quiet office. The database was
automatically labelled using CMU Sphinx using the FestVox labelling
scripts. No hand correction has been made.

%package voice-english-rms-cg
Summary:	US English male speaker "RMS" for Festival
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	festival-voice

%description voice-english-rms-cg
US English male speaker ("RMS") voice for Festival.

This is a HMM-based Speech Synthesis System (HTS) voice from the
Nagoya Institute of Technology, trained using the CMU ARCTIC database.
This voice is based on 1132 utterances spoken by a US English male
speaker. The speaker is experienced in building synthetic voices. This
was recorded at 16bit 32KHz, in a sound proof room, in stereo, one
channel was the waveform, the other EGG. The database was
automatically labelled using EHMM an HMM labeler that is included in
the FestVox distribution. No hand correction has been made.

%package voice-english-slt-arctic-hts
Summary:	US English female speaker "SLT" for Festival
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	festival-voice

%description voice-english-slt-arctic-hts
US English female speaker ("SLT") voice for Festival.

This is a HMM-based Speech Synthesis System (HTS) voice from the
Nagoya Institute of Technology, trained using the CMU ARCTIC database.
This voice is based on 1132 utterances spoken by a US English female
speaker. The speaker is experienced in building synthetic voices. This
was recorded at 16bit 32KHz, in a sound proof room, in stereo, one
channel was the waveform, the other EGG. The database was
automatically labelled using CMU Sphinx using the FestVox labelling
scripts. No hand correction has been made.

%prep
%setup -q -n %{name} -b1 -b2 -b3 -b4 -b5
%patch0 -p1
%patch1 -p1

ln -s %{_libdir}/speech_tools/base_class src/modules/MultiSyn
ln -s %{_libdir}/speech_tools/config/modules/pulse_audio.mak config/modules

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

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
%dir %{_datadir}/%{name}/lib/multisyn
%dir %{_datadir}/%{name}/lib/voices
%dir %{_datadir}/%{name}/lib/voices/english
%dir %{_datadir}/%{name}/lib/etc
%dir %{_datadir}/%{name}/lib/etc/%{fostype}
# XXX: ELF binary, fix it!
%attr(755,root,root) %{_datadir}/%{name}/lib/etc/%{fostype}/audsp
%{_datadir}/%{name}/lib/etc/email_filter
%{_datadir}/%{name}/lib/*.scm
%{_datadir}/%{name}/lib/Sable.v0_2.dtd
%{_datadir}/%{name}/lib/Singing.v0_1.dtd
%{_datadir}/%{name}/lib/VCLocalRules
%{_datadir}/%{name}/lib/festival.el
%{_datadir}/%{name}/lib/sable-latin.ent
%{_datadir}/%{name}/lib/scfg_wsj_wp20.gram
%{_datadir}/%{name}/lib/sec.*.ngrambin
%{_datadir}/%{name}/lib/speech.properties
%{_datadir}/%{name}/lib/multisyn/*.scm
%{_datadir}/%{name}/examples

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_libdir}/libFestival.a
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/config

%files voice-english-kal-diphone
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/lib/voices
%dir %{_datadir}/%{name}/lib/voices/english
%{_datadir}/%{name}/lib/voices/english/kal_diphone

%files voice-english-rab-diphone
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/lib/voices
%dir %{_datadir}/%{name}/lib/voices/english
%{_datadir}/%{name}/lib/voices/english/rab_diphone

%files voice-english-awb-cg
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/lib/voices
%dir %{_datadir}/%{name}/lib/voices/us
%{_datadir}/%{name}/lib/voices/us/cmu_us_awb_cg

%files voice-english-rms-cg
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/lib/voices
%dir %{_datadir}/%{name}/lib/voices/us
%{_datadir}/%{name}/lib/voices/us/cmu_us_rms_cg

%files voice-english-slt-arctic-hts
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/lib/voices
%dir %{_datadir}/%{name}/lib/voices/us
%{_datadir}/%{name}/lib/voices/us/cmu_us_slt_arctic_hts
