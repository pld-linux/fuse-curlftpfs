%define		_name	curlftpfs
Summary:	A filesystem for accessing FTP sites
Summary(pl.UTF-8):	System plików pozwalający na dostęp do serwerów FTP
Name:		fuse-curlftpfs
Version:	0.9.1
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/curlftpfs/%{_name}-%{version}.tar.gz
# Source0-md5:	969998e9cf1663824f44739e94c703a1
URL:		http://curlftpfs.sourceforge.net/
BuildRequires:	curl-devel >= 7.15.2
BuildRequires:	glib2-devel
BuildRequires:	libfuse-devel
BuildRequires:	libstdc++-devel
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
%setup -q -n %{_name}-%{version}

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/curlftpfs
%{_mandir}/man1/curlftpfs.1*
