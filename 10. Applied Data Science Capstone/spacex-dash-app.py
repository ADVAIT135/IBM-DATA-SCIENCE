# Import required libraries
import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the SpaceX data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Prepare dropdown options (include "ALL")
launch_sites = sorted(spacex_df['Launch Site'].unique())
dropdown_options = [{'label': 'All Sites', 'value': 'ALL'}] + [
    {'label': site, 'value': site} for site in launch_sites
]

# Create an app layout
app.layout = html.Div(children=[
    html.H1(
        'SpaceX Launch Records Dashboard',
        style={'textAlign': 'center', 'color': '#503D36', 'fontSize': 40}
    ),

    # TASK 1: Launch Site dropdown
    dcc.Dropdown(
        id='site-dropdown',
        options=dropdown_options,
        value='ALL',
        placeholder='Select a Launch Site',
        clearable=False
    ),
    html.Br(),

    # TASK 2: Pie chart
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),

    # TASK 3: Payload range slider
    dcc.RangeSlider(
        id='payload-slider',
        min=int(min_payload),
        max=int(max_payload),
        step=100,
        marks={
            int(min_payload): str(int(min_payload)),
            int(max_payload): str(int(max_payload))
        },
        value=[int(min_payload), int(max_payload)]
    ),
    html.Br(),

    # TASK 4: Scatter chart
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# TASK 2:
# Callback for pie chart
@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def get_pie_chart(entered_site):
    # Defensive checks and logging
    print("get_pie_chart called with:", entered_site)
    print("Columns:", spacex_df.columns.tolist())

    # Normalize column names if there might be stray spaces
    df = spacex_df.rename(columns=lambda c: c.strip())

    # Ensure 'class' and 'Launch Site' exist
    if 'class' not in df.columns or 'Launch Site' not in df.columns:
        # return a simple empty figure with message
        fig = px.pie(names=['No data'], values=[1], title='Required columns missing')
        return fig

    # If dropdown not set, treat as ALL
    if not entered_site:
        entered_site = 'ALL'

    if entered_site == 'ALL':
        # Count successful launches per site
        success_counts = df[df['class'] == 1].groupby('Launch Site').size().reset_index(name='successes')
        if success_counts.empty:
            # fallback figure to indicate no successes found
            fig = px.pie(names=['No successful launches'], values=[1], title='No successful launches found')
            return fig
        fig = px.pie(success_counts, values='successes', names='Launch Site',
                     title='Total Successful Launches by Site')
        return fig
    else:
        # For a specific site, show success vs failure counts
        site_df = df[df['Launch Site'] == entered_site]
        if site_df.empty:
            fig = px.pie(names=['No launches for selected site'], values=[1],
                         title=f'No launches for {entered_site}')
            return fig

        outcome_counts = site_df['class'].value_counts().reset_index()
        outcome_counts.columns = ['outcome', 'count']
        outcome_counts['outcome'] = outcome_counts['outcome'].map({1: 'Success', 0: 'Failure'}).fillna('Other')
        fig = px.pie(outcome_counts, values='count', names='outcome',
                     title=f'Success vs Failure for {entered_site}')
        return fig

# TASK 4:
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'),
     Input('payload-slider', 'value')]
)
def get_scatter_chart(entered_site, payload_range):
    # Defensive logging (prints appear in server console)
    print("get_scatter_chart called with:", entered_site, payload_range)

    # Normalize column names to avoid stray-space issues
    df = spacex_df.rename(columns=lambda c: c.strip())

    # Ensure required columns exist
    required = ['Payload Mass (kg)', 'class', 'Launch Site']
    for col in required:
        if col not in df.columns:
            # Return a simple placeholder figure if columns missing
            return px.scatter(x=[0], y=[0], title=f"Missing column: {col}")

    # Handle missing slider value
    if not payload_range or len(payload_range) != 2:
        low = int(df['Payload Mass (kg)'].min())
        high = int(df['Payload Mass (kg)'].max())
    else:
        low, high = payload_range

    # Filter by payload range
    mask = (df['Payload Mass (kg)'] >= low) & (df['Payload Mass (kg)'] <= high)
    filtered_df = df[mask]

    # Handle missing/None dropdown value
    if not entered_site or entered_site == 'ALL':
        # keep all sites
        pass
    else:
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]

    # If no data after filtering, return a clear placeholder figure
    if filtered_df.empty:
        return px.scatter(
            x=[0], y=[0],
            title='No data for selected site and payload range'
        )

    # Choose a color column if available
    color_col = 'Booster Version Category' if 'Booster Version Category' in filtered_df.columns else None

    fig = px.scatter(
        filtered_df,
        x='Payload Mass (kg)',
        y='class',
        color=color_col,
        hover_data=['Launch Site', 'Payload Mass (kg)'],
        title='Payload vs. Launch Outcome'
    )
    fig.update_yaxes(tickvals=[0, 1], ticktext=['Failure', 'Success'])
    return fig

# Run the app
if __name__ == '__main__':
    app.run()