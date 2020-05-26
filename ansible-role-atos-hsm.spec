
%global srcname ansible_role_atos_hsm
%global rolename ansible-role-atos-hsm

%{!?upstream_version: %global upstream_version %{commit}}
%global commit e51c244f4f323175d9c7db73065b087369701711
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

Name:           %{rolename}
Version:        0.1.0
Release:        0.1%{?alphatag}%{?dist}
Summary:        Ansible role for configuring ATOS HSM Clients

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://git.openstack.org/cgit/openstack/ansible-role-atos-hsm
Source0:        https://github.com/openstack/%{rolename}/archive/%{commit}.tar.gz#/%{rolename}-%{shortcommit}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires:       python3dist(ansible)

%description

Ansible role to configure ATOS HSM clients

%prep
%autosetup -n %{rolename}-%{upstream_version} -S git


%build
%{py3_build}


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{py3_install}


%files
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/roles/


%changelog
* Tue May 26 2020 Yatin Karel <ykarel@redhat.com> - 0.1.0-0.1
- Update to post 0.1.0 (e51c244f4f323175d9c7db73065b087369701711)

