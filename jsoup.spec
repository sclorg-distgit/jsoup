%{?scl:%scl_package jsoup}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

Name:           %{?scl_prefix}jsoup
Version:        1.8.2
Release:        2.3%{?dist}
Summary:        Java library for working with real-world HTML
License:        MIT
URL:            http://%{pkg_name}.org/
BuildArch:      noarch

Source0:        https://github.com/jhy/jsoup/archive/jsoup-%{version}%{?vertag}.tar.gz

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix_java_common}mvn(junit:junit)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.maven.plugins:maven-source-plugin)

%description
jsoup is a Java library for working with real-world HTML.
It provides a very convenient API for extracting and manipulating data,
using the best of DOM, CSS, and jquery-like methods.

jsoup implements the WHATWG HTML5 specification,
and parses HTML to the same DOM as modern browsers do.

 - scrape and parse HTML from a URL, file, or string
 - find and extract data, using DOM traversal or CSS selectors
 - manipulate the HTML elements, attributes, and text
 - clean user-submitted content against a safe white-list,
   to prevent XSS attacks
 - output tidy HTML

jsoup is designed to deal with all varieties of HTML found in the wild;
from pristine and validating, to invalid tag-soup;
jsoup will create a sensible parse tree.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%setup -q -n jsoup-jsoup-%{version}%{?vertag}
%pom_remove_plugin :animal-sniffer-maven-plugin
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%doc README CHANGES
%doc LICENSE
%dir %{_javadir}/jsoup
%dir %{_mavenpomdir}/jsoup

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Mon Jul 20 2015 Mat Booth <mat.booth@redhat.com> - 1.8.2-2.3
- Fix unowned directories

* Tue Jun 30 2015 Mat Booth <mat.booth@redhat.com> - 1.8.2-2.2
- Avoid license macro

* Tue Jun 23 2015 Mat Booth <mat.booth@redhat.com> - 1.8.2-2.1
- Import latest from Fedora

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.2-1
- Update to upstream version 1.8.2

* Mon Sep 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.1-1
- Update to upstream version 1.8.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7.2-3
- Update to current packaging guidelines

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.7.2-2
- Use Requires: java-headless rebuild (#1067528)

* Mon Aug 12 2013 Alexander Kurtakov <akurtako@redhat.com> 1.7.2-1
- Update to latest upstream.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.6.1-6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 04 2012 Jaromir Capik <jcapik@redhat.com> - 1.6.1-4
- Removing maven from Requires

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Jaromir Capik <jcapik@redhat.com> - 1.6.1-2
- Switching to sources from github

* Fri Jul 22 2011 Jaromir Capik <jcapik@redhat.com> - 1.6.1-1
- Initial package
