import React from 'react';
// Dynamically import the 3D component to ensure it's client-side only
import dynamic from 'next/dynamic';

const DelhiMap3D = dynamic(() => import('./3d/DelhiMap3D'), {
  ssr: false, // No server-side rendering for this 3D component
  loading: () => <div style={{ height: '400px', display: 'flex', alignItems: 'center', justifyContent: 'center', background: '#111', color: 'white' }}>Loading 3D Map...</div>,
});

const IndiaMapSection: React.FC = () => {
  return (
    <section id="map-delhi" className="py-16 md:py-24 bg-black text-white">
      <div className="container mx-auto px-6">
        <div className="text-center mb-12 md:mb-16">
          <h2 className="text-4xl md:text-5xl font-bold font-display mb-4">
            Our Heart in <span className="text-delhi-red">Delhi</span>, Our Reach <span className="text-india-green">Nationwide</span>
          </h2>
          <p className="text-xl text-gray-300 max-w-3xl mx-auto">
            Explore our strategic focus on Delhi, the hub of innovation, while we extend digital
            excellence across India. Interact with the map to see our core.
          </p>
        </div>

        <div className="max-w-4xl mx-auto bg-gray-900 p-4 md:p-8 rounded-xl shadow-2xl border border-gray-700">
          <DelhiMap3D />
        </div>
      </div>
    </section>
  );
};

export default IndiaMapSection;
