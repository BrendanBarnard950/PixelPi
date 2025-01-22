# Running a PixelPi: Step-by-Step Guide

This guide will help you set up and run PixelPi.
THIS IS A TEST PROJECT. IT FEATURES VERY LITTLE SECURITY MEASURES AND MOST DJANGO DEFAULT SETTINGS HAVE BEEN LEFT UNCHANGED.
Not for production use, be careful, don't sue me, all that good stuff

---

## Prerequisites

- **Linux or Windows Subsystem for Linux (WSL):** If you're using Windows, ensure you have WSL installed and set up.
- **Git:** You’ll need Git to fetch the project from a repository.
- **Python 3.12.3 installer:** Make sure Python 3.12.3 is downloaded or accessible.

---

## Instructions

### 1. Open a Terminal
- On Linux or Mac, open your terminal.
- On Windows, open a WSL terminal.
- - Instructions on how to enable and use WSL can be found [here]([www.google.com](https://learn.microsoft.com/en-us/windows/wsl/install))

---

### 2. Install Git (if not already installed)
1. Check if Git is installed:
   ```bash
   git --version
   ```
   If it returns a version number, Git is already installed.

2. If Git is not installed, install it using the following commands:
   - On Ubuntu/Debian-based systems:
     ```bash
     sudo apt update
     sudo apt install git
     ```

3. Verify the installation:
   ```bash
   git --version
   ```

---

### 3. Clone the Project Repository
1. Navigate to the folder where you want to download the project. For example:
   ```bash
   cd /preferred/project/path
   ```
2. Clone the repository:
   ```bash
   git clone https://github.com/BrendanBarnard950/PixelPi.git
   ```

3. Navigate into the project folder:
   ```bash
   cd PixelPi
   ```

---

### 4. Create a Virtual Environment
1. In the project folder, create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
2. Activate the virtual environment:
   - On Linux or WSL:
     ```bash
     source venv/bin/activate
     ```
   - You’ll see `(venv)` appear at the beginning of your terminal prompt, indicating the environment is active.

---

### 5. Install Python 3.12.3
If Python 3.12.3 isn’t already installed:
1. Download Python 3.12.3 using your package manager or download it from the [official Python website](https://www.python.org/downloads/).
2. Ensure it’s installed in your virtual environment by running:
   ```bash
   python --version
   ```
   You should see something like `Python 3.12.3`.

---

### 6. Install Project Requirements
1. Locate the requirements document. From the project root, it should be at:
   ```bash
   aux/pip/requirements.txt
   ```
2. Use `pip` to install the requirements:
   ```bash
   pip install -r aux/pip/requirements.txt
   ```

---

### 7. Run the PixelPi
Now that everything is set up:
1. Run the usual Django commands to get started.
   - To apply migrations:
     ```bash
     python manage.py migrate
     ```
   - To start the development server:
     ```bash
     python manage.py runserver
     ```
2. Access PixelPi by visiting the link provided (usually `http://127.0.0.1:8000`) in your browser.

---

### 8. Using PixelPi...

The home page should show you time image store. It will appear similar to a 'Gallery' app on a phone. I'm pre-loading the repository with some random images off my hard drive. The very blurry gradient-ish ones are to test different tiny pixel dimensions.

#### 1. Uploading a new picture
1. At the top of the browser window click the **Upload Image** link.
2. Click on the **Choose File** widget and select a image file.
3. Click on the **Upload** button to proceed, or the **Back to Image List** button to go back to the Gallery.

#### 2. Viewing a full picture
1. Navigate to the home page.
2. Click on the **View Full** button, or directly on the image.
3. To exit the full image view, click the **Back** butto at the top left.

#### 3. Seeing the hex value of the center pixels of an image
1. On the image cards on the homepage, check the bottom left of each card for a hex code and a sample of the colour.
2. In the full image view, check the very top of the page.

#### 4. Deleting an image
1. On the homepage, click the red **Delete** button on the image you want to delete.
---

This document is brought to you by ChatGPT's complete inability to generate a Markdown document with code blocks in it without everything falling apart. Dont take shortcuts, kids, they usually just take longer than a 10 minute video to refresh yourself on Markdown formatting.
