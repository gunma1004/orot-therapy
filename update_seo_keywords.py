import os
import re

SITE_NAME = "블레스바디"

# 서울, 경기, 인천 전체 지역 폴더명 매핑 (영문 폴더명: 한글 지역명)
REGION_MAP = {
    # [서울]
    "dobong": "도봉구", "dongdaemun": "동대문구", "dongjak": "동작구", "eunpyeong": "은평구",
    "gangbuk": "강북구", "gangdong": "강동구", "gangnam": "강남구", "gangse": "강서구",
    "gangseo": "강서구", "geumcheon": "금천구", "guro": "구로구", "gwangjin": "광진구",
    "jongno": "종로구", "junggu": "중구", "jungnang": "중랑구", "mapo": "마포구",
    "nowon": "노원구", "seocho": "서초구", "seodaemun": "서대문구", "seongbuk": "성북구",
    "seongdong": "성동구", "songpa": "송파구", "yangcheon": "양천구", "yeongdeungpo": "영등포구",
    "yongsan": "용산구",

    # [경기]
    "suwon": "수원", "seongnam": "성남", "goyang": "고양 일산", "yongin": "용인",
    "bucheon": "부천", "ansan": "안산", "anyang": "안양", "namyangju": "남양주",
    "hwaseong": "화성 동탄", "pyeongtaek": "평택", "uijeongbu": "의정부", "siheung": "시흥",
    "paju": "파주", "gimpo": "김포", "gwangmyeong": "광명", "gwangju-gy": "경기광주",
    "gunpo": "군포", "hanam": "하남", "osan": "오산", "icheon": "이천",

    # [인천]
    "bupyeong": "인천 부평구", "namdong": "인천 남동구", "incheon-seo": "인천 서구",
    "yeonsu": "인천 연수구 송도", "michuhol": "인천 미추홀구", "incheon-jung": "인천 중구 영종",
    "gyeyang": "인천 계양구", "incheon-dong": "인천 동구"
}

def update_all_html_files():
    current_dir = os.getcwd()
    print(f"📂 작업 대상 경로: {current_dir}\n")
    
    updated_count = 0
    
    for root, dirs, files in os.walk(current_dir):
        # 숨김 폴더(.git 등) 제외
        dirs[:] = [d for d in dirs if not d.startswith((".", "_"))]
        
        for file in files:
            if file.lower().endswith('.html'):
                file_path = os.path.join(root, file)
                norm_path = os.path.normpath(file_path)
                rel_path = os.path.relpath(file_path, current_dir).replace("\\", "/")
                path_parts = [p.lower() for p in norm_path.split(os.sep)]
                
                # 1. 루트 index.html은 출장마사지 제외 규칙이 적용되어 있으므로 건너뜀
                if rel_path == "index.html":
                    print(f"⏩ [스킵 - 메인 페이지] {rel_path}")
                    continue

                # 2. 폴더 경로에서 지역 이름 감지
                region_name = None
                for key, val in REGION_MAP.items():
                    if key in path_parts:
                        region_name = val
                        break

                # 파일 읽기
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except UnicodeDecodeError:
                    try:
                        with open(file_path, 'r', encoding='euc-kr', errors='ignore') as f:
                            content = f.read()
                    except Exception:
                        continue

                # 3. 폴더명 매핑 실패 시 본문에서 '00구' or '00시' 자동 감지
                if not region_name:
                    match = re.search(r'([가-힗]{2,4}[구|시])', content)
                    if match:
                        region_name = match.group(1)
                    else:
                        region_name = "수도권"

                # --- SEO 키워드 교체 (블레스바디 + {지역명} 출장마사지) ---
                
                # <title> 교체
                content = re.sub(
                    r'<title>(.*?)</title>',
                    f'<title>{region_name} 출장마사지 & 24시 홈케어 - {SITE_NAME}</title>',
                    content, flags=re.IGNORECASE | re.DOTALL
                )
                
                # <meta description> 교체
                content = re.sub(
                    r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']\s*/?>',
                    f'<meta name="description" content="{region_name} 출장마사지 및 24시 방문 테라피 전문 추천. {SITE_NAME}의 프라이빗 아로마, 스웨디시 1:1 맞춤 케어를 만나보세요.">',
                    content, flags=re.IGNORECASE | re.DOTALL
                )
                
                # <h1> 메인 타이틀 교체
                content = re.sub(
                    r'<h1>(.*?)</h1>',
                    f'<h1>{region_name} 출장마사지 <span>{SITE_NAME} 24시 방문 케어</span></h1>',
                    content, flags=re.IGNORECASE | re.DOTALL
                )
                
                # Open Graph 타이틀 교체 (존재 시)
                content = re.sub(
                    r'<meta\s+property=["\']og:title["\']\s+content=["\'](.*?)["\']\s*/?>',
                    f'<meta property="og:title" content="{region_name} 출장마사지 - {SITE_NAME}">',
                    content, flags=re.IGNORECASE | re.DOTALL
                )

                # 파일 저장
                try:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    print(f"✅ [교체 완료] {rel_path} ({region_name})")
                    updated_count += 1
                except Exception as e:
                    print(f"❌ [오류] {file_path}: {e}")

    print(f"\n🎉 총 {updated_count}개 지역 서브 페이지의 SEO 키워드 교체가 완료되었습니다!")

if __name__ == "__main__":
    update_all_html_files()