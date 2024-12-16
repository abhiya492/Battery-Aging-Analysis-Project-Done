
import plotly.graph_objects as go  

class BatteryAgingVisualizer:  
    def create_aging_plots(self, cleaned_data):  
        fig = go.Figure()  

        # Voltage vs Cycle  
        if 'Voltage_measured' in cleaned_data.columns:  
            fig.add_trace(go.Scatter(  
                x=cleaned_data['Cycle'],   
                y=cleaned_data['Voltage_measured'],   
                mode='lines',   
                name='Voltage Measured'  
            ))  
        else:  
            print("Warning: 'Voltage_measured' column is missing.")  

        # Current vs Cycle  
        if 'Current_measured' in cleaned_data.columns:  
            fig.add_trace(go.Scatter(  
                x=cleaned_data['Cycle'],   
                y=cleaned_data['Current_measured'],   
                mode='lines',   
                name='Current Measured'  
            ))  
        else:  
            print("Warning: 'Current_measured' column is missing.")  

        # Temperature vs Cycle if the column exists  
        if 'Temperature' in cleaned_data.columns:  
            fig.add_trace(go.Scatter(  
                x=cleaned_data['Cycle'],   
                y=cleaned_data['Temperature'],   
                mode='lines',   
                name='Temperature'  
            ))  

        # Charge Transfer Resistance vs Cycle if Rct is available  
        if 'Rct' in cleaned_data.columns and cleaned_data['Rct'].notnull().any():  
            fig.add_trace(go.Scatter(  
                x=cleaned_data['Cycle'],   
                y=cleaned_data['Rct'],   
                mode='lines',   
                name='Charge Transfer Resistance'  
            ))  
        else:  
            print("Warning: 'Rct' column is not available for plotting.")  

        # Update layout  
        fig.update_layout(  
            title='Battery Aging Analysis',   
            xaxis_title='Cycle',   
            yaxis_title='Values'  
        )  
        return fig