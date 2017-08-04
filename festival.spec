# TODO: kill ELF binary from %{_datadir}, see files
Summary:	The Festival speech sythesis system
Summary(pl.UTF-8):	System syntezy mowy Festival
Name:		festival
Version:	2.4
Release:	1
License:	BSD-like (except for festival.el, which is on GPL)
Group:		Applications/Sound
Source0:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/%{name}-%{version}-release.tar.gz
# Source0-md5:	49707d2f6744d5a67f81a96c36f7cb59
Source1:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/voices/festvox_cmu_us_ahw_cg.tar.gz
# Source1-md5:	523b518e9da28c90e80c87a06de470a4
Source2:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/voices/festvox_cmu_us_aup_cg.tar.gz
# Source2-md5:	b2c4c78a0be1fc878ba8893e3e15bb9f
Source3:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/voices/festvox_cmu_us_awb_cg.tar.gz
# Source3-md5:	53d93d0ee910bde62d85ca261edd67e1
Source4:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/voices/festvox_cmu_us_axb_cg.tar.gz
# Source4-md5:	4f3b23b522482139a51a1083a30542cb
Source5:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/voices/festvox_cmu_us_bdl_cg.tar.gz
# Source5-md5:	d665708938035b0aa4e87de855e5e013
Source6:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/voices/festvox_cmu_us_clb_cg.tar.gz
# Source6-md5:	0931e03fd79a4c3bbdef5beca2b72429
Source7:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/voices/festvox_cmu_us_fem_cg.tar.gz
# Source7-md5:	06455a3b3fca52087a63708356decc1d
Source8:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/voices/festvox_cmu_us_gka_cg.tar.gz
# Source8-md5:	ecbbb2f0d516ea315242cd0765e866bd
Source9:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/voices/festvox_cmu_us_jmk_cg.tar.gz
# Source9-md5:	e5a7900dd0878d9ea1f366a5c4dcb39b
Source10:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/voices/festvox_cmu_us_ksp_cg.tar.gz
# Source10-md5:	ada3249931e3cbab8f624d5c7107a2eb
Source11:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/voices/festvox_cmu_us_rms_cg.tar.gz
# Source11-md5:	9dca49338804f4081ebc2e65ac1b88fe
Source12:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/voices/festvox_cmu_us_rxr_cg.tar.gz
# Source12-md5:	4d349e3fe9cdf81af97b42604509647a
Source13:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/voices/festvox_cmu_us_slt_cg.tar.gz
# Source13-md5:	d7f992fea3000e2aa2139d72103dd17f
Source14:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/voices/festvox_kallpc16k.tar.gz
# Source14-md5:	3869af78f473b616601cac3fa83cc14e
Source15:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/voices/festvox_rablpc16k.tar.gz
# Source15-md5:	34cb2478f5b8fa1ed02f5cbb496c1dcd
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

%package voice-english-kal-diphone
Summary:	American English male speaker "Kevin" for Festival
Summary(pl.UTF-8):	Głos męski "Kevin" mówiący amerykańską odmianą angielskiego dla syntezatora mowy Festival
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

%description voice-english-kal-diphone -l pl.UTF-8
Głos męski "Kevin" mówiący amerykańską odmianą angielskiego dla
syntezatora mowy Festival.

Głos powstał przy użyciu syntezy dwuzgłosek metodą liniowej predykcji
pobudzonej sygnałem resztkowym. Frazowanie prozodyczne zapewnia moduł
uczony statystycznie wykorzystujący części mowy i lokalną dystrybucję
przerw. Intonację zapewnia drzewo CART przewidujące akcenty ToBI oraz
kontur F0 wygenerowany przez model wyuczonego z mowy naturalnej. Model
iloczasów został także wyuczony z danych przy użyciu drzewa CART.

%package voice-english-rab-diphone
Summary:	British RP English male speaker "Roger" for Festival
Summary(pl.UTF-8):	Głos męski "Roger" mówiący brytyjską (RP) odmianą angielskiego dla syntezatora mowy Festival
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

%description voice-english-rab-diphone -l pl.UTF-8
Głos męski "Roger" mówiący brytyjską (RP) odmianą angielskiego dla
syntezatora mowy Festival.

