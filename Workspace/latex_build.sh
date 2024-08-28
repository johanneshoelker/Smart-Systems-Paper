pandoc -f csv -t latex -o './includings/methods.tex' '../Findings/methods.csv'
# okular main.pdf &
# Set your API Key, User ID, and Collection ID
# API_KEY="SiQPnCcEMmppgThbSGuVm5Rv"
# USER_ID="7485781"
# COLLECTION_ID="7JIJ4G7F"
#
# # Initial URL to fetch the first page of results
# URL="https://api.zotero.org/users/$USER_ID/collections/$COLLECTION_ID/items?format=bibtex&limit=100&sort=title"
#
# # Output file for BibTeX data
# OUTPUT_FILE="bibs/main.bib"
#
# # Empty the output file initially
# > "$OUTPUT_FILE"
#
# # Loop until there are no more pages
# while [ -n "$URL" ]; do
#   # Perform the request and capture headers and body
#   RESPONSE=$(curl -s -D - -H "Zotero-API-Key: $API_KEY" "$URL")
#   echo "$RESPONSE"
#   # Extract the body (actual BibTeX data) and append it to the output file
#   echo "$RESPONSE" | sed -n '/^{/,$p' >> "$OUTPUT_FILE"
#
#   # Extract the Link header to check for the next page
#   URL=$(echo "$RESPONSE" | grep -oP '(?<=<)[^>]+(?=>; rel="next")')
#
#   # Wait a short time before the next request to avoid rate limiting (optional)
#   sleep 1
# done
curl -s -H "Zotero-API-Key: SiQPnCcEMmppgThbSGuVm5Rv" "https://api.zotero.org/users/7485781/collections/7JIJ4G7F/items?format=bibtex&limit=100&sort=title" > bibs/main.bib
pdflatex -pdf -aux-directory=./temp -output-directory=./output main.tex
bibtex output/main
pdflatex -pdf -aux-directory=./temp -output-directory=./output main.tex
pdflatex -pdf -aux-directory=./temp -output-directory=./output main.tex
cp output/main.pdf .
