# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/SIunits
# catalog-date 2008-06-16 17:21:40 +0200
# catalog-license lppl1.3
# catalog-version 1.36
Name:		texlive-SIunits
Version:	1.36
Release:	3
Summary:	International System of Units
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/SIunits
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/SIunits.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/SIunits.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/SIunits.source.tar.xz
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
%{_texmfdistdir}/tex/latex/SIunits/SIunits.cfg
%{_texmfdistdir}/tex/latex/SIunits/SIunits.sty
%{_texmfdistdir}/tex/latex/SIunits/binary.sty
%doc %{_texmfdistdir}/doc/latex/SIunits/README
%doc %{_texmfdistdir}/doc/latex/SIunits/SIunits.pdf
#- source
%doc %{_texmfdistdir}/source/latex/SIunits/SIunits.drv
%doc %{_texmfdistdir}/source/latex/SIunits/SIunits.dtx
%doc %{_texmfdistdir}/source/latex/SIunits/SIunits.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.36-2
+ Revision: 756033
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.36-1
+ Revision: 719542
- texlive-SIunits
- texlive-SIunits
- texlive-SIunits
- texlive-SIunits
- texlive-SIunits

