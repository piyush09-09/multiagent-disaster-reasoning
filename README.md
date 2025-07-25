Multi-Agent Crisis AI Reasoning System

A modular multi-agent AI framework designed to analyze disaster-related visual and textual data to generate structured crisis summaries and response plans. This system integrates computer vision, natural language understanding, geolocation, and planning capabilities to provide real-time actionable insights from multimodal sources.



Overview

This project implements a multi-agent architecture for multimodal crisis reasoning using:



Disaster-related tweets and metadata



Aerial/street-level imagery



Location and timestamp information



Pretrained vision and language models



Objective

The system is capable of:



Identifying the disaster type and affected elements



Estimating damage severity from images



Extracting and reasoning over tweet-based context



Inferring geolocation from GPS metadata or textual location clues



Generating response action plans



Exporting human-readable reports with visual overlays and structured JSON/PDF formats



System Architecture

Pipeline Flow:



Preprocessor Agent

Extracts metadata like GPS coordinates and timestamps from images or tweet content.



Vision Agent

Performs image captioning, disaster classification, and severity assessment using deep vision models.



Language Agent

Summarizes tweet content, infers contextual crisis information using pretrained transformers.



Planning Agent

Uses rules or generative LLMs to recommend crisis response actions.



Reporting Agent

Compiles outputs into structured formats: JSON, PDFs, and front-end display.



Agents and Models

Agent	Description	Tools/Models Used

Preprocessor	Extracts GPS, timestamp from image/tweet metadata	exifread, Pillow, geopy

Vision Agent	Classifies disasters, generates captions, detects damage	ResNet5

Language Agent	Summarizes tweets and infers crisis context	BERTweet, BART, T5, LangChain

Planning Agent	Generates response plans based on vision + language output	GPT-4, rule-based logic

Reporting Agent	Compiles final report (textual, JSON, PDF)	Jinja2, pdfkit, Streamlit



Datasets Used

Dataset	Purpose

CrisisMMD	Multimodal tweet-image pairs

link: https://crisisnlp.qcri.org/crisismmd



Metadata Format

Each image-tweet pair is enriched with structured metadata:



json

Copy

Edit

{

&nbsp; "tweet\_id": "1234567890",

&nbsp; "image\_name": "flood\_001.jpg",

&nbsp; "disaster\_type": "flood",

&nbsp; "timestamp": "2025-07-14T16:32:00+05:30",

&nbsp; "latitude": 28.6139,

&nbsp; "longitude": 77.2090

}

Example Output

Input:

A disaster image and associated tweet content.



Output:



Crisis summary: "Severe flooding observed in East Delhi. Three buildings submerged."



Location: "East Delhi, Zone B"



Action plan:



Evacuate residential blocks in Zone B



Deploy rescue boats and medical units



Block traffic on NH-24 for relief access



Export: PDF report and structured JSON



Getting Started

Prerequisites

Python 3.8+



PyTorch, HuggingFace Transformers



torchvision, Pillow, pandas, geopy



Steps to Run

Clone the repository and set up the environment:



bash

Copy

Edit

pip install -r requirements.txt

Upload datasets (images, tweets, metadata.json) to the appropriate folders.



Run the agent pipeline sequentially or through main.py:



bash

Copy

Edit

python main.py

Final reports are saved in /reports/ as JSON and PDF.



Tech Stack

Backend: PyTorch, Transformers, FastAPI



Frontend: Streamlit / Gradio (optional)



Storage: MongoDB (for logging and metadata)



Coordination: LangChain Agent Graph (for modular orchestration)



Future Work

Dynamic integration with WhatsApp/Telegram for public alerting



OpenStreetMap overlays with bounding box outputs



Multilingual support for tweet/news summaries



Integration with real-time crisis feeds (e.g., NDMA, GDACS)



License \& Ethical Use

Uses only open-source datasets and public APIs



No facial recognition or personal identification



Intended for research, education, and humanitarian use only



Users must validate outputs before acting on them in real-world situations

