Name:		texlive-iscram
Version:	45801
Release:	2
Summary:	A LaTeX class to publish article to ISCRAM conferences
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/iscram
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iscram.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iscram.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX class to publish article to ISCRAM (International
Conference on Information Systems for Crisis Response and
Management).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/iscram
%doc %{_texmfdistdir}/doc/latex/iscram

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
