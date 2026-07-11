%global tl_name siunits
%global tl_revision 59702

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.36
Release:	%{tl_revision}.1
Summary:	International System of Units
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/SIunits
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/siunits.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/siunits.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/siunits.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Typeset physical units following the rules of the International System
of Units (SI). The package requires amstext, for proper representation
of some values. Note that the package is now superseded by siunitx;
siunits has maintenance-only support, now.

