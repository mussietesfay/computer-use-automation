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

## Target Application

The target application is a controlled banking/member portal used
to demonstrate computer-use automation.

### Manual Workflow

1. Login
2. Open Member Search
3. Enter a member ID
4. Search for the member
5. View member details
6. Read the savings balance

### Test Credentials

Username:

admin

Password:

password

### Example Member

Member ID:

12345

Expected:

- Name: John Smith
- Status: Active
- Email: john@example.com
- Savings Balance: $12,450.00