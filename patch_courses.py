#!/usr/bin/env python3
"""
AnilCloudLab - All Courses Page Patcher
Run this script on your original index.html to apply the courses page updates.
Usage: python3 patch_courses.py index.html
"""
import sys
import re

if len(sys.argv) < 2:
    print("Usage: python3 patch_courses.py index.html")
    sys.exit(1)

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    html = f.read()

# Read patch files
import os, pathlib
base = pathlib.Path(__file__).parent

with open(base / 'page_div.html') as f:
    new_courses_page = f.read()
with open(base / 'modals.html') as f:
    new_modals = f.read()
with open(base / 'extra_style.css') as f:
    extra_css = f.read()
with open(base / 'extra_script.js') as f:
    extra_js = f.read()

# 1. Inject extra CSS before </style> (first occurrence after :root)
extra_css_block = "\n/* === COURSES PAGE ADDITIONS === */\n" + extra_css
html = html.replace('/* ANIMATIONS */', extra_css_block + '\n/* ANIMATIONS */', 1)

# 2. Replace old #page-courses div
# Find: <div class="page" id="page-courses"> ... </div>
# followed by <!-- PAGE: PLACEMENTS -->
old_courses_pattern = r'<div class="page" id="page-courses">.*?</div>\s*(?=<!-- ===|<!-- PAGE: PLACEMENTS -->)'
match = re.search(old_courses_pattern, html, re.DOTALL)
if match:
    html = html[:match.start()] + new_courses_page + '\n' + html[match.end():]
    print("✅ Courses page section replaced successfully")
else:
    print("⚠️  Could not find courses page section - trying alternate method")
    # Try simpler approach - find by id
    start_marker = '<div class="page" id="page-courses">'
    end_marker = '<!-- PAGE: PLACEMENTS -->'
    start_idx = html.find(start_marker)
    end_idx = html.find(end_marker)
    if start_idx > -1 and end_idx > -1:
        html = html[:start_idx] + new_courses_page + '\n\n' + html[end_idx:]
        print("✅ Courses page replaced (alternate method)")
    else:
        print("❌ ERROR: Could not locate courses section. Please apply manually.")

# 3. Add new modals before </body>
html = html.replace('</body>', new_modals + '\n</body>', 1)
print("✅ Course modals injected")

# 4. Add extra JS at end of existing <script> block (before last </script>)
last_script_close = html.rfind('</script>')
if last_script_close > -1:
    extra_js_block = "\n/* === COURSES PAGE JS === */\n" + extra_js
    html = html[:last_script_close] + extra_js_block + '\n</script>' + html[last_script_close+9:]
    print("✅ JavaScript functions injected")

# Write output
output_file = 'index_patched.html'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n🎉 Done! Output written to: {output_file}")
print("   Review it, then rename to index.html")
