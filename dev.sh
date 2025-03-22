#!/bin/bash
# Start the API
cd api && source ./venv/Scripts/activate && fastapi dev &
# Wait a few seconds for the API to start
sleep 5
# Start the app
cd ../app && npm run dev 