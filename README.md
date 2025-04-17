# ThermoTune - Analog Pressure Gauge Reader

ThermoTune is a computer vision application that automatically reads analog pressure gauges using various image processing techniques. The application provides a user-friendly interface for image adjustments and text extraction.

## Features

- Image preprocessing and enhancement
- Multiple pressure reading techniques
- Real-time image adjustments
- OCR text extraction
- User-friendly interface

## Installation

### Method 1: Using Virtual Environment (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/Smith-S-S/extract_with_easyocr.git
cd extract_with_easyocr
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Method 2: Global Installation

1. Clone the repository:
```bash
git clone https://github.com/Smith-S-S/extract_with_easyocr.git
cd extract_with_easyocr
```

2. Install dependencies globally:
```bash
pip install -r requirements.txt
```

## Project Structure

```
extract_with_easyocr/
├── app.py                 # Main application file
├── config.yaml            # Configuration file
├── requirements.txt       # Project dependencies
├── data/                  # Data directory
├── essentials/            # Core functionality modules
│   ├── image_adjustments.py
│   ├── ocr_processor.py
│   ├── presets.py
│   └── ui_components.py
├── research/              # Research and development
└── documentation/         # Project documentation
```

## Code Structure

![Project Structure]![diagram](https://github.com/user-attachments/assets/d888e22b-db6f-448f-9c84-915d2c3bfffe)


## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Upload an image of a pressure gauge
3. Adjust image parameters as needed
4. Click "Extract Text" to perform OCR

## Dependencies

- streamlit==1.32.0
- Pillow==10.2.0
- numpy==1.26.4
- PyYAML==6.0.1
- pandas==2.2.1
- easyocr==1.7.1
- opencv-python==4.9.0.80


This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- EasyOCR for text recognition
- Streamlit for the web interface
- OpenCV for image processing 
