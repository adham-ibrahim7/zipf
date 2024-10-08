.PHONY : all clean settings help results

DATA=$(wildcard data/*.txt)
RESULTS=$(patsubst data/%.txt, results/%.csv, $(DATA))

COUNT=bin/countwords.py
COLLATE=bin/collate.py
PLOT=bin/plotcounts.py

## results/%.csv: Regenerate results for each book.
results/%.csv : data/%.txt $(COUNT)
	python $(COUNT) $< > $@
	
## results/collated.csv: collate all results.
results/collated.csv : $(RESULTS) $(COLLATE)
	@mkdir -p results
	python $(COLLATE) $(RESULTS) > $@
	
## results/collated.png: plot collated results.
results/collated.png: results/collated.csv $(PLOT)
	python $(PLOT) $< --outfile $@ --plotparams plotparams.yml

## all: Regenerate all results.
all : results/collated.png

## results: update only the result csvs, do not collate. (Exercise 9.11.5)
results: $(RESULTS)

## clean: Remove all generated files.
clean :
	rm -f $(RESULTS) results/collated.csv results/collated.png
	
## settings: Show variable values.
settings:
	@echo COUNT: $(COUNT)
	@echo DATA: $(DATA)
	@echo RESULTS: $(RESULTS)
	
## help: show this message.
help :
	@grep '^##' ./Makefile