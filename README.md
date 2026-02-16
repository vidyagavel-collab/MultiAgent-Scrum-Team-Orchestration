Here is a professional **README.md** tailored to your project structure and the provided `requirements.txt`  and `streamlit_app.py` .

You can copy this directly into a `README.md` file in your root folder.

---

# 🤖 MultiAgent Scrum Team Orchestration

AI-powered Agile Scrum Team Simulator built with **Azure OpenAI**, **Semantic Kernel**, and **Streamlit**.

This project simulates a real Agile Scrum team (Product Owner, Analyst, Developer, QA) using Large Language Models. It allows you to compare:

* 🧍 Manual workflow
* 🤖 Single-Agent LLM execution
* 👥 Multi-Agent orchestrated execution

Developed as part of the **UZH CAS Generative AI** project.

---

## 📌 Overview

The system simulates how a Scrum team would process high-level business requirements and transform them into:

* Prioritized backlog
* User stories with acceptance criteria
* Proposed system architecture
* Test cases
* Final deliverable artifact

The application provides a **Scrum Board-style UI** where you can see each agent’s contribution in real time.

---

## 🏗 Project Structure

```
MultiAgent-Scrum-Team-Orchestration/
│
├── streamlit_app.py        # Main UI application
├── requirements.txt        # Dependencies
│
├── agents/                 # AI role agents (PO, Dev, QA, etc.)
├── manager/                # Orchestration & coordination logic
├── runtime/                # run_scrum_team orchestration entrypoint
├── plugins/                # Semantic Kernel plugins/tools
├── output/                 # Generated artifacts (if persisted)
├── application_run_video/  # Demo recording
```

---

## ⚙️ Tech Stack

* **Azure OpenAI**
* **Semantic Kernel**
* **Streamlit**
* **Python 3.9+**
* pandas, matplotlib (for data extensions)

Dependencies (from `requirements.txt`):

```
semantic-kernel
azure-identity
python-dotenv
requests
streamlit
pyyaml
pandas
matplotlib
```

---

## 🚀 Features

### 1️⃣ Multi-Agent Mode (Default)

* Orchestrates multiple AI agents
* Each role contributes independently
* Real-time Scrum Board updates
* Best simulation of real Agile workflow

### 2️⃣ Single-Agent Mode

* One unified LLM prompt
* Simulates entire Scrum team in one call
* Faster but less realistic collaboration

### 3️⃣ Manual Mode

* Baseline comparison
* Manual timer to compare productivity gains

---

## 🔐 Azure OpenAI Setup

You need:

* Azure OpenAI Endpoint
* API Key
* Deployment Name (Model Name)

You can provide them either:

### Option A — Environment Variables (.env file)

Create a `.env` file in root:

```env
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_KEY=your_api_key
MODEL_NAME=your_deployment_name
```

### Option B — Enter in Streamlit Sidebar

The UI allows manual input of:

* Endpoint
* API Key
* Deployment Name

---

## ▶️ How to Run

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd MultiAgent-Scrum-Team-Orchestration
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Application

```bash
streamlit run streamlit_app.py
```

App will launch in your browser:

```
http://localhost:8501
```

---

## 🖥 How It Works

### Step 1 — Enter User Requirement

Example:

```
We need a system that calculates LGD for defaulted loans, updates recoveries and generates dashboards.
```

### Step 2 — Select Execution Mode

* Manual
* Single-Agent
* Multi-Agent

### Step 3 — Run Simulation

The system:

1. Triggers orchestration logic (`runtime/run_scrum_team`)
2. Calls Azure OpenAI models
3. Streams outputs per agent
4. Displays:

   * 🗂 Scrum Board
   * 👤 Individual agent tabs
   * 📦 Final downloadable markdown deliverable
   * ⏱ Runtime measurement

---

## 🧠 Architecture (Conceptual)

```
User Requirement
        │
        ▼
Streamlit UI
        │
        ▼
Execution Mode Router
        │
 ┌───────────────┬────────────────┐
 │               │                │
Manual      Single-Agent     Multi-Agent
                                  │
                                  ▼
                        run_scrum_team()
                                  │
                                  ▼
                        Agent Orchestration
                                  │
                                  ▼
                           Final Deliverable
```

---

## 📊 Educational Purpose

This project demonstrates:

* Multi-agent LLM orchestration
* Role-based prompt engineering
* Real-time UI feedback loops
* Comparative AI productivity measurement
* Human vs AI vs Multi-Agent benchmarking

---

## 🧪 Potential Extensions

* Add cost tracking per agent
* Add token usage dashboard
* Persist backlog to database
* Add sprint velocity simulation
* Integrate DevOps pipeline simulation
* Add memory between sprints
* Add RAG for domain knowledge grounding

---

## 🎥 Demo

See `application_run_video/` for recorded execution demo.

---

## 📈 Why Multi-Agent?

Single prompts can generate structured outputs — but multi-agent systems:

* Improve modular reasoning
* Enable role specialization
* Provide traceability
* Mimic real enterprise workflows
* Allow orchestration research experimentation

---

## 🛡 Security Notes

* Do NOT commit `.env` file
* Do NOT expose Azure API keys
* Use environment variables in production
* Consider Azure Managed Identity for enterprise deployment

---

## 📄 License

This project is created for academic and experimental purposes under UZH CAS Gen AI.

(Add your license here if publishing publicly.)

---

## 👤 Author

Vidya
---

If you'd like, I can also generate:

* 🔬 A more academic research-style README
* 🏢 A corporate enterprise-style README
* 📊 A version including architecture diagrams (mermaid)
* 📄 A polished GitHub-ready version with badges
* 🧾 A project report summary for submission

Just tell me the target audience.