Głos powstał przy użyciu syntezy dwuzgłosek metodą liniowej predykcji
pobudzonej sygnałem resztkowym. Wykorzystuje wymowę ze zmodyfikowanego
słownika Oxford Advanced Learners' Dictionary. Frazowanie prozodyczne
zapewnia moduł uczony statystycznie wykorzystujący części mowy i
lokalną dystrybucję przerw. Intonację zapewnia drzewo CART
przewidujące akcenty ToBI oraz kontur F0 wygenerowany przez model
wyuczonego z mowy naturalnej. Model iloczasów został także wyuczony z
danych przy użyciu drzewa CART.

%package voice-english-ahw-cg
Summary:	German-accent US English male speaker "AHW" for Festival
Summary(pl.UTF-8):	Głos męski "AHW" mówiący amerykańską odmianą angielskiego z niemieckim akcentem dla syntezatora mowy Festival
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	festival-voice

%description voice-english-ahw-cg
German-accent US English male speaker "AHW" for Festival.

%description voice-english-ahw-cg -l pl.UTF-8
Głos męski "AHW" mówiący amerykańską odmianą angielskiego z niemieckim
akcentem dla syntezatora mowy Festival.

%package voice-english-aup-cg
Summary:	Indian English male speaker "AUP" for Festival
Summary(pl.UTF-8):	Głos męski "AUP" mówiący indyjską odmianą angielskiego dla syntezatora mowy Festival
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	festival-voice

%description voice-english-aup-cg
Indian English male speaker "AUP" for Festival.

%description voice-english-aup-cg -l pl.UTF-8
Głos męski "AUP" mówiący indyjską odmianą angielskiego dla syntezatora
mowy Festival.

%package voice-english-awb-cg
Summary:	Scottish-accent US English male speaker "AWB" for Festival
Summary(pl.UTF-8):	Głos męski "AWB" mówiący amerykańską odmianą angielskiego ze szkockim akcentem dla syntezatora mowy Festival
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	festival-voice

%description voice-english-awb-cg
US English male speaker ("AWB") for Festival. AWB is a native Scottish
English speaker, but the voice uses the US English front end.

This voice is based on 1138 utterances spoken by a Scottish English
male speaker. The speaker is very experienced in building synthetic
voices and matched prompted US English, though his vowels are very
different from US English vowels. Scottish English speakers will
probably find synthesizers based on this voice strange. Unlike the
other CMU_ARCTIC databases this was recorded in 16 bit 16kHz mono
without EGG, on a Dell Laptop in a quiet office. The database was
automatically labelled using CMU Sphinx using the FestVox labelling
scripts. No hand correction has been made.

%description voice-english-awb-cg -l pl.UTF-8
Głos męski "AWB" mówiący amerykańską odmianą angielskiego ze szkockim
akcentem dla syntezatora mowy Festival.

Głos jest oparty na 1138 wyrażeniach mówionych przez mężczyznę
posługującego się szkockim angielskim. Człowiek ten ma duże
doświadczenie w tworzeniu głosów syntetycznych i dostosowywał się do
podpowiedzi w amerykańskiej odmianie angielskiego, chociaż jego
samogłoski różnią się od samogłosek w odmianie amerykańskiej. Mówiący
szkockim angielskim prawdopodobnie uznają syntezatory oparte na tym
głosie za brzmiące dziwnie. W przeciwieństwie do innych głosów z bazy
CMU_ARCTIC ten został nagrany w 16 bitach przy 16kHz mono bez EGG, na
laptopie Dell w cichym biurze. Baza danych była automatycznie
oznaczana przez CMU Sphinx przy użyciu skryptów oznaczających FestVox.
Nie były wykonywane żadne ręczne korekty.

%package voice-english-axb-cg
Summary:	Indian English female speaker "AXB" for Festival
Summary(pl.UTF-8):	Głos żeński "AXB" mówiący indyjską odmianą angielskiego dla syntezatora mowy Festival
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	festival-voice

%description voice-english-axb-cg
Indian English female speaker "AXB" for Festival.

%description voice-english-axb-cg -l pl.UTF-8
Głos żeński "AXB" mówiący indyjską odmianą angielskiego dla
syntezatora mowy Festival.

%package voice-english-bdl-cg
Summary:	US English male speaker "BDL" for Festival
Summary(pl.UTF-8):	Głos męski "BDL" mówiący amerykańską odmianą angielskiego dla syntezatora mowy Festival
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	festival-voice

%description voice-english-bdl-cg
US English male speaker "BDL" for Festival.

%description voice-english-bdl-cg -l pl.UTF-8
Głos męski "BDL" mówiący amerykańską odmianą angielskiego dla
syntezatora mowy Festival.

