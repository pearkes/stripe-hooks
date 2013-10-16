deps:
	@sudo pip install -r requirements.txt

run:
	@DEBUG=True forego run python app.py

test:
	@ENVIRONMENT=test PYTHONPATH=. forego run py.test -v test/

.PHONY: deps run test

