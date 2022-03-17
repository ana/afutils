# Conditional for release vs. snapshot builds. Set to 1 for release build.
%if ! 0%{?rel_build:1}
    %global rel_build 1
%endif

# Settings used for build from snapshots.
%if 0%{?rel_build}
    %global gittar          afutils-%{version}.tar.gz
%else
    %if ! 0%{?commit:1}
        %global commit      a74bc734330c9c9f2b91df4e796c4422ac57b918
    %endif
    %if ! 0%{?commit_date:1}
        %global commit_date 20211019
    %endif
    %global shortcommit     %(c=%{commit};echo ${c:0:9})
    %global gitrel          .%{commit_date}git%{shortcommit}
    %global gittar          afutils-%{shortcommit}.tar.gz
%endif

Summary: Avocado Utility Libraries
Name: python-afutils
Version: 0.0.1
Release: 1%{?gitrel}%{?dist}
License: GPLv2+ and GPLv2
URL: https://github.com/ana/afutils
%if 0%{?rel_build}
Source0: %{url}/archive/%{version}/%{gittar}
%else
Source0: %{url}/archive/%{commit}/%{gittar}
%endif

BuildArch: noarch
BuildRequires: python3-setuptools

%description
Avocado is a framework to perform automated testing.
This package contains libraries used by Avocado.

%package -n python3-afutils
Summary: %{summary}

%description -n python3-afutils
Avocado is a framework to perform automated testing.
This package contains libraries used by Avocado.

%prep
%if 0%{?rel_build}
%setup -q -n afutils-%{version}
%else
%setup -q -n afutils-%{commit}
%endif

%build
%py3_build

%install
%py3_install

%files -n python3-afutils
%license LICENSE
%doc README.md
%{_pkgdocdir}/README.rst
%{python3_sitelib}/afutils*


%changelog
* Thu Marc 17 2022 Ana Guerrero Lopez <anguerre@redhat.com> - 0.0.1-1
- Initial release

