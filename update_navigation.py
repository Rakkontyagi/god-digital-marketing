#!/usr/bin/env python3
"""
Script to update header and footer navigation across all HTML files
"""

import os
import re
from pathlib import Path

# Base directory
BASE_DIR = Path(r"C:\Users\dell\Documents\God digital marketing website 2")

def get_relative_path(file_path, target_depth):
    """Calculate relative path prefix based on file depth"""
    # Count how many levels deep the file is
    rel_path = file_path.relative_to(BASE_DIR)
    depth = len(rel_path.parents) - 1

    # Return appropriate ../ prefix
    if depth == 0:
        return ""
    elif depth == 1:
        return "../"
    elif depth == 2:
        return "../../"
    else:
        return "../" * depth

def generate_header(rel_prefix):
    """Generate header navigation with correct relative paths"""
    header = f'''    <!-- Scroll Progress Bar -->
    <div class="scroll-progress" id="scrollProgress"></div>

    <!-- Navigation -->
    <nav id="navbar">
        <div class="nav-container">
            <a href="{rel_prefix}index.html" class="logo">
                <span class="logo-highlight">God</span> Digital Marketing
            </a>
            <ul class="nav-menu" id="navMenu">
                <li class="has-dropdown">
                    <a href="{rel_prefix}services/seo-services/index.html">SEO Services <i class="fas fa-chevron-down"></i></a>
                    <div class="dropdown-menu">
                        <div class="dropdown-section">
                            <h4>By State</h4>
                            <div class="dropdown-grid">
                                <a href="{rel_prefix}services/seo-services/maharashtra/index.html">Maharashtra</a>
                                <a href="{rel_prefix}services/seo-services/karnataka/index.html">Karnataka</a>
                                <a href="{rel_prefix}services/seo-services/tamil-nadu/index.html">Tamil Nadu</a>
                                <a href="{rel_prefix}services/seo-services/gujarat/index.html">Gujarat</a>
                                <a href="{rel_prefix}services/seo-services/delhi/index.html">Delhi</a>
                                <a href="{rel_prefix}services/seo-services/uttar-pradesh/index.html">Uttar Pradesh</a>
                                <a href="{rel_prefix}services/seo-services/west-bengal/index.html">West Bengal</a>
                                <a href="{rel_prefix}services/seo-services/telangana/index.html">Telangana</a>
                                <a href="{rel_prefix}services/seo-services/kerala/index.html">Kerala</a>
                                <a href="{rel_prefix}services/seo-services/rajasthan/index.html">Rajasthan</a>
                                <a href="{rel_prefix}services/seo-services/punjab/index.html">Punjab</a>
                                <a href="{rel_prefix}services/seo-services/haryana/index.html">Haryana</a>
                            </div>
                        </div>
                        <div class="dropdown-section">
                            <h4>Top Cities</h4>
                            <div class="dropdown-grid">
                                <a href="{rel_prefix}services/seo-services/mumbai/index.html">Mumbai</a>
                                <a href="{rel_prefix}services/seo-services/bangalore/index.html">Bangalore</a>
                                <a href="{rel_prefix}services/seo-services/delhi/index.html">Delhi NCR</a>
                                <a href="{rel_prefix}services/seo-services/hyderabad/index.html">Hyderabad</a>
                                <a href="{rel_prefix}services/seo-services/chennai/index.html">Chennai</a>
                                <a href="{rel_prefix}services/seo-services/kolkata/index.html">Kolkata</a>
                                <a href="{rel_prefix}services/seo-services/pune/index.html">Pune</a>
                                <a href="{rel_prefix}services/seo-services/ahmedabad/index.html">Ahmedabad</a>
                                <a href="{rel_prefix}services/seo-services/jaipur/index.html">Jaipur</a>
                                <a href="{rel_prefix}services/seo-services/lucknow/index.html">Lucknow</a>
                                <a href="{rel_prefix}services/seo-services/kanpur/index.html">Kanpur</a>
                                <a href="{rel_prefix}services/seo-services/nagpur/index.html">Nagpur</a>
                            </div>
                        </div>
                        <div class="dropdown-section">
                            <h4>By Industry</h4>
                            <div class="dropdown-grid">
                                <a href="{rel_prefix}industries/ecommerce/index.html">E-commerce</a>
                                <a href="{rel_prefix}industries/saas/index.html">SaaS</a>
                                <a href="{rel_prefix}industries/healthcare/index.html">Healthcare</a>
                                <a href="{rel_prefix}industries/finance/index.html">Finance</a>
                                <a href="{rel_prefix}industries/real-estate/index.html">Real Estate</a>
                                <a href="{rel_prefix}industries/education/index.html">Education</a>
                                <a href="{rel_prefix}industries/hospitality/index.html">Hospitality</a>
                                <a href="{rel_prefix}industries/automotive/index.html">Automotive</a>
                            </div>
                        </div>
                    </div>
                </li>
                <li class="has-dropdown">
                    <a href="{rel_prefix}services/ppc/index.html">PPC Advertising <i class="fas fa-chevron-down"></i></a>
                    <div class="dropdown-menu">
                        <div class="dropdown-section">
                            <h4>Top Cities</h4>
                            <div class="dropdown-grid">
                                <a href="{rel_prefix}services/ppc/jaipur/index.html">Jaipur</a>
                                <a href="{rel_prefix}services/ppc/lucknow/index.html">Lucknow</a>
                                <a href="{rel_prefix}services/ppc/ahmedabad/index.html">Ahmedabad</a>
                                <a href="{rel_prefix}services/ppc/surat/index.html">Surat</a>
                                <a href="{rel_prefix}services/ppc/indore/index.html">Indore</a>
                                <a href="{rel_prefix}services/ppc/coimbatore/index.html">Coimbatore</a>
                                <a href="{rel_prefix}services/ppc/kochi/index.html">Kochi</a>
                                <a href="{rel_prefix}services/ppc/visakhapatnam/index.html">Visakhapatnam</a>
                                <a href="{rel_prefix}services/ppc/ludhiana/index.html">Ludhiana</a>
                                <a href="{rel_prefix}services/ppc/patna/index.html">Patna</a>
                                <a href="{rel_prefix}services/ppc/vadodara/index.html">Vadodara</a>
                                <a href="{rel_prefix}services/ppc/nashik/index.html">Nashik</a>
                            </div>
                        </div>
                        <div class="dropdown-section">
                            <h4>PPC Types</h4>
                            <div class="dropdown-grid">
                                <a href="{rel_prefix}services/ppc/google-ads/index.html">Google Ads</a>
                                <a href="{rel_prefix}services/ppc/facebook-ads/index.html">Facebook Ads</a>
                                <a href="{rel_prefix}services/ppc/index.html">Display Ads</a>
                                <a href="{rel_prefix}services/ppc/index.html">Shopping Ads</a>
                            </div>
                        </div>
                        <div class="dropdown-section">
                            <h4>By Industry</h4>
                            <div class="dropdown-grid">
                                <a href="{rel_prefix}industries/ecommerce/index.html">E-commerce</a>
                                <a href="{rel_prefix}industries/saas/index.html">SaaS</a>
                                <a href="{rel_prefix}industries/healthcare/index.html">Healthcare</a>
                                <a href="{rel_prefix}industries/finance/index.html">Finance</a>
                            </div>
                        </div>
                    </div>
                </li>
                <li class="has-dropdown">
                    <a href="{rel_prefix}services/social-media-marketing/index.html">Social Media <i class="fas fa-chevron-down"></i></a>
                    <div class="dropdown-menu">
                        <div class="dropdown-section">
                            <h4>Top Cities</h4>
                            <div class="dropdown-grid">
                                <a href="{rel_prefix}services/social-media-marketing/ahmedabad/index.html">Ahmedabad</a>
                                <a href="{rel_prefix}services/social-media-marketing/jaipur/index.html">Jaipur</a>
                                <a href="{rel_prefix}services/social-media-marketing/lucknow/index.html">Lucknow</a>
                                <a href="{rel_prefix}services/social-media-marketing/indore/index.html">Indore</a>
                                <a href="{rel_prefix}services/social-media-marketing/nagpur/index.html">Nagpur</a>
                                <a href="{rel_prefix}services/social-media-marketing/coimbatore/index.html">Coimbatore</a>
                                <a href="{rel_prefix}services/social-media-marketing/kochi/index.html">Kochi</a>
                                <a href="{rel_prefix}services/social-media-marketing/chandigarh/index.html">Chandigarh</a>
                            </div>
                        </div>
                        <div class="dropdown-section">
                            <h4>By Industry</h4>
                            <div class="dropdown-grid">
                                <a href="{rel_prefix}industries/ecommerce/index.html">E-commerce</a>
                                <a href="{rel_prefix}industries/healthcare/index.html">Healthcare</a>
                                <a href="{rel_prefix}industries/hospitality/index.html">Hospitality</a>
                                <a href="{rel_prefix}industries/real-estate/index.html">Real Estate</a>
                            </div>
                        </div>
                    </div>
                </li>
                <li class="has-dropdown">
                    <a href="{rel_prefix}services/content-marketing/index.html">Content Marketing <i class="fas fa-chevron-down"></i></a>
                    <div class="dropdown-menu">
                        <div class="dropdown-section">
                            <h4>Top Cities</h4>
                            <div class="dropdown-grid">
                                <a href="{rel_prefix}services/content-marketing/mumbai/index.html">Mumbai</a>
                                <a href="{rel_prefix}services/content-marketing/bangalore/index.html">Bangalore</a>
                                <a href="{rel_prefix}services/content-marketing/delhi/index.html">Delhi</a>
                                <a href="{rel_prefix}services/content-marketing/pune/index.html">Pune</a>
                                <a href="{rel_prefix}services/content-marketing/hyderabad/index.html">Hyderabad</a>
                                <a href="{rel_prefix}services/content-marketing/chennai/index.html">Chennai</a>
                                <a href="{rel_prefix}services/content-marketing/jaipur/index.html">Jaipur</a>
                                <a href="{rel_prefix}services/content-marketing/ahmedabad/index.html">Ahmedabad</a>
                            </div>
                        </div>
                        <div class="dropdown-section">
                            <h4>By Industry</h4>
                            <div class="dropdown-grid">
                                <a href="{rel_prefix}industries/saas/index.html">SaaS</a>
                                <a href="{rel_prefix}industries/healthcare/index.html">Healthcare</a>
                                <a href="{rel_prefix}industries/finance/index.html">Finance</a>
                                <a href="{rel_prefix}industries/education/index.html">Education</a>
                            </div>
                        </div>
                    </div>
                </li>
                <li class="has-dropdown">
                    <a href="{rel_prefix}services/web-design-development/index.html">Web Design <i class="fas fa-chevron-down"></i></a>
                    <div class="dropdown-menu">
                        <div class="dropdown-section">
                            <h4>Services</h4>
                            <div class="dropdown-grid">
                                <a href="{rel_prefix}services/web-design-development/index.html">Web Design</a>
                                <a href="{rel_prefix}services/web-design-development/index.html">Web Development</a>
                                <a href="{rel_prefix}services/web-design-development/index.html">E-commerce</a>
                                <a href="{rel_prefix}services/web-design-development/index.html">UI/UX Design</a>
                            </div>
                        </div>
                        <div class="dropdown-section">
                            <h4>By Industry</h4>
                            <div class="dropdown-grid">
                                <a href="{rel_prefix}industries/ecommerce/index.html">E-commerce</a>
                                <a href="{rel_prefix}industries/saas/index.html">SaaS</a>
                                <a href="{rel_prefix}industries/healthcare/index.html">Healthcare</a>
                                <a href="{rel_prefix}industries/hospitality/index.html">Hospitality</a>
                            </div>
                        </div>
                    </div>
                </li>
                <li class="has-dropdown">
                    <a href="{rel_prefix}services/marketing-automation/index.html">AI Automation <i class="fas fa-chevron-down"></i></a>
                    <div class="dropdown-menu">
                        <div class="dropdown-section">
                            <h4>Services</h4>
                            <div class="dropdown-grid">
                                <a href="{rel_prefix}services/marketing-automation/index.html">Marketing Automation</a>
                                <a href="{rel_prefix}services/marketing-automation/index.html">AI Chatbots</a>
                                <a href="{rel_prefix}services/marketing-automation/index.html">AI Content</a>
                                <a href="{rel_prefix}services/marketing-automation/index.html">Workflow Automation</a>
                            </div>
                        </div>
                        <div class="dropdown-section">
                            <h4>By Industry</h4>
                            <div class="dropdown-grid">
                                <a href="{rel_prefix}industries/ecommerce/index.html">E-commerce</a>
                                <a href="{rel_prefix}industries/saas/index.html">SaaS</a>
                                <a href="{rel_prefix}industries/finance/index.html">Finance</a>
                                <a href="{rel_prefix}industries/healthcare/index.html">Healthcare</a>
                            </div>
                        </div>
                    </div>
                </li>
                <li><a href="{rel_prefix}about-us.html">About</a></li>
                <li><a href="{rel_prefix}contact-us.html">Contact</a></li>
            </ul>
            <a href="#contact" class="nav-cta">Get Quote</a>
            <div class="hamburger" id="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    </nav>
'''
    return header

