# Instagram Reach Analysis

## Project Overview
The "Instagram Reach Analysis" project aims to predict the reach of Instagram posts based on user input parameters. This tool assists content creators and social media strategists in understanding and optimizing their content's performance on Instagram.

### Key Factors Considered:
- **Followers**: The total number of followers an account has.
- **Caption Length**: The number of characters in the post's caption.
- **Hashtags Length**: The number of hashtags used in the post.

By inputting these parameters, users can predict the potential reach of their posts, enabling them to tailor their content strategies effectively.

## Features
- **User-Friendly Interface**: Clean and responsive web interface for easy input and prediction.
- **Real-Time Predictions**: Immediate computation of reach predictions.
- **Data-Driven Insights**: Helps users make informed decisions to enhance Instagram engagement.

## Technologies Used
- **Backend**: Flask - Lightweight web application framework in Python.
- **Frontend**: HTML, CSS - For structuring and styling the interface.
- **Machine Learning**: Scikit-learn - For building and deploying the prediction model.

## Getting Started

### Step 1: Clone the Repository
```bash
git clone https://github.com/abhay-2108/Instagram-Reach-Analysis.git
```

### Step 2: Navigate to the Project Directory
```bash
cd Instagram-Reach-Analysis
```

### Step 3: Install Dependencies
Ensure you have Python installed. Then, install the required packages:
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Access the Application
Open your web browser and navigate to `http://127.0.0.1:5000/` to use the Instagram Reach Predictor.

## Usage
- Enter the number of followers, caption length, and hashtags length into the respective fields.
- Click the "Predict" button to see the estimated reach of your Instagram post.
