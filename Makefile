# Minimal Makefile for the Sphinx site
SPHINXBUILD ?= uv run sphinx-build
SOURCEDIR    = docs
BUILDDIR     = docs/_build

.PHONY: help install html serve clean

help:
	@echo "Targets:"
	@echo "  install   - install dependencies via uv"
	@echo "  html      - build the HTML site into $(BUILDDIR)/html"
	@echo "  serve     - build and serve locally with autoreload"
	@echo "  clean     - remove build artifacts"

install:
	uv sync

html:
	$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html"

serve:
	uv run sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)/html" --open-browser

clean:
	rm -rf "$(BUILDDIR)"
