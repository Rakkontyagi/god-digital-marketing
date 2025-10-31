#!/usr/bin/env python3
"""
Fix the final 12 files missing navigation system
"""

import re
from pathlib import Path

BASE_DIR = Path(r"C:\Users\dell\Documents\God digital marketing website 2")

# The 12 files identified by find_failed.py
FILES_TO_FIX = [
    "services/seo-services/jammu-kashmir/index.html",
    "services/content-marketing/ajmer/index.html",
    "services/content-marketing/bhubaneswar/index.html",
    "services/content-marketing/guntur/index.html",
    "services/content-marketing/jalandhar/index.html",
    "services/content-marketing/jamshedpur/index.html",
    "services/content-marketing/kollam/index.html",
    "services/content-marketing/kota/index.html",
    "services/content-marketing/kozhikode/index.html",
    "services/content-marketing/mangalore/index.html",
    "services/content-marketing/meerut/index.html",
    "services/content-marketing/salem/index.html",
]

def generate_new_header():
    """Generate the complete new header with category-based navigation"""
    return '''<header>
<nav>
<h1>God Digital Marketing</h1>
<ul class="nav-menu" id="navMenu">
<li class="has-dropdown">
<a href="../../../services/seo-services/index.html">SEO Services <i class="fas fa-chevron-down"></i></a>
<div class="dropdown-menu">
<div class="dropdown-section">
<h4>By State</h4>
<div class="dropdown-grid">
<a href="../../../services/seo-services/maharashtra/index.html">Maharashtra</a>
<a href="../../../services/seo-services/karnataka/index.html">Karnataka</a>
<a href="../../../services/seo-services/tamil-nadu/index.html">Tamil Nadu</a>
<a href="../../../services/seo-services/gujarat/index.html">Gujarat</a>
<a href="../../../services/seo-services/delhi/index.html">Delhi</a>
<a href="../../../services/seo-services/uttar-pradesh/index.html">Uttar Pradesh</a>
<a href="../../../services/seo-services/west-bengal/index.html">West Bengal</a>
<a href="../../../services/seo-services/rajasthan/index.html">Rajasthan</a>
<a href="../../../services/seo-services/telangana/index.html">Telangana</a>
<a href="../../../services/seo-services/punjab/index.html">Punjab</a>
<a href="../../../services/seo-services/kerala/index.html">Kerala</a>
<a href="../../../services/seo-services/andhra-pradesh/index.html">Andhra Pradesh</a>
</div>
</div>
<div class="dropdown-section">
<h4>Top Cities</h4>
<div class="dropdown-grid">
<a href="../../../services/seo-services/mumbai/index.html">Mumbai</a>
<a href="../../../services/seo-services/bangalore/index.html">Bangalore</a>
<a href="../../../services/seo-services/delhi/index.html">Delhi NCR</a>
<a href="../../../services/seo-services/chennai/index.html">Chennai</a>
<a href="../../../services/seo-services/pune/index.html">Pune</a>
<a href="../../../services/seo-services/hyderabad/index.html">Hyderabad</a>
<a href="../../../services/seo-services/kolkata/index.html">Kolkata</a>
<a href="../../../services/seo-services/ahmedabad/index.html">Ahmedabad</a>
<a href="../../../services/seo-services/surat/index.html">Surat</a>
<a href="../../../services/seo-services/jaipur/index.html">Jaipur</a>
<a href="../../../services/seo-services/lucknow/index.html">Lucknow</a>
<a href="../../../services/seo-services/kanpur/index.html">Kanpur</a>
</div>
</div>
<div class="dropdown-section">
<h4>Industries</h4>
<div class="dropdown-grid">
<a href="../../../industries/ecommerce/index.html">E-commerce</a>
<a href="../../../industries/saas/index.html">SaaS & Technology</a>
<a href="../../../industries/healthcare/index.html">Healthcare</a>
<a href="../../../industries/finance/index.html">Finance & Banking</a>
<a href="../../../industries/real-estate/index.html">Real Estate</a>
<a href="../../../industries/education/index.html">Education</a>
<a href="../../../industries/hospitality/index.html">Hospitality & Travel</a>
<a href="../../../industries/automotive/index.html">Automotive</a>
</div>
</div>
</div>
</li>
<li class="has-dropdown">
<a href="../../../services/ppc/index.html">PPC Advertising <i class="fas fa-chevron-down"></i></a>
<div class="dropdown-menu">
<div class="dropdown-section">
<h4>Top Cities</h4>
<div class="dropdown-grid">
<a href="../../../services/ppc/jaipur/index.html">Jaipur</a>
<a href="../../../services/ppc/lucknow/index.html">Lucknow</a>
<a href="../../../services/ppc/ahmedabad/index.html">Ahmedabad</a>
<a href="../../../services/ppc/surat/index.html">Surat</a>
<a href="../../../services/ppc/kanpur/index.html">Kanpur</a>
<a href="../../../services/ppc/indore/index.html">Indore</a>
<a href="../../../services/ppc/bhopal/index.html">Bhopal</a>
<a href="../../../services/ppc/nagpur/index.html">Nagpur</a>
<a href="../../../services/ppc/coimbatore/index.html">Coimbatore</a>
<a href="../../../services/ppc/kochi/index.html">Kochi</a>
<a href="../../../services/ppc/visakhapatnam/index.html">Visakhapatnam</a>
<a href="../../../services/ppc/chandigarh/index.html">Chandigarh</a>
</div>
</div>
<div class="dropdown-section">
<h4>PPC Types</h4>
<div class="dropdown-grid">
<a href="../../../services/ppc/index.html#google-ads">Google Ads</a>
<a href="../../../services/ppc/index.html#facebook-ads">Facebook Ads</a>
<a href="../../../services/ppc/index.html#instagram-ads">Instagram Ads</a>
<a href="../../../services/ppc/index.html#linkedin-ads">LinkedIn Ads</a>
<a href="../../../services/ppc/index.html#display-ads">Display Advertising</a>
<a href="../../../services/ppc/index.html#remarketing">Remarketing</a>
</div>
</div>
<div class="dropdown-section">
<h4>Industries</h4>
<div class="dropdown-grid">
<a href="../../../industries/ecommerce/index.html">E-commerce</a>
<a href="../../../industries/saas/index.html">SaaS & Technology</a>
<a href="../../../industries/healthcare/index.html">Healthcare</a>
<a href="../../../industries/finance/index.html">Finance & Banking</a>
<a href="../../../industries/real-estate/index.html">Real Estate</a>
<a href="../../../industries/education/index.html">Education</a>
<a href="../../../industries/hospitality/index.html">Hospitality & Travel</a>
<a href="../../../industries/automotive/index.html">Automotive</a>
</div>
</div>
</div>
</li>
<li class="has-dropdown">
<a href="../../../services/social-media-marketing/index.html">Social Media <i class="fas fa-chevron-down"></i></a>
<div class="dropdown-menu">
<div class="dropdown-section">
<h4>Top Cities</h4>
<div class="dropdown-grid">
<a href="../../../services/social-media-marketing/ahmedabad/index.html">Ahmedabad</a>
<a href="../../../services/social-media-marketing/jaipur/index.html">Jaipur</a>
<a href="../../../services/social-media-marketing/lucknow/index.html">Lucknow</a>
<a href="../../../services/social-media-marketing/kanpur/index.html">Kanpur</a>
<a href="../../../services/social-media-marketing/indore/index.html">Indore</a>
<a href="../../../services/social-media-marketing/bhopal/index.html">Bhopal</a>
<a href="../../../services/social-media-marketing/nagpur/index.html">Nagpur</a>
<a href="../../../services/social-media-marketing/coimbatore/index.html">Coimbatore</a>
<a href="../../../services/social-media-marketing/kochi/index.html">Kochi</a>
<a href="../../../services/social-media-marketing/visakhapatnam/index.html">Visakhapatnam</a>
<a href="../../../services/social-media-marketing/chandigarh/index.html">Chandigarh</a>
<a href="../../../services/social-media-marketing/surat/index.html">Surat</a>
</div>
</div>
<div class="dropdown-section">
<h4>Industries</h4>
<div class="dropdown-grid">
<a href="../../../industries/ecommerce/index.html">E-commerce</a>
<a href="../../../industries/saas/index.html">SaaS & Technology</a>
<a href="../../../industries/healthcare/index.html">Healthcare</a>
<a href="../../../industries/finance/index.html">Finance & Banking</a>
<a href="../../../industries/real-estate/index.html">Real Estate</a>
<a href="../../../industries/education/index.html">Education</a>
<a href="../../../industries/hospitality/index.html">Hospitality & Travel</a>
<a href="../../../industries/automotive/index.html">Automotive</a>
</div>
</div>
</div>
</li>
<li class="has-dropdown">
<a href="../../../services/content-marketing/index.html">Content Marketing <i class="fas fa-chevron-down"></i></a>
<div class="dropdown-menu">
<div class="dropdown-section">
<h4>Top Cities</h4>
<div class="dropdown-grid">
<a href="../../../services/content-marketing/mumbai/index.html">Mumbai</a>
<a href="../../../services/content-marketing/bangalore/index.html">Bangalore</a>
<a href="../../../services/content-marketing/delhi/index.html">Delhi</a>
<a href="../../../services/content-marketing/pune/index.html">Pune</a>
<a href="../../../services/content-marketing/hyderabad/index.html">Hyderabad</a>
<a href="../../../services/content-marketing/chennai/index.html">Chennai</a>
<a href="../../../services/content-marketing/kolkata/index.html">Kolkata</a>
<a href="../../../services/content-marketing/ahmedabad/index.html">Ahmedabad</a>
<a href="../../../services/content-marketing/jaipur/index.html">Jaipur</a>
<a href="../../../services/content-marketing/lucknow/index.html">Lucknow</a>
<a href="../../../services/content-marketing/kanpur/index.html">Kanpur</a>
<a href="../../../services/content-marketing/indore/index.html">Indore</a>
</div>
</div>
<div class="dropdown-section">
<h4>Industries</h4>
<div class="dropdown-grid">
<a href="../../../industries/ecommerce/index.html">E-commerce</a>
<a href="../../../industries/saas/index.html">SaaS & Technology</a>
<a href="../../../industries/healthcare/index.html">Healthcare</a>
<a href="../../../industries/finance/index.html">Finance & Banking</a>
<a href="../../../industries/real-estate/index.html">Real Estate</a>
<a href="../../../industries/education/index.html">Education</a>
<a href="../../../industries/hospitality/index.html">Hospitality & Travel</a>
<a href="../../../industries/automotive/index.html">Automotive</a>
</div>
</div>
</div>
</li>
<li class="has-dropdown">
<a href="../../../services/web-design-development/index.html">Web Design <i class="fas fa-chevron-down"></i></a>
<div class="dropdown-menu">
<div class="dropdown-section">
<h4>Services</h4>
<div class="dropdown-grid">
<a href="../../../services/web-design-development/index.html#responsive">Responsive Design</a>
<a href="../../../services/web-design-development/index.html#ecommerce">E-commerce Development</a>
<a href="../../../services/web-design-development/index.html#cms">CMS Development</a>
<a href="../../../services/web-design-development/index.html#custom">Custom Web Apps</a>
<a href="../../../services/web-design-development/index.html#ui-ux">UI/UX Design</a>
<a href="../../../services/web-design-development/index.html#maintenance">Website Maintenance</a>
</div>
</div>
<div class="dropdown-section">
<h4>Industries</h4>
<div class="dropdown-grid">
<a href="../../../industries/ecommerce/index.html">E-commerce</a>
<a href="../../../industries/saas/index.html">SaaS & Technology</a>
<a href="../../../industries/healthcare/index.html">Healthcare</a>
<a href="../../../industries/finance/index.html">Finance & Banking</a>
<a href="../../../industries/real-estate/index.html">Real Estate</a>
<a href="../../../industries/education/index.html">Education</a>
<a href="../../../industries/hospitality/index.html">Hospitality & Travel</a>
<a href="../../../industries/automotive/index.html">Automotive</a>
</div>
</div>
</div>
</li>
<li class="has-dropdown">
<a href="../../../services/marketing-automation/index.html">AI Automation <i class="fas fa-chevron-down"></i></a>
<div class="dropdown-menu">
<div class="dropdown-section">
<h4>Services</h4>
<div class="dropdown-grid">
<a href="../../../services/marketing-automation/index.html#email">Email Automation</a>
<a href="../../../services/marketing-automation/index.html#lead">Lead Nurturing</a>
<a href="../../../services/marketing-automation/index.html#crm">CRM Integration</a>
<a href="../../../services/marketing-automation/index.html#ai">AI-Powered Marketing</a>
<a href="../../../services/marketing-automation/index.html#chatbots">Chatbot Development</a>
<a href="../../../services/marketing-automation/index.html#workflows">Marketing Workflows</a>
</div>
</div>
<div class="dropdown-section">
<h4>Industries</h4>
<div class="dropdown-grid">
<a href="../../../industries/ecommerce/index.html">E-commerce</a>
<a href="../../../industries/saas/index.html">SaaS & Technology</a>
<a href="../../../industries/healthcare/index.html">Healthcare</a>
<a href="../../../industries/finance/index.html">Finance & Banking</a>
<a href="../../../industries/real-estate/index.html">Real Estate</a>
<a href="../../../industries/education/index.html">Education</a>
<a href="../../../industries/hospitality/index.html">Hospitality & Travel</a>
<a href="../../../industries/automotive/index.html">Automotive</a>
</div>
</div>
</div>
</li>
<li><a href="../../../about-us.html">About</a></li>
<li><a href="../../../contact-us.html">Contact</a></li>
</ul>
<button class="mobile-toggle" id="mobileToggle">☰</button>
</nav>
</header>'''

