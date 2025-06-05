import React from 'react';

// Basic SVG Icon Components (can be replaced with Lucide or other libraries later)
const PhoneIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6 mr-3 text-orange-400">
    <path strokeLinecap="round" strokeLinejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z" />
  </svg>
);

const EmailIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6 mr-3 text-orange-400">
    <path strokeLinecap="round" strokeLinejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75" />
  </svg>
);

const LocationIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6 mr-3 text-orange-400">
    <path strokeLinecap="round" strokeLinejoin="round" d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z" />
    <path strokeLinecap="round" strokeLinejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z" />
  </svg>
);


const ContactSection: React.FC = () => {
  return (
    <section id="contact" className="py-16 md:py-24 bg-black text-white">
      <div className="container mx-auto px-6">
        <div className="text-center mb-12 md:mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-4">
            Let's <span className="text-orange-400">Connect</span>
          </h2>
          <p className="text-xl text-gray-300 max-w-2xl mx-auto">
            Ready to elevate your brand with cutting-edge digital marketing and 3D design?
            Reach out to our Delhi team today!
          </p>
        </div>

        <div className="grid lg:grid-cols-2 gap-12 items-start">
          {/* Left Column: Contact Information */}
          <div className="space-y-8">
            <div>
              <h3 className="text-2xl font-semibold text-orange-400 mb-4">Contact Details</h3>
              <div className="flex items-center mb-4 p-4 bg-white/5 rounded-lg">
                <PhoneIcon />
                <div>
                  <p className="text-gray-400">Call Us</p>
                  <a href="tel:+91XXXXXXXXXX" className="text-lg text-white hover:text-orange-300 transition-colors">+91-98765XXXXX (Delhi)</a>
                </div>
              </div>
              <div className="flex items-center mb-4 p-4 bg-white/5 rounded-lg">
                <EmailIcon />
                <div>
                  <p className="text-gray-400">Email Us</p>
                  <a href="mailto:info@goddigitalmarketing.com" className="text-lg text-white hover:text-orange-300 transition-colors">info@goddigitalmarketing.com</a>
                </div>
              </div>
              <div className="flex items-center p-4 bg-white/5 rounded-lg">
                <LocationIcon />
                <div>
                  <p className="text-gray-400">Our Office</p>
                  <p className="text-lg text-white">123 Digital Avenue, Connaught Place, New Delhi, Delhi 110001</p>
                </div>
              </div>
            </div>
          </div>

          {/* Right Column: Placeholder for Contact Form */}
          <div className="bg-white/10 backdrop-blur-md rounded-xl p-8 shadow-xl border border-white/20">
            <h3 className="text-2xl font-semibold text-white mb-6">Send Us a Message</h3>
            <form>
              <div className="mb-4">
                <label htmlFor="name" className="block text-gray-300 mb-2">Full Name</label>
                <input type="text" id="name" name="name" className="w-full p-3 bg-white/5 border border-white/20 rounded-lg text-white focus:ring-2 focus:ring-orange-400 outline-none" placeholder="Your Name" disabled />
              </div>
              <div className="mb-4">
                <label htmlFor="email" className="block text-gray-300 mb-2">Email Address</label>
                <input type="email" id="email" name="email" className="w-full p-3 bg-white/5 border border-white/20 rounded-lg text-white focus:ring-2 focus:ring-orange-400 outline-none" placeholder="your.email@example.com" disabled />
              </div>
              <div className="mb-6">
                <label htmlFor="message" className="block text-gray-300 mb-2">Message</label>
                <textarea id="message" name="message" rows={4} className="w-full p-3 bg-white/5 border border-white/20 rounded-lg text-white focus:ring-2 focus:ring-orange-400 outline-none" placeholder="How can we help you achieve digital godhood?" disabled></textarea>
              </div>
              <button type="submit" className="w-full bg-orange-500 hover:bg-orange-600 text-white font-semibold py-3 px-6 rounded-lg transition-all duration-300 cursor-not-allowed opacity-70">
                Send Message (Form Inactive)
              </button>
            </form>
            <p className="text-center text-sm text-gray-400 mt-4">Our interactive contact form is currently under construction. Please use the details on the left to reach us.</p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ContactSection;
