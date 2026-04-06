import socket
import threading
import time

HOST = "0.0.0.0"
PORT = 5000

scores = {}
attempted_ips = set()
clients = []
lock = threading.Lock()

questions = [
    ("2 + 2 = ?", {"A":"3","B":"4","C":"5","D":"6"}, "B"),
    ("Largest planet?", {"A":"Earth","B":"Mars","C":"Jupiter","D":"Venus"}, "C"),
    ("Capital of India?", {"A":"Delhi","B":"Mumbai","C":"Chennai","D":"Kolkata"}, "A"),
    ("Python is which type?", {"A":"Low-level","B":"High-level","C":"Assembly","D":"Machine"}, "B"),
    ("Which connects networks?", {"A":"Router","B":"Mouse","C":"Keyboard","D":"Monitor"}, "A")
]

def generate_leaderboard():
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    table = "\n===== LEADERBOARD =====\n"
    table += "Rank   Name       Score\n"
    table += "-----------------------\n"

    rank = 1
    for name, score in sorted_scores:
        table += f"{rank}      {name}      {score}\n"
        rank += 1

    return table


def broadcast_leaderboard():
    leaderboard = generate_leaderboard()

    with lock:
        for c in clients:
            try:
                c.sendall(leaderboard.encode())
            except:
                pass


def run_quiz(conn, name):
    score = 0

    conn.sendall("Quiz started!\n".encode())

    for q, options, answer in questions:

        question = "\n========================\n"
        question += "QUESTION\n"
        question += f"{q}\n"

        for k, v in options.items():
            question += f"{k}) {v}\n"

        question += "You have 20 seconds\n"
        question += "========================\n"

        conn.sendall(question.encode())

        start_time = time.time()
        TIME_LIMIT = 20
        answered = False

        while True:
            remaining = TIME_LIMIT - (time.time() - start_time)

            if remaining <= 0:
                conn.sendall("Time is up!\n".encode())
                break

            try:
                conn.settimeout(remaining)
                ans = conn.recv(1024).decode().strip().upper()

                if answered:
                    continue

                if ans not in ["A", "B", "C", "D"]:
                    conn.sendall("Invalid option! Enter A/B/C/D\n".encode())
                    continue

                answered = True

                if ans == answer:
                    conn.sendall("Correct!\n".encode())
                    score += 1
                else:
                    conn.sendall("Wrong!\n".encode())

                break

            except:
                conn.sendall("Time is up!\n".encode())
                break

        # clear buffer
        try:
            conn.settimeout(0.1)
            while conn.recv(1024):
                pass
        except:
            pass

        conn.settimeout(None)

    with lock:
        scores[name] = score

    conn.sendall(f"\nQuiz Finished! Your score: {score}\n".encode())


    broadcast_leaderboard()

   
    while True:
        try:
            time.sleep(5)
        except:
            break


def handle_client(conn, addr):
    ip = addr[0]

    with lock:
        if ip in attempted_ips:
            conn.sendall("You already attempted the quiz.\n".encode())
            conn.close()
            return

        attempted_ips.add(ip)
        clients.append(conn)

    name = conn.recv(1024).decode().strip()

    print(f"{name} joined from {ip}")

    threading.Thread(target=run_quiz, args=(conn, name)).start()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("Server running... waiting for clients (5 minutes)\n")

    start_time = time.time()
    WAIT_TIME = 300

    while time.time() - start_time < WAIT_TIME:
        try:
            server.settimeout(1)
            conn, addr = server.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()
        except:
            pass

    print("5 minutes over. Server stopped accepting new clients.")


start_server()
