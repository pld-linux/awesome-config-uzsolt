Summary:	Uzsolt's settings to awesome window manager
Summary(hu.UTF-8):	Uzsolt beállításai az awesome ablakkezelőhöz
Name:		awesome-config-uzsolt
Version:	20090512
Release:	1
License:	GPL v2
Group:		X11/Window Managers
Source0:	http://carme.pld-linux.org/~uzsolt/sources/%{name}-%{version}.tar.bz2
# Source0-md5:	dbc39f8245288fc1bb39bae9625eec86
Requires:	awesome < 3.3
Requires:	awesome >= 3.2.1
Requires:	awesome-plugin-beautiful
Requires:	awesome-plugin-naughty
Requires:	awesome-plugin-wicked
Requires:	roxterm
Requires:	urxvt
Suggests:	claws-mail
Suggests:	irssi
Suggests:	lua-etree
Suggests:	lua-sqlite3
Suggests:	moc
Suggests:	newsbeuter
Suggests:	rsstail
Suggests:	taskcoach
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Uzsolt's settings to awesome window manager. Details see on README.

%description -l hu.UTF-8
Uzsolt beállításai az awesome ablakkezelőhöz. A részletekért lásd a
README-t.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/awesome-configs/uzsolt
tar -C $RPM_BUILD_ROOT%{_examplesdir}/awesome-configs/uzsolt -x -f %{SOURCE0}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_examplesdir}/awesome-configs
%dir %{_examplesdir}/awesome-configs/uzsolt
%attr(755,root,root) %{_examplesdir}/awesome-configs/uzsolt/start-newsbeuter
%{_examplesdir}/awesome-configs/uzsolt/*.lua
%{_examplesdir}/awesome-configs/uzsolt/README
%{_examplesdir}/awesome-configs/uzsolt/xinitrc
%{_examplesdir}/awesome-configs/uzsolt/awesome-resources
