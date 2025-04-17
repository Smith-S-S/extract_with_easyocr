import yaml
import streamlit as st

class PresetManager:
    def __init__(self, config_path='config.yaml'):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
    
    def get_preset_names(self):
        """Get all available preset names"""
        return list(self.config['presets'].keys())
    
    def get_preset_values(self, preset_name):
        """Get adjustment values for a specific preset"""
        return self.config['presets'].get(preset_name, {})
    
    def apply_preset(self, preset_name):
        """Apply preset values to session state"""
        preset_values = self.get_preset_values(preset_name)
        for key, value in preset_values.items():
            st.session_state[key] = value 