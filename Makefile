
# ----------------------------------
# App settings
# ----------------------------------
DJANGO_MODULE=src.dutyfree_api
HOST=0.0.0.0
PORT=8000
ROOT_DIR=src
APP_DIR=$(ROOT_DIR)/dutyfree_api
APP_TEST_DIR=$(APP_DIR)/tests
TAG=latest

# ----------------------------------
# Default Help
# ----------------------------------
.PHONY: help
help:
	@echo "Usage: make <target>"
	@echo "Available targets:"
	@echo "  venv         - Create virtual environment"
	@echo "  install      - Install Python dependencies"
	@echo "  run          - Run FastAPI app with Uvicorn"
	@echo "  test         - Run tests with pytest"
	@echo "  lint         - Lint code using ruff"
	@echo "  format       - Format code using black"



# ----------------------------------
# Run
# ----------------------------------

.PHONY: run
run:
	cd $(APP_DIR) && python manage.py runserver $(HOST):$(PORT)

.PHONY: init-db
init-db:
	cd $(APP_DIR) && python manage.py generate_purchases

.PHONY: delete_all
delete_all:
	cd $(APP_DIR) && python manage.py delete_all


# ----------------------------------
# Formatting, Linting
# ----------------------------------
.PHONY: check-black
check-black:
	black $(APP_DIR) $(APP_TEST_DIR)

.PHONY: check-lint
check-lint:
	ruff check $(APP_DIR) $(APP_TEST_DIR)

.PHONY: check-bandit
check-bandit:
	bandit -r $(APP_DIR) $(APP_TEST_DIR)

.PHONY: check-isort
check-isort:
	isort $(APP_DIR) $(APP_TEST_DIR)

.PHONY: check-typing
check-typing:
	mypy $(APP_DIR) $(APP_TEST_DIR)


.PHONY: check-all
check-all: check-black check-lint check-isort check-typing
	check-black
	check-lint
	check-isort
	check-typing
	check-bandit
	echo "Quality checks passed!"

fix-lint:
	ruff check $(APP_DIR) $(APP_TEST_DIR) --fix 



# ----------------------------------
# Test & Validation
# ----------------------------------

.PHONY: test_send_csv_data
test_send_csv_data:
	cd $(ROOT_DIR) && python purchase_api_cli data/customers.csv data/purchases.csv "http://127.0.0.1:8000/v1/customers/"
