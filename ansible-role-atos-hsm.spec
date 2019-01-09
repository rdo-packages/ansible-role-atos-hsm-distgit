%global srcname ansible_role_atos_hsm
%global rolename ansible-role-atos-hsm

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{rolename}
Version:        0.1.0
Release:        1
Summary:        Ansible role for configuring ATOS HSM Clients

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://github.com/dmend/ansible-role-atos-hsm
Source0:        https://github.com/dmend/ansible-role-atos-hsm/archive/v0.1.0.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python-d2to1
BuildRequires:  python2-pbr

Requires: ansible

%description

Ansible role to configure ATOS HSM clients

%prep
%autosetup -n %{rolename}-%{upstream_version} -S git


%build
%py2_build


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%py2_install


%files
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/roles/


%changelog
