Name:		texlive-beamer
Version:	64388
Release:	1
Summary:	A LaTeX class for producing presentations and slides
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer.r64388.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer.doc.r64388.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-pgf
Requires:	texlive-xcolor

%description
The beamer LaTeX class can be used for producing slides. Its
functionality is similar to Prosper but does not need any
external programs and can directly produce a presentation using
pdflatex. Beamer uses pgf for pdf/ps independent graphics.
Frames are created using \frame{...}, and a frame can build
multiple slides through a simple notation for specifying
material for each slide within a frame. Beamer supports
bibliographies, appendicies and transitions. Short versions of
title, authors, institute can also be specified as optional
parameters. A \plainframe{} allows a picture, for example, to
fill the whole frame. Support figure and table environments,
transparency effects, a \transduration command, animation
commands, a pauses environment. Beamer also provides
compatibility with other packages like prosper. The package now
incorporates the functionality of the former translator
package, which is used for customising the package for use in
other language environments.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/beamer
%doc %{_texmfdistdir}/doc/latex/beamer

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
