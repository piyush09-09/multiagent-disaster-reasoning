 Multi-Agent Crisis AI Reasoning System
A modular, multi-agent AI framework designed to analyze disaster-related visual and textual data to generate structured crisis summaries and response plans.

📌 Overview
This project integrates multimodal data—disaster-related tweets, metadata, aerial/street-level imagery—to build an end-to-end reasoning pipeline that includes classification, damage estimation, summarization, and response planning using a multi-agent architecture.

🎯 Goals
Classify disaster types from images and text

Estimate severity of damage using vision models

Understand tweet context and urgency

Infer location and time from metadata

Generate structured response action plans

Export final reports in JSON and PDF format

🛠️ Tools & Technologies
Core Libraries: Python, Pandas, NumPy, OpenCV

Vision Models: ResNet50 (PyTorch)

Language Models: BERTweet, T5, BART (Hugging Face)

Logic/Planner: GPT-4 via LangChain or rule-based logic

Frontend: Streamlit / Gradio (optional)

Report Generation: Jinja2, pdfkit

Version Control: Git, GitHub

🧱 Project Structure
bash
Copy
Edit
multiagent-crisis-ai/
├── data/              # Raw data and pretrained models
├── notebooks/         # Experiments and analysis
├── src/               # All agent implementations
├── reports/           # Generated PDFs/JSON reports
├── app/               # Streamlit or Gradio UI (optional)
├── meta/              # Metadata like meta.json
├── requirements.txt
├── main.py
└── README.md
🧩 Agent Architecture
Agent	Description
Preprocessor Agent	Extracts GPS, timestamps, and tweet metadata
Vision Agent	Performs image captioning and disaster classification
Language Agent	Analyzes tweet context and urgency
Planning Agent	Generates action plans via LLMs or logic rules
Reporting Agent	Compiles summaries into exportable reports (PDF, JSON)

🤖 Models Used
Agent	Model(s)	Task
Vision Agent	ResNet50	Damage classification, captioning
Language Agent	BERTweet, T5, BART	Tweet analysis and summarization
Planning Agent	GPT-4 (LangChain) / Rule-based	Action plan generation
Reporting Agent	Jinja2, pdfkit	Report formatting and exporting

📁 Datasets
CrisisMMD: Annotated tweet-image pairs
🔗 CrisisMMD Dataset

🗃️ Metadata Format
Sample from meta.json:

json
Copy
Edit
{
  "tweet_id": "1234567890",
  "image_name": "flood_001.jpg",
  "disaster_type": "flood",
  "timestamp": "2025-07-14T16:32:00+05:30",
  "latitude": 28.6139,
  "longitude": 77.2090
}
🧪 Sample Output
Input: A tweet with an associated image
Output:

Disaster Summary: "Severe flooding in East Delhi, multiple buildings submerged."

Location: "East Delhi, Zone B"

Action Plan:

Evacuate Zone B

Deploy medical and rescue units

Restrict access to main roads

Export Formats:

report_1234567890.pdf

report_1234567890.json

⚙️ Getting Started
✅ Prerequisites
Python 3.8+

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
🚀 Run the Pipeline
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-repo/multiagent-crisis-ai.git
cd multiagent-crisis-ai
Upload Datasets and Pretrained Models into the data/ folder.

Run the main script

bash
Copy
Edit
python main.py
📍 Milestones
Week 1–2: Metadata extraction & preprocessing

Week 3–4: Vision & language model training

Week 5: Agent integration & decision logic

Week 6: Report generation & formatting

Week 7: Optional UI (Streamlit/Gradio)

Week 8: Final packaging & deployment

🧑‍💻 Contributions
Built by Piyush Kumar
🎓 Capstone Project: Real-world AI for humanitarian response

🔗 Resources
Resource	Link
📂 Dataset	CrisisMMD
🧠 Trained Models	Google Drive
📄 Sample Reports	Google Drive


🛡️ License & Ethics
Fully open-source and academic

No personally identifiable information used

Designed for humanitarian and research use

Human-in-the-loop verification required for real-world deployment