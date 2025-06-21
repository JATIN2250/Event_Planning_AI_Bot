import json
import streamlit as st

# Load vendor data from JSON files
def load_vendor_data(category):
    with open(f'Vendors/{category}.json', 'r') as f:
        return json.load(f)

# Initialize session state
if "chat" not in st.session_state:
    st.session_state.chat = []
if "step" not in st.session_state:
    st.session_state.step = "greet"
if "input" not in st.session_state:
    st.session_state.input = ""

st.title("🤖 Event Planner Assistant Bot")

# Chat input form (clears on submit)
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", value=st.session_state.input, key="input_box")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    st.session_state.chat.append(("🧑", user_input))

    if st.session_state.step == "greet":
        st.session_state.chat.append(("🤖", "Hello! How can I help you today?"))
        st.session_state.step = "ask_event"

    elif st.session_state.step == "ask_event":
        if "event" in user_input.lower():
            st.session_state.chat.append(("🤖", "What type of event? (Wedding or Birthday)"))
            st.session_state.step = "ask_budget_location"
        else:
            st.session_state.chat.append(("🤖", "Please tell me what kind of event you'd like to plan."))

    elif st.session_state.step == "ask_budget_location":
        st.session_state.event_type = user_input.strip().title()
        st.session_state.chat.append(("🤖", "Great! What is your total budget and location? (Example: 300000, Jaipur)"))
        st.session_state.step = "guest_count"

    elif st.session_state.step == "guest_count":
        try:
            parts = user_input.split(',')
            budget = int(parts[0].strip())
            location = parts[1].strip().title()
            st.session_state.budget = budget
            st.session_state.location = location

            st.session_state.chat.append(("🤖", "How many guests are expected?"))
            st.session_state.step = "recommend"
        except Exception as e:
            st.session_state.chat.append(("🤖", "Please enter budget and location in correct format (e.g., 300000, Jaipur)"))

    elif st.session_state.step == "recommend":
        try:
            guest_count = int(user_input.strip())
            st.session_state.guest_count = guest_count

            venue_data = load_vendor_data("venue")
            cater_data_raw = load_vendor_data("Catering")
            decor_data = load_vendor_data("Decor")

            cater_data = []
            for v in cater_data_raw:
                total_catering_price = v["price"] * guest_count
                cater_data.append({**v, "price": total_catering_price})

            budget_per_service = st.session_state.budget // 3

            def score(vendor):
                p = vendor["price"]
                r = vendor["rating"]
                return (5 - abs(p - budget_per_service) / budget_per_service) + (r * 2)

            def filter_and_score(vendors):
                return sorted(
                    [
                        v for v in vendors
                        if st.session_state.location.lower() in v["location"].lower()
                        and st.session_state.event_type.lower() in [e.lower() for e in v["event_types"]]
                    ],
                    key=score,
                    reverse=True
                )[:2]

            st.session_state.chat.append(("🤖", "Here are your top vendor suggestions:"))
            for service, data in [("Venue", venue_data), ("Catering", cater_data), ("Decor", decor_data)]:
                top = filter_and_score(data)
                if top:
                    st.session_state.chat.append(("🤖", f"**Top {service} Vendors:**"))
                    for vendor in top:
                        st.session_state.chat.append((
                            "🤖",
                            f"- {vendor['name']} ({vendor['location']}), ₹{vendor['price']}, ⭐ {vendor['rating']}"
                        ))
                else:
                    st.session_state.chat.append(("🤖", f"No {service} vendors found for your location and event."))

            st.session_state.chat.append(("🤖", "Thank you for using our event planner! 🎉 Let me know if you'd like to plan another event."))
            st.session_state.step = "done"

        except:
            st.session_state.chat.append(("🤖", "Please enter a valid number for guest count."))

# Display chat
for speaker, msg in st.session_state.chat:
    st.markdown(f"**{speaker}:** {msg}")
