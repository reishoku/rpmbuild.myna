
%define gh_user jpki
%define gh_repo myna

%global goipath     github.com/%{gh_user}/%{gh_repo}

Name:  %{gh_repo:myna}
Version: 0.5.1
Release: 1%{dist}
Summary: Mynumber Card Utility and JPKI Signing Tool

License: MIT
URL: https://github.com/%{gh_user}/%{gh_repo}
Source0: %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires: golang
BuildRequires: go-rpm-macros
BuildRequires: pcsc-lite-devel
Recommends: openssl
Requires: pcsc-lite-libs

%description
Mynumber Card Utility and Signing Tool

%prep
%goprep -A

%build
%global gomodulesmode GO111MODULE=on;
%gobuild .

%install
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -D -s -p -m 0755 myna %{buildroot}%{_bindir}

%files
%{_bindir}/myna
%license LICENSE
%doc README.md

%changelog
* Sat Nov 01 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 0.5.1-1
- Initial RPM package for jpki/myna
