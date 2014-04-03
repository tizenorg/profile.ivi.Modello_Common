PROJECT = html5_UI_Common

VERSION := 0.0.1
PACKAGE = $(PROJECT)-$(VERSION)

#INSTALL_FILES = $(PROJECT).wgt
INSTALL_DIR = ${DESTDIR}/opt/usr/apps/_common

all:
	#zip -r $(PROJECT).wgt config.xml index.html icon.png js css

install:
	@echo "Installing Common UI files package, stand by..."
	mkdir -p $(INSTALL_DIR)/
	cp -r css $(INSTALL_DIR)/
	cp -r js $(INSTALL_DIR)/

dist:
	tar czf ../$(PACKAGE).tar.bz2 .

