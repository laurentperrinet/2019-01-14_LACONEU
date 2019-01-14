default: html

SRC=2019-01-14_LACONEU

edit:
	atom $(SRC).py

html:
	python3 $(SRC).py $(SRC).html

page:
	python3 $(SRC).py
	cat /tmp/wiki.txt |pbcopy
	open https://invibe.net/cgi-bin/index.cgi/Presentations/$(SRC)?action=edit

show: html
#	open -a firefox $(SRC).html
	open $(SRC).html

blog: html
	cp $(SRC).html  ~/pool/blog/invibe/files
	# sh deploy.sh
	cd ~/pool/blog/invibe/ ; nikola build ; nikola deploy
	open http://blog.invibe.net/files/$(SRC).html

github:
	git commit -am' adding notes'
	git push
