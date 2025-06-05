import React from 'react';

const AboutSection: React.FC = () => {
  const stats = [
    { value: '500+', label: 'Happy Clients in Delhi' },
    { value: '750+', label: 'Innovative Projects Delivered' },
    { value: '10+', label: 'Years of Local Expertise' },
    { value: '100%', label: 'Commitment to 3D & Modern Tech' },
  ];

  const strengths = [
    'Delhi-Focused Digital Strategies',
    'Pioneering 3D Web & Marketing Solutions',
    'Measurable Data-Driven Results',
    'Unwavering Client-Centric Approach',
    'Super Modern & Unbelievable Designs',
  ];

  return (
    <section id="about" className="py-16 md:py-24 bg-gradient-to-b from-gray-900 to-black text-white">
      <div className="container mx-auto px-6">
        <div className="text-center mb-12 md:mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-4">
            Meet <span className="text-orange-400">God</span> <span className="text-blue-300">Digital</span> Marketing
          </h2>
          <p className="text-xl text-gray-300 max-w-3xl mx-auto">
            We are Delhi's premier digital marketing architects, sculpting dynamic online presences
            with a fusion of 3D innovation, strategic insight, and hyper-local expertise.
          </p>
        </div>

        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Left Column: Description and Strengths */}
          <div className="space-y-6">
            <p className="text-lg text-gray-300 leading-relaxed">
              At God Digital Marketing, we don't just build campaigns; we engineer digital experiences.
              Our roots are deeply embedded in Delhi, allowing us to craft strategies that resonate
              powerfully with the local audience. We leverage the full spectrum of digital marketing,
              enhanced by breathtaking 3D elements and modern design philosophies, to ensure your
              brand not only stands out but also achieves tangible growth.
            </p>
            <div>
              <h3 className="text-2xl font-semibold text-orange-400 mb-4">Why Partner With Us?</h3>
              <ul className="space-y-3">
                {strengths.map((strength, index) => (
                  <li key={index} className="flex items-center">
                    <svg className="w-5 h-5 text-green-400 mr-2 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd"></path>
                    </svg>
                    <span className="text-gray-200">{strength}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>

          {/* Right Column: Stats */}
          <div className="grid grid-cols-2 gap-6 md:gap-8">
            {stats.map((stat, index) => (
              <div key={index} className="bg-white/5 backdrop-blur-sm p-6 rounded-lg text-center shadow-lg border border-white/10">
                <div className="text-4xl font-bold text-orange-400 mb-2">{stat.value}</div>
                <div className="text-gray-300">{stat.label}</div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default AboutSection;
