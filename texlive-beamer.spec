%global tl_name beamer
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.77
Release:	%{tl_revision}.1
Summary:	A LaTeX class for producing presentations and slides
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer
License:	lppl1.3c gpl2+ fdl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Requires:	texlive(amscls)
Requires:	texlive(amsfonts)
Requires:	texlive(amsmath)
Requires:	texlive(atbegshi)
Requires:	texlive(etoolbox)
Requires:	texlive(geometry)
Requires:	texlive(hyperref)
Requires:	texlive(iftex)
Requires:	texlive(pgf)
Requires:	texlive(translator)
Requires:	texlive(xcolor)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The beamer LaTeX class can be used for producing slides. The class works
in both PostScript and direct PDF output modes, using the pgf graphics
system for visual effects. Content is created in the frame environment,
and each frame can be made up of a number of slides using a simple
notation for specifying material to appear on each slide within a frame.
Short versions of title, authors, institute can also be specified as
optional parameters. Whole frame graphics are supported by plain frames.
The class supports figure and table environments, transparency effects,
varying slide transitions and animations. Beamer also provides
compatibility with other packages like prosper. The package now
incorporates the functionality of the former translator package, which
is used for customising the package for use in other language
environments. Beamer depends on the following other packages: atbegshi,
etoolbox, hyperref, ifpdf, pgf, and translator.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamer
%dir %{_datadir}/texmf-dist/tex/latex/beamer
%dir %{_datadir}/texmf-dist/doc/latex/beamer/emulation-examples
%dir %{_datadir}/texmf-dist/doc/latex/beamer/examples
%dir %{_datadir}/texmf-dist/doc/latex/beamer/licenses
%dir %{_datadir}/texmf-dist/doc/latex/beamer/solutions
%dir %{_datadir}/texmf-dist/doc/latex/beamer/examples/a-conference-talk
%dir %{_datadir}/texmf-dist/doc/latex/beamer/examples/a-lecture
%dir %{_datadir}/texmf-dist/doc/latex/beamer/solutions/conference-talks
%dir %{_datadir}/texmf-dist/doc/latex/beamer/solutions/generic-talks
%dir %{_datadir}/texmf-dist/doc/latex/beamer/solutions/short-talks
%doc %{_datadir}/texmf-dist/doc/latex/beamer/AUTHORS.md
%doc %{_datadir}/texmf-dist/doc/latex/beamer/CHANGELOG.md
%doc %{_datadir}/texmf-dist/doc/latex/beamer/LICENSE.md
%doc %{_datadir}/texmf-dist/doc/latex/beamer/README.md
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamercolorthemeexample.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerexample-conference-talk.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerexample-lecture-beamer-version.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerexample-lecture-print-version.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerfontthemeexample.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerinnerthemeexample.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerlogo.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerouterthemeexample.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerthemeexample.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerthemeexamplebase.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-animations.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-color.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-compatibility.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-elements.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-emulation.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-fonts.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-frames.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-globalstructure.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-graphics.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-guidelines.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-installation.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-interaction.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-introduction.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-license.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-localstructure.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-macros.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-nonpresentation.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-notes.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-overlays.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-solutions.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-themes.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-transparencies.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-tricks.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-tutorial.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-twoscreens.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beamerug-workflow.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beameruserguide.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamer/beameruserguide.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/emulation-examples/beamerexample-foils.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/emulation-examples/beamerexample-prosper.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/emulation-examples/beamerexample-seminar.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/emulation-examples/beamerexample-texpower.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/examples/a-conference-talk/beamerexample-conference-talk.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-beamer-version.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-body.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-logo.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic1.jpg
%doc %{_datadir}/texmf-dist/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic2.jpg
%doc %{_datadir}/texmf-dist/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic3.jpg
%doc %{_datadir}/texmf-dist/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic4.jpg
%doc %{_datadir}/texmf-dist/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic5.jpg
%doc %{_datadir}/texmf-dist/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic6.jpg
%doc %{_datadir}/texmf-dist/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-print-version.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-style.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/licenses/fdl.txt
%doc %{_datadir}/texmf-dist/doc/latex/beamer/licenses/gpl-2.0.txt
%doc %{_datadir}/texmf-dist/doc/latex/beamer/licenses/lppl-1-3c.txt
%doc %{_datadir}/texmf-dist/doc/latex/beamer/licenses/manifest-code.txt
%doc %{_datadir}/texmf-dist/doc/latex/beamer/licenses/manifest-documentation.txt
%doc %{_datadir}/texmf-dist/doc/latex/beamer/solutions/conference-talks/conference-ornate-20min.de.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/solutions/conference-talks/conference-ornate-20min.en.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/solutions/conference-talks/conference-ornate-20min.fr.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/solutions/generic-talks/generic-ornate-15min-45min.de.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/solutions/generic-talks/generic-ornate-15min-45min.en.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/solutions/generic-talks/generic-ornate-15min-45min.fr.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/solutions/short-talks/speaker_introduction-ornate-2min.de.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/solutions/short-talks/speaker_introduction-ornate-2min.en.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer/solutions/short-talks/speaker_introduction-ornate-2min.fr.tex
%{_datadir}/texmf-dist/tex/latex/beamer/beamer.cls
%{_datadir}/texmf-dist/tex/latex/beamer/beamerarticle.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbasearticle.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbaseauxtemplates.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbaseboxes.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbasecolor.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbasecompatibility.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbasedecode.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbasefont.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbaseframe.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbaseframecomponents.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbaseframesize.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbaselocalstructure.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbasemisc.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbasemodes.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbasenavigation.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbasenavigationsymbols.tex
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbasenotes.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbaseoptions.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbaseoverlay.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbaserequires.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbasesection.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbasetemplates.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbasethemes.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbasetheorems.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbasetitle.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbasetoc.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbasetranslator.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbasetwoscreens.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerbaseverbatim.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamercolorthemealbatross.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamercolorthemebeaver.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamercolorthemebeetle.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamercolorthemecrane.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamercolorthemedefault.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamercolorthemedolphin.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamercolorthemedove.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamercolorthemefly.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamercolorthemelily.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamercolorthememonarca.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamercolorthemeorchid.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamercolorthemerose.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamercolorthemeseagull.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamercolorthemeseahorse.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamercolorthemesidebartab.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamercolorthemespruce.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamercolorthemestructure.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamercolorthemewhale.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamercolorthemewolverine.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerfoils.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerfontthemedefault.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerfontthemeprofessionalfonts.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerfontthemeserif.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerfontthemestructurebold.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerfontthemestructureitalicserif.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerfontthemestructuresmallcapsserif.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamericonarticle.20.eps
%{_datadir}/texmf-dist/tex/latex/beamer/beamericonarticle.20.pdf
%{_datadir}/texmf-dist/tex/latex/beamer/beamericonarticle.eps
%{_datadir}/texmf-dist/tex/latex/beamer/beamericonarticle.pdf
%{_datadir}/texmf-dist/tex/latex/beamer/beamericonarticle.tex
%{_datadir}/texmf-dist/tex/latex/beamer/beamericonbook.20.eps
%{_datadir}/texmf-dist/tex/latex/beamer/beamericonbook.20.pdf
%{_datadir}/texmf-dist/tex/latex/beamer/beamericonbook.eps
%{_datadir}/texmf-dist/tex/latex/beamer/beamericonbook.pdf
%{_datadir}/texmf-dist/tex/latex/beamer/beamericonbook.tex
%{_datadir}/texmf-dist/tex/latex/beamer/beamericononline.20.eps
%{_datadir}/texmf-dist/tex/latex/beamer/beamericononline.20.pdf
%{_datadir}/texmf-dist/tex/latex/beamer/beamericononline.eps
%{_datadir}/texmf-dist/tex/latex/beamer/beamericononline.pdf
%{_datadir}/texmf-dist/tex/latex/beamer/beamerinnerthemecircles.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerinnerthemedefault.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerinnerthemeinmargin.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerinnerthemerectangles.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerinnerthemerounded.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerouterthemedefault.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerouterthemeinfolines.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerouterthememiniframes.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerouterthemeshadow.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerouterthemesidebar.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerouterthemesmoothbars.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerouterthemesmoothtree.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerouterthemesplit.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerouterthemetree.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerpatchparalist.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerprosper.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerseminar.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamertexpower.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeAnnArbor.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeAntibes.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeBergen.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeBerkeley.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeBerlin.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeBoadilla.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeCambridgeUS.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeCopenhagen.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeDarmstadt.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeDresden.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeEastLansing.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeFrankfurt.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeGoettingen.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeHannover.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeIlmenau.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeJuanLesPins.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeLuebeck.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeMadrid.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeMalmoe.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeMarburg.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeMontpellier.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemePaloAlto.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemePittsburgh.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeRochester.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeSingapore.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeSzeged.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeWarsaw.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemebars.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeboxes.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeclassic.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemecompatibility.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemedefault.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemelined.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeplain.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemeshadow.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemesidebar.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemesplit.sty
%{_datadir}/texmf-dist/tex/latex/beamer/beamerthemetree.sty
%{_datadir}/texmf-dist/tex/latex/beamer/multimedia.sty
%{_datadir}/texmf-dist/tex/latex/beamer/multimediasymbols.sty
%{_datadir}/texmf-dist/tex/latex/beamer/xmpmulti.sty
