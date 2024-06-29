#!/bin/bash

# Run the first Python script in the background
python3 main.py &

# Run the second Python script in the background
python3 cmt.py &

# Wait for both scripts to finish
wait

echo ""
echo ""
echo "Server terminated"

