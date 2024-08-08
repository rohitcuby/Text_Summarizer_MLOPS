#!/bin/sh

# Run both main.py and app.py
python3 main.py &  # Run main.py in the background
python3 app.py     # Run app.py in the foreground
