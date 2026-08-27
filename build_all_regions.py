import os
import random

SITE_NAME = "블레스바디"
BASE_URL = "https://blissbody.netlify.app"

# 5개 업체 원본 데이터 (이미지 URL 포함)
VENDORS = [
    {
        "name": "미인클럽테라피",
        "phone": "0507-1280-3193",
        "image": "https://images.unsplash.com/photo-1544161515-4ab6ce6db874?auto=format&fit=crop&w=800&q=80",
        "tagline": "★ {region_title} 전 지역 30분 내 신속 방문 케어 지원",
        "courses": "시그니처 바디케어, 프리미엄 아로마 힐링 코스",
        "features": "전문 자격 관리사, 천연 에센셜 오일, 맞춤 릴렉싱 컨디셔닝"
    },
    {
        "name": "혼혈스웨디시테라피",
        "phone": "0507-1280-3334",
        "image": "https://images.unsplash.com/photo-1519823551278-64ac92734fb1?auto=format&fit=crop&w=800&q=80",
        "tagline": "★ 감성적이고 부드러운 스페셜 림프 & 스웨디시 케어",
        "courses": "스웨디시 딥티슈 케어, 전신 림프 순환 프로그램",
        "features": "24시간 운영, 1:1 맞춤 프라이빗 테라피, 철저한 소독 관리"
    },
    {
        "name": "한국골든테라피",
        "phone": "0507-1280-3361",
        "image": "https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?auto=format&fit=crop&w=800&q=80",
        "tagline": "★ 실력파 한국인 전문 테라피스트의 품격 있는 골든 케어",
        "courses": "VIP 골든 힐링 코스, 맞춤형 근육 이완 케어, 센슈얼 아로마",
        "features": "베테랑 한국인 관리사 항시 대기, 투명한 정찰제 시스템"
    },
    {
        "name": "기쁨조테라피",
        "phone": "0507-1280-3223",
        "image": "https://images.unsplash.com/photo-1600334089648-b0d9d3028eb2?auto=format&fit=crop&w=800&q=80",
        "tagline": "★ 하루의 피로와 스트레스를 풀어주는 활력 집중 케어",
        "courses": "스페셜 콤보 힐링 케어, 호텔식 VIP 1:1 집중 관리",
        "features": "{region_title} 신속 출동, 고객 맞춤형 압 조절 및 피로회복"
    },
    {
        "name": "한국미인테라피",
        "phone": "0507-1280-3303",
        "image": "https://images.unsplash.com/photo-1515377905703-c4788e51af15?auto=format&fit=crop&w=800&q=80",
        "tagline": "★ 친절하고 섬세한 힐링 테라피, 안심 후불제 운영",
        "courses": "클래식 테라피, 습식 프리미엄 아로마, 전신 스페셜 코스",
        "features": "합리적이고 투명한 요금 구성, 정성 가득한 일대일 고객 응대"
    }
]

