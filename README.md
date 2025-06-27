# Shimano DI2 Wind Tunnel Simulation

This repository includes a minimal example of a browser-based wind tunnel simulation written in Python. The example focuses on estimating aerodynamic drag for a bicycle with a rider using a simplified formula.

## Running the Web App

1. Install dependencies (Flask):
   ```bash
   pip install -r web_sim/requirements.txt
   ```
2. Start the server:
   ```bash
   python web_sim/app.py
   ```
3. Open your browser and navigate to `http://localhost:5000` to enter simulation parameters.

The current implementation computes drag force with `0.5 * rho * Cd * A * v^2`.