def generate_footer(rel_prefix):
    """Generate footer with correct relative paths"""
    footer = f'''    <footer>
        <div class="footer-content">
            <div class="footer-column">
                <h3>Digital Marketing Services</h3>
                <ul>
                    <li><a href="{rel_prefix}services/seo-services/index.html">SEO Services</a></li>
                    <li><a href="{rel_prefix}services/ppc/index.html">PPC Advertising</a></li>
                    <li><a href="{rel_prefix}services/social-media-marketing/index.html">Social Media Marketing</a></li>
                    <li><a href="{rel_prefix}services/content-marketing/index.html">Content Marketing</a></li>
                    <li><a href="{rel_prefix}services/email-marketing/index.html">Email Marketing</a></li>
                    <li><a href="{rel_prefix}services/web-design-development/index.html">Web Design</a></li>
                    <li><a href="{rel_prefix}services/conversion-optimization/index.html">Conversion Optimization</a></li>
                    <li><a href="{rel_prefix}services/analytics-reporting/index.html">Analytics & Reporting</a></li>
                    <li><a href="{rel_prefix}services/online-reputation-management/index.html">Reputation Management</a></li>
                    <li><a href="{rel_prefix}services/marketing-automation/index.html">Marketing Automation</a></li>
                    <li><a href="{rel_prefix}services/local-seo/index.html">Local SEO</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h3>SEO Services - States</h3>
                <ul>
                    <li><a href="{rel_prefix}services/seo-services/maharashtra/index.html">Maharashtra</a></li>
                    <li><a href="{rel_prefix}services/seo-services/karnataka/index.html">Karnataka</a></li>
                    <li><a href="{rel_prefix}services/seo-services/tamil-nadu/index.html">Tamil Nadu</a></li>
                    <li><a href="{rel_prefix}services/seo-services/gujarat/index.html">Gujarat</a></li>
                    <li><a href="{rel_prefix}services/seo-services/delhi/index.html">Delhi</a></li>
                    <li><a href="{rel_prefix}services/seo-services/uttar-pradesh/index.html">Uttar Pradesh</a></li>
                    <li><a href="{rel_prefix}services/seo-services/west-bengal/index.html">West Bengal</a></li>
                    <li><a href="{rel_prefix}services/seo-services/telangana/index.html">Telangana</a></li>
                    <li><a href="{rel_prefix}services/seo-services/kerala/index.html">Kerala</a></li>
                    <li><a href="{rel_prefix}services/seo-services/rajasthan/index.html">Rajasthan</a></li>
                    <li><a href="{rel_prefix}services/seo-services/punjab/index.html">Punjab</a></li>
                    <li><a href="{rel_prefix}services/seo-services/haryana/index.html">Haryana</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h3>SEO Services - Top Cities</h3>
                <ul>
                    <li><a href="{rel_prefix}services/seo-services/mumbai/index.html">Mumbai</a></li>
                    <li><a href="{rel_prefix}services/seo-services/bangalore/index.html">Bangalore</a></li>
                    <li><a href="{rel_prefix}services/seo-services/delhi/index.html">Delhi NCR</a></li>
                    <li><a href="{rel_prefix}services/seo-services/hyderabad/index.html">Hyderabad</a></li>
                    <li><a href="{rel_prefix}services/seo-services/chennai/index.html">Chennai</a></li>
                    <li><a href="{rel_prefix}services/seo-services/kolkata/index.html">Kolkata</a></li>
                    <li><a href="{rel_prefix}services/seo-services/pune/index.html">Pune</a></li>
                    <li><a href="{rel_prefix}services/seo-services/ahmedabad/index.html">Ahmedabad</a></li>
                    <li><a href="{rel_prefix}services/seo-services/jaipur/index.html">Jaipur</a></li>
                    <li><a href="{rel_prefix}services/seo-services/lucknow/index.html">Lucknow</a></li>
                    <li><a href="{rel_prefix}services/seo-services/kanpur/index.html">Kanpur</a></li>
                    <li><a href="{rel_prefix}services/seo-services/nagpur/index.html">Nagpur</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h3>PPC Advertising - Cities</h3>
                <ul>
                    <li><a href="{rel_prefix}services/ppc/jaipur/index.html">Jaipur PPC</a></li>
                    <li><a href="{rel_prefix}services/ppc/lucknow/index.html">Lucknow PPC</a></li>
                    <li><a href="{rel_prefix}services/ppc/ahmedabad/index.html">Ahmedabad PPC</a></li>
                    <li><a href="{rel_prefix}services/ppc/surat/index.html">Surat PPC</a></li>
                    <li><a href="{rel_prefix}services/ppc/indore/index.html">Indore PPC</a></li>
                    <li><a href="{rel_prefix}services/ppc/coimbatore/index.html">Coimbatore PPC</a></li>
                    <li><a href="{rel_prefix}services/ppc/kochi/index.html">Kochi PPC</a></li>
                    <li><a href="{rel_prefix}services/ppc/visakhapatnam/index.html">Visakhapatnam PPC</a></li>
                    <li><a href="{rel_prefix}services/ppc/ludhiana/index.html">Ludhiana PPC</a></li>
                    <li><a href="{rel_prefix}services/ppc/patna/index.html">Patna PPC</a></li>
                    <li><a href="{rel_prefix}services/ppc/vadodara/index.html">Vadodara PPC</a></li>
                    <li><a href="{rel_prefix}services/ppc/nashik/index.html">Nashik PPC</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h3>Social Media Marketing</h3>
                <ul>
                    <li><a href="{rel_prefix}services/social-media-marketing/ahmedabad/index.html">Ahmedabad SMM</a></li>
                    <li><a href="{rel_prefix}services/social-media-marketing/jaipur/index.html">Jaipur SMM</a></li>
                    <li><a href="{rel_prefix}services/social-media-marketing/lucknow/index.html">Lucknow SMM</a></li>
                    <li><a href="{rel_prefix}services/social-media-marketing/kanpur/index.html">Kanpur SMM</a></li>
                    <li><a href="{rel_prefix}services/social-media-marketing/indore/index.html">Indore SMM</a></li>
                    <li><a href="{rel_prefix}services/social-media-marketing/nagpur/index.html">Nagpur SMM</a></li>
                    <li><a href="{rel_prefix}services/social-media-marketing/coimbatore/index.html">Coimbatore SMM</a></li>
                    <li><a href="{rel_prefix}services/social-media-marketing/kochi/index.html">Kochi SMM</a></li>
                    <li><a href="{rel_prefix}services/social-media-marketing/chandigarh/index.html">Chandigarh SMM</a></li>
                    <li><a href="{rel_prefix}services/social-media-marketing/surat/index.html">Surat SMM</a></li>
                    <li><a href="{rel_prefix}services/social-media-marketing/vadodara/index.html">Vadodara SMM</a></li>
                    <li><a href="{rel_prefix}services/social-media-marketing/ludhiana/index.html">Ludhiana SMM</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h3>Content Marketing - Top Cities</h3>
                <ul>
                    <li><a href="{rel_prefix}services/content-marketing/mumbai/index.html">Mumbai</a></li>
                    <li><a href="{rel_prefix}services/content-marketing/bangalore/index.html">Bangalore</a></li>
                    <li><a href="{rel_prefix}services/content-marketing/delhi/index.html">Delhi</a></li>
                    <li><a href="{rel_prefix}services/content-marketing/pune/index.html">Pune</a></li>
                    <li><a href="{rel_prefix}services/content-marketing/hyderabad/index.html">Hyderabad</a></li>
                    <li><a href="{rel_prefix}services/content-marketing/chennai/index.html">Chennai</a></li>
                    <li><a href="{rel_prefix}services/content-marketing/jaipur/index.html">Jaipur</a></li>
                    <li><a href="{rel_prefix}services/content-marketing/ahmedabad/index.html">Ahmedabad</a></li>
                    <li><a href="{rel_prefix}services/content-marketing/surat/index.html">Surat</a></li>
                    <li><a href="{rel_prefix}services/content-marketing/lucknow/index.html">Lucknow</a></li>
                    <li><a href="{rel_prefix}services/content-marketing/kanpur/index.html">Kanpur</a></li>
                    <li><a href="{rel_prefix}services/content-marketing/indore/index.html">Indore</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h3>Email Marketing - Cities</h3>
                <ul>
                    <li><a href="{rel_prefix}services/email-marketing/mumbai/index.html">Mumbai</a></li>
                    <li><a href="{rel_prefix}services/email-marketing/bangalore/index.html">Bangalore</a></li>
                    <li><a href="{rel_prefix}services/email-marketing/delhi/index.html">Delhi</a></li>
                    <li><a href="{rel_prefix}services/email-marketing/hyderabad/index.html">Hyderabad</a></li>
                    <li><a href="{rel_prefix}services/email-marketing/chennai/index.html">Chennai</a></li>
                    <li><a href="{rel_prefix}services/email-marketing/kolkata/index.html">Kolkata</a></li>
                    <li><a href="{rel_prefix}services/email-marketing/pune/index.html">Pune</a></li>
                    <li><a href="{rel_prefix}services/email-marketing/ahmedabad/index.html">Ahmedabad</a></li>
                    <li><a href="{rel_prefix}services/email-marketing/jaipur/index.html">Jaipur</a></li>
                    <li><a href="{rel_prefix}services/email-marketing/lucknow/index.html">Lucknow</a></li>
                    <li><a href="{rel_prefix}services/email-marketing/kanpur/index.html">Kanpur</a></li>
                    <li><a href="{rel_prefix}services/email-marketing/indore/index.html">Indore</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h3>Industries We Serve</h3>
                <ul>
                    <li><a href="{rel_prefix}industries/ecommerce/index.html">E-commerce</a></li>
                    <li><a href="{rel_prefix}industries/saas/index.html">SaaS & Technology</a></li>
                    <li><a href="{rel_prefix}industries/healthcare/index.html">Healthcare</a></li>
                    <li><a href="{rel_prefix}industries/finance/index.html">Finance & Banking</a></li>
                    <li><a href="{rel_prefix}industries/real-estate/index.html">Real Estate</a></li>
                    <li><a href="{rel_prefix}industries/education/index.html">Education</a></li>
                    <li><a href="{rel_prefix}industries/hospitality/index.html">Hospitality & Travel</a></li>
                    <li><a href="{rel_prefix}industries/automotive/index.html">Automotive</a></li>
                    <li><a href="{rel_prefix}industries/legal/index.html">Legal Services</a></li>
                    <li><a href="{rel_prefix}industries/manufacturing/index.html">Manufacturing</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h3>Resources & Company</h3>
                <ul>
                    <li><a href="{rel_prefix}about-us.html">About Us</a></li>
                    <li><a href="{rel_prefix}contact-us.html">Contact</a></li>
                    <li><a href="{rel_prefix}blog.html">Blog & Insights</a></li>
                    <li><a href="{rel_prefix}case-studies.html">Case Studies</a></li>
                    <li><a href="{rel_prefix}resources.html">Resources</a></li>
                    <li><a href="{rel_prefix}tools.html">Free Tools</a></li>
                    <li><a href="{rel_prefix}careers.html">Careers</a></li>
                    <li><a href="{rel_prefix}privacy-policy.html">Privacy Policy</a></li>
                    <li><a href="{rel_prefix}terms-of-service.html">Terms of Service</a></li>
                    <li><a href="{rel_prefix}sitemap.html">Sitemap</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2025 God Digital Marketing. All rights reserved. | <a href="{rel_prefix}services/seo-services/index.html">SEO</a> | <a href="{rel_prefix}services/ppc/index.html">PPC</a> | <a href="{rel_prefix}services/social-media-marketing/index.html">Social</a> | <a href="{rel_prefix}services/content-marketing/index.html">Content</a> | <a href="{rel_prefix}services/email-marketing/index.html">Email</a> | <a href="{rel_prefix}services/web-design-development/index.html">Web Design</a> | <a href="{rel_prefix}services/analytics-reporting/index.html">Analytics</a></p>
            <div>
                <a href="{rel_prefix}privacy-policy.html">Privacy</a>
                <a href="{rel_prefix}terms-of-service.html">Terms</a>
                <a href="{rel_prefix}contact-us.html">Contact</a>
                <a href="{rel_prefix}sitemap.html">Sitemap</a>
            </div>
        </div>
    </footer>
'''
    return footer

