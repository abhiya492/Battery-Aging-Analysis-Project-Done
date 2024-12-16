# main.py  

import os  
import sys  
import plotly.io as pio  

# Add the project root to the Python path  
project_root = os.path.dirname(os.path.abspath(__file__))  
sys.path.insert(0, project_root)  

from src.data_loader import BatteryDataLoader  
from src.data_preprocessing import BatteryDataPreprocessor  
from src.visualization import BatteryAgingVisualizer  

def main():  
    # Define paths  
    data_dir = 'data/cleaned_dataset/data'  
    results_dir = 'results/plots'  
    
    # Create results directory if it doesn't exist  
    os.makedirs(results_dir, exist_ok=True)  

    # Load data  
    data_loader = BatteryDataLoader(data_dir)  
    
    try:  
        # Combine all datasets  
        combined_data = data_loader.combine_datasets()  
        print("Combined DataFrame columns:", combined_data.columns.tolist())  # Debugging line  
        
        # Preprocess data  
        preprocessor = BatteryDataPreprocessor()  
        cleaned_data = preprocessor.clean_data(combined_data)  
        print("Cleaned DataFrame columns:", cleaned_data.columns.tolist())  # Debugging line  
        
        if cleaned_data is not None:  
            # Create visualizations  
            visualizer = BatteryAgingVisualizer()  
            fig = visualizer.create_aging_plots(cleaned_data)  
            
            # Save interactive plot  
            pio.write_html(fig, file=os.path.join(results_dir, 'battery_aging_analysis.html'))  
            
            # Optional: Save static image  
            pio.write_image(fig, os.path.join(results_dir, 'battery_aging_analysis.png'))  
            
            print("Analysis complete. Check results in the 'results/plots' directory.")  
        else:  
            print("Data preprocessing failed.")  
    
    except Exception as e:  
        print(f"An error occurred: {e}")  

if __name__ == "__main__":  
    main()