# revision 32232
# category Package
# catalog-ctan /macros/latex/contrib/beamer
# catalog-date 2013-11-24 13:34:05 +0100
# catalog-license gpl
# catalog-version 3.32
Name:		texlive-beamer
Version:	3.32
Release:	5
Summary:	A LaTeX class for producing presentations and slides
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/beamer/art/beamericonarticle.20.eps
%{_texmfdistdir}/tex/latex/beamer/art/beamericonarticle.20.pdf
%{_texmfdistdir}/tex/latex/beamer/art/beamericonarticle.eps
%{_texmfdistdir}/tex/latex/beamer/art/beamericonarticle.pdf
%{_texmfdistdir}/tex/latex/beamer/art/beamericonarticle.tex
%{_texmfdistdir}/tex/latex/beamer/art/beamericonbook.20.eps
%{_texmfdistdir}/tex/latex/beamer/art/beamericonbook.20.pdf
%{_texmfdistdir}/tex/latex/beamer/art/beamericonbook.eps
%{_texmfdistdir}/tex/latex/beamer/art/beamericonbook.pdf
%{_texmfdistdir}/tex/latex/beamer/art/beamericonbook.tex
%{_texmfdistdir}/tex/latex/beamer/art/beamericononline.20.eps
%{_texmfdistdir}/tex/latex/beamer/art/beamericononline.20.pdf
%{_texmfdistdir}/tex/latex/beamer/art/beamericononline.eps
%{_texmfdistdir}/tex/latex/beamer/art/beamericononline.pdf
%{_texmfdistdir}/tex/latex/beamer/beamer.cls
%{_texmfdistdir}/tex/latex/beamer/beamerarticle.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasearticle.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbaseauxtemplates.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbaseboxes.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasecolor.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasecompatibility.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasedecode.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbaseexercise.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasefont.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbaseframe.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbaseframecomponents.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbaseframesize.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbaselocalstructure.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasemisc.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasemodes.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasenavigation.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasenotes.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbaseoptions.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbaseoverlay.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasercs.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbaserequires.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasesection.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasetemplates.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasethemes.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasetheorems.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasetitle.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasetoc.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasetranslator.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasetwoscreens.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbaseverbatim.sty
%{_texmfdistdir}/tex/latex/beamer/emulation/beamerfoils.sty
%{_texmfdistdir}/tex/latex/beamer/emulation/beamerprosper.sty
%{_texmfdistdir}/tex/latex/beamer/emulation/beamerseminar.sty
%{_texmfdistdir}/tex/latex/beamer/emulation/beamertexpower.sty
%{_texmfdistdir}/tex/latex/beamer/emulation/examples/beamerexample-foils.tex
%{_texmfdistdir}/tex/latex/beamer/emulation/examples/beamerexample-prosper.tex
%{_texmfdistdir}/tex/latex/beamer/emulation/examples/beamerexample-seminar.tex
%{_texmfdistdir}/tex/latex/beamer/emulation/examples/beamerexample-texpower.tex
%{_texmfdistdir}/tex/latex/beamer/multimedia/multimedia.sty
%{_texmfdistdir}/tex/latex/beamer/multimedia/multimediasymbols.sty
%{_texmfdistdir}/tex/latex/beamer/multimedia/xmpmulti.sty
%{_texmfdistdir}/tex/latex/beamer/themes/color/beamercolorthemealbatross.sty
%{_texmfdistdir}/tex/latex/beamer/themes/color/beamercolorthemebeaver.sty
%{_texmfdistdir}/tex/latex/beamer/themes/color/beamercolorthemebeetle.sty
%{_texmfdistdir}/tex/latex/beamer/themes/color/beamercolorthemecrane.sty
%{_texmfdistdir}/tex/latex/beamer/themes/color/beamercolorthemedefault.sty
%{_texmfdistdir}/tex/latex/beamer/themes/color/beamercolorthemedolphin.sty
%{_texmfdistdir}/tex/latex/beamer/themes/color/beamercolorthemedove.sty
%{_texmfdistdir}/tex/latex/beamer/themes/color/beamercolorthemefly.sty
%{_texmfdistdir}/tex/latex/beamer/themes/color/beamercolorthemelily.sty
%{_texmfdistdir}/tex/latex/beamer/themes/color/beamercolorthememonarca.sty
%{_texmfdistdir}/tex/latex/beamer/themes/color/beamercolorthemeorchid.sty
%{_texmfdistdir}/tex/latex/beamer/themes/color/beamercolorthemerose.sty
%{_texmfdistdir}/tex/latex/beamer/themes/color/beamercolorthemeseagull.sty
%{_texmfdistdir}/tex/latex/beamer/themes/color/beamercolorthemeseahorse.sty
%{_texmfdistdir}/tex/latex/beamer/themes/color/beamercolorthemesidebartab.sty
%{_texmfdistdir}/tex/latex/beamer/themes/color/beamercolorthemespruce.sty
%{_texmfdistdir}/tex/latex/beamer/themes/color/beamercolorthemestructure.sty
%{_texmfdistdir}/tex/latex/beamer/themes/color/beamercolorthemewhale.sty
%{_texmfdistdir}/tex/latex/beamer/themes/color/beamercolorthemewolverine.sty
%{_texmfdistdir}/tex/latex/beamer/themes/font/beamerfontthemedefault.sty
%{_texmfdistdir}/tex/latex/beamer/themes/font/beamerfontthemeprofessionalfonts.sty
%{_texmfdistdir}/tex/latex/beamer/themes/font/beamerfontthemeserif.sty
%{_texmfdistdir}/tex/latex/beamer/themes/font/beamerfontthemestructurebold.sty
%{_texmfdistdir}/tex/latex/beamer/themes/font/beamerfontthemestructureitalicserif.sty
%{_texmfdistdir}/tex/latex/beamer/themes/font/beamerfontthemestructuresmallcapsserif.sty
%{_texmfdistdir}/tex/latex/beamer/themes/inner/beamerinnerthemecircles.sty
%{_texmfdistdir}/tex/latex/beamer/themes/inner/beamerinnerthemedefault.sty
%{_texmfdistdir}/tex/latex/beamer/themes/inner/beamerinnerthemeinmargin.sty
%{_texmfdistdir}/tex/latex/beamer/themes/inner/beamerinnerthemerectangles.sty
%{_texmfdistdir}/tex/latex/beamer/themes/inner/beamerinnerthemerounded.sty
%{_texmfdistdir}/tex/latex/beamer/themes/outer/beamerouterthemedefault.sty
%{_texmfdistdir}/tex/latex/beamer/themes/outer/beamerouterthemeinfolines.sty
%{_texmfdistdir}/tex/latex/beamer/themes/outer/beamerouterthememiniframes.sty
%{_texmfdistdir}/tex/latex/beamer/themes/outer/beamerouterthemeshadow.sty
%{_texmfdistdir}/tex/latex/beamer/themes/outer/beamerouterthemesidebar.sty
%{_texmfdistdir}/tex/latex/beamer/themes/outer/beamerouterthemesmoothbars.sty
%{_texmfdistdir}/tex/latex/beamer/themes/outer/beamerouterthemesmoothtree.sty
%{_texmfdistdir}/tex/latex/beamer/themes/outer/beamerouterthemesplit.sty
%{_texmfdistdir}/tex/latex/beamer/themes/outer/beamerouterthemetree.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeAnnArbor.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeAntibes.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeBergen.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeBerkeley.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeBerlin.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeBoadilla.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeCambridgeUS.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeCopenhagen.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeDarmstadt.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeDresden.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeEastLansing.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeFrankfurt.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeGoettingen.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeHannover.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeIlmenau.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeJuanLesPins.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeLuebeck.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeMadrid.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeMalmoe.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeMarburg.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeMontpellier.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemePaloAlto.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemePittsburgh.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeRochester.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeSingapore.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeSzeged.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeWarsaw.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemeboxes.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/beamerthemedefault.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/compatibility/beamerthemebars.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/compatibility/beamerthemeclassic.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/compatibility/beamerthemecompatibility.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/compatibility/beamerthemelined.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/compatibility/beamerthemeplain.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/compatibility/beamerthemeshadow.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/compatibility/beamerthemesidebar.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/compatibility/beamerthemesplit.sty
%{_texmfdistdir}/tex/latex/beamer/themes/theme/compatibility/beamerthemetree.sty
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-basic-dictionary/translator-basic-dictionary-Brazilian.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-basic-dictionary/translator-basic-dictionary-Croatian.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-basic-dictionary/translator-basic-dictionary-English.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-basic-dictionary/translator-basic-dictionary-French.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-basic-dictionary/translator-basic-dictionary-German.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-basic-dictionary/translator-basic-dictionary-Greek.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-basic-dictionary/translator-basic-dictionary-Norsk.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-basic-dictionary/translator-basic-dictionary-Nynorsk.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-basic-dictionary/translator-basic-dictionary-Polish.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-basic-dictionary/translator-basic-dictionary-Serbian.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-basic-dictionary/translator-basic-dictionary-Spanish.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-bibliography-dictionary/translator-bibliography-dictionary-Brazilian.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-bibliography-dictionary/translator-bibliography-dictionary-Croatian.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-bibliography-dictionary/translator-bibliography-dictionary-English.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-bibliography-dictionary/translator-bibliography-dictionary-French.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-bibliography-dictionary/translator-bibliography-dictionary-German.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-bibliography-dictionary/translator-bibliography-dictionary-Greek.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-bibliography-dictionary/translator-bibliography-dictionary-Polish.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-bibliography-dictionary/translator-bibliography-dictionary-Serbian.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-bibliography-dictionary/translator-bibliography-dictionary-Spanish.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-environment-dictionary/translator-environment-dictionary-Brazilian.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-environment-dictionary/translator-environment-dictionary-Croatian.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-environment-dictionary/translator-environment-dictionary-English.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-environment-dictionary/translator-environment-dictionary-French.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-environment-dictionary/translator-environment-dictionary-German.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-environment-dictionary/translator-environment-dictionary-Greek.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-environment-dictionary/translator-environment-dictionary-Polish.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-environment-dictionary/translator-environment-dictionary-Serbian.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-environment-dictionary/translator-environment-dictionary-Spanish.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-months-dictionary/translator-months-dictionary-Brazilian.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-months-dictionary/translator-months-dictionary-Croatian.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-months-dictionary/translator-months-dictionary-English.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-months-dictionary/translator-months-dictionary-French.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-months-dictionary/translator-months-dictionary-German.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-months-dictionary/translator-months-dictionary-Greek.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-months-dictionary/translator-months-dictionary-Norsk.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-months-dictionary/translator-months-dictionary-Nynorsk.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-months-dictionary/translator-months-dictionary-Polish.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-months-dictionary/translator-months-dictionary-Serbian.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-months-dictionary/translator-months-dictionary-Spanish.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-numbers-dictionary/translator-numbers-dictionary-Brazilian.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-numbers-dictionary/translator-numbers-dictionary-Croatian.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-numbers-dictionary/translator-numbers-dictionary-English.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-numbers-dictionary/translator-numbers-dictionary-French.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-numbers-dictionary/translator-numbers-dictionary-German.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-numbers-dictionary/translator-numbers-dictionary-Greek.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-numbers-dictionary/translator-numbers-dictionary-Norsk.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-numbers-dictionary/translator-numbers-dictionary-Nynorsk.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-numbers-dictionary/translator-numbers-dictionary-Polish.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-numbers-dictionary/translator-numbers-dictionary-Serbian.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-numbers-dictionary/translator-numbers-dictionary-Spanish.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-theorem-dictionary/translator-theorem-dictionary-Brazilian.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-theorem-dictionary/translator-theorem-dictionary-Croatian.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-theorem-dictionary/translator-theorem-dictionary-English.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-theorem-dictionary/translator-theorem-dictionary-French.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-theorem-dictionary/translator-theorem-dictionary-German.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-theorem-dictionary/translator-theorem-dictionary-Greek.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-theorem-dictionary/translator-theorem-dictionary-Norsk.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-theorem-dictionary/translator-theorem-dictionary-Polish.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-theorem-dictionary/translator-theorem-dictionary-Serbian.dict
%{_texmfdistdir}/tex/latex/beamer/translator/dicts/translator-theorem-dictionary/translator-theorem-dictionary-Spanish.dict
%{_texmfdistdir}/tex/latex/beamer/translator/translator-language-mappings.tex
%{_texmfdistdir}/tex/latex/beamer/translator/translator.sty
%doc %{_texmfdistdir}/doc/latex/beamer/AUTHORS
%doc %{_texmfdistdir}/doc/latex/beamer/ChangeLog
%doc %{_texmfdistdir}/doc/latex/beamer/FILES
%doc %{_texmfdistdir}/doc/latex/beamer/INSTALL
%doc %{_texmfdistdir}/doc/latex/beamer/README
%doc %{_texmfdistdir}/doc/latex/beamer/TODO
%doc %{_texmfdistdir}/doc/latex/beamer/doc/Makefile
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamercolorthemeexample.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerfontthemeexample.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerinnerthemeexample.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerlogo.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerouterthemeexample.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerthemeexample.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerthemeexamplebase.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-animations.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-color.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-compatibility.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-elements.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-emulation.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-fonts.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-frames.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-globalstructure.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-graphics.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-guidelines.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-installation.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-interaction.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-introduction.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-license.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-localstructure.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-macros.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-nonpresentation.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-notes.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-overlays.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-solutions.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-themes.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-translator.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-transparencies.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-tricks.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-tutorial.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-twoscreens.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerug-workflow.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugcolorthemealbatross.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugcolorthemealbatrossstylish.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugcolorthemebeaver.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugcolorthemebeetle.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugcolorthemecrane.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugcolorthemedefault.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugcolorthemedolphin.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugcolorthemedove.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugcolorthemefly.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugcolorthemelily.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugcolorthemeorchid.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugcolorthemerose.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugcolorthemeseagull.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugcolorthemeseahorse.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugcolorthemesidebartab.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugcolorthemespruce.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugcolorthemestructure.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugcolorthemewhale.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugcolorthemewolverine.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugfontthemedefault.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugfontthemeserif.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugfontthemestructurebold.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugfontthemestructureitalicserif.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugfontthemestructuresmallcapsserif.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beameruginnerthemecircles.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beameruginnerthemedefault.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beameruginnerthemeinmargin.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beameruginnerthemerectangles.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beameruginnerthemerounded.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugouterthemedefault.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugouterthemeinfolines.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugouterthememiniframes.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugouterthemeshadow.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugouterthemesidebar.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugouterthemesmoothbars.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugouterthemesmoothtree.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugouterthemesplit.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugouterthemetree.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeAnnArbor.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeAntibes.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeBergen.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeBerkeley.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeBerlin.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeBoadilla.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeCambridgeUS.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeCopenhagen.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeDarmstadt.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeDresden.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeEastLansing.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeFrankfurt.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeGoettingen.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeHannover.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeIlmenau.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeJuanLesPins.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeLuebeck.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeMadrid.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeMalmoe.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeMarburg.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeMontpellier.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemePaloAlto.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemePittsburgh.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeRochester.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeSingapore.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeSzeged.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeWarsaw.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemeboxes.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beamerugthemedefault.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beameruserguide.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/doc/beameruserguide.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/licenses/LICENSE
%doc %{_texmfdistdir}/doc/latex/beamer/doc/themeexamples/beamerthemeexample.tex
%doc %{_texmfdistdir}/doc/latex/beamer/doc/themeexamples/beamerthememakeexamples.sh
%doc %{_texmfdistdir}/doc/latex/beamer/emacs/beamer.el
%doc %{_texmfdistdir}/doc/latex/beamer/examples/Makefile
%doc %{_texmfdistdir}/doc/latex/beamer/examples/a-conference-talk/beamerexample-conference-talk.tex
%doc %{_texmfdistdir}/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-beamer-version.tex
%doc %{_texmfdistdir}/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-body.tex
%doc %{_texmfdistdir}/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-logo.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic1.jpg
%doc %{_texmfdistdir}/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic2.jpg
%doc %{_texmfdistdir}/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic3.jpg
%doc %{_texmfdistdir}/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic4.jpg
%doc %{_texmfdistdir}/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic5.jpg
%doc %{_texmfdistdir}/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic6.jpg
%doc %{_texmfdistdir}/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-print-version.tex
%doc %{_texmfdistdir}/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-style.tex
%doc %{_texmfdistdir}/doc/latex/beamer/examples/beamerexample-conference-talk.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/examples/beamerexample-lecture-beamer-version.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/examples/beamerexample-lecture-print-version.pdf
%doc %{_texmfdistdir}/doc/latex/beamer/solutions/conference-talks/conference-ornate-20min.de.tex
%doc %{_texmfdistdir}/doc/latex/beamer/solutions/conference-talks/conference-ornate-20min.en.tex
%doc %{_texmfdistdir}/doc/latex/beamer/solutions/conference-talks/conference-ornate-20min.fr.tex
%doc %{_texmfdistdir}/doc/latex/beamer/solutions/generic-talks/generic-ornate-15min-45min.de.tex
%doc %{_texmfdistdir}/doc/latex/beamer/solutions/generic-talks/generic-ornate-15min-45min.en.tex
%doc %{_texmfdistdir}/doc/latex/beamer/solutions/generic-talks/generic-ornate-15min-45min.fr.tex
%doc %{_texmfdistdir}/doc/latex/beamer/solutions/short-talks/speaker_introduction-ornate-2min.de.tex
%doc %{_texmfdistdir}/doc/latex/beamer/solutions/short-talks/speaker_introduction-ornate-2min.en.tex
%doc %{_texmfdistdir}/doc/latex/beamer/solutions/short-talks/speaker_introduction-ornate-2min.fr.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
