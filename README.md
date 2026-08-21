# Computer Use Automation

A computer-use automation system that discovers browser workflows using
LLM-driven automation and converts successful workflows into reusable,
deterministic capabilities.

## Architecture

The project consists of:

- React + TypeScript frontend
- Node.js + Express + TypeScript backend
- Python automation service
- LangGraph
- Playwright
- Target web application

## High-Level Flow

User
→ React
→ Express
→ Python
→ LangGraph
→ Playwright
→ Target Application

Discovery
→ Artifact
→ Deterministic Replay

## Project Status
- Stage 1 - Project initialization
- Stage 2 - Development environments configured

## Development Stack

### Frontend
- React
- TypeScript
- Vite

### Backend
- Node.js
- Express
- TypeScript

### Automation
- Python
- Playwright

### Planned AI Layer
- LangGraph
- LLM