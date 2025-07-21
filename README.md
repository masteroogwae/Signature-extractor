# E-Signature Extractor

A modern Flask app to extract handwritten signatures from images.

Upload a document, preview the extracted signature with a transparent background, and download it instantly.

## Features
- Upload scanned documents or photos (JPG, PNG)
- Automatic signature detection and extraction
- Transparent background for easy reuse
- Modern, blue-themed UI
- Preview and download the extracted signature

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
   cd YOUR-REPO
   ```
2. Install dependencies:
   ```bash
   pip install flask opencv-python numpy
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Usage
- Click "Upload & Extract" to select and upload an image.
- View the extracted signature preview with a transparent background.
- Download the extracted signature as a PNG file.

--- 