pandoc -f csv -t latex -o './includings/methods.tex' '../Findings/methods.csv'
sed -i "s/\bno\b/\\\\xmark/g" './includings/methods.tex'
sed -i "s/\byes\b/\\\\cmark/g" './includings/methods.tex'
# okular main.pdf &
curl -s -H "Zotero-API-Key: SiQPnCcEMmppgThbSGuVm5Rv" "https://api.zotero.org/users/7485781/collections/7JIJ4G7F/items?format=bibtex&limit=100&sort=title"  > bibs/main.bib
curl -s -H "Zotero-API-Key: SiQPnCcEMmppgThbSGuVm5Rv" "https://api.zotero.org/users/7485781/collections/7JIJ4G7F/items?format=bibtex&limit=100&sort=title&start=100" >> bibs/main.bib
pdflatex -pdf -aux-directory=./temp -output-directory=./output main.tex
bibtex output/main
pdflatex -pdf -aux-directory=./temp -output-directory=./output main.tex
pdflatex -pdf -aux-directory=./temp -output-directory=./output main.tex
cp output/main.pdf .
