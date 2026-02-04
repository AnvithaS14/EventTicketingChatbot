import streamlit as st
import json
from datetime import datetime

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="🎟️ Event Ticketing Chatbot", layout="wide")

# ---------- SESSION STATE ----------
if "search_query" not in st.session_state:
    st.session_state.search_query = ""

if "results" not in st.session_state:
    st.session_state.results = []

if "last_search" not in st.session_state:
    st.session_state.last_search = ""

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.stApp { background-color: #f5f7fb; }

h1 { color: #2c2f4a; font-weight: 700; }

.event-card {
    background: white;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

.price-badge {
    background: linear-gradient(90deg, #ff8a00, #e52e71);
    color: white;
    padding: 6px 14px;
    border-radius: 999px;
    font-weight: 600;
}

.success-box {
    background-color: #ecfdf5;
    color: #065f46;
    padding: 14px;
    border-radius: 12px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---------- LOAD EVENTS ----------
def load_events():
    with open("data/ticketmaster_events.json", "r") as f:
        return json.load(f)

# ---------- SEARCH ----------
def search_events(keyword):
    keyword = keyword.lower().strip()
    return [
        e for e in load_events()
        if keyword in e["name"].lower()
        or keyword in e["venue"].lower()
    ]

# ---------- RECOMMENDATION LOGIC ----------
def recommend_events(keyword):
    keyword = keyword.lower()
    events = load_events()

    if "music" in keyword:
        return [e for e in events if "music" in e["name"].lower()]
    if "tech" in keyword or "ai" in keyword:
        return [e for e in events if "conference" in e["name"].lower() or "summit" in e["name"].lower()]
    if "startup" in keyword:
        return [e for e in events if "startup" in e["name"].lower()]
    
    return events[:3]

# ---------- DYNAMIC PRICING (SIMULATED) ----------
def calculate_price(base_price=500):
    price = base_price

    # Simulated demand surge
    price *= 1.2

    # Weekend surge pricing
    if datetime.now().weekday() >= 5:
        price *= 1.15

    return round(price, 2)

# ---------- HEADER ----------
st.markdown("""
<h1 style="text-align:center;">🎟️ Event Ticketing Chatbot</h1>
<p style="text-align:center; color:gray;">
Dynamic pricing • Group discounts • Smart recommendations
</p>
""", unsafe_allow_html=True)

# ---------- SEARCH BAR ----------
st.markdown("### 🔍 Search Events")
query = st.text_input(
    "Search by event name or venue",
    placeholder="music, tech, bangalore...",
    key="search_query"
)

if query:
    st.session_state.results = search_events(query)
    st.session_state.last_search = query

# ---------- RESULTS ----------
if query:
    if st.session_state.results:
        st.markdown("### 🎉 Available Events")

        for e in st.session_state.results:
            price = calculate_price()

            st.markdown(f"""
            <div class="event-card">
                <h3>🎫 {e['name']}</h3>
                <p>📍 <b>{e['venue']}</b></p>
                <p>📅 {e['date']} | ⏰ {e['time']}</p>
                <span class="price-badge">₹{price} / ticket</span>
            </div>
            """, unsafe_allow_html=True)

            qty = st.number_input(
                "🎟️ Select number of tickets",
                min_value=1,
                max_value=10,
                value=1,
                key=f"qty_{e['id']}"
            )

            total_price = price * qty

            if qty >= 5:
                st.success("🎉 Group Discount Applied (10%)")
                total_price *= 0.9

            st.markdown(f"### 💳 Total Price: ₹{round(total_price, 2)}")

            if st.button("🎫 Book Now", key=f"book_{e['id']}"):
                st.markdown("""
                <div class="success-box">
                    ✅ Booking Confirmed! Thank you for choosing EventBot 🎉
                </div>
                """, unsafe_allow_html=True)

                st.info(f"🎟️ Event: {e['name']}")
                st.info(f"🎟️ Tickets: {qty}")
                st.info(f"💳 Amount Paid: ₹{round(total_price, 2)}")

            st.divider()

    else:
        st.warning("No events found 😕")

# ---------- SMART RECOMMENDATIONS ----------
if st.session_state.last_search:
    st.markdown("## 🤖 Recommended Events For You")

    for r in recommend_events(st.session_state.last_search):
        st.markdown(f"""
        <div class="event-card">
            <h4>✨ {r['name']}</h4>
            <p>📍 {r['venue']}</p>
            <p>📅 {r['date']} | ⏰ {r['time']}</p>
        </div>
        """, unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>© 2026 Event Ticketing Chatbot | Ticketmaster Simulation</p>",
    unsafe_allow_html=True
)
