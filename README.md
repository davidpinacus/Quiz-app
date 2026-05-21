# 🧠 Quizzler App (Python - Tkinter + API)

An interactive True/False quiz application built with Python Tkinter.
Questions are fetched dynamically from the Open Trivia Database API for a fresh quiz experience every time.

This App has a Beautiful colour palette

---

## 🎯 Features

* 🌐 Fetches live quiz questions from API
* 🖥️ Modern GUI using Tkinter
* ✅ True / False answer system
* 📊 Real-time score tracking
* 🎨 Visual feedback for correct & wrong answers
* 🔄 Dynamic question loading

```

### Files Overview

* **main.py** → Starts the application and creates quiz objects 
* **data.py** → Fetches questions from Trivia API 
* **quiz_brain.py** → Handles quiz logic and score system 
* **question_model.py** → Defines Question object model 
* **ui.py** → GUI design and button interactions 

---

Install dependency:

```id="j3o9ka"
pip install requests
```

---

## 🌐 API Used

This project uses the **Open Trivia Database API** to fetch quiz questions dynamically.

API Endpoint:

```id="m8w2pa"
https://opentdb.com/api.php
```

---

## 🎮 How It Works

* Questions are downloaded from the Trivia API
* User answers using:

  * ✅ True
  * ❌ False
* App checks answers instantly
* Score updates in real-time
* Background color changes:

  * 🟢 Green → Correct
  * 🔴 Red → Wrong

