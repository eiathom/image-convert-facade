docker-build:
	docker build -t image-convert-facade .

docker-run:
	docker run -it --rm --name icf image-convert-facade bash

docker-run-tests:
	docker run --rm --name icf image-convert-facade

install:
	pip install -r requirements.txt

unit:
	pytest -sv lib/test/unit

test: unit

clean:
	find . -type f -name "*.pyc" -delete
	rm -fr .cache .mypy_cache .pytest_cache
	rm -f images/scaled*

create-venv:
	rm -rf venv
	python3 -m venv venv

generate-pip-conf:
	echo '[global]\ntimeout = 60\nindex-url = https://pypi.python.org/simple/\n' >> venv/pip.conf


.PHONY: docker-build docker-run docker-run-tests install unit test clean, create-venv, generate-pip-conf
 
