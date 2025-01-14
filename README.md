# Dice Simulation

A web-based dice simulation game built with Flask. The application allows users to roll different types of dice, track roll history, and analyze the results.

## Features:
- **Dice Rolling**: Roll multiple dice of various types (e.g., D6, D20).
- **Result Tracking**: Save and display the results of each roll.
- **Statistics**: Calculate and display roll statistics.
- **API**: 
  - `/api/roll` - Roll dice via API with customizable parameters.
  - `/api/history` - Retrieve the history of rolls in JSON format.

## Technologies Used:
- Flask
- Flask-SQLAlchemy
- HTML, CSS (Frontend with simple animations)

## Setup Instructions:
1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
