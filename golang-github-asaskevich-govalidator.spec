# https://github.com/asaskevich/govalidator
%global goipath         github.com/asaskevich/govalidator
%global commit          f9ffefc3facfbe0caee3fea233cbb6e8208f4541
Version:                9

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        Validators and sanitizers for strings, numerics, slices and structs
# Detected licences
# - Expat License at 'LICENSE'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}.


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}.

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%check
# I think some tests need an Internet connection to work
%gochecks -d .


%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md


%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 9-1.20181112gitf9ffefc
- bump to commit f9ffefc3facfbe0caee3fea233cbb6e8208f4541
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 14 2018 Ed Marshall <esm@logic.net> - 8-2
- Work around unit test breakage due to changes to net/uri in Go 1.10.

* Sat Oct 07 2017 Ed Marshall <esm@logic.net> - 8-1
- Update to latest upstream release.

* Sat Oct 07 2017 Ed Marshall <esm@logic.net> - 7-1
- Update to latest upstream release.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 04 2017 Ed Marshall <esm@logic.net> - 6-1
- First package for Fedora

