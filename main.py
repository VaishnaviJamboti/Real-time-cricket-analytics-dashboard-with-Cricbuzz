import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Cricbuzz LiveStats",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        color: #1a73e8;
        text-align: center;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #555;
        text-align: center;
        margin-bottom: 30px;
    }
    .card {
        background: linear-gradient(135deg, #1a73e8, #0d47a1);
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 10px;
    }
    .tool-badge {
        background: #e8f0fe;
        color: #1a73e8;
        padding: 5px 14px;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
        margin: 4px;
    }
    .page-card {
        border-left: 5px solid #1a73e8;
        padding: 12px 16px;
        background: #f8f9fa;
        border-radius: 6px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<p class="main-title">🏏 Cricbuzz LiveStats</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Real-Time Cricket Insights & SQL-Based Analytics Dashboard</p>', unsafe_allow_html=True)

st.divider()

# --- PROJECT OVERVIEW ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📌 Project Overview")
    st.markdown("""
    **Cricbuzz LiveStats** is a comprehensive cricket analytics platform that integrates 
    live data from the **Cricbuzz API** with a **PostgreSQL database** to deliver an 
    interactive, data-driven web application built with **Streamlit**.

    This dashboard enables:
    - ⚡ **Real-time match updates** — live scorecard data fetched from the Cricbuzz API
    - 📊 **Player performance analytics** — top stats by runs, wickets, sixes, and more
    - 🧮 **SQL-driven insights** — 25 queries from beginner to advanced level
    - 🛠️ **CRUD operations** — manage player records directly via a form-based UI
    """)

with col2:
    st.subheader("🎯 Domain")
    st.info("**Sports Analytics**")
    st.subheader("⏱️ Timeline")
    st.success("14-Day Project")

st.divider()

# --- TOOLS USED ---
st.subheader("🛠️ Tools & Technologies")
tools = ["Python", "Streamlit", "SQL", "PostgreSQL", "REST API", "pandas", "requests", "SQLAlchemy", "Plotly", "JSON"]
badges_html = "".join([f'<span class="tool-badge">{t}</span>' for t in tools])
st.markdown(badges_html, unsafe_allow_html=True)

st.divider()

# --- PAGE NAVIGATION GUIDE ---
st.subheader("📂 Application Pages")
st.markdown("Use the **left sidebar** to navigate between the following pages:")

pages = [
    ("🏠", "Home (Main)", "Project overview, tools, and navigation guide — you are here."),
    ("📡", "Live Match", "Real-time IPL match scores and player performance fetched from the Cricbuzz API."),
    ("🏆", "Top Player Stats", "Tournament leaderboards — Most Runs, Wickets, Sixes, and Highest Scores."),
    ("📊", "SQL Analytics", "25 SQL queries (Beginner → Advanced) run against the PostgreSQL database."),
    ("🛠️", "CRUD Operations", "Add, view, update, and delete player match records in the database."),
    ("🧠", "Advanced Analytics", "KPI metrics, performance clusters, correlation charts, and a live SQL terminal."),
]

for icon, name, desc in pages:
    st.markdown(f"""
    <div class="page-card">
        <strong>{icon} {name}</strong><br>
        <span style="color:#555;">{desc}</span>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- BUSINESS USE CASES ---
st.subheader("💼 Business Use Cases")

uc_col1, uc_col2, uc_col3 = st.columns(3)

with uc_col1:
    st.markdown("**📺 Sports Media & Broadcasting**")
    st.caption("Real-time updates for commentary teams, player analysis for pre-match discussions, and historical trends for match predictions.")

    st.markdown("**🎮 Fantasy Cricket Platforms**")
    st.caption("Player form tracking, head-to-head stats for team selection, and real-time score updates for fantasy leagues.")

with uc_col2:
    st.markdown("**📈 Cricket Analytics Firms**")
    st.caption("Advanced statistical modeling, performance trend analysis across formats, and data-driven team management insights.")

    st.markdown("**🎓 Educational Use**")
    st.caption("Teaching database operations with real-world data, SQL practice with cricket datasets, and API integration learning.")

with uc_col3:
    st.markdown("**🎲 Sports Prediction**")
    st.caption("Historical performance for odds calculation, player momentum tracking, and venue-specific performance analysis.")

st.divider()

# --- DATABASE SCHEMA INFO ---
st.subheader("🗄️ Database Schema")
st.markdown("This project uses a **PostgreSQL** database (`Cricket`) with the following primary table:")

st.code("""
TABLE: match_stats
─────────────────────────────────────────────────
  id            SERIAL PRIMARY KEY
  player_name   VARCHAR(100)
  runs          INTEGER
  balls         INTEGER
  fours         INTEGER
  sixes         INTEGER
  strike_rate   FLOAT
  match_id      VARCHAR(50)
─────────────────────────────────────────────────
""", language="sql")

# --- FOOTER ---
st.divider()
st.caption("🏏 Cricbuzz LiveStats | Final Project Portfolio | Vaishnavi Jamboti")
st.caption("Built with Python · Streamlit · PostgreSQL · Cricbuzz REST API")