FILE=2021-02-26-Modelling-Mail-In-Votes-In-the-2020-US-Election

${FILE}.ipynb: ${FILE}.md
	notedown $< > $@

html: ${FILE}.html
${FILE}.html: ${FILE}.ipynb
	jupyter nbconvert --to html $< --output $@
