black:
	python -m black --line-length 119 .
flake8:
	python -m flake8
pyright:
	python -m pyright
isort:
	python -m isort .
autoflake:
	python -m autoflake -r --in-place --remove-unused-variables --remove-all-unused-imports --expand-star-imports --ignore-init-module-imports .
format:
	python -m black --line-length 119 .
	python -m isort .
