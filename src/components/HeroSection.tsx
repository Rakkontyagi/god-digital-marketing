import React from 'react';
import dynamic from 'next/dynamic';

const Hero3D = dynamic(() => import('./3d/Hero3D'), {
  ssr: false,
  loading: () => <div style={{ height: '100%', width: '100%', position: 'absolute', background: 'transparent' }} />, // Minimal loader for Hero3D
});

const ParticleBackground = dynamic(() => import('./3d/ParticleBackground'), {
  ssr: false,
  loading: () => null, // No specific loader, it's a background element
});

const HeroSection: React.FC = () => {
  return (
    <section id="home" className="relative flex items-center justify-center h-screen bg-gradient-to-br from-blue-900 via-blue-700 to-indigo-900 text-white overflow-hidden">
      <ParticleBackground count={3000} color="#FFFFFF" size={0.02} speed={0.05} />
      {/* Wrapper for Hero3D to ensure correct layering and full coverage */}
      <div style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', zIndex: 0 }}>
        <Hero3D />
      </div>

      <div className="relative z-10 container mx-auto px-6 text-center flex flex-col items-center">
        <h1 className="text-5xl md:text-7xl font-bold font-display mb-6 leading-tight">
          <span className="text-god-orange-DEFAULT">God</span>{' '}
          <span className="text-white">Digital</span><br />
          <span className="text-god-blue-light">Marketing</span>
        </h1>
        <p className="text-xl md:text-2xl mb-8 max-w-3xl">
          Premier Digital Marketing Agency in{' '}
          <span className="text-delhi-red font-semibold">Delhi</span><br />
          Driving Business Growth with 3D Innovation & Proven Strategies.
        </p>
        <div className="flex flex-col sm:flex-row gap-4">
          <button className="px-8 py-4 bg-god-orange-DEFAULT hover:bg-god-orange-dark text-white font-semibold rounded-lg transition-all duration-300 transform hover:scale-105 shadow-xl hover:shadow-2xl">
            Get Free Consultation
          </button>
          <button className="px-8 py-4 border-2 border-white text-white hover:bg-white hover:text-god-blue-dark font-semibold rounded-lg transition-all duration-300 transform hover:scale-105 shadow-xl hover:shadow-2xl">
            View Our Work
          </button>
        </div>
      </div>
      {/* Optional: Add some subtle overlay or gradient if needed to enhance text readability over 3D */}
      <div className="absolute inset-0 bg-black opacity-10 z-0"></div>
    </section>
  );
};

export default HeroSection;
