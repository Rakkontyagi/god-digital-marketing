import React from 'react';

interface ServiceItemProps {
  title: string;
  description: string;
  icon?: React.ReactNode; // Optional: for future 3D icons or SVGs
}

const ServiceItem: React.FC<ServiceItemProps> = ({ title, description, icon }) => {
  return (
    <div className="bg-white/10 backdrop-blur-md rounded-xl p-6 md:p-8 shadow-lg hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1 border border-white/20">
      {icon && <div className="text-orange-400 mb-4">{icon}</div>}
      <h3 className="text-2xl font-semibold text-white mb-3">{title}</h3>
      <p className="text-blue-200 leading-relaxed">{description}</p>
    </div>
  );
};

const ServicesSection: React.FC = () => {
  const services: ServiceItemProps[] = [
    {
      title: 'Advanced SEO & 3D SEM',
      description: 'Dominate Google rankings with Delhi-focused SEO and cutting-edge 3D Search Engine Marketing strategies that make your brand unforgettable.',
      // icon: <PlaceholderIcon /> // Example for future icon
    },
    {
      title: 'Targeted PPC Campaigns',
      description: 'Drive immediate, qualified traffic and maximize ROI with precisely targeted Pay-Per-Click campaigns tailored for the Delhi market.',
    },
    {
      title: 'Immersive Social Media',
      description: 'Build a vibrant community and elevate your brand presence across all social platforms with engaging content and 3D interactive posts.',
    },
    {
      title: 'Next-Gen Web Design',
      description: 'Captivate your audience with stunning, super-modern websites featuring unbelievable 3D designs, optimized for all devices.',
    },
  ];

  return (
    <section id="services" className="py-16 md:py-24 bg-gradient-to-b from-blue-800 to-blue-900">
      <div className="container mx-auto px-6">
        <div className="text-center mb-12 md:mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-white mb-4">
            Our <span className="text-orange-400">Signature</span> Services
          </h2>
          <p className="text-xl text-blue-200 max-w-3xl mx-auto">
            We craft bespoke digital marketing solutions that blend innovation with strategy,
            focusing on delivering exceptional results for businesses in Delhi.
          </p>
        </div>
        <div className="grid md:grid-cols-2 lg:grid-cols-2 gap-8 md:gap-10">
          {services.map((service, index) => (
            <ServiceItem
              key={index}
              title={service.title}
              description={service.description}
              icon={service.icon}
            />
          ))}
        </div>
      </div>
    </section>
  );
};

export default ServicesSection;
