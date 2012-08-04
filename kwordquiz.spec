Name:		kwordquiz
Summary:	A general purpose flash card program
Version: 4.9.0
Release: 1
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2 GFDL
URL:		http://edu.kde.org/kwordquiz
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	libkdeedu-devel >= %{version}
Requires:	libkdeedu = %{version}

%description
KWordQuiz is a general purpose flash card program. It can be used for
vocabulary learning and many other subjects. If you need more advanced
language learning features, please try KVocTrain.

%files
%doc AUTHORS COPYING COPYING.LIB COPYING.DOC
%{_kde_appsdir}/kwordquiz
%{_kde_bindir}/kwordquiz
%{_kde_iconsdir}/*/*/apps/kwordquiz.*
%{_kde_iconsdir}/*/*/mimetypes/application-x-kwordquiz.*
%{_kde_applicationsdir}/kwordquiz.desktop
%{_kde_datadir}/config.kcfg/kwordquiz.kcfg
%{_kde_configdir}/kwordquiz.knsrc
%{_kde_docdir}/*/*/kwordquiz

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

