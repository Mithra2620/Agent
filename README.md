Voice-Controlled Multi-Agent Assistant

A voice-activated personal automation assistant that listens for spoken commands, interprets intent, and executes actions across Gmail and YouTube — powered by an LLM (Gemini/GPT) and orchestrated by a central Controller Agent.

🎯 Overview

This project lets you talk to your computer and have it act on your behalf: draft and send emails, generate content, and play videos — all triggered by voice, with a guard layer validating actions before they execute.

🧠 Architecture

The system is built around a layered agent architecture:

Controller Agent — top-level orchestrator that routes requests to the correct sub-agent
Agentic AI Transactional Guard — validates and authorizes actions before execution (e.g., confirming before sending an email)
Voice Pipeline — front end → trigger → mic/hotkey input → backend function-calling logic → RAG-based output evaluation

Runtime Flow (Algorithm)

Voice input
Voice-to-text conversion
Keyword checking
Keyword matching
Function call — dispatches to the correct API (Gmail or YouTube)
Authentication
LLM (Gemini/GPT) generates the response or content
Output is generated and typed/executed

🔌 Integrations

Gmail Agent

URL generation
Google API — query & result generation
Gmail — visits inbox/compose and types content

YouTube Agent

Handles playback and video search via play.py
