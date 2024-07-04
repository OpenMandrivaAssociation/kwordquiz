#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	A general purpose flash card program
Name:		plasma6-kwordquiz
Version:	24.05.2
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kwordquiz
%if 0%{?git:1}
Source0:	https://invent.kde.org/education/kwordquiz/-/archive/%{gitbranch}/kwordquiz-%{gitbranchd}.tar.bz2#/kwordquiz-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kwordquiz-%{version}.tar.xz
%endif
# Currently can't do this because Plasma 5 provides it too
#BuildRequires:	cmake(LibKEduVocDocument)
BuildRequires:	%mklibname -d KEduVocDocument6
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6Sonnet)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Phonon4Qt6)

%description
KWordQuiz is a general purpose flash card program. It can be used for
vocabulary learning and many other subjects. If you need more advanced
language learning features, please try KVocTrain.

%files -f kwordquiz.lang
%{_datadir}/knsrcfiles/kwordquiz.knsrc
%{_bindir}/kwordquiz
%{_datadir}/metainfo/org.kde.kwordquiz.appdata.xml
%{_datadir}/config.kcfg/kwordquiz.kcfg
%{_datadir}/applications/org.kde.kwordquiz.desktop
%{_datadir}/kwordquiz
%{_iconsdir}/hicolor/*/*/*kwordquiz.*

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n kwordquiz-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kwordquiz --with-html
