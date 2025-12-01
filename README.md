# Agent-Orchestration-Framework-with-LangChain
This repository contains a simple agent framework built using LangChain and OpenAI’s gpt-4o-mini model.
The goal of the project is to demonstrate how a conversational agent can be constructed using modular components such as custom tools, memory, and a console-based interaction loop.

# Overview
The agent is capable of performing basic tasks through the use of tools, maintaining context across turns, and responding to user queries in natural language.

The implementation focuses on:

Using LangChain’s agent orchestration capabilities
Integrating external tools for specific actions
Managing conversational state through memory
Providing a clean command-line interface for interaction

# Features

# Custom Tools

A greeting tool that responds with a personalized message
A weather tool that retrieves live temperature data using the wttr.in API

# Agent Capabilities

Dynamically selects tools when appropriate
Generates natural language responses using the chosen model
Maintains conversation history for context-aware interaction

# Console Interface

Allows continuous back-and-forth communication
Accepts user queries until an explicit exit command is given


# Setup Instructions
Install dependencies:
pip install -r requirements.txt
Create a .env file in the project root and include:
OPENAI_API_KEY=your_api_key_here
Run the agent from the console:
python src/main.py

# Technologies Used
Python 3.12/n
LangChain
OpenAI gpt-4o-mini
Requests library
python-dotenv for environment variable management

# License
This project is released under the MIT License.
