#
# ToDo:
# - fix desktop file

Summary:	Clone of popular hearts game
Summary(pl):	Klon popularnej gry hearts
Name:		hearts
Version:	1.98
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/hearts/%{name}-%{version}.tar.bz2
# Source0-md5:	160c349537d963234aa9b984cb124bb5
Patch0:		%{name}-am_fixes.patch
URL:		http://hearts.luispedro.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a clone of MS Windows' hearts game. Currently a stable version
supports local play, while a development version supports network
play.

%description -l pl
Jest to klon znanej z MS Windows gry hearts (kierki). Wersja stabilna
pozwala tylko na grê lokaln±, w wersji rozwojowej dostêpna jest
mo¿liwo¶c gry przez sieæ.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT{%{_datadir}/applnk/Games/Card/,%{_desktopdir}/kde}/hearts.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kde/hearts.desktop
%{_datadir}/apps/%{name}
%{_iconsdir}/hicolor/16x16/apps/hearts.png
%{_iconsdir}/hicolor/32x32/apps/hearts.png
