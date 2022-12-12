VERSION := $(shell python setup.py --version)

.PHONY: build

lint:
	flake8 .

format:
	black .
	isort .

build:
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/* --skip-existing

tag:
	git tag -m "v${VERSION}" v${VERSION}
	git push --tags

# build and upload to pypi and push tag to github
workflow:
	make build
	make upload
	make tag
