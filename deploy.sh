#!/bin/bash

# God Digital Marketing 3D Website - Quick Deployment Script
# This script helps deploy the website to Vercel for immediate viewing

echo "🚀 God Digital Marketing 3D Website - Deployment Script"
echo "=================================================="

# Check if required tools are installed
echo "📋 Checking prerequisites..."

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js from https://nodejs.org/"
    exit 1
fi

# Check npm
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not installed. Please install npm"
    exit 1
fi

echo "✅ Node.js and npm are installed"

# Install dependencies
echo "📦 Installing dependencies..."
npm install

# Check if Vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "🔧 Installing Vercel CLI..."
    npm install -g vercel
fi

# Build the project
echo "🏗️ Building the project..."
npm run build

# Deploy to Vercel
echo "🚀 Deploying to Vercel..."
echo "📝 Please follow the prompts to deploy:"
echo "   1. Set up and deploy: Yes"
echo "   2. Which scope: Select your account"
echo "   3. Link to existing project: No"
echo "   4. Project name: god-digital-marketing-3d"
echo "   5. Directory: ./"
echo "   6. Want to override settings: No"

vercel --prod

echo "🎉 Deployment complete!"
echo "🌐 Your website should be live at the URL provided by Vercel"
echo "📱 The website is optimized for mobile and desktop viewing"
echo "🎯 Featuring Delhi-focused 3D digital marketing showcase"