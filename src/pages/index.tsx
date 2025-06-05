import Head from 'next/head';
import React from 'react';
import Navigation from '../components/Navigation';
import Hero from '../components/HeroSection';
import ServicesSection from '../components/ServiceSection';
import AboutSection from '../components/AboutSection';
import ContactSection from '../components/ContactSection';
import Footer from '../components/Footer';

// Placeholder components (will be replaced by actual imports later)

const HomePage: React.FC = () => {
  return (
    <>
      <Head>
        <title>God Digital Marketing Delhi | 3D SEO & Web Design Agency</title>
        <meta
          name="description"
          content="God Digital Marketing: Delhi's #1 3D digital marketing agency. Expert SEO, PPC, social media, and unbelievable modern web design. Elevate your brand!"
        />
        <meta
          name="keywords"
          content="God Digital Marketing, Digital Marketing Delhi, 3D Website Delhi, SEO Delhi, PPC Delhi, Social Media Marketing Delhi, Modern Web Design, React Three Fiber, Next.js"
        />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" /> {/* Assuming a favicon.ico will be in public folder */}

        {/* Open Graph Meta Tags */}
        <meta property="og:title" content="God Digital Marketing Delhi | 3D SEO & Web Design" />
        <meta property="og:description" content="Transform your Delhi business with God Digital Marketing's cutting-edge 3D websites, expert SEO, and innovative digital strategies." />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="https://www.goddigitalmarketing.delhi" /> {/* Replace with actual domain */}
        <meta property="og:image" content="https://www.goddigitalmarketing.delhi/og-image.jpg" /> {/* Replace with actual image URL */}
        <meta property="og:site_name" content="God Digital Marketing Delhi" />

        {/* Twitter Card Meta Tags */}
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="God Digital Marketing Delhi | 3D SEO & Web Design" />
        <meta name="twitter:description" content="Delhi's leading agency for 3D digital marketing, SEO, PPC, and modern web design. Contact God Digital Marketing today!" />
        <meta name="twitter:image" content="https://www.goddigitalmarketing.delhi/twitter-image.jpg" /> {/* Replace with actual image URL */}
        {/* <meta name="twitter:site" content="@YourTwitterHandle" /> Optional */}

        {/* Canonical URL */}
        <link rel="canonical" href="https://www.goddigitalmarketing.delhi" /> {/* Replace with actual domain */}

        {/* Robots Meta Tag (optional, Next.js handles sitemap and indexing well by default) */}
        {/* <meta name="robots" content="index, follow" /> */}
      </Head>

      <div className="flex flex-col min-h-screen">
        <Navigation />
        <main className="flex-grow">
          <Hero />
          <ServicesSection />
          <AboutSection />
          <ContactSection />
        </main>
        <Footer />
      </div>
    </>
  );
};

export default HomePage;
