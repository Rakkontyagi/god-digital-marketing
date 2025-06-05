#!/bin/bash

# God Digital Marketing - Instant Deploy Script
echo "🚀 Deploying God Digital Marketing 3D Website..."

# Check if Vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "📦 Installing Vercel CLI..."
    npm install -g vercel
fi

# Deploy with auto-configuration
echo "🌐 Deploying to live URL..."
vercel --prod --yes --name="god-digital-marketing" --public

echo "✅ Deployment complete!"
echo "🌐 Your website is now LIVE!"
echo "📋 Copy the URL from above and share with clients"
echo "🎯 Perfect for Delhi digital marketing showcase"