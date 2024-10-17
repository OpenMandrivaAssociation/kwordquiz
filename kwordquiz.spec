%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	A general purpose flash card program
Name:		kwordquiz
Version:	23.08.5
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://edu.kde.org/kwordquiz
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(LibKEduVocDocument)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5Sonnet)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5KirigamiAddons)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Phonon4Qt5)

%description
KWordQuiz is a general purpose flash card program. It can be used for
vocabulary learning and many other subjects. If you need more advanced
language learning features, please try KVocTrain.

%files -f %{name}.lang
%{_datadir}/knsrcfiles/kwordquiz.knsrc
%{_bindir}/kwordquiz
%{_datadir}/metainfo/org.kde.kwordquiz.appdata.xml
%{_datadir}/config.kcfg/kwordquiz.kcfg
%{_datadir}/applications/org.kde.kwordquiz.desktop
%{_datadir}/knotifications5/kwordquiz.notifyrc
%{_datadir}/kwordquiz
%{_iconsdir}/hicolor/*/*/*kwordquiz.*

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