# 서울 / 경기 / 인천 전체 지역 데이터
REGIONS = {
    # [서울 25개 구]
    "gangnam": {"name": "서울 강남구", "dongs": ["역삼동", "개포동", "청담동", "삼성동", "대치동", "신사동", "논현동", "압구정동", "세곡동", "자곡동", "일원동", "수서동", "도곡동"]},
    "gangdong": {"name": "서울 강동구", "dongs": ["명일동", "고덕동", "상일동", "길동", "둔촌동", "암사동", "성내동", "천호동", "강일동"]},
    "gangbuk": {"name": "서울 강북구", "dongs": ["미아동", "번동", "수유동", "우이동"]},
    "gangseo": {"name": "서울 강서구", "dongs": ["염창동", "등촌동", "화곡동", "가양동", "마곡동", "공항동", "방화동"]},
    "gwanak": {"name": "서울 관악구", "dongs": ["봉천동", "신림동", "남현동", "보라매동", "청룡동", "낙성대동"]},
    "gwangjin": {"name": "서울 광진구", "dongs": ["중곡동", "능동", "구의동", "광장동", "자양동", "화양동", "군자동"]},
    "guro": {"name": "서울 구로구", "dongs": ["신도림동", "구로동", "가리봉동", "고척동", "개봉동", "오류동", "항동", "온수동"]},
    "geumcheon": {"name": "서울 금천구", "dongs": ["가산동", "독산동", "시흥동"]},
    "nowon": {"name": "서울 노원구", "dongs": ["월계동", "공릉동", "하계동", "상계동", "중계동"]},
    "dobong": {"name": "서울 도봉구", "dongs": ["쌍문동", "방학동", "창동", "도봉동"]},
    "dongdaemun": {"name": "서울 동대문구", "dongs": ["용두동", "제기동", "전농동", "답십리동", "장안동", "청량리동", "회기동", "이문동"]},
    "dongjak": {"name": "서울 동작구", "dongs": ["노량진동", "상도동", "흑석동", "동작동", "사당동", "대방동", "신대방동"]},
    "mapo": {"name": "서울 마포구", "dongs": ["아현동", "공덕동", "도화동", "합정동", "망원동", "연남동", "성산동", "상암동", "서교동"]},
    "seodaemun": {"name": "서울 서대문구", "dongs": ["충정로", "천연동", "연희동", "홍제동", "홍은동", "남가좌동", "북가좌동", "신촌"]},
    "seocho": {"name": "서울 서초구", "dongs": ["서초동", "잠원동", "반포동", "방배동", "양재동", "우면동", "내곡동"]},
    "seongdong": {"name": "서울 성동구", "dongs": ["왕십리", "마장동", "사근동", "행당동", "응봉동", "금호동", "옥수동", "성수동"]},
    "seongbuk": {"name": "서울 성북구", "dongs": ["성북동", "돈암동", "안암동", "보문동", "정릉동", "길음동", "종암동", "월곡동", "장위동"]},
    "songpa": {"name": "서울 송파구", "dongs": ["잠실동", "신천동", "풍납동", "송파동", "석촌동", "삼전동", "가락동", "문정동", "장지동", "방이동", "오금동"]},
    "yangcheon": {"name": "서울 양천구", "dongs": ["목동", "신월동", "신정동"]},
    "yeongdeungpo": {"name": "서울 영등포구", "dongs": ["영등포동", "여의도동", "당산동", "도림동", "문래동", "양평동", "신길동", "대림동"]},
    "yongsan": {"name": "서울 용산구", "dongs": ["후암동", "용산동", "남영동", "청파동", "효창동", "한강로동", "이촌동", "이태원동", "한남동", "보광동"]},
    "eunpyeong": {"name": "서울 은평구", "dongs": ["녹번동", "불광동", "갈현동", "구산동", "대조동", "응암동", "역촌동", "신사동", "진관동"]},
    "jongno": {"name": "서울 종로구", "dongs": ["청운동", "효자동", "사직동", "삼청동", "부암동", "평창동", "가회동", "혜화동", "명륜동"]},
    "junggu": {"name": "서울 중구", "dongs": ["소공동", "회현동", "명동", "필동", "장충동", "을지로동", "신당동", "약수동", "황학동"]},
    "jungnang": {"name": "서울 중랑구", "dongs": ["면목동", "상봉동", "중화동", "묵동", "망우동", "신내동"]},

    # [경기 주요 시·구]
    "suwon": {"name": "경기 수원시", "dongs": ["팔달구", "영통구", "장안구", "권선구", "인계동", "매탄동", "광교동", "영통동", "세류동"]},
    "seongnam": {"name": "경기 성남시", "dongs": ["분당구", "수정구", "중원구", "서현동", "야탑동", "정자동", "판교동", "수내동", "금곡동"]},
    "goyang": {"name": "경기 고양시", "dongs": ["일산동구", "일산서구", "덕양구", "백석동", "마두동", "주엽동", "화정동", "행신동", "삼송동"]},
    "yongin": {"name": "경기 용인시", "dongs": ["수지구", "기흥구", "처인구", "풍덕천동", "죽전동", "동백동", "신갈동", "보정동", "상현동"]},
    "bucheon": {"name": "경기 부천시", "dongs": ["원미동", "심곡동", "중동", "상동", "소사본동", "괴안동", "오정동", "역곡동"]},
    "ansan": {"name": "경기 안산시", "dongs": ["단원구", "상록구", "고잔동", "중앙동", "초지동", "본오동", "선부동", "와동"]},
    "anyang": {"name": "경기 안양시", "dongs": ["만안구", "동안구", "평촌동", "범계동", "비산동", "안양동", "석수동", "호계동", "관양동"]},
    "namyangju": {"name": "경기 남양주시", "dongs": ["다산동", "별내동", "와부읍", "진접읍", "화도읍", "평내동", "호평동", "오남읍"]},
    "hwaseong": {"name": "경기 화성시", "dongs": ["동탄1동", "동탄2동", "향남읍", "남양읍", "봉담읍", "병점동", "반송동", "청계동"]},
    "pyeongtaek": {"name": "경기 평택시", "dongs": ["고덕동", "비전동", "세교동", "안중읍", "포승읍", "송탄동", "서정동"]},
    "uijeongbu": {"name": "경기 의정부시", "dongs": ["의정부동", "호원동", "장암동", "신곡동", "송산동", "자금동", "가능동", "민락동"]},
    "siheung": {"name": "경기 시흥시", "dongs": ["정왕동", "배곧동", "은계동", "목감동", "신천동", "대야동", "은행동", "장현동"]},
    "paju": {"name": "경기 파주시", "dongs": ["운정동", "교하동", "금촌동", "문산읍", "야당동", "동패동", "와동동"]},
    "gimpo": {"name": "경기 김포시", "dongs": ["구래동", "장기동", "운양동", "사우동", "풍무동", "걸포동", "마산동"]},
    "gwangmyeong": {"name": "경기 광명시", "dongs": ["철산동", "하안동", "소하동", "일직동", "광명동"]},
    "gwangju-gy": {"name": "경기 광주시", "dongs": ["경안동", "송정동", "태전동", "오포읍", "초월읍", "곤지암읍"]},
    "gunpo": {"name": "경기 군포시", "dongs": ["산본동", "금정동", "당동", "당정동", "대야미동", "부곡동"]},
    "hanam": {"name": "경기 하남시", "dongs": ["미사동", "위례동", "신장동", "덕풍동", "감일동", "풍산동"]},
    "osan": {"name": "경기 오산시", "dongs": ["원동", "궐동", "오산동", "세교동", "수청동", "갈곶동"]},
    "icheon": {"name": "경기 이천시", "dongs": ["창전동", "관고동", "증포동", "부발읍", "안흥동"]},

    # [인천 주요 구]
    "bupyeong": {"name": "인천 부평구", "dongs": ["부평동", "십정동", "산곡동", "청천동", "삼산동", "갈산동", "부개동"]},
    "namdong": {"name": "인천 남동구", "dongs": ["구월동", "간석동", "만수동", "논현동", "서창동", "도림동"]},
    "incheon-seo": {"name": "인천 서구", "dongs": ["청라동", "루원시티", "가정동", "석남동", "검암동", "당하동", "원당동", "검단동"]},
    "yeonsu": {"name": "인천 연수구", "dongs": ["송도동", "연수동", "동춘동", "옥련동", "청학동", "선학동"]},
    "michuhol": {"name": "인천 미추홀구", "dongs": ["주안동", "도화동", "숭의동", "용현동", "학익동", "관교동", "문학동"]},
    "incheon-jung": {"name": "인천 중구", "dongs": ["영종동", "운서동", "하늘도시", "신포동", "연안동", "북성동"]},
    "gyeyang": {"name": "인천 계양구", "dongs": ["계산동", "작전동", "효성동", "임학동", "박촌동", "동양동"]},
    "incheon-dong": {"name": "인천 동구", "dongs": ["송림동", "송현동", "화수동", "만석동"]}
}

