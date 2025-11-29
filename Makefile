.PHONY: show-task

DAY ?= 01

show-task:
	@echo "========================================"
	@echo "🎄 Task for Day $(DAY) 🎄"
	@echo "========================================"
	@if [ -f day$(DAY)/task.md ]; then \
		cat day$(DAY)/task.md; \
	else \
		echo "❌ Task file for day $(DAY) not found (day$(DAY)/task.md)"; \
	fi
	@echo ""
	@echo "========================================"
	@echo "📂 Input Files (day$(DAY)/input/):"
	@echo "========================================"
	@if [ -d day$(DAY)/input ]; then \
		ls -1 day$(DAY)/input/; \
	else \
		echo "❌ Input directory for day $(DAY) not found"; \
	fi
	@echo "========================================"

day%: force
	@$(MAKE) show-task DAY=$*

.PHONY: show-task force
force: ;
