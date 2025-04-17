import yaml
import easyocr
import numpy as np
import pandas as pd
import re

class OCRProcessor:
    def __init__(self, config_path='config.yaml'):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        
        self.languages = self.config['ocr_config'].get('languages', ['en'])
        self.min_confidence = self.config['ocr_config'].get('min_confidence', 0.0)
        self.number_only = self.config['ocr_config'].get('number_only', False)
        
        self.reader = easyocr.Reader(self.languages)
    
    def extract_text(self, image):
        """Extract text from image using EasyOCR with filters."""
        img_array = np.array(image)
        result = self.reader.readtext(img_array)
        
        texts = []
        confidences = []
        
        for detection in result:
            text = detection[1]
            confidence = detection[2]
            
            # Skip if confidence is too low
            if confidence < self.min_confidence:
                continue
            
            # Skip if number_only is True and text doesn't contain digits
            if self.number_only:
                numbers = re.findall(r'\d+', text)
                if not numbers:
                    continue
                text = ' '.join(numbers)  # Or ''.join(numbers) for one long string
            
            texts.append(text)
            confidences.append(f"{confidence:.2f}")
        
        df = pd.DataFrame({
            'Text Extracted': texts,
            'Confidence Score': confidences
        })
        return df
