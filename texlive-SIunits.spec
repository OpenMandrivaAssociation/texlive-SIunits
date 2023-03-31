Name:		texlive-SIunits
Version:	59702
Release:	2
Summary:	International System of Units
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/SIunits
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/siunits.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/siunits.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/siunits.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Typeset physical units following the rules of the International
System of Units (SI). The package requires amstext, for proper
representation of some values. Note that the package is now
superseded by siunitx; siunits has maintenance-only support,
now.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/siunits
%doc %{_texmfdistdir}/doc/latex/siunits
#- source
%doc %{_texmfdistdir}/source/latex/siunits

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