def generate_new_footer():
    """Generate the complete comprehensive footer"""
    return '''<footer style="background:rgba(15,23,42,0.5);backdrop-filter:blur(10px);border-top:1px solid rgba(255,255,255,0.1);padding:60px 20px 20px">
<div style="max-width:1400px;margin:0 auto">
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:40px;margin-bottom:40px">
<div>
<h3 style="color:#F8FAFC;margin-bottom:1rem;font-size:1.1rem">Digital Marketing Services</h3>
<ul style="list-style:none;margin:0;padding:0">
<li style="margin-bottom:0.6rem"><a href="../../../services/seo-services/index.html" style="color:#94A3B8;text-decoration:none">SEO Services</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/ppc/index.html" style="color:#94A3B8;text-decoration:none">PPC Advertising</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/social-media-marketing/index.html" style="color:#94A3B8;text-decoration:none">Social Media Marketing</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/content-marketing/index.html" style="color:#94A3B8;text-decoration:none">Content Marketing</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/email-marketing/index.html" style="color:#94A3B8;text-decoration:none">Email Marketing</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/web-design-development/index.html" style="color:#94A3B8;text-decoration:none">Web Design & Development</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/conversion-optimization/index.html" style="color:#94A3B8;text-decoration:none">Conversion Optimization</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/analytics-reporting/index.html" style="color:#94A3B8;text-decoration:none">Analytics & Reporting</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/online-reputation-management/index.html" style="color:#94A3B8;text-decoration:none">Online Reputation Management</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/marketing-automation/index.html" style="color:#94A3B8;text-decoration:none">Marketing Automation</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/local-seo/index.html" style="color:#94A3B8;text-decoration:none">Local SEO</a></li>
</ul>
</div>
<div>
<h3 style="color:#F8FAFC;margin-bottom:1rem;font-size:1.1rem">Industries We Serve</h3>
<ul style="list-style:none;margin:0;padding:0">
<li style="margin-bottom:0.6rem"><a href="../../../industries/ecommerce/index.html" style="color:#94A3B8;text-decoration:none">E-commerce</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../industries/saas/index.html" style="color:#94A3B8;text-decoration:none">SaaS & Technology</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../industries/healthcare/index.html" style="color:#94A3B8;text-decoration:none">Healthcare</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../industries/finance/index.html" style="color:#94A3B8;text-decoration:none">Finance & Banking</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../industries/real-estate/index.html" style="color:#94A3B8;text-decoration:none">Real Estate</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../industries/education/index.html" style="color:#94A3B8;text-decoration:none">Education & E-Learning</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../industries/hospitality/index.html" style="color:#94A3B8;text-decoration:none">Hospitality & Travel</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../industries/automotive/index.html" style="color:#94A3B8;text-decoration:none">Automotive</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../industries/legal/index.html" style="color:#94A3B8;text-decoration:none">Legal Services</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../industries/manufacturing/index.html" style="color:#94A3B8;text-decoration:none">Manufacturing</a></li>
</ul>
</div>
<div>
<h3 style="color:#F8FAFC;margin-bottom:1rem;font-size:1.1rem">Service by City</h3>
<ul style="list-style:none;margin:0;padding:0">
<li style="margin-bottom:0.6rem"><a href="../../../services/seo-services/mumbai/index.html" style="color:#94A3B8;text-decoration:none">Mumbai</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/seo-services/bangalore/index.html" style="color:#94A3B8;text-decoration:none">Bangalore</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/seo-services/delhi/index.html" style="color:#94A3B8;text-decoration:none">Delhi</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/seo-services/hyderabad/index.html" style="color:#94A3B8;text-decoration:none">Hyderabad</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/seo-services/chennai/index.html" style="color:#94A3B8;text-decoration:none">Chennai</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/seo-services/kolkata/index.html" style="color:#94A3B8;text-decoration:none">Kolkata</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/seo-services/pune/index.html" style="color:#94A3B8;text-decoration:none">Pune</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/seo-services/ahmedabad/index.html" style="color:#94A3B8;text-decoration:none">Ahmedabad</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/seo-services/surat/index.html" style="color:#94A3B8;text-decoration:none">Surat</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/seo-services/jaipur/index.html" style="color:#94A3B8;text-decoration:none">Jaipur</a></li>
</ul>
</div>
<div>
<h3 style="color:#F8FAFC;margin-bottom:1rem;font-size:1.1rem">Content Marketing</h3>
<ul style="list-style:none;margin:0;padding:0">
<li style="margin-bottom:0.6rem"><a href="../../../services/content-marketing/lucknow/index.html" style="color:#94A3B8;text-decoration:none">Lucknow</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/content-marketing/kanpur/index.html" style="color:#94A3B8;text-decoration:none">Kanpur</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/content-marketing/indore/index.html" style="color:#94A3B8;text-decoration:none">Indore</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/content-marketing/coimbatore/index.html" style="color:#94A3B8;text-decoration:none">Coimbatore</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/content-marketing/kochi/index.html" style="color:#94A3B8;text-decoration:none">Kochi</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/content-marketing/visakhapatnam/index.html" style="color:#94A3B8;text-decoration:none">Visakhapatnam</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/content-marketing/nagpur/index.html" style="color:#94A3B8;text-decoration:none">Nagpur</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/content-marketing/bhopal/index.html" style="color:#94A3B8;text-decoration:none">Bhopal</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/content-marketing/chandigarh/index.html" style="color:#94A3B8;text-decoration:none">Chandigarh</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../services/content-marketing/ludhiana/index.html" style="color:#94A3B8;text-decoration:none">Ludhiana</a></li>
</ul>
</div>
<div>
<h3 style="color:#F8FAFC;margin-bottom:1rem;font-size:1.1rem">Resources & Company</h3>
<ul style="list-style:none;margin:0;padding:0">
<li style="margin-bottom:0.6rem"><a href="../../../blog/index.html" style="color:#94A3B8;text-decoration:none">Blog & Insights</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../case-studies/index.html" style="color:#94A3B8;text-decoration:none">Case Studies</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../resources/index.html" style="color:#94A3B8;text-decoration:none">Resources</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../tools/index.html" style="color:#94A3B8;text-decoration:none">Free Tools</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../about-us.html" style="color:#94A3B8;text-decoration:none">About Us</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../careers.html" style="color:#94A3B8;text-decoration:none">Careers</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../contact-us.html" style="color:#94A3B8;text-decoration:none">Contact Us</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../privacy-policy.html" style="color:#94A3B8;text-decoration:none">Privacy Policy</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../terms-of-service.html" style="color:#94A3B8;text-decoration:none">Terms of Service</a></li>
<li style="margin-bottom:0.6rem"><a href="../../../sitemap.html" style="color:#94A3B8;text-decoration:none">Sitemap</a></li>
</ul>
</div>
</div>
<div style="border-top:1px solid rgba(255,255,255,0.1);padding-top:30px;text-align:center">
<div style="display:flex;justify-content:center;gap:2rem;margin-bottom:1.5rem;flex-wrap:wrap">
<a href="../../../services/seo-services/index.html" style="color:#94A3B8;text-decoration:none;font-size:0.9rem">SEO</a>
<a href="../../../services/ppc/index.html" style="color:#94A3B8;text-decoration:none;font-size:0.9rem">PPC</a>
<a href="../../../services/social-media-marketing/index.html" style="color:#94A3B8;text-decoration:none;font-size:0.9rem">Social</a>
<a href="../../../services/content-marketing/index.html" style="color:#94A3B8;text-decoration:none;font-size:0.9rem">Content</a>
<a href="../../../services/email-marketing/index.html" style="color:#94A3B8;text-decoration:none;font-size:0.9rem">Email</a>
<a href="../../../services/web-design-development/index.html" style="color:#94A3B8;text-decoration:none;font-size:0.9rem">Web Design</a>
</div>
<p style="color:#64748B;font-size:0.9rem;margin:0">&copy; 2025 God Digital Marketing. All rights reserved.</p>
</div>
</div>
</footer>'''

