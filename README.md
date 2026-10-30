# Emotion Detector - AI Web Application

A Flask-based web application that analyzes the emotional tone of text using the IBM Watson NLP EmotionPredict library. The application evaluates customer statements for five core emotions (**anger**, **disgust**, **fear**, **joy**, and **sadness**) and identifies the **dominant emotion**.

This project is the final capstone project for the course **Developing AI Applications with Python and Flask** offered by IBM on Coursera.

---

## Features

- **Embedded AI Emotion Analysis**: Integrates with the Watson NLP Embeddable AI library (`emotion_aggregated-workflow_lang_en_stock`).
- **Granular Emotion Scores**: Quantifies five emotional dimensions: `anger`, `disgust`, `fear`, `joy`, and `sadness`.
- **Dominant Emotion Identification**: Automatically isolates the emotion with the highest score.
- **Flask Web Deployment**: Serves an interactive HTML/JavaScript frontend and an API endpoint (`/emotionDetector`).
- **Robust Error Handling**: Handles empty statements, blank whitespace, and HTTP 400 bad requests by gracefully returning `Invalid text! Please try again!`.
- **Unit Testing**: Verified with Python's built-in `unittest` test suite across five benchmark statements.
- **Static Code Analysis**: 100% compliant with PEP 8 standards, achieving a perfect **10.00/10** score on Pylint across all application modules.

---

## Project Structure

```text
final_project/
├── EmotionDetection/
│   ├── __init__.py           # Exposes emotion_detector package function
│   └── emotion_detection.py  # Interacts with the Watson NLP service
├── static/
│   └── mywebscript.js        # Frontend AJAX request handling
├── templates/
│   └── index.html            # Web user interface layout
├── Coursera_Submission/      # All required submission evidence and guides
│   ├── 1_folder_structure.png
│   ├── 2a_application_creation.png
│   ├── 2b_application_output.png
│   ├── 3a_output_formatting.png
│   ├── 3b_output_formatting.png
│   ├── 4a_packaging.png
│   ├── 4b_packaging.png
│   ├── 5a_unit_testing.png
│   ├── 5b_unit_testing.png
│   ├── 6a_server.png
│   ├── 6b_deployment.png
│   ├── 7a_error_handling.png
│   ├── 7b_error_handling.png
│   ├── 8a_pylint.png
│   ├── FINAL_SUBMISSION_GUIDE.txt
│   └── versions/             # Preserved code versions for every milestone
├── server.py                 # Flask server application routing
├── test_emotion_detection.py # Automated unit test suite
├── .gitignore
├── LICENSE
└── README.md
```

---

## Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/shreyawankhade224-sketch/oaqjp-final-project-emb-ai.git final_project
   cd final_project
   ```

2. **Install Dependencies**:
   ```bash
   python -m pip install flask requests pylint
   ```

---

## Running the Application

1. **Start the Flask Server**:
   ```bash
   python server.py
   ```

2. **Access the Web Interface**:
   Open your browser and navigate to:
   ```text
   http://127.0.0.1:5000/
   ```

3. **Sample Inputs and Responses**:
   - **Input**: `"I am glad this happened"`
   - **Response**:
     ```text
     For the given statement, the system response is 'anger': 0.005, 'disgust': 0.002, 'fear': 0.009, 'joy': 0.968 and 'sadness': 0.015. The dominant emotion is joy.
     ```
   - **Blank Input**: `""`
   - **Response**:
     ```text
     Invalid text! Please try again!
     ```

---

## Running Unit Tests

Run the test suite using Python's `unittest` runner:

```bash
python -m unittest test_emotion_detection.py
```

Expected output:
```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.852s

OK
```

---

## Static Code Analysis (Pylint)

To verify PEP 8 compliance and code quality, run Pylint:

```bash
pylint server.py
pylint EmotionDetection/emotion_detection.py
pylint test_emotion_detection.py
```

All source files are rated at **10.00/10**.

---

## Author

- **GitHub**: [@shreyawankhade224-sketch](https://github.com/shreyawankhade224-sketch)
- **Repository**: [oaqjp-final-project-emb-ai](https://github.com/shreyawankhade224-sketch/oaqjp-final-project-emb-ai)
