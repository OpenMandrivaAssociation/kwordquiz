Summary:	A general purpose flash card program
Name:		kwordquiz
Version:	15.04.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kwordquiz
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdeedu-devel >= %{version}
BuildRequires:	kdelibs-devel

%description
KWordQuiz is a general purpose flash card program. It can be used for
vocabulary learning and many other subjects. If you need more advanced
language learning features, please try KVocTrain.

%files
%doc AUTHORS COPYING COPYING.LIB COPYING.DOC
%doc %{_kde_docdir}/*/*/kwordquiz
%{_kde_applicationsdir}/kwordquiz.desktop
%{_kde_appsdir}/kwordquiz
%{_kde_bindir}/kwordquiz
%{_kde_configdir}/kwordquiz.knsrc
%{_kde_datadir}/appdata/kwordquiz.appdata.xml
%{_kde_datadir}/config.kcfg/kwordquiz.kcfg
%{_kde_iconsdir}/*/*/apps/kwordquiz.*
%{_kde_iconsdir}/*/*/mimetypes/application-x-kwordquiz.*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