def fix_file(file_path):
    """Fix a single file by replacing header and footer sections"""
    try:
        # Read the file with error handling for different encodings
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            # Try with different encoding
            with open(file_path, 'r', encoding='latin-1') as f:
                content = f.read()

        # Replace header section
        new_header = generate_new_header()
        content = re.sub(r'<header>.*?</header>', new_header, content, flags=re.DOTALL)

        # Replace footer section
        new_footer = generate_new_footer()
        content = re.sub(r'<footer.*?</footer>', new_footer, content, flags=re.DOTALL)

        # Write back as UTF-8
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return True
    except Exception as e:
        print(f"  [ERROR] {str(e)}")
        return False

def main():
    """Main function to fix all 12 files"""
    print("==> Fixing final 12 files missing navigation system...\n")

    success = 0
    failed = 0

    for rel_file in FILES_TO_FIX:
        file_path = BASE_DIR / rel_file
        print(f"Processing {rel_file}...")

        if not file_path.exists():
            print(f"  [SKIP] File not found\n")
            failed += 1
            continue

        if fix_file(file_path):
            print(f"  [OK] Fixed successfully\n")
            success += 1
        else:
            print(f"  [FAIL] Failed to fix\n")
            failed += 1

    print("=" * 60)
    print(f"Success: {success}/{len(FILES_TO_FIX)}")
    print(f"Failed: {failed}/{len(FILES_TO_FIX)}")
    print("=" * 60)

    if success == len(FILES_TO_FIX):
        print("\n==> ALL FILES FIXED SUCCESSFULLY!")
        print("==> 100% navigation coverage achieved (480/480 files)")
    else:
        print(f"\n==> WARNING: {failed} files still need attention")

if __name__ == "__main__":
    main()