%package voice-english-clb-cg
Summary:	US English female speaker "CLB" for Festival
Summary(pl.UTF-8):	Głos żeński "CLB" mówiący amerykańską odmianą angielskiego dla syntezatora mowy Festival
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	festival-voice

%description voice-english-clb-cg
US English female speaker "BDL" for Festival.

%description voice-english-clb-cg -l pl.UTF-8
Głos żeński "BDL" mówiący amerykańską odmianą angielskiego dla
syntezatora mowy Festival.

%package voice-english-fem-cg
Summary:	German-accent US English male speaker "FEM" for Festival
Summary(pl.UTF-8):	Głos męski "FEM" mówiący amerykańską odmianą angielskiego z niemieckim akcentem dla syntezatora mowy Festival
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	festival-voice

%description voice-english-fem-cg
German-accent US English male speaker "FEM" for Festival.

%description voice-english-fem-cg -l pl.UTF-8
Głos męski "FEM" mówiący amerykańską odmianą angielskiego z niemieckim
akcentem dla syntezatora mowy Festival.

%package voice-english-gka-cg
Summary:	Indian English male speaker "GKA" for Festival
Summary(pl.UTF-8):	Głos męski "GKA" mówiący indyjską odmianą angielskiego dla syntezatora mowy Festival
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	festival-voice

%description voice-english-gka-cg
Indian English male speaker "GKA" for Festival.

%description voice-english-gka-cg -l pl.UTF-8
Głos męski "GKA" mówiący indyjską odmianą angielskiego dla
syntezatora mowy Festival.

%package voice-english-jmk-cg
Summary:	US English male speaker "JMK" for Festival
Summary(pl.UTF-8):	Głos męski "JMK" mówiący amerykańską odmianą angielskiego dla syntezatora mowy Festival
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	festival-voice

%description voice-english-jmk-cg
US English male speaker "JMK" for Festival.

%description voice-english-jmk-cg -l pl.UTF-8
Głos męski "JMK" mówiący amerykańską odmianą angielskiego dla
syntezatora mowy Festival.

%package voice-english-ksp-cg
Summary:	Indian English male speaker "KSP" for Festival
Summary(pl.UTF-8):	Głos męski "KSP" mówiący indyjską odmianą angielskiego dla syntezatora mowy Festival
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	festival-voice

%description voice-english-ksp-cg
Indian English male speaker "KSP" for Festival.

%description voice-english-ksp-cg -l pl.UTF-8
Głos męski "KSP" mówiący indyjską odmianą angielskiego dla
syntezatora mowy Festival.

%package voice-english-rms-cg
Summary:	US English male speaker "RMS" for Festival
Summary(pl.UTF-8):	Głos męski "RMS" mówiący amerykańską odmianą angielskiego dla syntezatora mowy Festival
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	festival-voice

%description voice-english-rms-cg
US English male speaker ("RMS") voice for Festival.

This voice is based on 1132 utterances spoken by a US English male
speaker. The speaker is experienced in building synthetic voices. This
was recorded at 16bit 32kHz, in a sound proof room, in stereo, one
channel was the waveform, the other EGG. The database was
automatically labelled using EHMM and HMM labeler that is included in
the FestVox distribution. No hand correction has been made.

%description voice-english-rms-cg -l pl.UTF-8
Głos męski "RMS" mówiący amerykańską odmianą angielskiego dla
syntezatora mowy Festival.

Głos jest oparty na 1132 wyrażeniach mówionych w amerykańskiej
odmianie języka angielskiego przez mężczyznę mającego doświadczenie w
tworzeniu głosów syntetycznych. Nagranie wykonano w 16 bitach przy
32kHz, w dźwiękoszczelnym pomieszczeniu, stereofonicznie - jeden kanał
był właściwą falą, drugi EGG. Baza danych była automatycznie oznaczana
przez narzędzia EHMM i HMM z dystrybucji FestVox. Nie były wykonywane
żadne ręczne korekty.

%package voice-english-rxr-cg
Summary:	US English male speaker "RXR" for Festival
Summary(pl.UTF-8):	Głos męski "RXR" mówiący amerykańską odmianą angielskiego dla syntezatora mowy Festival
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	festival-voice

%description voice-english-rxr-cg
US English male speaker "RXR" for Festival.

%description voice-english-rxr-cg -l pl.UTF-8
Głos męski "RXR" mówiący amerykańską odmianą angielskiego dla
syntezatora mowy Festival.

