# Multi-Client Online Quiz System with Real-Time Ranking

To run this project, you will find two primary Python scripts in this repository. You must run them in the following order:
1.  [cite_start]Run the Server file: This initializes the quiz environment and waits for connections[cite: 6, 9].
2.  [cite_start]Run the Client file: Each participant must run this script to join the quiz[cite: 9, 19]. [cite_start]You can run multiple instances of the client file for different players[cite: 16, 19].

---

## Overview
[cite_start]This project is a Python-based online quiz system built on a client-server architecture[cite: 6, 13]. [cite_start]It allows multiple users to participate in a quiz over a network, submit answers, and receive scores in real-time[cite: 4, 5].



[Image of client-server architecture diagram]


---

## Core Features
Multi-Client Support: Uses threading to allow several participants to join and play simultaneously[cite: 9, 16].
Real-Time Interaction: Delivers questions and collects answers instantly via TCP socket programming[cite: 6, 10].
Live Leaderboard: Maintains a dynamic ranking system that updates and displays scores as the quiz progresses[cite: 11, 22].
Automated Processing: The system automatically checks answers and calculates scores for all connected clients[cite: 15, 21].

---

## Technical Stack
Language: Python [cite: 13, 25]
Networking: TCP Socket Programming [cite: 6, 10]
Concurrency: Threading (to handle multiple users at once) [cite: 16]

---

## Methodology
Connectivity: The project utilizes Python's socket library to establish communication between the server and multiple clients[cite: 13, 19].
Data Flow: The server broadcasts questions to all connected clients and receives their responses through the network[cite: 14, 20].
Validation: Scores are updated and checked automatically by the server script upon receiving answers[cite: 15, 21].
Testing: The system was tested to ensure accurate score calculation and reliable communication between files[cite: 17].

---

## Future Enhancements
Adding a Graphical User Interface (GUI) for a more user-friendly experience[cite: 27].
Integrating a database to store quiz questions and permanent historical results[cite: 27].
