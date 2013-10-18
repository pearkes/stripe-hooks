test:
	@ENVIRONMENT=test PYTHONPATH=. py.test -v test/

run:
	@DEBUG=True forego run python app.py

deps:
	@sudo pip install -r requirements.txt

.PHONY: deps run test

