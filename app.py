import streamlit as st
from essentials.image_adjustments import ImageAdjuster
from essentials.presets import PresetManager
from essentials.ui_components import UIComponents
from essentials.ocr_processor import OCRProcessor

def main():
    # Initialize components
    ui = UIComponents()
    image_adjuster = ImageAdjuster()
    preset_manager = PresetManager()
    ocr_processor = OCRProcessor()
    
    # Setup page
    ui.setup_page()
    
    # Create sidebar
    ui.create_sidebar(preset_manager)
    
    # Main content area
    if 'original_image' in st.session_state:
        # Get current adjustments from session state
        adjustments = {
            'brightness': st.session_state.get('brightness', 0),
            'contrast': st.session_state.get('contrast', 0),
            'highlights': st.session_state.get('highlights', 0),
            'shadows': st.session_state.get('shadows', 0),
            'whites': st.session_state.get('whites', 0),
            'blacks': st.session_state.get('blacks', 0)
        }
        
        # Apply adjustments and display image
        adjusted_img = image_adjuster.apply_all_adjustments(
            st.session_state['original_image'],
            adjustments
        )
        ui.display_image(adjusted_img)
        
        # Extract Text button
        if st.button("Extract Text"):
            with st.spinner("Extracting text from image..."):
                try:
                    st.session_state['ocr_results'] = ocr_processor.extract_text(adjusted_img)
                except Exception as e:
                    st.error(f"Error extracting text: {e}")
        
        # Display OCR results if available
        ui.display_ocr_results(st.session_state.get('ocr_results'))
    else:
        ui.display_instructions()

if __name__ == "__main__":
    main() 