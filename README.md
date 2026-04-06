# Multi-Client Online Quiz System with Real-Time Ranking

To run this project, you will find two primary Python scripts in this repository. You must run them in the following order:
1. Run the Server file: This initializes the quiz environment and waits for connections.
2. Run the Client file: Each participant must run this script to join the quiz.You can run multiple instances of the client file for different players.

---

## Overview
This project is a Python-based online quiz system built on a client-server architecture.It allows multiple users to participate in a quiz over a network, submit answers, and receive scores in real-time.


## Core Features
Multi-Client Support: Uses threading to allow several participants to join and play simultaneously.
Real-Time Interaction: Delivers questions and collects answers instantly via TCP socket programming.
Live Leaderboard: Maintains a dynamic ranking system that updates and displays scores as the quiz progresses.
Automated Processing: The system automatically checks answers and calculates scores for all connected clients.

---

## Technical Stack
Language: Python 
Networking: TCP Socket Programming 
Concurrency: Threading (to handle multiple users at once).

---

## Methodology
Connectivity: The project utilizes Python's socket library to establish communication between the server and multiple clients.
Data Flow: The server broadcasts questions to all connected clients and receives their responses through the network.
Validation: Scores are updated and checked automatically by the server script upon receiving answers.
Testing: The system was tested to ensure accurate score calculation and reliable communication between files.

---

## Future Enhancements
Adding a Graphical User Interface (GUI) for a more user-friendly experience.
Integrating a database to store quiz questions and permanent historical results.
