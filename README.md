## Project -  AI Customer Support Agent (Agentic AI)

An end-to-end Agentic AI Customer Support System built using modern LLM engineering principles: intent classification, memory, RAG, deterministic tools, and an agent loop.

This project demonstrates how to design reliable, safe, and scalable AI agents beyond basic chatbots.

# Features

Intent classification (order status, refunds, complaints, policies, chitchat)
Session-based memory (multi-turn conversations)
Retrieval-Augmented Generation (RAG) for grounded answers
Deterministic backend tools (order lookup, refund initiation, ticket creation)
Agent loop with follow-up handling
Safety & guardrails to prevent hallucinations and infinite loops
Modular, production-ready architecture

# Architecture Overview
User
 ↓
FastAPI Endpoint
 ↓
Agent Controller (run_agent)
 ↓
Intent Classification
 ↓
Memory Update + Fallback
 ↓
Task Completion Check
 ↓
Routing Layer
 ├── Tools (Order / Refund / Ticket)
 ├── RAG (Policies / Docs)
 └── LLM (Chat / Explanation)
 ↓
Final Response

# Project Structure
app/
├── agents/
│   ├── agent.py          # Agent loop controller
│   ├── intent.py         # Intent classification
│   ├── router.py         # Tool / RAG / LLM routing
│   ├── completion.py     # Task completion logic
│   └── followup.py       # Follow-up questions
│
├── memory/
│   ├── session.py        # Session-based memory store
│   └── extract.py        # Entity extraction (order_id)
│
├── rag/
│   ├── documents.py      # Knowledge base
│   ├── embed.py          # Embedding logic
│   ├── store.py          # Vector store
│   └── retriever.py      # Similarity search
│
├── tools/
│   ├── orders.py         # Order status tool
│   ├── refunds.py        # Refund initiation tool
│   └── tickets.py        # Support ticket tool
│
├── prompts/
│   └── template.py       # Prompt templates
│
├── llm/
│   └── client.py         # LLM abstraction
│
├── main.py               # FastAPI entry point
└── config.py             # Configuration

# Key Concepts Implemented
1. Intent-Based Routing

Each user message is classified into a clear intent and routed deterministically.

2. Memory

Session-based memory allows the agent to:
remember order IDs
persist intent across turns
avoid repeating questions

3. RAG (Retrieval-Augmented Generation)

Policies and FAQs are retrieved and injected into prompts to:
prevent hallucinations
ensure factual answers
keep data updatable without retraining

4. Tools

Critical actions (order lookup, refunds) are handled via pure Python functions, not LLM guesses.

5. Agent Loop

The agent checks:
Is required information present?
If not → ask follow-up
If yes → act

6. Safety & Guardrails

Prompt injection protection
Empty RAG handling
Tool failure handling
Loop break conditions

# How to Run
uvicorn app.main:app --reload


Test via Swagger:

http://127.0.0.1:8000/docs
