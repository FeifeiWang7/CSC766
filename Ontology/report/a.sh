latex sig-alternate
bibtex sig-alternate
latex sig-alternate
latex sig-alternate
input="sig-alternate.bbl"
output="sig-alternate.tex"
while read -r line
do
	echo $line >> "$output"
done < "$input"
pdflatex sig-alternate.tex
rm sig-alternate.aux
rm sig-alternate.blg
#rm sig-alternate.bbl
rm sig-alternate.dvi
rm sig-alternate.log
