# README: Multi-Client Online Quiz System

## Overview
[cite_start]This project is a **Python-based online quiz system** designed using a **client-server architecture**[cite: 2, 6, 13]. [cite_start]It enables multiple participants to join a quiz session over a network simultaneously, answer questions in real-time, and view their rankings on a live leaderboard[cite: 4, 5, 11].

---

## Core Features
* [cite_start]**Multi-Client Support:** Uses **threading** to allow several users to connect and participate at once[cite: 16, 19].
* [cite_start]**Real-Time Interaction:** Instant question delivery and answer submission via **TCP socket programming**[cite: 6, 10, 20].
* [cite_start]**Dynamic Leaderboard:** Automatically calculates scores and displays player rankings during the quiz[cite: 11, 22].
* [cite_start]**Automated Evaluation:** The server checks answers and updates scores without manual intervention[cite: 15, 21].


---

## Technical Stack
* [cite_start]**Language:** Python [cite: 13, 25]
* [cite_start]**Networking:** TCP Socket Programming [cite: 6, 10]
* [cite_start]**Concurrency:** Threading (for handling multiple simultaneous clients) [cite: 16]

---

## Methodology
1.  [cite_start]**Connection:** Clients connect to the central server via a network[cite: 14, 19].
2.  [cite_start]**Quiz Flow:** The server broadcasts questions to all connected participants[cite: 14, 20].
3.  [cite_start]**Processing:** The server receives answers, validates them, and updates the shared leaderboard[cite: 15, 21, 22].
4.  [cite_start]**Testing:** The system was verified for communication stability and score accuracy[cite: 17].

---

## Future Enhancements
* [cite_start]Development of a **Graphical User Interface (GUI)** for better user experience[cite: 27].
* [cite_start]Integration of a **database** to store and manage persistent quiz results[cite: 27].
