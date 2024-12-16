import plotly.graph_objs as go
from plotly.subplots import make_subplots

class BatteryAgingVisualizer:
    @staticmethod
    def create_aging_plots(df):
        """
        Create interactive Plotly visualizations for battery aging parameters
        
        Parameters:
        -----------
        df : pd.DataFrame
            Preprocessed battery aging data
        
        Returns:
        --------
        plotly.graph_objs.Figure
            Interactive figure showing battery parameter changes
        """
        # Create subplot figure
        fig = make_subplots(rows=2, cols=2, 
                             subplot_titles=('Battery Impedance vs Cycle', 
                                             'Charge Transfer Resistance vs Cycle',
                                             'Battery Impedance by Temperature', 
                                             'Charge Transfer Resistance by Temperature'))

        # Battery Impedance vs Cycle (Scatter Plot)
        fig.add_trace(
            go.Scatter(
                x=df['Cycle'], 
                y=df['Battery_impedance'], 
                mode='markers',
                name='Battery Impedance',
                marker=dict(color=df['Cycle'], colorscale='Viridis')
            ),
            row=1, col=1
        )

        # Charge Transfer Resistance vs Cycle (Scatter Plot)
        fig.add_trace(
            go.Scatter(
                x=df['Cycle'], 
                y=df['Rct'], 
                mode='markers',
                name='Charge Transfer Resistance',
                marker=dict(color=df['Cycle'], colorscale='Plasma')
            ),
            row=1, col=2
        )

        # Battery Impedance by Temperature (Box Plot)
        fig.add_trace(
            go.Box(
                x=df['Temperature'], 
                y=df['Battery_impedance'], 
                name='Impedance Distribution'
            ),
            row=2, col=1
        )

        # Charge Transfer Resistance by Temperature (Box Plot)
        fig.add_trace(
            go.Box(
                x=df['Temperature'], 
                y=df['Rct'], 
                name='Rct Distribution'
            ),
            row=2, col=2
        )

        # Update layout for better readability
        fig.update_layout(
            title='Battery Aging Parameters Analysis',
            height=800,
            width=1200,
            showlegend=True
        )

        # Update x and y axis labels
        fig.update_xaxes(title_text='Cycle Number', row=1, col=1)
        fig.update_xaxes(title_text='Cycle Number', row=1, col=2)
        fig.update_xaxes(title_text='Temperature', row=2, col=1)
        fig.update_xaxes(title_text='Temperature', row=2, col=2)
        
        fig.update_yaxes(title_text='Battery Impedance (Ω)', row=1, col=1)
        fig.update_yaxes(title_text='Charge Transfer Resistance (Ω)', row=1, col=2)
        fig.update_yaxes(title_text='Battery Impedance (Ω)', row=2, col=1)
        fig.update_yaxes(title_text='Charge Transfer Resistance (Ω)', row=2, col=2)

        return fig
