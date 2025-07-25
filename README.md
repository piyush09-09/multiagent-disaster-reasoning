\# Multi-Agent Crisis AI Reasoning System



A modular multi-agent AI framework that analyzes disaster-related visual and textual data to generate structured crisis summaries and response plans.



---



\## 🔍 Overview



This project implements a \*\*multi-agent architecture\*\* for multimodal crisis reasoning using:



\* Disaster-related tweets and metadata

\* Aerial and street-level imagery

\* Location and timestamp information

\* Pretrained vision and language models



---



\## 🎯 Objective



The system is capable of:



\* Classifying disaster types from images and text

\* Estimating damage severity from visual inputs

\* Extracting crisis context from tweets

\* Inferring geolocation from metadata or textual clues

\* Generating structured action plans

\* Exporting readable reports (JSON/PDF)



---



\## 🧹 Architecture Overview



\### Core Agents:



\* \*\*Preprocessor Agent\*\*



&nbsp; \* Extracts GPS, timestamps, and tweet metadata



\* \*\*Vision Agent\*\*



&nbsp; \* Performs image captioning and disaster classification

&nbsp; \* Detects severity and key crisis elements



\* \*\*Language Agent\*\*



&nbsp; \* Analyzes tweet context

&nbsp; \* Extracts disaster type and urgency indicators



\* \*\*Planning Agent\*\*



&nbsp; \* Uses logic/LLMs to create a response plan



\* \*\*Reporting Agent\*\*



&nbsp; \* Compiles summaries into reports (PDF, JSON, UI)



---



\## 🧠 Agent Models Used



| Agent           | Model(s)                            | Task                                |

| --------------- | ----------------------------------- | ----------------------------------- |

| Vision Agent    | ResNet50                            | Damage classification \& captioning  |

| Language Agent  | BERTweet, T5, BART                  | Tweet understanding \& summarization |

| Planning Agent  | GPT-4 (via LangChain) or rule-based | Action plan generation              |

| Reporting Agent | Jinja2, pdfkit                      | Report generation                   |



---



\## 📃 Datasets



\* \*\*CrisisMMD\*\* – Tweet-image pairs with annotations

Link : https://crisisnlp.qcri.org/crisismmd

---



\## 🗃️ Metadata Format



Sample entry from `meta.json`:



```json

{

&nbsp; "tweet\_id": "1234567890",

&nbsp; "image\_name": "flood\_001.jpg",

&nbsp; "disaster\_type": "flood",

&nbsp; "timestamp": "2025-07-14T16:32:00+05:30",

&nbsp; "latitude": 28.6139,

&nbsp; "longitude": 77.2090

}

```



---



\## 🧪 Output Example



\* \*\*Input\*\*: A tweet and an associated image

\* \*\*Output\*\*:



&nbsp; \* \*\*Disaster Summary\*\*: "Severe flooding in East Delhi, multiple buildings submerged."

&nbsp; \* \*\*Location\*\*: "East Delhi, Zone B"

&nbsp; \* \*\*Action Plan\*\*:



&nbsp;   \* Evacuate Zone B

&nbsp;   \* Deploy medical and rescue units

&nbsp;   \* Restrict access to main roads

&nbsp; \* \*\*Export Formats\*\*:



&nbsp;   \* JSON

&nbsp;   \* PDF



---



\## ⚙️ Getting Started



\### Prerequisites



\* Python 3.8+

\* Install dependencies:



&nbsp; ```bash

&nbsp; pip install -r requirements.txt

&nbsp; ```



\### Steps



1\. Clone the repository:



&nbsp;  ```bash

&nbsp;  git clone https://github.com/your-repo/multiagent-crisis-ai.git

&nbsp;  cd multiagent-crisis-ai

&nbsp;  ```



2\. Upload datasets and pretrained models into appropriate folders.



3\. Run the main pipeline:



&nbsp;  ```bash

&nbsp;  python main.py

&nbsp;  ```



---



\## 🚀 Tech Stack



\* \*\*Backend\*\*: PyTorch, HuggingFace Transformers

\* \*\*Coordination (Optional)\*\*: LangChain

\* \*\*Frontend (Optional)\*\*: Streamlit / Gradio

\* \*\*Exporting Reports\*\*: Jinja2, pdfkit



---



\## 🚦 Future Enhancements



\* Real-time alerts via WhatsApp/Telegram

\* OSM overlays for live maps

\* Multilingual tweet analysis

\* Integration with NDMA/GDACS APIs



---



\## 📄 License \& Ethics



\* Uses open-source and public datasets only

\* No personally identifiable data used

\* Strictly for academic and humanitarian use

\* Ensure human verification before any real-world use



