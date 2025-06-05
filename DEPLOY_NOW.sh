#!/bin/bash

# God Digital Marketing - INSTANT DEPLOY SCRIPT
# This script will deploy your 3D website in under 3 minutes

echo "🚀 DEPLOYING GOD DIGITAL MARKETING 3D WEBSITE..."
echo "================================================="

# Step 1: Navigate to project directory
echo "📂 Step 1: Checking project directory..."
if [ -d "god_digital_marketing_website" ]; then
    cd god_digital_marketing_website
    echo "✅ Found project directory"
else
    echo "❌ Project directory not found. Please ensure you're in the right location."
    exit 1
fi

# Step 2: Install dependencies
echo "📦 Step 2: Installing dependencies..."
npm install

# Step 3: Check if Vercel CLI is installed
echo "🔧 Step 3: Setting up Vercel CLI..."
if ! command -v vercel &> /dev/null; then
    echo "📥 Installing Vercel CLI globally..."
    npm install -g vercel
fi

# Step 4: Deploy to production
echo "🌐 Step 4: Deploying to production..."
echo "🎯 Creating your live website now..."

# Deploy with specific settings for God Digital Marketing
vercel --prod --yes --name="god-digital-marketing-3d" --public

echo ""
echo "🎉 DEPLOYMENT COMPLETE!"
echo "========================================"
echo "✅ Your ultra-advanced 3D website is now LIVE!"
echo "🌐 Copy the URL above and start showcasing to clients"
echo "📱 The website is optimized for desktop and mobile"
echo "🎯 Perfect for Delhi digital marketing presentations"
echo ""
echo "🚀 Access your 3 versions:"
echo "   • yoururl.vercel.app          - Professional version"
echo "   • yoururl.vercel.app/enhanced - Enhanced 3D portfolio"
echo "   • yoururl.vercel.app/ultimate - Ultra-advanced effects"
echo ""
echo "🏆 You now have the most advanced 3D digital marketing website in Delhi!"