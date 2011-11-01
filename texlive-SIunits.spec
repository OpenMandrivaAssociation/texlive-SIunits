Name:		texlive-SIunits
Version:	1.36
Release:	1
Summary:	International System of Units
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/SIunits
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/SIunits.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/SIunits.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/SIunits.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Typeset physical units following the rules of the International
System of Units (SI). The package requires amstext, for proper
representation of some values. Note that the package is now
superseded by siunitx; siunits has maintenance-only support,
now.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
