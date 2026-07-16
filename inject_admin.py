import re

file_path = r'C:\Users\DELL.000\Desktop\QR_CodeDemo\reviewflow_clone\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# The script to inject
admin_script = """
    <!-- Admin Upgrade Features -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // 1. Inject Admin Dashboard Button to the bottom right
            const adminBtn = document.createElement('a');
            adminBtn.href = 'admin.html';
            adminBtn.innerHTML = '<i class="fa-solid fa-lock"></i> Admin';
            adminBtn.style.cssText = 'position: fixed; bottom: 20px; right: 20px; background: var(--gray-900); color: white; padding: 10px 20px; border-radius: 50px; font-weight: bold; text-decoration: none; z-index: 9999; box-shadow: 0 4px 12px rgba(0,0,0,0.2); font-size: 0.85rem; display: flex; align-items: center; gap: 8px; font-family: "Plus Jakarta Sans", sans-serif; transition: all 0.2s ease;';
            
            adminBtn.onmouseover = () => { adminBtn.style.transform = 'translateY(-2px)'; };
            adminBtn.onmouseout = () => { adminBtn.style.transform = 'translateY(0)'; };
            
            document.body.appendChild(adminBtn);

            // 2. Add Inline Editing (CMS Mode) toggle button
            const cmsBtn = document.createElement('button');
            cmsBtn.innerHTML = '<i class="fa-solid fa-pen-to-square"></i> Edit Mode';
            cmsBtn.style.cssText = 'position: fixed; bottom: 70px; right: 20px; background: var(--green-600); color: white; padding: 10px 20px; border-radius: 50px; border: none; cursor: pointer; font-weight: bold; z-index: 9999; box-shadow: 0 4px 12px rgba(52,168,83,0.3); font-size: 0.85rem; display: flex; align-items: center; gap: 8px; font-family: "Plus Jakarta Sans", sans-serif; transition: all 0.2s ease;';
            
            cmsBtn.onmouseover = () => { cmsBtn.style.transform = 'translateY(-2px)'; };
            cmsBtn.onmouseout = () => { cmsBtn.style.transform = 'translateY(0)'; };

            let editMode = false;
            cmsBtn.onclick = () => {
                editMode = !editMode;
                const textElements = document.querySelectorAll('h1, h2, h3, p, span');
                
                if (editMode) {
                    cmsBtn.innerHTML = '<i class="fa-solid fa-check"></i> Save Changes';
                    cmsBtn.style.background = '#F59E0B'; // Amber
                    textElements.forEach(el => {
                        el.contentEditable = "true";
                        el.style.border = "1px dashed var(--green-400)";
                        el.style.padding = "2px";
                    });
                } else {
                    cmsBtn.innerHTML = '<i class="fa-solid fa-pen-to-square"></i> Edit Mode';
                    cmsBtn.style.background = 'var(--green-600)';
                    textElements.forEach(el => {
                        el.contentEditable = "false";
                        el.style.border = "none";
                        el.style.padding = "0";
                    });
                    // Simulate saving to DB
                    alert('Changes saved successfully to database!');
                }
            };
            document.body.appendChild(cmsBtn);
        });
    </script>
</body>
"""

# Replace </body> with the injected script + </body>
if '<!-- Admin Upgrade Features -->' not in html:
    html = html.replace('</body>', admin_script)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Injected admin features successfully.")
else:
    print("Admin features already injected.")
