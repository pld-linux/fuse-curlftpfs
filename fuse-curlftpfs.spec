Summary:	A filesystem for accessing FTP sites
Summary(pl.UTF-8):	System plików pozwalający na dostęp do serwerów FTP
Name:		fuse-curlftpfs
Version:	0.9.2
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/curlftpfs/curlftpfs-%{version}.tar.gz
# Source0-md5:	b452123f755114cd4461d56c648d9f12
URL:		http://curlftpfs.sourceforge.net/
BuildRequires:	curl-devel >= 7.17.0
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libfuse-devel >= 2.2
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
Requires:	curl-libs >= 7.17.0
Requires:	libfuse >= 2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A filesystem for accessing FTP sites. You can "mount" FTP shared
directories in your very personal file system and take advantage of
local files ops. It's based on libcurl and automatically reconnects
when the server times out.

%description -l pl.UTF-8
System plików CurlFtpFS. Dzięki niemu można podmontować katalogi FTP
do swojego systemu plików i korzystać z nich jak z plików lokalnych.
Bazuje na blibliotece libcurl, obsługuje SSL i automatyczne odnawianie
połączenia.

%prep
%setup -q -n curlftpfs-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install curlftpfs $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/curlftpfs
%{_mandir}/man1/curlftpfs.1*
