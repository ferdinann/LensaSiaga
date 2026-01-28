#!/bin/bash

echo "🚨 Starting LensaSiaga - AI Disaster Detection System 🚨"
echo "=================================================="
echo ""
echo "📋 Checking dependencies..."

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python3 found: $(python3 --version)"

# Check if requirements are installed
echo ""
echo "📦 Installing/Updating dependencies..."
pip install -r requirements.txt

# Check if model files exist
echo ""
echo "🔍 Checking model files..."

if [ ! -f "mobilenet_final_model.h5" ]; then
    echo "⚠️  Warning: mobilenet_final_model.h5 not found!"
    echo "   Please make sure the model file is in the same directory."
fi

if [ ! -f "class_names.json" ]; then
    echo "⚠️  Warning: class_names.json not found!"
    echo "   Please make sure the class names file is in the same directory."
fi

# Run the application
echo ""
echo "🚀 Launching LensaSiaga..."
echo "=================================================="
echo ""
streamlit run app.py
