import re

with open(r'C:\Users\DELL.000\Desktop\QR_CodeDemo\reviewflow_clone\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace src="assets/... with src="https://reviewflowai.in/assets/...
html = re.sub(r'src="(/)?(assets|uploads|img|js)', r'src="https://reviewflowai.in/\2', html)
html = re.sub(r'href="(/)?(assets|uploads|img)', r'href="https://reviewflowai.in/\2', html)

with open(r'C:\Users\DELL.000\Desktop\QR_CodeDemo\reviewflow_clone\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Paths updated.")
