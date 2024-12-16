import os
import pandas as pd
import numpy as np

class BatteryDataLoader:
    def __init__(self, data_dir):
        """
        Initialize data loader for battery aging datasets
        
        Parameters:
        -----------
        data_dir : str
            Path to directory containing CSV files
        """
        self.data_dir = data_dir
        self.csv_files = self._get_csv_files()

    def _get_csv_files(self):
        """
        Get list of CSV files in the data directory
        
        Returns:
        --------
        list
            List of full paths to CSV files
        """
        return [
            os.path.join(self.data_dir, f) 
            for f in os.listdir(self.data_dir) 
            if f.endswith('.csv')
        ]

    def load_single_file(self, file_path):
        """
        Load a single CSV file
        
        Parameters:
        -----------
        file_path : str
            Full path to the CSV file
        
        Returns:
        --------
        pd.DataFrame
            Loaded DataFrame
        """
        try:
            df = pd.read_csv(file_path)
            # Add filename as a column for tracking
            df['source_file'] = os.path.basename(file_path)
            return df
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            return None

    def load_all_files(self):
        """
        Load all CSV files in the directory
        
        Returns:
        --------
        list
            List of DataFrames
        """
        return [
            self.load_single_file(file_path) 
            for file_path in self.csv_files
        ]

    def combine_datasets(self):
        """
        Combine all loaded datasets
        
        Returns:
        --------
        pd.DataFrame
            Combined DataFrame
        """
        dataframes = [df for df in self.load_all_files() if df is not None]
        
        if not dataframes:
            raise ValueError("No valid datasets found")
        
        return pd.concat(dataframes, ignore_index=True)