# EventTicketingChatbot
**Event Ticketing Chatbot**

A smart event ticket booking web application built using Python and Streamlit.
The application allows users to search events, view dynamically adjusted ticket prices, apply automatic group discounts, and book tickets through an intuitive and visually clean user interface.

This project simulates a Ticketmaster-style ticket booking system with dynamic pricing logic and session-stable search functionality.

**Features**
**Event Discovery**

Single unified search bar (search by event name or venue)

Real-time event filtering

Live seat availability display

**Pricing Intelligence**

Dynamic ticket pricing based on seat availability

Weekend surge pricing logic

Automatic group discount (10% for 5 or more tickets)

**Booking System**

Ticket quantity selector

Price recalculation without page refresh

Booking confirmation with transaction summary

**User Experience**

Modern dashboard with custom CSS styling

Stable UI using Streamlit session state

Clean layout optimized for readability

**Integration**

Ticketmaster-style integration (simulated using JSON dataset)

**Technology Stack**
Technology	     Purpose
Python	         Core application logic
Streamlit	       Web application framework
JSON	           Event dataset simulation
HTML & CSS	     Custom UI styling
Datetime	        Dynamic pricing logic

**Project Structure**
Event Ticket Chatbot/
│
├── app.py
├── data/
│   └── ticketmaster_events.json
└── README.md

**How to Run the Project**
Step 1: Install Dependencies
pip install streamlit

Step 2: Run the Application
streamlit run app.py

Step 3: Open in Browser
http://localhost:8501

**Sample Event Data (ticketmaster_events.json)**
[
  {
    "id": 1,
    "name": "Live Music Concert",
    "venue": "Bangalore Stadium",
    "date": "2026-03-20",
    "time": "7:00 PM"
  },
  {
    "id": 2,
    "name": "Tech Conference 2026",
    "venue": "Hyderabad Convention Center",
    "date": "2026-04-10",
    "time": "10:00 AM"
  }
]

**Key Concepts Implemented**

Streamlit session state management

Dynamic pricing based on demand and time

Stable UI rendering during user interaction

Modular, function-based code structure

Real-world event ticket booking simulation

**Use Cases**

College Mini Project or Major Project

Resume and Portfolio Project

Streamlit Framework Learning

Demonstration of UI with Business Logic

Interview and Viva Voce Explanation

**Future Enhancements**

User authentication and login system

Payment gateway integration

Sales and booking analytics dashboard

Location-based event recommendations

Mobile-responsive layout

Real Ticketmaster API integration
