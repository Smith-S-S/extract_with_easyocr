import streamlit as st
import yaml
from PIL import Image
import io

class UIComponents:
    def __init__(self, config_path='config.yaml'):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
    
    def setup_page(self):
        """Setup the Streamlit page configuration"""
        st.set_page_config(
            page_title=self.config['app_config']['page_title'],
            layout=self.config['app_config']['layout']
        )
        st.title("Image Light Adjustment Tool")
    
    def create_sidebar(self, preset_manager):
        """Create the sidebar with upload and controls"""
        with st.sidebar:
            st.header("Upload Image")
            uploaded_file = st.file_uploader(
                "Choose an image...",
                type=self.config['app_config']['allowed_file_types']
            )
            
            if uploaded_file is not None:
                if 'original_image' not in st.session_state:
                    st.session_state['original_image'] = Image.open(uploaded_file).convert('RGB')
                
                self._create_preset_controls(preset_manager)
                self._create_adjustment_controls()
    
    def _create_preset_controls(self, preset_manager):
        """Create preset selection controls"""
        st.subheader("Meter Type Presets")
        preset_options = [name.replace('_', ' ').title() for name in preset_manager.get_preset_names()]
        selected_preset = st.selectbox("Select meter type:", preset_options)
        
        if st.button("Apply Preset"):
            preset_manager.apply_preset(selected_preset.lower().replace(' ', '_'))
            st.rerun()
    
    def _create_adjustment_controls(self):
        """Create adjustment sliders"""
        st.subheader("Adjustment Controls")
        st.markdown("☀️ **Light**")
        
        adjustments = self.config['image_adjustments']
        for adjustment, params in adjustments.items():
            if adjustment not in st.session_state:
                st.session_state[adjustment] = params['default']
            
            st.slider(
                adjustment.title(),
                params['min'],
                params['max'],
                st.session_state[adjustment],
                key=f'{adjustment}_slider',
                on_change=lambda adj=adjustment: setattr(st.session_state, adj, st.session_state[f'{adj}_slider'])
            )
        
        if st.button("Reset Adjustments"):
            for adjustment in adjustments:
                st.session_state[adjustment] = adjustments[adjustment]['default']
            st.rerun()
    
    def display_image(self, adjusted_img):
        """Display the adjusted image and download button"""
        st.image(adjusted_img, caption="Adjusted Image", use_column_width=True)
        
        buf = io.BytesIO()
        adjusted_img.save(buf, format="PNG")
        byte_im = buf.getvalue()
        
        st.download_button(
            label="Download Adjusted Image",
            data=byte_im,
            file_name="adjusted_image.png",
            mime="image/png"
        )
    
    def display_ocr_results(self, ocr_results):
        """Display OCR results in a table"""
        if ocr_results is not None:
            st.subheader("Extracted Text")
            st.dataframe(ocr_results, use_container_width=True)
            
            # Option to download results as CSV
            csv = ocr_results.to_csv(index=False)
            st.download_button(
                label="Download Text Results (CSV)",
                data=csv,
                file_name="extracted_text.csv",
                mime="text/csv"
            )
    
    def display_instructions(self):
        """Display instructions when no image is uploaded"""
        st.info("👈 Please upload an image using the sidebar to get started.")
        st.write("""
        This tool allows you to adjust various light properties of your image:
        
        - **Brightness**: Overall lightness of the image
        - **Contrast**: Difference between light and dark areas
        - **Highlights**: Adjustment for the brightest areas
        - **Shadows**: Adjustment for the darkest areas
        - **Whites**: Fine-tuning for white areas
        - **Blacks**: Fine-tuning for black areas
        
        You can also select meter type presets for:
        - Digital Meter
        - Analog Meter
        - Gauge
        
        After adjusting the image, you can extract text from it using the "Extract Text" button.
        """) 