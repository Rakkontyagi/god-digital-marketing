import React from 'react';
import Hero3D from './3d/Hero3D'; // Assuming Hero3D is in a subfolder

const HeroSection: React.FC = () => {
  return (
    <section id="home" className="relative flex items-center justify-center h-screen bg-gradient-to-br from-blue-900 via-blue-700 to-indigo-900 text-white overflow-hidden">
      {/* 3D Background - ensure it's loaded dynamically if client-side only */}
      {typeof window !== 'undefined' && <Hero3D />}

      <div className="relative z-10 container mx-auto px-6 text-center flex flex-col items-center">
        <h1 className="text-5xl md:text-7xl font-bold mb-6 leading-tight">
          <span className="text-orange-400">God</span>{' '}
          <span className="text-white">Digital</span><br />
          <span className="text-blue-300">Marketing</span>
        </h1>
        <p className="text-xl md:text-2xl mb-8 max-w-3xl">
          Premier Digital Marketing Agency in{' '}
          <span className="text-red-400 font-semibold">Delhi</span><br />
          Driving Business Growth with 3D Innovation & Proven Strategies.
        </p>
        <div className="flex flex-col sm:flex-row gap-4">
          <button className="px-8 py-4 bg-orange-500 hover:bg-orange-600 text-white font-semibold rounded-lg transition-all duration-300 transform hover:scale-105 shadow-xl hover:shadow-2xl">
            Get Free Consultation
          </button>
          <button className="px-8 py-4 border-2 border-white text-white hover:bg-white hover:text-blue-900 font-semibold rounded-lg transition-all duration-300 transform hover:scale-105 shadow-xl hover:shadow-2xl">
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
