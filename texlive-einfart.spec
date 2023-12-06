Name:		texlive-einfart
Version:	68376
Release:	1
Summary:	Write your articles in a simple and clear way
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/einfart
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/einfart.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/einfart.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a LaTeX class for typesetting articles
with a simple and clear design. Currently, it has native
support for Chinese (simplified and traditional), English,
French, German, Italian, Japanese, Portuguese (European and
Brazilian), Russian and Spanish typesetting. It compiles with
either XeLaTeX or LuaLaTeX. This is part of the minimalist
class series and depends on minimalist.sty from the minimalist
package. The package name "einfart" is taken from the German
word "einfach" ("simple"), combined with the first three
letters of "Artikel" ("article").

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/einfart
%doc %{_texmfdistdir}/doc/latex/einfart

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
