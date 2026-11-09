# Run `make` or `make help` to list all commands.
# Overridable variables: make inspect SERVER=path/to/other.py
SERVER ?= src/langchain_course/mcp_server.py

.DEFAULT_GOAL := help
.PHONY: help inspect

help: ## Show this list of commands
	@grep -hE "^[a-zA-Z_-]+:.*## " $(MAKEFILE_LIST) | awk -F ":.*## " '{printf "  %-10s %s\n", $$1, $$2}'

inspect: ## Open MCP Inspector for the server set in SERVER
	npx @modelcontextprotocol/inspector uv run python $(SERVER)
