#!/usr/bin/env python3
"""
AnilCloudLab index.html Auto-Fixer
===================================
Applies 3 fixes to resolve Google Search Console JS errors and improve SEO.

Usage:
  1. Place this script in the SAME folder as your index.html
  2. Run: python3 fix_index.py
  3. Commit and push the updated index.html to GitHub
  4. Request Indexing again in Google Search Console

Fixes applied:
  Fix 1: SEO Meta Tags (description, keywords, canonical, Open Graph)
  Fix 2: Countdown HTML elements (fixes 86+ JS null reference errors)
  Fix 3: Title optimization with "anilcloudlab" keyword
"""

import os
import sys
import shutil
from datetime import datetime

def main():
    filepath = "index.html"
    
    if not os.path.exists(filepath):
        print(f"❌ ERROR: '{filepath}' not found!")
        print("   Place this script in the same folder as your index.html")
        sys.exit(1)
    
    # Read original
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Backup
    backup = f"index_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    shutil.copy2(filepath, backup)
    print(f"✅ Backup created: {backup}")
    
    fixes_applied = 0
    
    # =========================================
    # FIX 1: SEO Meta Tags
    # =========================================
    seo_meta = '''<meta name="description" content="AnilCloudLab - India's leading DevOps, DevSecOps & Multi-Cloud Training Institute. Real-time project-based courses with 100% Placement Assurance. Live online classes for Australia, US, Canada, Singapore & Germany professionals. ₹80,000 all-inclusive.">
<meta name="keywords" content="anilcloudlab, devops training, devsecops training, multi-cloud training, AWS training, Azure training, kubernetes training, devops course hyderabad, cloud computing course, placement assurance, anilcloudlab devops">
<link rel="canonical" href="https://anilcloudlab.github.io/" />
<meta property="og:title" content="AnilCloudLab DevOps Consulting | Real-Time Project-Based Training | 100% Placement Assurance">
<meta property="og:description" content="Advanced DevOps, DevSecOps & Multi-Cloud Training with real production projects. 100% Placement Assurance. Designed for international professionals.">
<meta property="og:url" content="https://anilcloudlab.github.io/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="AnilCloudLab DevOps Consulting">
<meta name="robots" content="index, follow">
<meta name="author" content="AnilCloudLab DevOps Consulting">'''

    # Check if SEO meta already exists
    if '<meta name="description"' not in content:
        # Insert after google-site-verification meta tag
        marker = '<meta name="google-site-verification"'
        if marker in content:
            # Find the end of that line
            idx = content.index(marker)
            line_end = content.index("\n", idx)
            content = content[:line_end+1] + seo_meta + "\n" + content[line_end+1:]
            fixes_applied += 1
            print("✅ Fix 1: SEO Meta Tags ADDED (description, canonical, Open Graph)")
        else:
            # Insert after <head> tag
            content = content.replace("<head>", "<head>\n" + seo_meta, 1)
            fixes_applied += 1
            print("✅ Fix 1: SEO Meta Tags ADDED after <head>")
    else:
        print("⏭️  Fix 1: SEO Meta Tags already exist — SKIPPED")

    # =========================================
    # FIX 2: Countdown HTML Elements
    # =========================================
    countdown_html = '<span class="countdown"><span class="cd-u" id="cd-d">0d</span><span class="cd-u" id="cd-h">0h</span><span class="cd-u" id="cd-m">0m</span><span class="cd-u" id="cd-s">0s</span></span>'
    
    if 'id="cd-d"' not in content:
        # Find the top-bar-offer span closing tag and insert after it
        marker = '</span>\n<button class="grab-btn"'
        # Try to find the top-bar-offer context
        if 'top-bar-offer' in content:
            # Find closing of top-bar-offer span
            offer_idx = content.index('top-bar-offer')
            # Find the </span> after it
            span_end = content.index('</span>', offer_idx)
            insert_pos = span_end + len('</span>')
            content = content[:insert_pos] + "\n" + countdown_html + content[insert_pos:]
            fixes_applied += 1
            print("✅ Fix 2: Countdown HTML elements ADDED (cd-d, cd-h, cd-m, cd-s)")
        else:
            print("⚠️  Fix 2: Could not find 'top-bar-offer' — MANUAL FIX NEEDED")
            print("   Add this line after the top-bar-offer span:")
            print(f"   {countdown_html}")
    else:
        print("⏭️  Fix 2: Countdown elements already exist — SKIPPED")

    # =========================================
    # FIX 3: Title Optimization
    # =========================================
    new_title = '<title>AnilCloudLab — DevOps, DevSecOps & Multi-Cloud Training | Real-Time Projects | 100% Placement Assurance</title>'
    
    if '<title>' in content and 'AnilCloudLab —' not in content:
        import re
        content = re.sub(r'<title>.*?</title>', new_title, content, count=1)
        fixes_applied += 1
        print("✅ Fix 3: Title UPDATED with 'AnilCloudLab' keyword")
    else:
        print("⏭️  Fix 3: Title already optimized — SKIPPED")

    # =========================================
    # Write fixed file
    # =========================================
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"\n{'='*50}")
    print(f"🎉 DONE! {fixes_applied} fix(es) applied to index.html")
    print(f"📁 Backup saved as: {backup}")
    print(f"{'='*50}")
    
    if fixes_applied > 0:
        print("\n📋 Next Steps:")
        print("   1. git add index.html")
        print("   2. git commit -m 'Fix JS errors + SEO meta tags'")
        print("   3. git push origin main")
        print("   4. Google Search Console → Request Indexing")
        print("   5. Wait 1-3 days for ranking update")
    else:
        print("\n✨ All fixes were already applied!")

if __name__ == "__main__":
    main()
