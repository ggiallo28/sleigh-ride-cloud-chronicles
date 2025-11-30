.PHONY: help list-days show-task force day%

help:
	@echo "Available commands:"
	@echo ""
	@echo "  make help               Show this help message"
	@echo "  make list-days          List all available day folders"
	@echo "  make show-task DAY=XX   Show the task and inputs for a given day"
	@echo "  make dayXX              Shortcut for make show-task DAY=XX"
	@echo ""
	@echo "Examples:"
	@echo "  make show-task DAY=01"
	@echo "  make day01"
	@echo ""

list-days:
	@echo "📅 Available Days:"
	@ls -d days/day*/ 2>/dev/null | sort | sed 's/:\|days\/day//g;s/\///g'

show-task:
	@if [ -z "$(DAY)" ]; then \
		echo "❌ DAY variable not set. Use: make show-task DAY=01"; \
		exit 1; \
	fi
	@echo "========================================"
	@echo "🎄 Task for Day $(DAY)"
	@echo "========================================"
	@if [ -f days/day$(DAY)/task.md ]; then \
		cat days/day$(DAY)/task.md; \
	else \
		echo "❌ Task file not found: days/day$(DAY)/task.md"; \
	fi
	@echo ""
	@echo "========================================"
	@echo "📂 Input Files (days/day$(DAY)/input/)"
	@echo "========================================"
	@if [ -d days/day$(DAY)/input ]; then \
		ls -1 days/day$(DAY)/input/; \
	else \
		echo "❌ Input directory not found for day $(DAY)"; \
	fi
	@echo "========================================"

day%: force
	@if [ -d days/day$* ]; then \
		$(MAKE) show-task DAY=$*; \
	else \
		echo "❌ No such day: days/day$*"; \
	fi

force: ;