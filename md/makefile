
PANDOC=/usr/bin/pandoc
PANDOC_OPTIONS=--standalone
PANDOC_HTML_OPTIONS=--to html5

SOURCE_DOCS := $(wildcard *.md)

HTML_OUTPUT_DIR=../html

EXPORTED_DOCS=\
 $(SOURCE_DOCS:.md=.html)

%.html: %.md
	@mkdir -p $(HTML_OUTPUT_DIR)
	$(PANDOC) $(PANDOC_OPTIONS) $(PANDOC_HTML_OPTIONS) -o $(HTML_OUTPUT_DIR)/$@ $<

.PHONY: all

all : $(EXPORTED_DOCS)

