import numpy as np
from PIL import Image
import yaml

class ImageAdjuster:
    def __init__(self, config_path='config.yaml'):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
    
    def adjust_brightness(self, img, factor):
        """Adjust the brightness of the image"""
        img_array = np.array(img).astype(float)
        img_array = img_array + factor
        img_array = np.clip(img_array, 0, 255)
        return Image.fromarray(img_array.astype(np.uint8))

    def adjust_contrast(self, img, factor):
        """Adjust the contrast of the image"""
        img_array = np.array(img).astype(float)
        factor = (factor + 100) / 100
        img_array = (img_array - 128) * factor + 128
        img_array = np.clip(img_array, 0, 255)
        return Image.fromarray(img_array.astype(np.uint8))

    def adjust_highlights(self, img, value):
        """Adjust the highlights of the image"""
        img_array = np.array(img).astype(float)
        mask = img_array > 128
        adjustment = abs(value) / 100 * 128
        
        if value < 0:
            img_array[mask] = img_array[mask] - (mask[mask] * adjustment)
        else:
            img_array[mask] = img_array[mask] + ((255 - img_array[mask]) / 128 * adjustment)
        
        img_array = np.clip(img_array, 0, 255)
        return Image.fromarray(img_array.astype(np.uint8))

    def adjust_shadows(self, img, value):
        """Adjust the shadows of the image"""
        img_array = np.array(img).astype(float)
        mask = img_array < 128
        adjustment = abs(value) / 100 * 128
        
        if value < 0:
            img_array[mask] = img_array[mask] - (img_array[mask] / 128 * adjustment)
        else:
            img_array[mask] = img_array[mask] + (mask[mask] * adjustment)
        
        img_array = np.clip(img_array, 0, 255)
        return Image.fromarray(img_array.astype(np.uint8))

    def adjust_whites(self, img, value):
        """Adjust the whites of the image"""
        img_array = np.array(img).astype(float)
        mask = img_array > 200
        adjustment = abs(value) / 100 * 55
        
        if value < 0:
            img_array[mask] = img_array[mask] - (mask[mask] * adjustment)
        else:
            img_array[mask] = img_array[mask] + ((255 - img_array[mask]) / 55 * adjustment)
        
        img_array = np.clip(img_array, 0, 255)
        return Image.fromarray(img_array.astype(np.uint8))

    def adjust_blacks(self, img, value):
        """Adjust the blacks of the image"""
        img_array = np.array(img).astype(float)
        mask = img_array < 50
        adjustment = abs(value) / 100 * 50
        
        if value < 0:
            img_array[mask] = img_array[mask] - (img_array[mask] / 50 * adjustment)
        else:
            img_array[mask] = img_array[mask] + (mask[mask] * adjustment)
        
        img_array = np.clip(img_array, 0, 255)
        return Image.fromarray(img_array.astype(np.uint8))

    def apply_all_adjustments(self, original_img, adjustments):
        """Apply all adjustments in sequence"""
        img = original_img.copy()
        img = self.adjust_brightness(img, adjustments['brightness'])
        img = self.adjust_contrast(img, adjustments['contrast'])
        img = self.adjust_highlights(img, adjustments['highlights'])
        img = self.adjust_shadows(img, adjustments['shadows'])
        img = self.adjust_whites(img, adjustments['whites'])
        img = self.adjust_blacks(img, adjustments['blacks'])
        return img 
