FILE=mail_vote_model

${FILE}.ipynb: ${FILE}.md
	notedown $< --run > $@

html: ${FILE}.html
${FILE}.html: ${FILE}.ipynb
	jupyter nbconvert --to html $< --output $@
