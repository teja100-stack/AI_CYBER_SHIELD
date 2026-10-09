import streamlit as st
import joblib
model = joblib.load("cyber_threat_model.pkl")
st.title("AI Cyber Threat Detection")
st.write("An AI-powered system that detects suspicious cyber activity, explains the threat, and recommends a response.")
st.subheader("Enter Cyber Activity")

failed_logins = st.number_input("Failed Login Attempts", min_value=0)
data_transferred = st.number_input("Data Transferred (MB)", min_value=0)
unknown_device = st.checkbox("Login from an unknown device")
if st.button("Detect Threat"):
    prediction = model.predict([[failed_logins, data_transferred, int(unknown_device)]])[0]
    if prediction == -1:
        st.info("🤖 AI Model: Anomalous activity detected")
    else:
        st.info("🤖 AI Model: Activity appears normal")
    threat_score = 0

    if failed_logins >= 10:
        threat_score += 40

    if data_transferred >= 500:
        threat_score += 30

    if unknown_device:
        threat_score += 30
    st.metric("Threat Score", f"{threat_score}/100")
    if threat_score >= 60:
        st.error("🔴 Risk Level: HIGH")
    elif threat_score >= 30:
        st.warning("🟡 Risk Level: MEDIUM")
    else:
        st.success("🟢 Risk Level: LOW")    
    if failed_logins >= 10 or data_transferred >= 500 or unknown_device:
        st.error("⚠️ Threat Detected!")
        if failed_logins >= 10:
            st.write("Reason: Multiple failed login attempts may indicate a brute-force attack.")

        if data_transferred >= 500:
            st.write("Reason: Unusually high data transfer may indicate suspicious data activity.")

        if unknown_device:
            st.write("Reason: Login from an unknown device may indicate unauthorized access.")
        st.warning("Recommended Action: Isolate the suspicious device, block the account if necessary, and review the activity logs.")
    else:
        st.success("✅ Activity is Normal")