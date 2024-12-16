import pandas as pd
import numpy as np

class BatteryDataPreprocessor:
    @staticmethod
    def clean_data(df):
        """
        Clean and preprocess battery aging data
        
        Parameters:
        -----------
        df : pd.DataFrame
            Input DataFrame
        
        Returns:
        --------
        pd.DataFrame
            Cleaned DataFrame
        """
        # Remove rows with missing critical values
        critical_columns = ['Cycle', 'Temperature', 'Battery_impedance', 'Rct']
        
        # Check if all critical columns exist
        missing_columns = [col for col in critical_columns if col not in df.columns]
        if missing_columns:
            print(f"Warning: Missing columns {missing_columns}. Available columns: {df.columns}")
            return None
        
        # Clean the data
        cleaned_df = df.dropna(subset=critical_columns).copy()
        
        # Convert to numeric, coerce errors to NaN
        for col in critical_columns:
            cleaned_df[col] = pd.to_numeric(cleaned_df[col], errors='coerce')
        
        # Remove any remaining rows with NaN after conversion
        cleaned_df.dropna(subset=critical_columns, inplace=True)
        
        return cleaned_df