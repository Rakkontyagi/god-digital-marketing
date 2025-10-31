#!/usr/bin/env python3
"""
Fix the remaining 5 files with different HTML structure
"""

import re
from pathlib import Path

BASE_DIR = Path(r"C:\Users\dell\Documents\God digital marketing website 2")

FILES = [
    "services/content-marketing/thrissur/index.html",
    "services/content-marketing/tiruchirappalli/index.html",
    "services/content-marketing/tirunelveli/index.html",
    "services/content-marketing/udaipur/index.html",
    "services/content-marketing/vijayawada/index.html",
]

def generate_new_header_section():
    """Generate the entire header section"""
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
                </div>
            </div>
            <div class="dropdown-section">
                <h4>Top Cities</h4>
                <div class="dropdown-grid">
                    <a href="../../../services/seo-services/mumbai/index.html">Mumbai</a>
                    <a href="../../../services/seo-services/bangalore/index.html">Bangalore</a>
                    <a href="../../../services/seo-services/delhi/index.html">Delhi NCR</a>
                    <a href="../../../services/seo-services/chennai/index.html">Chennai</a>
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
                </div>
            </div>
        </div>
    </li>
    <li><a href="../../../about-us.html">About</a></li>
    <li><a href="../../../contact-us.html">Contact</a></li>
</ul>
</nav>
</header>'''

def fix_file(file_path):
    """Fix a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace header section
        header_pattern = r'<header>.*?</header>'
        new_header = generate_new_header_section()

        new_content = re.sub(header_pattern, new_header, content, flags=re.DOTALL)

        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True
    except Exception as e:
        print(f"  [ERROR] {str(e)}")
        return False

def main():
    """Main function"""
    print("==> Fixing remaining 5 files with different structure...")

    success = 0
    failed = 0

    for rel_file in FILES:
        file_path = BASE_DIR / rel_file
        print(f"Processing {rel_file}...")

        if fix_file(file_path):
            print(f"  [OK] Fixed successfully\n")
            success += 1
        else:
            print(f"  [FAIL] Failed\n")
            failed += 1

    print("=" * 60)
    print(f"Success: {success}/{len(FILES)}")
    print(f"Failed: {failed}/{len(FILES)}")
    print("=" * 60)

if __name__ == "__main__":
    main()
