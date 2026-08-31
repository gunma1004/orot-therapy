import os
import re
import random

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

def generate_seo_meta(region_name):
    """
    20가지 완충 키워드 조합 템플릿 ('출장 [완충단어] 마사지' 구조 통일)
    """
    templates = [
        # 1. 1:1 방문 홈케어
        {
            "title": f"{region_name} 출장 1:1 방문 홈케어 마사지 & 테라피 - {SITE_NAME}",
            "desc": f"{region_name} 출장 전문 1:1 방문 홈케어 마사지 안내. {SITE_NAME}의 프라이빗 맞춤 테라피로 편안한 힐링을 경험해보세요.",
            "h1": f"{region_name} 출장 <span>방문 홈케어 마사지</span>",
            "h2": f"{region_name} 1:1 프라이빗 방문 홈케어 및 바디 힐링 프로그램",
            "og_title": f"{region_name} 출장 1:1 방문 홈케어 마사지 - {SITE_NAME}",
            "replace_word": f"{region_name} 출장 방문 홈케어 마사지",
            "tag_suffix": "홈케어 테라피"
        },
        # 2. 100% 건전 힐링
        {
            "title": f"{region_name} 출장 100% 건전 힐링 테라피 마사지 - {SITE_NAME}",
            "desc": f"{region_name} 출장 100% 건전 힐링 타이 마사지 추천. {SITE_NAME}의 품격 있는 바디 릴렉싱 케어를 안심하고 예약하세요.",
            "h1": f"{region_name} 출장 <span>건전 힐링 마사지</span>",
            "h2": f"믿을 수 있는 {region_name} 100% 건전 테라피 & 안심 바디 케어 코스",
            "og_title": f"{region_name} 출장 100% 건전 힐링 마사지 - {SITE_NAME}",
            "replace_word": f"{region_name} 출장 건전 힐링 마사지",
            "tag_suffix": "건전 테라피"
        },
        # 3. 상체 림프 순환 케어
        {
            "title": f"{region_name} 출장 상체 림프 순환 케어 마사지 - {SITE_NAME}",
            "desc": f"{region_name} 출장 상체 림프 순환 및 가슴 바디 케어 마사지. 전문 테라피스트의 손길로 뭉친 근육을 부드럽게 이완해 드립니다.",
            "h1": f"{region_name} 출장 <span>상체 림프 마사지</span>",
            "h2": f"{region_name} 상체 림프 순환 및 가슴 바디 릴렉싱 스페셜 케어",
            "og_title": f"{region_name} 출장 상체 림프 순환 마사지 - {SITE_NAME}",
            "replace_word": f"{region_name} 출장 상체 림프 마사지",
            "tag_suffix": "림프 바디케어"
        },
        # 4. 프리미엄 아로마 오일
        {
            "title": f"{region_name} 출장 프리미엄 아로마 오일 마사지 - {SITE_NAME}",
            "desc": f"{region_name} 출장 24시 프리미엄 홈타이 및 아로마 오일 마사지. {SITE_NAME}에서 은은한 향기와 함께 피로를 풀어보세요.",
            "h1": f"{region_name} 출장 <span>프리미엄 아로마 마사지</span>",
            "h2": f"천연 에센셜 오일 기반 {region_name} 프리미엄 아로마 바디 테라피",
            "og_title": f"{region_name} 출장 프리미엄 아로마 마사지 - {SITE_NAME}",
            "replace_word": f"{region_name} 출장 아로마 오일 마사지",
            "tag_suffix": "아로마 힐링"
        },
        # 5. 프라이빗 스웨디시 감성
        {
            "title": f"{region_name} 출장 프라이빗 스웨디시 감성 힐링 마사지 - {SITE_NAME}",
            "desc": f"{region_name} 출장 감성 스웨디시 힐링 마사지 전문. 섬세하고 부드러운 터칭으로 최상의 릴렉스를 선사합니다.",
            "h1": f"{region_name} 출장 <span>스웨디시 감성 마사지</span>",
            "h2": f"지친 일상을 녹여주는 {region_name} 프라이빗 스웨디시 감성 릴렉싱",
            "og_title": f"{region_name} 출장 감성 스웨디시 마사지 - {SITE_NAME}",
            "replace_word": f"{region_name} 출장 스웨디시 감성 마사지",
            "tag_suffix": "스웨디시 케어"
        },
        # 6. 상체 가슴 바디 릴렉싱
        {
            "title": f"{region_name} 출장 상체 가슴 바디 릴렉싱 마사지 - {SITE_NAME}",
            "desc": f"{region_name} 출장 전신 및 상체 가슴 릴렉스 케어 마사지. 편안한 공간에서 받는 1:1 맞춤형 힐링 프로그램입니다.",
            "h1": f"{region_name} 출장 <span>가슴 바디 릴렉싱 마사지</span>",
            "h2": f"{region_name} 상체 가슴 순환 및 전신 릴렉스 밸런스 프로그램",
            "og_title": f"{region_name} 출장 가슴 바디 릴렉싱 마사지 - {SITE_NAME}",
            "replace_word": f"{region_name} 출장 가슴 바디 릴렉싱 마사지",
            "tag_suffix": "바디 릴렉싱"
        },
        # 7. 안심 건전 힐링 케어
        {
            "title": f"{region_name} 출장 안심 건전 힐링 케어 마사지 - {SITE_NAME}",
            "desc": f"{region_name} 출장 건전 인증 힐링 테라피 마사지. {SITE_NAME}은 믿을 수 있는 전문 관리사의 정성스러운 케어를 제공합니다.",
            "h1": f"{region_name} 출장 <span>안심 건전 힐링 케어</span>",
            "h2": f"남녀노소 편안하게 이용하는 {region_name} 안심 건전 힐링 테라피",
            "og_title": f"{region_name} 출장 안심 건전 힐링 마사지 - {SITE_NAME}",
            "replace_word": f"{region_name} 출장 안심 건전 마사지",
            "tag_suffix": "건전 테라피"
        },
        # 8. 정통 홈타이 테라피
        {
            "title": f"{region_name} 출장 정통 홈타이 바디 테라피 마사지 - {SITE_NAME}",
            "desc": f"{region_name} 출장 정통 홈타이 테라피 마사지 안내. 시원한 스트레칭과 압 조절로 지친 몸의 컨디션을 회복해 드립니다.",
            "h1": f"{region_name} 출장 <span>정통 홈타이 마사지</span>",
            "h2": f"전신 근육 이완과 스트레칭을 돕는 {region_name} 정통 홈타이 케어",
            "og_title": f"{region_name} 출장 정통 홈타이 마사지 - {SITE_NAME}",
            "replace_word": f"{region_name} 출장 정통 홈타이 마사지",
            "tag_suffix": "홈타이 케어"
        },
        # 9. 맞춤 림프 드레나쥐
        {
            "title": f"{region_name} 출장 맞춤 림프 드레나쥐 마사지 & 테라피 - {SITE_NAME}",
            "desc": f"{region_name} 출장 림프 드레나쥐 및 상체 순환 마사지. 몸속 노폐물 배출과 붓기 완화에 도움을 주는 프라이빗 케어입니다.",
            "h1": f"{region_name} 출장 <span>림프 드레나쥐 마사지</span>",
            "h2": f"몸의 순환을 돕는 {region_name} 맞춤형 림프 드레나쥐 테라피 코스",
            "og_title": f"{region_name} 출장 맞춤 림프 테라피 마사지 - {SITE_NAME}",
            "replace_word": f"{region_name} 출장 림프 드레나쥐 마사지",
            "tag_suffix": "림프 드레나쥐"
        },
        # 10. 24시 야간 홈케어
        {
            "title": f"{region_name} 출장 24시 야간 홈케어 힐링 마사지 - {SITE_NAME}",
            "desc": f"{region_name} 출장 24시간 언제든 편하게 부르는 야간 홈케어 마사지. {SITE_NAME}에서 늦은 밤에도 부담 없이 관리받으세요.",
            "h1": f"{region_name} 출장 <span>24시 야간 홈케어 마사지</span>",
            "h2": f"심야 및 24시간 언제나 신속하게 찾아가는 {region_name} 야간 홈케어 서비스",
            "og_title": f"{region_name} 출장 24시 야간 홈케어 마사지 - {SITE_NAME}",
            "replace_word": f"{region_name} 출장 24시 홈케어 마사지",
            "tag_suffix": "24시 홈케어"
        },
        # 11. 가슴 림프 웰니스
        {
            "title": f"{region_name} 출장 가슴 림프 웰니스 바디 마사지 - {SITE_NAME}",
            "desc": f"{region_name} 출장 가슴 및 상체 림프 웰니스 바디 케어 마사지. 균형 잡힌 바디 라인과 깊은 휴식을 도와드립니다.",
            "h1": f"{region_name} 출장 <span>가슴 림프 웰니스 마사지</span>",
            "h2": f"{region_name} 가슴 림프 웰니스 및 상체 바디 밸런싱 케어",
            "og_title": f"{region_name} 출장 가슴 림프 웰니스 마사지 - {SITE_NAME}",
            "replace_word": f"{region_name} 출장 가슴 림프 마사지",
            "tag_suffix": "가슴 림프케어"
        },
        # 12. VIP 프리미엄 방문 테라피
        {
            "title": f"{region_name} 출장 VIP 프리미엄 방문 테라피 마사지 - {SITE_NAME}",
            "desc": f"{region_name} 출장 최고급 VIP 프리미엄 방문 마사지 서비스. {SITE_NAME}만의 차별화된 1:1 테라피 코스를 경험해보세요.",
            "h1": f"{region_name} 출장 <span>VIP 방문 테라피 마사지</span>",
            "h2": f"차별화된 고품격 힐링을 선사하는 {region_name} VIP 전용 방문 코스",
            "og_title": f"{region_name} 출장 VIP 방문 테라피 마사지 - {SITE_NAME}",
            "replace_word": f"{region_name} 출장 VIP 프리미엄 마사지",
            "tag_suffix": "VIP 테라피"
        },
        # 13. 전신 피로회복 딥티슈
        {
            "title": f"{region_name} 출장 전신 피로회복 딥티슈 마사지 - {SITE_NAME}",
            "desc": f"{region_name} 출장 피로회복 중심 딥티슈 테라피 마사지. 깊은 근육층까지 세심하게 케어하여 활력을 되찾아 드립니다.",
            "h1": f"{region_name} 출장 <span>피로회복 딥티슈 마사지</span>",
            "h2": f"만성 피로와 뭉친 근육을 깊숙이 풀어주는 {region_name} 딥티슈 테라피",
            "og_title": f"{region_name} 출장 전신 피로회복 딥티슈 마사지 - {SITE_NAME}",
            "replace_word": f"{region_name} 출장 피로회복 딥티슈 마사지",
            "tag_suffix": "피로회복 케어"
        },
        # 14. 힐링 에스테틱 홈스파
        {
            "title": f"{region_name} 출장 힐링 에스테틱 홈스파 마사지 - {SITE_NAME}",
            "desc": f"{region_name} 출장 홈스파 & 에스테틱 감성 마사지. 집에서 즐기는 럭셔리 힐링 타임을 {SITE_NAME}과 함께하세요.",
            "h1": f"{region_name} 출장 <span>에스테틱 홈스파 마사지</span>",
            "h2": f"집에서 누리는 프라이빗 스파 테라피, {region_name} 홈스파 힐링 케어",
            "og_title": f"{region_name} 출장 에스테틱 홈스파 마사지 - {SITE_NAME}",
            "replace_word": f"{region_name} 출장 홈스파 에스테틱 마사지",
            "tag_suffix": "에스테틱 홈스파"
        },
        # 15. 상체 집중 릴렉스
        {
            "title": f"{region_name} 출장 상체 집중 릴렉스 테라피 마사지 - {SITE_NAME}",
            "desc": f"{region_name} 출장 목, 어깨, 상체 가슴 집중 릴렉스 마사지. 굳은 상체 근육을 부드럽게 풀어 가벼운 몸을 만들어 드립니다.",
            "h1": f"{region_name} 출장 <span>상체 집중 릴렉스 마사지</span>",
            "h2": f"목, 어깨, 상체 가슴 중심의 {region_name} 집중 릴렉싱 바디 케어",
            "og_title": f"{region_name} 출장 상체 집중 릴렉스 마사지 - {SITE_NAME}",
            "replace_word": f"{region_name} 출장 상체 집중 릴렉스 마사지",
            "tag_suffix": "상체 릴렉스"
        },
        # 16. 건전 힐링 아로마
        {
            "title": f"{region_name} 출장 건전 힐링 아로마 테라피 마사지 - {SITE_NAME}",
            "desc": f"{region_name} 출장 건전 지향 아로마 테라피 마사지. 최고급 천연 오일을 사용하여 피부 보습과 릴렉스를 동시에 관리합니다.",
            "h1": f"{region_name} 출장 <span>건전 아로마 테라피 마사지</span>",
            "h2": f"천연 에센스 오일로 피부와 심신을 안정시키는 {region_name} 건전 아로마 테라피",
            "og_title": f"{region_name} 출장 건전 힐링 아로마 마사지 - {SITE_NAME}",
            "replace_word": f"{region_name} 출장 건전 아로마 마사지",
            "tag_suffix": "아로마 테라피"
        },
        # 17. 1:1 방문 맞춤 컨디셔닝
        {
            "title": f"{region_name} 출장 1:1 방문 맞춤 컨디셔닝 마사지 - {SITE_NAME}",
            "desc": f"{region_name} 출장 체형 맞춤 컨디셔닝 바디 마사지. 개개인의 신체 컨디션에 맞춘 최적의 테라피 솔루션을 제공합니다.",
            "h1": f"{region_name} 출장 <span>맞춤 컨디셔닝 마사지</span>",
            "h2": f"개인별 체형과 컨디션을 고려한 {region_name} 1:1 맞춤형 바디 솔루션",
            "og_title": f"{region_name} 출장 1:1 맞춤 컨디셔닝 마사지 - {SITE_NAME}",
            "replace_word": f"{region_name} 출장 맞춤 컨디셔닝 마사지",
            "tag_suffix": "맞춤 컨디셔닝"
        },
        # 18. 소프트 감성 스웨디시
        {
            "title": f"{region_name} 출장 소프트 감성 힐링 스웨디시 마사지 - {SITE_NAME}",
            "desc": f"{region_name} 출장 소프트 힐링 스웨디시 테라피 마사지. 부드럽고 섬세한 터치감으로 긴장된 하루의 스트레스를 완화합니다.",
            "h1": f"{region_name} 출장 <span>감성 힐링 스웨디시 마사지</span>",
            "h2": f"부드럽고 감미로운 터칭으로 긴장을 완화하는 {region_name} 소프트 스웨디시",
            "og_title": f"{region_name} 출장 소프트 감성 스웨디시 마사지 - {SITE_NAME}",
            "replace_word": f"{region_name} 출장 감성 스웨디시 마사지",
            "tag_suffix": "감성 스웨디시"
        },
        # 19. 바디 밸런스 림프
        {
            "title": f"{region_name} 출장 바디 밸런스 림프 순환 마사지 - {SITE_NAME}",
            "desc": f"{region_name} 출장 전신 및 가슴 림프 순환 마사지. 몸의 균형을 되찾아주는 프라이빗 테라피스트의 정성 가득한 방문 케어.",
            "h1": f"{region_name} 출장 <span>바디 밸런스 림프 마사지</span>",
            "h2": f"흐트러진 신체 밸런스를 바로잡는 {region_name} 림프 순환 바디 프로그램",
            "og_title": f"{region_name} 출장 바디 밸런스 림프 마사지 - {SITE_NAME}",
            "replace_word": f"{region_name} 출장 바디 림프 마사지",
            "tag_suffix": "바디 밸런스"
        },
        # 20. 프리미엄 홈타이 힐링
        {
            "title": f"{region_title} 출장 프리미엄 홈타이 힐링 테라피 마사지 - {SITE_NAME}" if 'region_title' in locals() else f"{region_name} 출장 프리미엄 홈타이 힐링 테라피 마사지 - {SITE_NAME}",
            "desc": f"{region_name} 출장 24시 프리미엄 홈타이 힐링 마사지. 깔끔하고 정돈된 전문 홈케어 서비스로 완벽한 휴식을 약속합니다.",
            "h1": f"{region_name} 출장 <span>프리미엄 홈타이 마사지</span>",
            "h2": f"편안한 내 집에서 누리는 {region_name} 프리미엄 홈타이 힐링 서비스",
            "og_title": f"{region_name} 출장 프리미엄 홈타이 마사지 - {SITE_NAME}",
            "replace_word": f"{region_name} 출장 프리미엄 홈타이 마사지",
            "tag_suffix": "홈타이 힐링"
        }
    ]
    
    return random.choice(templates)

