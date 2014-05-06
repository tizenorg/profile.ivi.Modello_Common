PROJECT = Modello_Common

VERSION := 0.0.2
PACKAGE = $(PROJECT)-$(VERSION)

INSTALL_DIR = ${DESTDIR}/opt/usr/apps/_common

all:

install:
	@echo "Installing Common UI files package, stand by..."
	mkdir -p $(INSTALL_DIR)/css
	mkdir -p $(INSTALL_DIR)/js
	cp -r css $(INSTALL_DIR)/
	cp -r js $(INSTALL_DIR)/