def update_html_file(file_path):
    """Update a single HTML file with new navigation"""
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Calculate relative path prefix
        rel_prefix = get_relative_path(file_path, 0)

        # Generate new header and footer
        new_header = generate_header(rel_prefix)
        new_footer = generate_footer(rel_prefix)

        # Find where to inject navigation (after opening body tag or after CSS)
        # Pattern: Look for </style> or <body> tag
        body_match = re.search(r'</style>\s*</head>\s*<body[^>]*>', content, re.DOTALL)

        if not body_match:
            print(f"  WARNING: Could not find body tag in {file_path}")
            return False

        # Find old nav end (</nav> tag)
        nav_end = re.search(r'</nav>', content)
        if not nav_end:
            print(f"  INFO: No existing nav in {file_path}, will add new one")
            # Insert header right after body tag
            insert_pos = body_match.end()
            new_content = content[:insert_pos] + '\n' + new_header + '\n' + content[insert_pos:]
        else:
            # Find nav start (look backwards from </nav> to find <nav or <!-- Scroll Progress)
            nav_start_match = re.search(r'(<!--\s*Scroll Progress|<div class="scroll-progress"|<nav)', content[:nav_end.start()])
            if nav_start_match:
                # Get the last match (closest to </nav>)
                nav_start_pos = nav_start_match.start()
                # Replace old navigation
                new_content = content[:nav_start_pos] + new_header + content[nav_end.end():]
            else:
                print(f"  WARNING: Could not find nav start in {file_path}")
                return False

        # Now update footer
        footer_match = re.search(r'<footer>', new_content)
        if footer_match:
            # Find footer end
            footer_end = re.search(r'</footer>', new_content)
            if footer_end:
                # Replace footer
                final_content = new_content[:footer_match.start()] + new_footer + new_content[footer_end.end():]
            else:
                print(f"  WARNING: Could not find footer end in {file_path}")
                return False
        else:
            print(f"  INFO: No existing footer in {file_path}, will add new one")
            # Add footer before closing body tag
            body_end = re.search(r'</body>', new_content)
            if body_end:
                final_content = new_content[:body_end.start()] + '\n' + new_footer + '\n' + new_content[body_end.start():]
            else:
                print(f"  WARNING: No closing body tag in {file_path}")
                return False

        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(final_content)

        return True

    except Exception as e:
        print(f"  ERROR: Error updating {file_path}: {str(e)}")
        return False

