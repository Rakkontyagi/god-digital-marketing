import React from 'react';
import Link from 'next/link'; // Using next/link for client-side navigation if pages were separate

const Navigation: React.FC = () => {
  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-black/30 backdrop-blur-md border-b border-white/20 shadow-lg">
      <div className="container mx-auto px-6 py-4 flex justify-between items-center">
        <div className="text-2xl font-bold text-white font-display">
          <Link href="#home">
            <a>
              <span className="text-god-orange-DEFAULT">God</span>{' '}
              <span className="text-god-blue-light">Digital</span>
            </a>
          </Link>
        </div>
        {/* Basic responsive menu: hidden on small screens, flex on medium and up */}
        <div className="hidden md:flex space-x-6 lg:space-x-8 text-white items-center">
          <Link href="#home">
            <a className="hover:text-god-orange-DEFAULT transition-colors duration-300">Home</a>
          </Link>
          <Link href="#services">
            <a className="hover:text-god-orange-DEFAULT transition-colors duration-300">Services</a>
          </Link>
          <Link href="#about">
            <a className="hover:text-god-orange-DEFAULT transition-colors duration-300">About</a>
          </Link>
          <Link href="#contact">
            <a className="hover:text-god-orange-DEFAULT transition-colors duration-300">Contact</a>
          </Link>
          <Link href="#contact">
            <a className="bg-god-orange-DEFAULT hover:bg-god-orange-dark text-white font-semibold px-5 py-2 rounded-lg transition-all duration-300 shadow-md hover:shadow-lg">
              Get Quote
            </a>
          </Link>
        </div>
        {/* Placeholder for mobile menu button - can be implemented later */}
        <div className="md:hidden">
          <button className="text-white focus:outline-none">
            {/* Basic SVG for menu icon */}
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16m-7 6h7"></path>
            </svg>
          </button>
        </div>
      </div>
    </nav>
  );
};

export default Navigation;
