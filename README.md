# 🎉 Vendor Recommendation & Event Planner AI Bot

A rule-based event planning assistant built with Python + Streamlit that helps users plan events and receive vendor recommendations based on their inputs.

✅ Uses local mock data only
❌ No external APIs used (no OpenAI, Dialogflow, etc.)
🛠 Built entirely with custom logic and static JSON datasets

---

## 🧠 Features
1. Conversational chatbot UI

2. Collects user inputs:

    Event type (e.g., Wedding, Birthday)

    Budget

    Location

    Number of guests

3. Recommends top vendors for:

    Venue

    Catering (per-plate logic based on guest count)

    Decoration

4. Uses a scoring system to rank vendors by:

    Price compatibility

    Rating

    Budget-fit per service


---

## 🧮 Logic Overview

1. User Interaction: Conversational bot collects event details.

2. Filtering: Filters vendors based on location and event type.

3. Budget Breakdown: Total budget divided across services (Venue, Catering, Decor).

4. Scoring Formula:

    score = (5 − (∣ vendor price − budget per service ∣) / ( budget per service )) + ( rating × 2 )

5. Recommendation: Top 2 vendors per category are suggested with pricing and ratings.

6. Thank-you Message: Closes the session with a polite summary.


---

## 📁 Project Structure

Event_Planning_AI/
│
├── app.py                   # Main Streamlit app
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
├── Demo Video/              # Folder containing demo recording
│
└── Vendors/
    ├── venue.json           # Venue vendor mock data
    ├── Catering.json        # Catering vendor mock data
    └── Decor.json    

---

## 📦 Installation & Run Instructions

1. **Clone the repository**:
    ```bash
        git clone https://github.com/your-username/Event_Planning_AI.git
        cd Event_Planning_AI
    ```

2. **Install dependencies**:
    ```bash
        pip install -r requirements.txt
    ```

3. **Run the Streamlit app**:
    ```bash
        streamlit run app.py
    ```

---

## 📌 Notes

1. All vendor data is mock data stored in JSON files.

2. This project is ideal for demo, offline prototyping, or hackathon submission.

3. No external APIs are used — perfect for testing in restricted environments.

---

## 🙌 Acknowledgements

This project was developed as a rule-based simulation of an intelligent assistant using:

1. Streamlit for UI

2. Python for logic

3. Manual JSON files for data simulation