%package voice-english-slt-cg
Summary:	US English female speaker "SLT" for Festival
Summary(pl.UTF-8):	Angielski (amerykański) głos żeński "SLT" dla Festivala
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	festival-voice
# shoud it obsolete or coexist?
#Obsoletes:	festival-voice-english-slt-arctic-hts

%description voice-english-slt-cg
US English female speaker ("SLT") voice for Festival.

This voice is based on 1132 utterances spoken by a US English female
speaker. The speaker is experienced in building synthetic voices. This
was recorded at 16bit 32kHz, in a sound proof room, in stereo, one
channel was the waveform, the other EGG. The database was
automatically labelled using CMU Sphinx using the FestVox labelling
scripts. No hand correction has been made.

%description voice-english-slt-cg -l pl.UTF-8
Angielski (amerykański) głos żeński "SLT" dla syntezatora Festival.

Głos jest oparty na 1132 wyrażeniach mówionych w amerykańskiej
odmianie języka angielskiego przez kobietę mającą doświadczenie w
tworzeniu głosów syntetycznych. Nagranie wykonano w 16 bitach przy
32kHz, w dźwiękoszczelnym pomieszczeniu, stereofonicznie - jeden kanał
był właściwą falą, drugi EGG. Baza danych była automatycznie oznaczana
przez CMU Sphinx przy użyciu skryptów oznaczających FestVox. Nie były
wykonywane żadne ręczne korekty.

%prep
%setup -q -n %{name} -b1 -b2 -b3 -b4 -b5 -b6 -b7 -b8 -b9 -b10 -b11 -b12 -b13 -b14 -b15
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
# REQUIRED_LIBDEPS is workaround not to need static speech_tools libraries

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

install doc/festival*.1 $RPM_BUILD_ROOT%{_mandir}/man1

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
%dir %{_datadir}/%{name}/lib/voices
%dir %{_datadir}/%{name}/lib/voices/english
%dir %{_datadir}/%{name}/lib/voices/us

%files devel
%defattr(644,root,root,755)
%{_libdir}/libFestival.a
%{_includedir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/config

%files voice-english-kal-diphone
%defattr(644,root,root,755)
%{_datadir}/%{name}/lib/voices/english/kal_diphone

%files voice-english-rab-diphone
%defattr(644,root,root,755)
%{_datadir}/%{name}/lib/voices/english/rab_diphone

%files voice-english-ahw-cg
%defattr(644,root,root,755)
%{_datadir}/%{name}/lib/voices/us/cmu_us_ahw_cg

%files voice-english-aup-cg
%defattr(644,root,root,755)
%{_datadir}/%{name}/lib/voices/us/cmu_us_aup_cg

%files voice-english-awb-cg
%defattr(644,root,root,755)
%{_datadir}/%{name}/lib/voices/us/cmu_us_awb_cg

%files voice-english-axb-cg
%defattr(644,root,root,755)
%{_datadir}/%{name}/lib/voices/us/cmu_us_axb_cg

%files voice-english-bdl-cg
%defattr(644,root,root,755)
%{_datadir}/%{name}/lib/voices/us/cmu_us_bdl_cg

%files voice-english-clb-cg
%defattr(644,root,root,755)
%{_datadir}/%{name}/lib/voices/us/cmu_us_clb_cg

%files voice-english-fem-cg
%defattr(644,root,root,755)
%{_datadir}/%{name}/lib/voices/us/cmu_us_fem_cg

%files voice-english-gka-cg
%defattr(644,root,root,755)
%{_datadir}/%{name}/lib/voices/us/cmu_us_gka_cg

%files voice-english-jmk-cg
%defattr(644,root,root,755)
%{_datadir}/%{name}/lib/voices/us/cmu_us_jmk_cg

%files voice-english-ksp-cg
%defattr(644,root,root,755)
%{_datadir}/%{name}/lib/voices/us/cmu_us_ksp_cg

%files voice-english-rms-cg
%defattr(644,root,root,755)
%{_datadir}/%{name}/lib/voices/us/cmu_us_rms_cg

%files voice-english-rxr-cg
%defattr(644,root,root,755)
%{_datadir}/%{name}/lib/voices/us/cmu_us_rxr_cg

%files voice-english-slt-cg
%defattr(644,root,root,755)
%{_datadir}/%{name}/lib/voices/us/cmu_us_slt_cg
