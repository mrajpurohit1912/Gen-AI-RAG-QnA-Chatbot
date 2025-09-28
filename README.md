# RAG Chatbot for ABC EdTech Platform

This project is a **Retrieval-Augmented Generation (RAG) chatbot** built for an EdTech platform. It allows users to ask questions related to courses, content, and services, and provides intelligent responses using a backend Flask API. The frontend is built using **React**, creating a modern, interactive web interface.  

---

## 🗂 Project Structure

```bash
rag-chatbot/
│
├── backend/               # Flask server
│   ├── main.py            # Entry point for backend API
│   ├── requirements.txt   # Python dependencies
│   └── ...                # Other backend files
│
├── frontend/              # React frontend
│   ├── package.json       # NPM configuration
│   ├── src/
│   │   ├── App.jsx        # Main App component
│   │   ├── components/    # React components (Button, SearchBar, etc.)
│   │   └── App.css        # Global styles
│   └── ...                # Other frontend files
│
└── README.md              # Project documentation
```

## ⚡ Features

```bash
Interactive Q&A interface: Users can type questions in a search bar.

Backend API (Flask): Receives questions via POST requests and returns answers.

RAG (Retrieval-Augmented Generation): Combines a knowledge base with AI responses.

Real-time response display: Answers appear on the page without pop-ups.

Theming support: Light/Dark theme support is integrated.
```



## 🛠 Tech Stack

```bash
Frontend: React, JavaScript, HTML, CSS

Backend: Python, Flask, Flask-CORS

Communication: REST API (fetch POST requests)
```

## 1. Backend Setup

Navigate to the backend folder:
```bash
cd backend
```

Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate   
venv\Scripts\activate      
```


Install dependencies:
```bash
pip install -r requirements.txt  or
uv pip install -r requirements.txt 
```

Run the Flask server:
```bash
python main.py
```

## 2. Frontend Setup

Navigate to the frontend folder:
```bash
cd frontend
```

Install dependencies:
```bash
npm install
```

Start the frontend development server:
```bash
npm run dev
```

Run the Flask server:
```bash
python main.py
```


📡 Usage

Open the frontend URL in your browser.

Type a question in the input box.

Click Submit.

The answer from the backend will be displayed below the input.