%global tl_name iscram
%global tl_revision 45801

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	A LaTeX class to publish article to ISCRAM conferences
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/iscram
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/iscram.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/iscram.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LaTeX class to publish article to ISCRAM (International Conference on
Information Systems for Crisis Response and Management).

