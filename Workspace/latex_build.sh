pandoc -f csv -t latex -o './includings/methods.tex' '../Findings/methods.csv'
curl -s -H "Zotero-API-Key: SiQPnCcEMmppgThbSGuVm5Rv" "https://api.zotero.org/users/7485781/collections/3LVTYECH/items?format=bibtex" > 'bibs/main.bib'
pdflatex -pdf -aux-directory=./temp -output-directory=./output main.tex
bibtex output/main
pdflatex -pdf -aux-directory=./temp -output-directory=./output main.tex
pdflatex -pdf -aux-directory=./temp -output-directory=./output main.tex
cp output/main.pdf .