def update_html_content(content, region_name, meta):
    """
    <head> 메타태그뿐만 아니라 body 내부의 h1, h2, img alt, 하단 링크 텍스트까지 안전 치환
    """
    # 1. <title> 교체
    content = re.sub(
        r'<title>(.*?)</title>',
        f'<title>{meta["title"]}</title>',
        content, flags=re.IGNORECASE | re.DOTALL
    )

    # 2. <meta description> 교체
    if re.search(r'<meta\s+name=["\']description["\']', content, re.IGNORECASE):
        content = re.sub(
            r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']\s*/?>',
            f'<meta name="description" content="{meta["desc"]}">',
            content, flags=re.IGNORECASE | re.DOTALL
        )
    else:
        content = re.sub(
            r'(<head[^>]*>)',
            r'\1\n    <meta name="description" content="' + meta["desc"] + '">',
            content, count=1, flags=re.IGNORECASE
        )

    # 3. Open Graph 교체
    if re.search(r'<meta\s+property=["\']og:title["\']', content, re.IGNORECASE):
        content = re.sub(
            r'<meta\s+property=["\']og:title["\']\s+content=["\'](.*?)["\']\s*/?>',
            f'<meta property="og:title" content="{meta["og_title"]}">',
            content, flags=re.IGNORECASE | re.DOTALL
        )
    
    if re.search(r'<meta\s+property=["\']og:description["\']', content, re.IGNORECASE):
        content = re.sub(
            r'<meta\s+property=["\']og:description["\']\s+content=["\'](.*?)["\']\s*/?>',
            f'<meta property="og:description" content="{meta["desc"]}">',
            content, flags=re.IGNORECASE | re.DOTALL
        )

    # 4. <h1> 메인 타이틀 교체
    content = re.sub(
        r'<h1>(.*?)</h1>',
        f'<h1>{meta["h1"]}</h1>',
        content, flags=re.IGNORECASE | re.DOTALL
    )

    # 5. <h2> 서브 타이틀 교체 (첫 번째 주요 h2)
    if re.search(r'<h2>(.*?)</h2>', content, re.IGNORECASE):
        content = re.sub(
            r'<h2>(.*?)</h2>',
            f'<h2>{meta["h2"]}</h2>',
            content, count=1, flags=re.IGNORECASE | re.DOTALL
        )

    # 6. 이미지 <img>의 alt 속성 보정
    content = re.sub(
        r'<img([^>]*?)alt=["\'](.*?)["\']([^>]*?)>',
        lambda m: f'<img{m.group(1)}alt="{region_name} 프라이빗 힐링 바디 테라피"{m.group(3)}>'
        if any(bad in m.group(2) for bad in ["출장마사지", "출장 마사지"]) else m.group(0),
        content, flags=re.IGNORECASE
    )

    # 7. 동 목록 태그 링크 텍스트 보정 (예: '역삼동 출장마사지' -> '역삼동 홈케어 테라피')
    content = re.sub(
        r'(<a[^>]*class=["\'][^"\']*dong-tag[^"\']*["\'][^>]*>)(.*?)(</a>)',
        lambda m: f'{m.group(1)}{re.sub(r"출장\s*마사지", meta["tag_suffix"], m.group(2))}{m.group(3)}',
        content, flags=re.IGNORECASE
    )

    # 8. 본문 텍스트 내 단순 '출장마사지' 단어 안전 일괄 치환
    def replace_text_between_tags(match):
        text = match.group(0)
        # 띄어쓰기 여부 무관하게 붙여쓴 '출장마사지'와 '출장 마사지'를 우회 문구로 정리
        text = re.sub(r'(?:' + re.escape(region_name) + r'\s*)?출장\s*마사지', meta["replace_word"], text)
        return text

    content = re.sub(r'>([^<]+)<', replace_text_between_tags, content)

    return content

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
                file_name_only = os.path.splitext(file)[0]
                
                # 1. 루트 index.html 스킵
                if rel_path == "index.html":
                    print(f"⏩ [스킵 - 루트 메인 페이지] {rel_path}")
                    continue

                # 2. 폴더명에서 시/구 지역명 추출
                gu_name = None
                for key, val in REGION_MAP.items():
                    if key in path_parts:
                        gu_name = val
                        break

                # 3. 세부 동 파일인 경우 (예: 역삼동.html) -> '강남구 역삼동' 형태로 조합
                if gu_name:
                    if file_name_only.lower() != "index":
                        region_name = f"{gu_name} {file_name_only}"
                    else:
                        region_name = gu_name
                else:
                    # 폴더 매핑 실패 시 파일 내용에서 감지
                    region_name = None

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

                # 지역명 최종 폴백
                if not region_name:
                    match = re.search(r'([가-힣]{2,4}[구|시])', content)
                    region_name = match.group(1) if match else "수도권"

                # 20가지 우회 템플릿 중 하나 랜덤 추출
                meta_info = generate_seo_meta(region_name)

                # 전체 태그 및 본문 일괄 치환
                updated_content = update_html_content(content, region_name, meta_info)

                # 파일 저장
                try:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    
                    print(f"✅ [교체 완료] {rel_path} ({region_name}) -> {meta_info['title']}")
                    updated_count += 1
                except Exception as e:
                    print(f"❌ [오류] {file_path}: {e}")

    print(f"\n🎉 총 {updated_count}개 서브 페이지의 전체 SEO 태그 및 본문 완벽 교체가 완료되었습니다!")

if __name__ == "__main__":
    update_all_html_files()