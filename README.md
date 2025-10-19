# 🪨 Rock ✋ Paper ✌️ Scissors – Streamlit Game

An interactive and visually engaging **Rock-Paper-Scissors** game built using **Python** and **Streamlit**.  
Play against the computer, track your score, and enjoy the smooth UI — all in your browser!

---

## 🚀 Features

- 🎮 Interactive gameplay with buttons and dropdowns  
- 🧠 Smart game logic based on modular arithmetic  
- 🏆 Real-time score tracking using `st.session_state`  
- 🔄 Reset option to start a fresh match anytime  
- 💻 Runs entirely in your browser — no console needed  
- 🌈 Clean and modern Streamlit interface  

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| Frontend UI | Streamlit |
| Backend Logic | Python |
| Randomization | Python `random` module |
| Styling | Streamlit widgets and emojis |

---

## 📁 Project Structure
```
rock-paper-scissors/
│
├── app.py # Main Streamlit app
├── requirements.txt # List of dependencies
└── README.md # Project documentation
```

---

## ⚙️ Installation & Setup

Follow these steps to run the game locally:

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/rock-paper-scissors.git
cd rock-paper-scissors

# create vertual environment

python -m venv venv
venv\Scripts\activate      # for Windows
# or
source venv/bin/activate   # for macOS/Linux

# install dependencies

pip install -r requirements.txt

# Run the web app

streamlit run app.py
```


### 🕹️ How to Play

Choose your move from the dropdown — Rock, Paper, or Scissor.

Click 🎮 Play to challenge the computer.

See who wins each round — your score updates automatically.

Click 🔄 Reset Game to start fresh anytime.

### 🧠 Game Logic

Rock beats Scissor 🪨✌️

Paper beats Rock ✋🪨

Scissor beats Paper ✌️✋

If both choices match → Draw 🤝

Uses numeric mapping internally:

rock = -1, paper = 0, scissor = 1


and checks (computer - user) difference to determine the result.

### 🌐 Deployment

You can easily deploy this game online using:

Streamlit Cloud → https://streamlit.io/cloud

Render, Hugging Face Spaces, or Heroku

Once deployed, share your game link for others to play!

🧑‍💻 Author

Anas Fareedi
B.Tech in AI & ML | Python Developer | ML & Data Enthusiast
📫 LinkedIn
 • GitHub

📜 License

This project is open-source under the MIT License

"Simple games build strong logic — one project at a time.”

<img width="951" height="823" alt="image" src="https://github.com/user-attachments/assets/4eb834f0-8ad7-4be0-baa7-894becfb13ec" />


