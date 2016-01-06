%{?scl:%scl_package jsoup}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

Name:           %{?scl_prefix}jsoup
Version:        1.7.2
Release:        2%{?dist}
Summary:        Java library for working with real-world HTML

Group:          Development/Libraries
License:        MIT
URL:            http://%{pkg_name}.org/
BuildArch:      noarch

# https://github.com/jhy/jsoup/archive/jsoup-1.7.2.tar.gz
Source0:        %{pkg_name}-%{pkg_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix_java_common}junit
BuildRequires:  %{?scl_prefix_maven}maven-plugin-bundle
BuildRequires:  %{?scl_prefix_maven}maven-source-plugin
%{?scl:Requires: %scl_runtime}

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
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{pkg_name}-%{pkg_name}-%{version}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE README CHANGES

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Mon May 11 2015 Mat Booth <mat.booth@redhat.com> - 1.7.2-2
- Resolves: rhbz#1219013 - Fails to build from source

* Mon May 26 2014 Sami Wagiaalla <swagiaal@redhat.com> 1.7.2-1
- Build for DTS 3
- import new sources from rawhide.

* Thu Apr 4 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.6.1-7
- Drop javadoc subpackage.
- Drop runtime dependency to java 7.

* Tue Feb 19 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.6.1-6
- Initial contribution to SCL.

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
