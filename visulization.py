import numpy as np
import plotly.graph_objects as go

# Generate sample data: 3D Torus/Spiral
t = np.linspace(0, 20, 500)
x = (3 + np.cos(0.5 * t)) * np.cos(t)
y = (3 + np.cos(0.5 * t)) * np.sin(t)
z = np.sin(0.5 * t)

# Create an interactive 3D scatter plot with color mapping
fig = go.Figure(data=[go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='lines+markers',
    marker=dict(
        size=4,
        color=z,             # Color by z-axis value
        colorscale='Viridis', # High-performance color palette
        opacity=0.8
    ),
    line=dict(color='rgba(255,255,255,0.3)', width=2)
)])

fig.update_layout(
    title='Advanced 3D Parametric Spiral in Python',
    scene=dict(
        xaxis_backgroundcolor="rgba(0,0,0,0)",
        yaxis_backgroundcolor="rgba(0,0,0,0)",
        zaxis_backgroundcolor="rgba(0,0,0,0)",
    ),
    template='plotly_dark'
)

fig.show()
