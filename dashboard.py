import streamlit as st
import pandas as pd

st.set_page_config(page_title="AWS Cost Optimizer", page_icon="💰", layout="wide")

st.title("💰 AWS Cost Optimizer")
st.caption("Automated FinOps Scanner - Python + Boto3")

# --- METRICS ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Monthly Savings", "$34.15", "+$409 /yr")
col2.metric("Unused EBS", "2 Volumes", "$10.00")
col3.metric("Elastic IPs", "1 Unused", "$3.65")
col4.metric("Status", "Demo Mode", "Portfolio Ready")

st.divider()

# --- DATA ---
data = [
    {"Resource ID": "vol-0a1b2c3d (100GB)", "Type": "Unused EBS", "Region": "us-east-1", "Monthly Cost": 10.00, "Action": "Delete / Snapshot"},
    {"Resource ID": "vol-0e4f5g6h (100GB)", "Type": "Unused EBS", "Region": "us-east-1", "Monthly Cost": 0.00, "Action": "Delete"},
    {"Resource ID": "eip-192.0.2.1", "Type": "Unused EIP", "Region": "us-east-1", "Monthly Cost": 3.65, "Action": "Release"},
    {"Resource ID": "snap-001 (50GB)", "Type": "Old Snapshot >90d", "Region": "us-east-1", "Monthly Cost": 2.50, "Action": "Delete"},
    {"Resource ID": "elb-idle-prod", "Type": "Idle ELB", "Region": "us-east-1", "Monthly Cost": 18.00, "Action": "Delete"},
]

df = pd.DataFrame(data)

col_left, col_right = st.columns([2,1])

with col_left:
    st.subheader("📊 Waste Breakdown")
    st.dataframe(df, use_container_width=True)

with col_right:
    st.subheader("💸 Cost by Type")
    chart_data = df.groupby("Type")["Monthly Cost"].sum()
    st.bar_chart(chart_data)
    st.success("POTENTIAL SAVINGS: $34.15 / month ($409.80 / year)")

st.divider()
st.subheader("🚀 CI/CD Pipeline")
st.code("GitHub → Python (Boto3) → Lambda + EventBridge (Daily 9AM) → Slack / Email Report → Streamlit Dashboard", language="text")

if st.button("🔄 Re-Run Scan (python src/main.py)"):
    st.info("Run in terminal: python src/main.py")