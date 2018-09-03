.PHONY: dev test clean relclean

all:
	@echo read Makefile for useful targets


################################################
### WINDOWS TARGETS
################################################
wdev:
	@echo "==> setting up dev virtualenv"
	@if [ ! -d venv ]; then virtualenv venv; fi
	@./venv/Scripts/pip install -e .
	@mkdir -p venv/etc
	@cp local.conf venv/etc/usgw.conf

wserver:
	@echo "==> starting dev server on http://localhost:5000"
	@FLASK_APP=usgw/app.py \
        FLASK_DEBUG=1 \
        ./venv/Scripts/flask run --host=0.0.0.0 --port=5000

wtest:
	wdev
	wserver
################################################



################################################
### LINUX TARGETS
################################################
ldev:
	@echo "==> setting up dev virtualenv"
	@if [ ! -d venv ]; then virtualenv venv; fi
	@./venv/bin/pip install -e .
	@mkdir -p venv/etc
	@cp local.conf venv/etc/usgw.conf

lserver:
	@echo "==> starting dev server on http://localhost:5000"
	@FLASK_APP=usgw/app.py \
        FLASK_DEBUG=1 \
        ./venv/bin/flask run --host=0.0.0.0 --port=5000

ltest:
	ldev
	lserver

################################################


clean:
	@echo "==> cleaning working files"
	@find . -name \*~ -delete
	@find . -name \*.pyc -delete
	@find . -name \#* -delete

relclean: clean
	@echo "==> removing dev venv"
	@rm -rf usgw.egg-info
	@rm -rf venv
