import streamlit as st
import os
import asyncio
from collections import defaultdict
from datetime import datetime

from runtime.run_scrum_team import run_scrum_team
from dotenv import load_dotenv

# -----------------------
# Load environment
# -----------------------
load_dotenv()

# -----------------------
# Page header, title and input setup
# -----------------------
st.set_page_config(page_title="🤖 AI Agile Scrum Team", layout="wide")
st.title("AI Agile Real Scrum Team Simulator")
st.markdown(
    "Simulate a real Agile team using Azure OpenAI models. "
    "Enter a task, run the AI agents, and see outputs for each role."
)

# -----------------------
# Sidebar: Azure Settings
# -----------------------
st.sidebar.header("Azure OpenAI Settings")

endpoint = st.sidebar.text_input(
    "Endpoint", value=os.getenv("AZURE_OPENAI_ENDPOINT", "")
)
api_key = st.sidebar.text_input(
    "API Key", type="password", value=os.getenv("AZURE_OPENAI_KEY", "")
)
deployment_name = st.sidebar.text_input(
    "Deployment Name", value=os.getenv("MODEL_NAME", "")
)

if endpoint:
    os.environ["AZURE_OPENAI_ENDPOINT"] = endpoint
if api_key:
    os.environ["AZURE_OPENAI_KEY"] = api_key
if deployment_name:
    os.environ["MODEL_NAME"] = deployment_name

# -----------------------
# Select Execution Mode
# -----------------------
st.sidebar.header("Execution Mode")
mode = st.sidebar.radio(
    "Select workflow",
    ["Manual", "Single-Agent", "Multi-Agent"],
    index=2  # default = multi
)

# -----------------------
# Task Input
# -----------------------
st.header("User Requirement")

task_description = st.text_area(
    "Enter the high level user requirements",
    value="e.g. We need a system that calculates LGD for defaulted loans, updates recoveries and generates dashboards."
)

run_button = st.button("🚀 Run Scrum Team Simulation")

# -----------------------
# Initialize Session State
# -----------------------
if "agent_logs" not in st.session_state:
    st.session_state.agent_logs = defaultdict(list)

if "final_output" not in st.session_state:
    st.session_state.final_output = ""

if "has_run" not in st.session_state:
    st.session_state.has_run = False

tabs_placeholder = st.empty()

# -----------------------
# Core Functions
# -----------------------

def run_manual_mode(task_description):
    """
    Manual baseline: just measure time while user prepares artifacts externally.
    """

    st.info("Manual mode selected.\nPrepare artifacts manually, then click 'Stop Manual Timer'.")

    if "manual_start" not in st.session_state:
        if st.button("▶ Start Manual Timer"):
            st.session_state.manual_start = datetime.now()
    else:
        elapsed = datetime.now() - st.session_state.manual_start
        st.write(f"⏱ Elapsed time: {elapsed}")

        if st.button("⏹ Stop Manual Timer"):
            total_minutes = elapsed.total_seconds() / 60
            st.success(f"Manual time recorded: {total_minutes:.2f} minutes")

            st.session_state.final_output = f"""
# Manual Mode
Time taken: {total_minutes:.2f} minutes
Artifacts prepared manually outside the system.
"""
            st.session_state.has_run = True
            del st.session_state.manual_start

async def run_single_agent(task_description, on_message):
    """
    Single LLM call that performs all Scrum activities at once.
    """

    from openai import AzureOpenAI

    client = AzureOpenAI(
        api_key=api_key,
        azure_endpoint=endpoint
    )

    prompt = f"""
You act as a complete Scrum team (Product Owner, Analyst, Developer, QA).

Given the requirements below:
1. Create prioritized backlog
2. Write user stories with acceptance criteria
3. Propose architecture
4. Create test cases

Requirements:
{task_description}

Return results in clearly separated sections.
"""

    on_message("Single-Agent", "Running unified Scrum agent...")

    resp = client.chat.completions.create(
        model=deployment_name,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    content = resp.choices[0].message.content

    on_message("Single-Agent", content)

    return content

# # -----------------------
# # Tabs Views - Agent, Scrum Board, Final output
# # -----------------------

def render_tabs_board():
    agent_logs = st.session_state.agent_logs
    agent_names = list(agent_logs.keys())

    with tabs_placeholder.container():
        tabs = st.tabs(
            ["🗂 Scrum Board"] + agent_names + ["📦 Final Deliverable"]
        )

        # -------- Scrum Board --------
        with tabs[0]:
            cols = st.columns(len(agent_names) or 1)
            for i, name in enumerate(agent_names):
                with cols[i]:
                    st.markdown(f"### {name}")
                    for msg in agent_logs[name]:
                        st.markdown(
                            f"""
                            <div style="background:#f6f6f6;
                                        padding:10px;
                                        border-radius:8px;
                                        margin-bottom:8px;">
                                {msg}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

        # -------- Agent Tabs --------
        for i, name in enumerate(agent_names):
            with tabs[i + 1]:
                st.markdown("\n\n---\n\n".join(agent_logs[name]))

        # -------- Final Deliverable --------
        with tabs[-1]:
            final_output = st.session_state.final_output
            if final_output:
                st.download_button(
                    "⬇ Download markdown",
                    final_output,
                    "scrum_output.md",
                    "text/markdown",
                    use_container_width=True
                )
                st.markdown(final_output)
            else:
                st.info("Final deliverable will appear here after the run.")

def on_message(agent_name, content):
    """Callback to update agent logs and re-render UI."""
    ts = datetime.now().strftime("%H:%M:%S")
    st.session_state.agent_logs[agent_name].append(
        f"**{ts}**\n{content}"
    )
    render_tabs_board()

# -----------------------
# Run Simulation
# -----------------------
if run_button:
    if not all([endpoint, api_key, deployment_name]):
        st.error("Please provide all Azure OpenAI settings.")
    elif not task_description.strip():
        st.error("Please enter a task description.")
    else:
        st.session_state.agent_logs.clear()
        st.session_state.final_output = ""
        st.session_state.has_run = False

        # -----------------------
        # Run async orchestration
        # -----------------------
        try:
            start_time = datetime.now()
            with st.spinner("Running workflow..."):
                if mode == "Multi-Agent":
                    final_output = asyncio.run(
                        run_scrum_team(task_description, on_message)
                    )
                elif mode == "Single-Agent":
                    final_output = asyncio.run(
                    run_single_agent(task_description, on_message)
                    )
                elif mode == "Manual":
                    run_manual_mode(task_description)
                    st.stop()

            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds() / 60

            st.session_state.final_output = f"""
            ⏱ Total runtime: {duration:.2f} minutes
            ---
            {final_output}
            """       

            # st.session_state.final_output = final_output
            st.session_state.has_run = True

        except Exception as e:
            st.error("❌ Simulation failed")
            st.exception(e)
            st.stop()
# -----------------------
# Render tabs if run has completed
# -----------------------
if st.session_state.has_run:
    render_tabs_board()

# -----------------------
# Sidebar Notes
# -----------------------
st.sidebar.markdown("---")
st.sidebar.write(
    "💡 Enter Azure credentials, select the execution mode, enter user requirement, and run the Scrum Team Simulator."
)
