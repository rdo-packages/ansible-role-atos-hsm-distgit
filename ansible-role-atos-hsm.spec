%global milestone .0rc1

%global srcname ansible_role_atos_hsm
%global rolename ansible-role-atos-hsm

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{rolename}
Version:        6.0.0
Release:        0.1%{?milestone}%{?dist}
Summary:        Ansible role for configuring ATOS HSM Clients

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://git.openstack.org/cgit/openstack/ansible-role-atos-hsm
Source0:        https://tarballs.openstack.org/%{rolename}/%{rolename}-%{upstream_version}.tar.gz

#
# patches_base=6.0.0.0rc1
#

BuildArch:      noarch
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires: (python3dist(ansible) or ansible-core >= 2.11)

%description

Ansible role to configure ATOS HSM clients

%prep
%autosetup -n %{rolename}-%{upstream_version} -S git
#Remove ansible from requirements.txt as dependency on ansible is managed manually
sed -i '/^ansible/d' requirements.txt


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
* Fri Oct 20 2023 RDO <dev@lists.rdoproject.org> 6.0.0-0.1.0rc1
- Update to 6.0.0.0rc1


