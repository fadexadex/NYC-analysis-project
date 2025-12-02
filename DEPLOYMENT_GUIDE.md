# Deployment Guide for PythonAnywhere

This guide walks you through deploying your NYC Yellow Taxi Analytics Dashboard to PythonAnywhere.

## Prerequisites

1.  **GitHub Account**: You need your code hosted on GitHub.
2.  **PythonAnywhere Account**: Sign up for a free account at [pythonanywhere.com](https://www.pythonanywhere.com/).
3.  **MongoDB Atlas**: Ensure your MongoDB cluster allows access from anywhere (0.0.0.0/0) or specifically from PythonAnywhere's IP addresses.

---

## Step 1: Prepare Your Code

1.  **Update `dashboard.py`**:
    PythonAnywhere requires the Dash app instance to be exposed as `application` (or you need to configure the WSGI file correctly).
    
    Ensure your `dashboard.py` exposes the server object:
    ```python
    # In dashboard.py, add this line after initializing app
    server = app.server
    ```

2.  **Push to GitHub**:
    Make sure your latest code, including `requirements.txt`, is pushed to a GitHub repository.

---

## Step 2: Set Up PythonAnywhere

1.  **Open a Bash Console**:
    Log in to PythonAnywhere, go to the **Consoles** tab, and start a **Bash** console.

2.  **Clone Your Repository**:
    Run the following command (replace with your repo URL):
    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
    ```

3.  **Create a Virtual Environment**:
    Navigate to your project folder and create a virtual environment:
    ```bash
    cd YOUR_REPO_NAME
    mkvirtualenv --python=/usr/bin/python3.10 myenv
    ```
    *(Note: `mkvirtualenv` automatically activates the environment)*

4.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

---

## Step 3: Configure the Web App

1.  **Create Web App**:
    *   Go to the **Web** tab.
    *   Click **Add a new web app**.
    *   Click **Next**.
    *   Select **Flask** (Dash is built on Flask).
    *   Select **Python 3.10** (or whichever version you used).
    *   **Path**: You can leave the default path for now (we will change it later).

2.  **Configure WSGI File**:
    *   On the **Web** tab, scroll down to the **Code** section.
    *   Click the link to edit the **WSGI configuration file** (e.g., `/var/www/yourusername_pythonanywhere_com_wsgi.py`).
    *   Delete everything in the file and replace it with this:

    ```python
    import sys
    import os

    # Add your project directory to the sys.path
    project_home = '/home/YOUR_USERNAME/YOUR_REPO_NAME'
    if project_home not in sys.path:
        sys.path = [project_home] + sys.path

    # Import the Dash app
    # 'dashboard' is the name of your python file (dashboard.py)
    # 'app' is the name of the Dash instance in that file
    from dashboard import app
    
    # PythonAnywhere looks for an object called 'application'
    application = app.server
    ```
    *   **Important**: Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual details.
    *   Save the file.

3.  **Set Virtual Environment**:
    *   Back on the **Web** tab, scroll to the **Virtualenv** section.
    *   Enter the path to your virtual environment:
        `/home/YOUR_USERNAME/.virtualenvs/myenv`

---

## Step 4: Finalize and Reload

1.  **Environment Variables**:
    Since we are using `python-dotenv`, you need to create a `.env` file in your project directory on PythonAnywhere.
    *   In the **Files** tab on PythonAnywhere, navigate to your project folder (`/home/YOUR_USERNAME/YOUR_REPO_NAME`).
    *   Create a new file named `.env`.
    *   Add your environment variables:
        ```
        MONGO_URI=your_mongodb_connection_string
        DB_NAME=yellow_taxi_stats
        ```
    *   Save the file.

2.  **Reload**:
    *   Go to the top of the **Web** tab.
    *   Click the big green **Reload** button.

3.  **Visit Your Site**:
    *   Click the link to your site (e.g., `https://yourusername.pythonanywhere.com`).

---

## Troubleshooting

*   **Error Logs**: If the site shows an error, check the **Error log** link on the **Web** tab. It usually tells you exactly what went wrong (e.g., missing module, wrong path).
*   **MongoDB Connection**: If data isn't loading, ensure your MongoDB Atlas Network Access whitelist includes `0.0.0.0/0` (Allow Access from Anywhere). PythonAnywhere IPs change, so whitelisting specific IPs is difficult on the free tier.