def generate_sub_pages():
    total_created = 0

    for folder, data in REGIONS.items():
        os.makedirs(folder, exist_ok=True)
        
        region_title = data["name"]
        dongs = data["dongs"]
        page_url = f"{BASE_URL}/{folder}/"
        
        dong_keywords = ", ".join([f"{region_title} {d} 출장마사지" for d in dongs])
        dong_badges = "".join([f'<span class="dong-tag">{d} 출장마사지</span>' for d in dongs])
        
        # 5개 업체를 매 지역마다 무작위 순서로 셔플
        shuffled_vendors = random.sample(VENDORS, len(VENDORS))
        
        vendor_html_blocks = []
        for idx, vendor in enumerate(shuffled_vendors, start=1):
            tagline_formatted = vendor["tagline"].format(region_title=region_title)
            features_formatted = vendor["features"].format(region_title=region_title)
            
            block = f"""
        <!-- 업체 {idx}: {vendor['name']} -->
        <div class="vendor-card">
            <img src="{vendor['image']}" alt="{region_title} {vendor['name']} 출장마사지" class="vendor-img">
            <div class="vendor-body">
                <div class="vendor-header">
                    <div>
                        <span class="vendor-badge">추천 0{idx}</span>
                        <span class="vendor-title">{vendor['name']}</span>
                    </div>
                    <div class="vendor-tagline">{tagline_formatted}</div>
                </div>
                <div class="info-row">
                    <div class="info-label">제공 코스</div>
                    <div class="info-content">{vendor['courses']}</div>
                </div>
                <div class="info-row">
                    <div class="info-label">매장 특징</div>
                    <div class="info-content">{features_formatted}</div>
                </div>
                <a href="tel:{vendor['phone']}" class="call-btn">📞 전화 문의 : {vendor['phone']}</a>
            </div>
        </div>"""
            vendor_html_blocks.append(block)

        vendors_rendered = "\n".join(vendor_html_blocks)

        html_code = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{region_title} 출장마사지 & 24시 홈타이 테라피 - {SITE_NAME}</title>
    <meta name="description" content="{region_title} 전 지역 신속 30분 방문 출장마사지 전문 {SITE_NAME}. 타이, 아로마, 스웨디시 1:1 맞춤 프리미엄 홈케어 예약.">
    <meta name="keywords" content="{region_title} 출장마사지, {region_title} 홈타이, {region_title} 스웨디시, {dong_keywords}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{page_url}">
    
    <meta property="og:type" content="website">
    <meta property="og:title" content="{region_title} 출장마사지 - {SITE_NAME}">
    <meta property="og:description" content="{region_title} 전 지역 24시간 1:1 맞춤 출장마사지 및 프라이빗 힐링 케어">
    <meta property="og:image" content="{shuffled_vendors[0]['image']}">
    <meta property="og:url" content="{page_url}">

    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Noto Sans KR', sans-serif; }}
        body {{ background-color: #0f1117; color: #e1e3e8; line-height: 1.6; padding-bottom: 40px; }}
        a {{ text-decoration: none; color: inherit; }}
        header {{ background: #161821; padding: 18px 20px; text-align: center; border-bottom: 2px solid #d4af37; position: sticky; top: 0; z-index: 100; }}
        header h1 {{ font-size: 1.3rem; color: #ffffff; }}
        header h1 span {{ color: #d4af37; }}
        .hero {{ background: linear-gradient(rgba(15,17,23,0.8), rgba(15,17,23,0.9)), url('https://images.unsplash.com/photo-1544161515-4ab6ce6db874?auto=format&fit=crop&w=1200&q=80') center/cover; padding: 45px 20px; text-align: center; border-bottom: 1px solid #2a2d37; }}
        .hero h2 {{ font-size: 1.5rem; color: #fff; margin-bottom: 8px; }}
        .hero p {{ font-size: 0.92rem; color: #d4af37; }}
        .container {{ max-width: 850px; margin: 0 auto; padding: 20px 15px; }}
        .section-title {{ font-size: 1.2rem; color: #ffffff; margin: 25px 0 15px 0; border-left: 4px solid #d4af37; padding-left: 10px; font-weight: 700; }}
        
        .vendor-card {{ background: #161821; border: 1px solid #2a2d37; border-radius: 12px; overflow: hidden; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.4); }}
        .vendor-img {{ width: 100%; height: 200px; object-fit: cover; display: block; }}
        .vendor-body {{ padding: 18px 20px; }}
        .vendor-header {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #2a2d37; padding-bottom: 10px; margin-bottom: 12px; flex-wrap: wrap; gap: 6px; }}
        .vendor-badge {{ background: #d4af37; color: #161821; font-size: 0.75rem; font-weight: bold; padding: 3px 8px; border-radius: 4px; }}
        .vendor-title {{ font-size: 1.15rem; color: #ffffff; font-weight: bold; }}
        .vendor-tagline {{ color: #2ecc71; font-size: 0.85rem; width: 100%; margin-top: 3px; font-weight: 600; }}
        .info-row {{ display: flex; font-size: 0.88rem; margin-bottom: 6px; }}
        .info-label {{ width: 85px; color: #d4af37; font-weight: bold; flex-shrink: 0; }}
        .info-content {{ color: #bbbfca; }}
        .call-btn {{ display: block; text-align: center; background: linear-gradient(135deg, #d4af37, #aa820a); color: #111; font-weight: bold; padding: 12px; border-radius: 6px; font-size: 0.95rem; margin-top: 14px; text-decoration: none; }}

        .card {{ background: #161821; border: 1px solid #2a2d37; border-radius: 12px; padding: 20px; margin-top: 25px; }}
        .card h3 {{ color: #d4af37; font-size: 1.1rem; margin-bottom: 10px; border-left: 4px solid #d4af37; padding-left: 8px; }}
        .dong-wrap {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px; }}
        .dong-tag {{ background: #1f2330; border: 1px solid #32384a; color: #e1e3e8; padding: 6px 12px; border-radius: 20px; font-size: 0.82rem; }}
        .back-btn {{ display: inline-block; background: #222634; color: #bbb; padding: 8px 16px; border-radius: 6px; font-size: 0.85rem; margin-top: 20px; }}
        footer {{ text-align: center; padding: 20px; font-size: 0.8rem; color: #777; border-top: 1px solid #2a2d37; margin-top: 30px; }}
    </style>
</head>
<body>
    <header>
        <h1>{region_title} 출장마사지 <span>{SITE_NAME}</span></h1>
    </header>

    <div class="hero">
        <h2>{region_title} 전 지역 신속 방문 출장마사지</h2>
        <p>고객님이 계신 편안한 공간으로 전문 테라피스트가 직접 찾아갑니다</p>
    </div>

    <div class="container">
        
        <h2 class="section-title">{region_title} 추천 테라피 매장 안내</h2>

{vendors_rendered}

        <!-- 세부 동 안내 카드 -->
        <div class="card">
            <h3>{region_title} 출장마사지 세부 서비스 구역</h3>
            <p>{region_title} 내 모든 동 및 인근 권역까지 30분 내 빠른 배정이 가능합니다.</p>
            <div class="dong-wrap">
                {dong_badges}
            </div>
        </div>

        <div style="text-align: center;">
            <a href="/" class="back-btn">← 메인 홈으로 돌아가기</a>
        </div>
    </div>

    <footer>
        <p>© {SITE_NAME}. All rights reserved.</p>
    </footer>
</body>
</html>
"""
        file_path = os.path.join(folder, "index.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_code)
        total_created += 1

    print(f"🎉 총 {total_created}개 지역 페이지에 이미지 포함 + 랜덤 배치가 완료되었습니다!")

if __name__ == "__main__":
    generate_sub_pages()