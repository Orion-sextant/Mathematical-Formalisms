.PHONY: verify test clean help

PAPERS := $(wildcard papers/*/)

help:
	@echo "Mathematical Formalisms - top-level targets"
	@echo ""
	@echo "  make verify   Install and test every paper subdirectory"
	@echo "  make test     Alias for verify"
	@echo "  make clean    Remove build artifacts and caches"

verify: $(PAPERS:%=verify-%)

verify-%:
	@echo "=== Verifying $* ==="
	@cd $* && pip install -e ".[dev]" --quiet && python -m pytest -q
	@echo ""

test: verify

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
