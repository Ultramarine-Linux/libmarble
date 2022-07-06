
Name:           libmarble
Version:        1.3.0
Release:        1%{?dist}
Summary:        A GTK Library
URL:            https://gitlab.com/raggesilver/marble/
Source0:        https://gitlab.com/raggesilver/marble/-/archive/v1.3.0/marble-v1.3.0.tar.gz
License:        GPLv3+
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  gtk3-devel
BuildRequires:  gtk4-devel

%description
A GTK Library similar to libgranite

%package devel
Summary:        Development files for libmarble
Group:          Development/Libraries
License:        GPLv3+
Requires:       libmarble
%description devel
%summary


%prep
%autosetup -n marble-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%files

%{_libdir}/libmarble*
%{_libdir}/girepository-1.0/*
%{_datadir}/gir-1.0/*

%files devel
%{_includedir}/marble.h
%{_libdir}/pkgconfig/marble.pc
%{_datadir}/vala/vapi/marble*

%changelog
* Wed Jul 06 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 1.3.0-2
- initial build
