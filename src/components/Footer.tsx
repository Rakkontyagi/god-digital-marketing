import React from 'react';
import Link from 'next/link';

// Placeholder for social icons - can be expanded with SVGs or a library
const SocialLink: React.FC<{ href: string; label: string }> = ({ href, label }) => (
  <a href={href} target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-god-orange-DEFAULT transition-colors">
    {label}
  </a>
);

const Footer: React.FC = () => {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="bg-gray-900 border-t border-gray-700 text-gray-300 py-12">
      <div className="container mx-auto px-6">
        <div className="grid md:grid-cols-3 gap-8 items-center">
          {/* Column 1: Brand and Copyright */}
          <div className="text-center md:text-left">
            <div className="text-2xl font-bold font-display mb-2">
              <Link href="#home">
                <a className="hover:text-white transition-colors">
                  <span className="text-god-orange-DEFAULT">God</span>{' '}
                  <span className="text-god-blue-light">Digital</span>
                </a>
              </Link>
            </div>
            <p className="text-sm text-gray-500">
              &copy; {currentYear} God Digital Marketing.
            </p>
            <p className="text-sm text-gray-500">All rights reserved. Delhi, India.
            </p>
          </div>

          {/* Column 2: Quick Links (Optional) */}
          <div className="text-center">
            <h5 className="text-lg font-semibold font-display text-white mb-3">Quick Links</h5>
            <ul className="space-y-2">
              <li><Link href="#home"><a className="hover:text-god-orange-DEFAULT transition-colors">Home</a></Link></li>
              <li><Link href="#services"><a className="hover:text-god-orange-DEFAULT transition-colors">Services</a></Link></li>
              <li><Link href="#about"><a className="hover:text-god-orange-DEFAULT transition-colors">About Us</a></Link></li>
              <li><Link href="#contact"><a className="hover:text-god-orange-DEFAULT transition-colors">Contact</a></Link></li>
            </ul>
          </div>

          {/* Column 3: Social Media Placeholder Links */}
          <div className="text-center md:text-right">
            <h5 className="text-lg font-semibold font-display text-white mb-3">Connect With Us</h5>
            <div className="flex justify-center md:justify-end space-x-4">
              <SocialLink href="#" label="Facebook" />
              <SocialLink href="#" label="Instagram" />
              <SocialLink href="#" label="LinkedIn" />
              <SocialLink href="#" label="Twitter" />
            </div>
            <p className="text-sm text-gray-500 mt-3">Follow us for updates and insights!</p>
          </div>
        </div>
        <div className="mt-8 pt-8 border-t border-gray-700 text-center text-sm text-gray-500">
          <p>
            Designed with <span className="text-delhi-red">&hearts;</span> for Modernity & Innovation in Delhi.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
