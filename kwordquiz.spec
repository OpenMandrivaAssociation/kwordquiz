Summary:	A general purpose flash card program
Name:		kwordquiz
Version:	15.04.3
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kwordquiz
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
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

%description
KWordQuiz is a general purpose flash card program. It can be used for
vocabulary learning and many other subjects. If you need more advanced
language learning features, please try KVocTrain.

%files
%doc AUTHORS COPYING
%doc %{_docdir}/HTML/*/kwordquiz
%{_bindir}/kwordquiz
%{_datadir}/appdata/kwordquiz.appdata.xml
%{_datadir}/config.kcfg/kwordquiz.kcfg
%{_datadir}/applications/org.kde.kwordquiz.desktop
%{_datadir}/knotifications5/kwordquiz.knsrc
%{_datadir}/kwordquiz
%{_datadir}/kxmlgui5/kwordquiz
%{_iconsdir}/hicolor/*/*/*kwordquiz.png

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