def main():
    """Main function to update all HTML files"""
    print("==> Starting sitewide navigation update...")
    print(f"Base directory: {BASE_DIR}")

    # Find all HTML files
    html_files = list(BASE_DIR.rglob("*.html"))
    total_files = len(html_files)

    print(f"Found {total_files} HTML files to update\n")

    success_count = 0
    fail_count = 0

    # Update each file
    for i, file_path in enumerate(html_files, 1):
        rel_path = file_path.relative_to(BASE_DIR)
        print(f"[{i}/{total_files}] Updating {rel_path}...")

        if update_html_file(file_path):
            print(f"  [OK] Successfully updated")
            success_count += 1
        else:
            print(f"  [FAIL] Failed to update")
            fail_count += 1

        # Progress indicator every 50 files
        if i % 50 == 0:
            print(f"\n==> Progress: {i}/{total_files} ({(i/total_files)*100:.1f}%)")
            print(f"   Success: {success_count} | Failed: {fail_count}\n")

    print("\n" + "="*60)
    print("FINAL SUMMARY")
    print("="*60)
    print(f"Total files: {total_files}")
    print(f"Successfully updated: {success_count}")
    print(f"Failed: {fail_count}")
    print(f"Success rate: {(success_count/total_files)*100:.1f}%")
    print("="*60)

if __name__ == "__main__":
    main()
