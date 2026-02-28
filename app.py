import streamlit as st

st.title("AI Smart Feedback Analyzer (Demo Mode)")

name = st.text_input("Enter your Name")
feedback = st.text_area("Enter your Feedback")

def analyze_feedback(text):
    text = text.lower()

    # sentiment detection
    positive_words = ["good", "great", "excellent", "helpful", "nice"]
    negative_words = ["slow", "bad", "poor", "worst", "outdated", "problem"]

    sentiment = "Neutral"
    if any(word in text for word in positive_words):
        sentiment = "Positive"
    if any(word in text for word in negative_words):
        sentiment = "Negative"

    # main issue detection
    if "wifi" in text or "internet" in text:
        issue = "Network/Internet Issue"
        suggestion = "Improve campus WiFi speed and coverage."
    elif "lab" in text or "computer" in text:
        issue = "Laboratory Infrastructure"
        suggestion = "Upgrade lab computers and equipment."
    elif "teacher" in text or "faculty" in text:
        issue = "Teaching/Faculty"
        suggestion = "Provide faculty training and interactive sessions."
    else:
        issue = "General Feedback"
        suggestion = "Review feedback and improve services."

    return sentiment, issue, suggestion


if st.button("Analyze"):
    if feedback:
        sentiment, issue, suggestion = analyze_feedback(feedback)

        st.subheader("AI Result:")
        st.write(f"**Sentiment:** {sentiment}")
        st.write(f"**Main Problem:** {issue}")
        st.write(f"**Suggested Improvement:** {suggestion}")
    else:
        st.warning("Please enter feedback")