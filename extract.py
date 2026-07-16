import re

with open(r'C:\Users\DELL.000\Desktop\QR_CodeDemo\reviewflow_original.html', 'r', encoding='utf-8') as f:
    html = f.read()

styles = re.findall(r'<style>(.*?)</style>', html, re.DOTALL)
css_content = '\n'.join(styles)

# Remove the inline styles and inject a link to index.css if not already present
new_html = re.sub(r'<style>.*?</style>', '<link rel="stylesheet" href="index.css">', html, flags=re.DOTALL)

# Since original uses <script> inline, let's extract that too or leave it. We will leave JS inline for now.
# Replace any absolute paths to assets if they don't load, but let's just save for now.
with open(r'C:\Users\DELL.000\Desktop\QR_CodeDemo\reviewflow_clone\index.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

with open(r'C:\Users\DELL.000\Desktop\QR_CodeDemo\reviewflow_clone\index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Extraction complete.")
