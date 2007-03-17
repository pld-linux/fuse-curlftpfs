%define		_name	curlftpfs
Summary:	Filesystem based on CVS
Summary(pl):	System plików oparty na CVS-ie
Name:		fuse-curlftpfs
Version:	0.9
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/curlftpfs/%{_name}-%{version}.tar.gz
# Source0-md5:	7e29eb1963d4023bb7ea530a1b4274c4
URL:		http://curlftpfs.sourceforge.net/
BuildRequires:	curl-devel >= 7.15.2
BuildRequires:	glib2-devel
BuildRequires:	libfuse-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A filesystem for accessing FTP sites.
You can "mount" FTP shared directories in your very personal file system
and take advantage of local files ops.
It's based on libcurl and automatically reconnects when the server times out.

%description -l pl
System plików CurlFtpFS.
Dziêki niemu mo¿esz podmontowaæ katalogi FTP do swojego systemu plików
i korzystaæ z nich jak z plików lokalnych.
Bazuje na blibliotece libcurl, wspiera SSL i automatyczne odnawianie
po³±czenia.

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
