import os
from datetime import datetime

domain = "https://blissbody.netlify.app"
today = datetime.now().strftime("%Y-%m-%d")

# 1. robots.txt 생성
robots_content = f"User-agent: *\nAllow: /\n\nSitemap: {domain}/sitemap.xml\n"
with open("robots.txt", "w", encoding="utf-8") as f:
    f.write(robots_content)
print("✅ robots.txt 생성 완료!")

# 2. sitemap.xml 생성
sitemap_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
]

added_urls = set()

for root, dirs, files in os.walk("."):
    # 숨김 폴더나 가상환경 등 제외
    dirs[:] = [d for d in dirs if not d.startswith((".", "_"))]
    
    for file in files:
        if file.endswith(".html"):
            rel_dir = os.path.relpath(root, ".").replace("\\", "/")
            
            if rel_dir == "." and file == "index.html":
                url = f"{domain}/"
                priority = "1.0"
            elif file == "index.html":
                url = f"{domain}/{rel_dir}/"
                priority = "0.9"
            else:
                url = f"{domain}/{file}" if rel_dir == "." else f"{domain}/{rel_dir}/{file}"
                priority = "0.8"

            if url not in added_urls:
                added_urls.add(url)
                sitemap_lines.append(f"  <url>\n    <loc>{url}</loc>\n    <lastmod>{today}</lastmod>\n    <priority>{priority}</priority>\n  </url>")

sitemap_lines.append('</urlset>')

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write("\n".join(sitemap_lines))

print("✅ sitemap.xml 생성 완료!")