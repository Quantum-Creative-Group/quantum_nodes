# Minimal makefile for Sphinx documentation

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
MODULE        = quantum_nodes

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
# Rename ../quantum_nodes/__init__.py to ../quantum_nodes/___init__.py so it won't throw an exception when animation_nodes is not found
%: Makefile
	mv ../$(MODULE)/__init__.py ../$(MODULE)/___init__.py
	find ../ -type f -name "*.py" -exec sed -i 's/@persistent/#@persistent/g' {} +

	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

	find ../ -type f -name "*.py" -exec sed -i 's/#@persistent/@persistent/g' {} +
	mv ../$(MODULE)/___init__.py ../$(MODULE)/__init__.py