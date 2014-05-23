PROJECT = Modello_Common

VERSION := 0.0.2
PACKAGE = $(PROJECT)-$(VERSION)

WIDGET_FILES = $(PROJECT).wgt
WIDGET_DIR = ${DESTDIR}/opt/usr/apps/.preinstallWidgets

INSTALL_FILES = css js
INSTALL_DIR = ${DESTDIR}/usr/share/tizen-web-ui-fw/modello/common

all:

wgtPkg:
	zip -r $(PROJECT).wgt config.xml css js icon.png index.html

install:
	@echo "Installing Common UI files package, stand by..."
	mkdir -p $(WIDGET_DIR)
	cp $(WIDGET_FILES) $(WIDGET_DIR)
	mkdir -p $(INSTALL_DIR)
	cp -r $(INSTALL_FILES) $(INSTALL_DIR)


dist:
	tar cfz ../$(PACKAGE).tar.bz2 .
