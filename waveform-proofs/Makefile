# make all: rerun every script present in src/ and capture stdout to outputs/
PY ?= python3
SCRIPTS := $(basename $(notdir $(wildcard src/*.py)))
RUN := $(filter-out metrics,$(SCRIPTS))

.PHONY: all $(RUN)
all: $(RUN)

$(RUN):
	cd src && $(PY) $@.py > ../outputs/$@.txt 2>&1
