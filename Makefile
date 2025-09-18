develop:
	$(MAKE) -C lib develop

serve:
	uvicorn --reload --reload-dir . --host 0.0.0.0 --port 8000 pybrary.server:app