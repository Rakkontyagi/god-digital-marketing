/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    appDir: true,
  },
  images: {
    domains: ['images.unsplash.com', 'cdn.jsdelivr.net'],
  },
  webpack: (config) => {
    // Handle Three.js dependencies
    config.externals = config.externals || [];
    config.externals.push({
      canvas: 'canvas',
    });
    return config;
  },
  env: {
    SITE_NAME: 'God Digital Marketing',
    SITE_URL: 'https://goddigitalmarketing.com',
    SITE_DESCRIPTION: 'Premier Digital Marketing Agency in Delhi - Driving Business Growth with 3D Innovation',
  },
};

module.exports = nextConfig;