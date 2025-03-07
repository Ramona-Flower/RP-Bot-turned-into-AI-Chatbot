# RP-Bot-turned-into-AI-Chatbot

A simple Python project that interfaces with the private API of the "spicychat.ai" website, to turn an AI Roleplay Bot into a simple AI chatbot that utilize the `L3-8B-Stheno-v3.2_novita` model for free !

## Overview

This project contains a Python script that allows you to communicate with an AI chatbot by using the "spicychat.ai" private API. It sends user prompts to the API and retrieves the AI's responses.

## Features

- Send custom prompts to the AI chatbot
- Simple command-line interface

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Ramona-Flower/RP-Bot-turned-into-AI-Chatbot.git
   cd RP-Bot-turned-into-AI-Chatbot
   ```

2. Install required dependencies:
   ```
   pip install requests
   ```

## Usage

Run the script with:

```
python main.py
```

When prompted, enter the message you want to send to the AI. The script will:
1. Send your message to the spicychat.ai API
2. Return the AI's response
3. Wait for you to press any key to exit

## How It Works

The script makes a POST request to the spicychat.ai API with:
- Your input message
- Configuration parameters for the AI response (temperature, token limits, etc.)

## Disclaimer

This project uses a private API that is not officially documented or supported for public use. Use at your own risk, as the API might change without notice.
