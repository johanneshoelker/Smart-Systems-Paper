pdflatex -pdf -aux-directory=./temp -output-directory=./output main.tex
bibtex main
pdflatex -pdf -aux-directory=./temp -output-directory=./output main.tex
pdflatex -pdf -aux-directory=./temp -output-directory=./output main.tex
cp output/main.pdf .
