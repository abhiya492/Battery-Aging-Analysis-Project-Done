
import plotly.graph_objects as go  

class BatteryAgingVisualizer:  
    def create_aging_plots(self, cleaned_data):  
        fig = go.Figure()  

        # Voltage vs Cycle  
        fig.add_trace(go.Scatter(  
            x=cleaned_data['Cycle'],   
            y=cleaned_data['Voltage_measured'],   
            mode='lines',   
            name='Voltage Measured'  
        ))  

        # Current vs Cycle  
        fig.add_trace(go.Scatter(  
            x=cleaned_data['Cycle'],   
            y=cleaned_data['Current_measured'],   
            mode='lines',   
            name='Current Measured'  
        ))  

        # Temperature vs Cycle if column exists  
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

        # Optionally add more traces based on available data...  

        fig.update_layout(  
            title='Battery Aging Analysis',   
            xaxis_title='Cycle',   
            yaxis_title='Values'  
        )  
        return fig