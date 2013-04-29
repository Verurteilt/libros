
MKHTML=rst2html --stylesheet=pystyle.css \
	--strip-elements-with-class="admonition-title"

ALLRST= index.html \
	ejer/tema-00/index.html \
	ejer/tema-01/index.html \
	ejer/tema-02/index.html \
	ejer/tema-03/index.html \
	ejer/tema-04/index.html \
	ejer/tema-05/index.html \
	ejer/tema-06/index.html \
	ejer/tema-07/index.html \
	ejer/tema-08/index.html 


%.html : %.rst
	$(MKHTML) $< > $@

all: $(ALLRST)

upload: all
	ncftpput -R -u u48595320 suicidesoft.com python-avanzado .

