import os
import random

SITE_NAME = "블레스바디"
BASE_URL = "https://blissbody.netlify.app"

# 구/동 전용 20가지 우회 템플릿 ('출장 [완충단어] 마사지' 구조)
def get_seo_template(region_title):
    templates = [
        # 1. 1:1 방문 홈케어
        {
            "title": f"{region_title} 출장 1:1 방문 홈케어 마사지 & 테라피 - {SITE_NAME}",
            "desc": f"{region_title} 출장 전문 1:1 방문 홈케어 마사지 안내. {SITE_NAME}의 프라이빗 맞춤 테라피로 편안한 힐링을 경험해보세요.",
            "h1_sub": "방문 홈케어 마사지",
            "hero_h2": f"{region_title} 출장 1:1 방문 홈케어 테라피",
            "hero_p": "고객님이 계신 편안한 공간으로 전문 테라피스트가 직접 찾아갑니다",
            "section_h2": f"{region_title} 추천 1:1 방문 홈케어 테라피 안내",
            "tag_suffix": "홈케어 테라피"
        },
        # 2. 100% 건전 힐링
        {
            "title": f"{region_title} 출장 100% 건전 힐링 테라피 마사지 - {SITE_NAME}",
            "desc": f"{region_title} 출장 100% 건전 힐링 타이 마사지 추천. {SITE_NAME}의 품격 있는 바디 릴렉싱 케어를 안심하고 예약하세요.",
            "h1_sub": "건전 힐링 마사지",
            "hero_h2": f"{region_title} 출장 안심 건전 힐링 테라피",
            "hero_p": "정통 테라피스트의 정성스러운 케어로 지친 심신에 활력을 불어넣습니다",
            "section_h2": f"{region_title} 안심 건전 힐링 바디 테라피 매장",
            "tag_suffix": "건전 테라피"
        },
        # 3. 상체 림프 순환 케어
        {
            "title": f"{region_title} 출장 상체 림프 순환 케어 마사지 - {SITE_NAME}",
            "desc": f"{region_title} 출장 상체 림프 순환 및 가슴 바디 케어 마사지. 전문 테라피스트의 손길로 뭉친 근육을 부드럽게 이완해 드립니다.",
            "h1_sub": "상체 림프 마사지",
            "hero_h2": f"{region_title} 출장 상체 림프 순환 바디 케어",
            "hero_p": "섬세한 림프 순환 케어로 무거운 몸을 한결 가볍고 상쾌하게",
            "section_h2": f"{region_title} 상체 림프 & 가슴 바디 릴렉싱 프로그램",
            "tag_suffix": "림프 바디케어"
        },
        # 4. 프리미엄 아로마 오일
        {
            "title": f"{region_title} 출장 프리미엄 아로마 오일 마사지 - {SITE_NAME}",
            "desc": f"{region_title} 출장 24시 프리미엄 홈타이 및 아로마 오일 마사지. {SITE_NAME}에서 은은한 향기와 함께 피로를 풀어보세요.",
            "h1_sub": "프리미엄 아로마 마사지",
            "hero_h2": f"{region_title} 출장 프리미엄 아로마 오일 힐링",
            "hero_p": "최고급 천연 오일로 피부 보습과 릴렉스를 동시에 관리하세요",
            "section_h2": f"{region_title} 프리미엄 천연 아로마 테라피 코스",
            "tag_suffix": "아로마 힐링"
        },
        # 5. 프라이빗 스웨디시 감성
        {
            "title": f"{region_title} 출장 프라이빗 스웨디시 감성 힐링 마사지 - {SITE_NAME}",
            "desc": f"{region_title} 출장 감성 스웨디시 힐링 마사지 전문. 섬세하고 부드러운 터칭으로 최상의 릴렉스를 선사합니다.",
            "h1_sub": "스웨디시 감성 마사지",
            "hero_h2": f"{region_title} 출장 프라이빗 스웨디시 감성 테라피",
            "hero_p": "따뜻하고 감미로운 터칭으로 하루의 스트레스를 완벽히 녹여드립니다",
            "section_h2": f"{region_title} 감성 힐링 스웨디시 전문 매장 안내",
            "tag_suffix": "스웨디시 케어"
        },
        # 6. 상체 가슴 바디 릴렉싱
        {
            "title": f"{region_title} 출장 상체 가슴 바디 릴렉싱 마사지 - {SITE_NAME}",
            "desc": f"{region_title} 출장 전신 및 상체 가슴 릴렉스 케어 마사지. 편안한 공간에서 받는 1:1 맞춤형 힐링 프로그램입니다.",
            "h1_sub": "가슴 바디 릴렉싱 마사지",
            "hero_h2": f"{region_title} 출장 상체 가슴 릴렉싱 케어",
            "hero_p": "흐트러진 바디 밸런스를 바로잡아주는 체계적인 맞춤 솔루션",
            "section_h2": f"{region_title} 상체 가슴 릴렉스 & 전신 바디 케어",
            "tag_suffix": "바디 릴렉싱"
        },
        # 7. 안심 건전 힐링 케어
        {
            "title": f"{region_title} 출장 안심 건전 힐링 케어 마사지 - {SITE_NAME}",
            "desc": f"{region_title} 출장 건전 인증 힐링 테라피 마사지. {SITE_NAME}은 믿을 수 있는 전문 관리사의 정성스러운 케어를 제공합니다.",
            "h1_sub": "안심 건전 힐링 케어",
            "hero_h2": f"{region_title} 출장 안심 건전 힐링 홈서비스",
            "hero_p": "철저한 위생 관리와 정직한 정찰제로 안심하고 이용하세요",
            "section_h2": f"{region_title} 믿고 맡기는 건전 힐링 테라피",
            "tag_suffix": "건전 테라피"
        },
        # 8. 정통 홈타이 테라피
        {
            "title": f"{region_title} 출장 정통 홈타이 바디 테라피 마사지 - {SITE_NAME}",
            "desc": f"{region_title} 출장 정통 홈타이 테라피 마사지 안내. 시원한 스트레칭과 압 조절로 지친 몸의 컨디션을 회복해 드립니다.",
            "h1_sub": "정통 홈타이 마사지",
            "hero_h2": f"{region_title} 출장 정통 홈타이 스트레칭 케어",
            "hero_p": "전문가의 시원한 손길로 굳은 몸의 긴장을 완벽하게 풀어냅니다",
            "section_h2": f"{region_title} 정통 타이 바디 테라피 코스 안내",
            "tag_suffix": "홈타이 케어"
        },
        # 9. 맞춤 림프 드레나쥐
        {
            "title": f"{region_title} 출장 맞춤 림프 드레나쥐 마사지 & 테라피 - {SITE_NAME}",
            "desc": f"{region_title} 출장 림프 드레나쥐 및 상체 순환 마사지. 몸속 노폐물 배출과 붓기 완화에 도움을 주는 프라이빗 케어입니다.",
            "h1_sub": "림프 드레나쥐 마사지",
            "hero_h2": f"{region_title} 출장 맞춤 림프 순환 드레나쥐",
            "hero_p": "림프 흐름을 원활하게 돕는 정교하고 부드러운 테라피",
            "section_h2": f"{region_title} 림프 드레나쥐 & 순환 힐링 케어",
            "tag_suffix": "림프 드레나쥐"
        },
        # 10. 24시 야간 홈케어
        {
            "title": f"{region_title} 출장 24시 야간 홈케어 힐링 마사지 - {SITE_NAME}",
            "desc": f"{region_title} 출장 24시간 언제든 편하게 부르는 야간 홈케어 마사지. {SITE_NAME}에서 늦은 밤에도 부담 없이 관리받으세요.",
            "h1_sub": "24시 야간 홈케어 마사지",
            "hero_h2": f"{region_title} 출장 24시 야간 신속 방문 힐링",
            "hero_p": "늦은 시간에도 고객님의 편안한 휴식을 위해 즉시 방문합니다",
            "section_h2": f"{region_title} 24시간 언제든 이용 가능한 홈케어 매장",
            "tag_suffix": "24시 홈케어"
        },
        # 11. 가슴 림프 웰니스
        {
            "title": f"{region_title} 출장 가슴 림프 웰니스 바디 마사지 - {SITE_NAME}",
            "desc": f"{region_title} 출장 가슴 및 상체 림프 웰니스 바디 케어 마사지. 균형 잡힌 바디 라인과 깊은 휴식을 도와드립니다.",
            "h1_sub": "가슴 림프 웰니스 마사지",
            "hero_h2": f"{region_title} 출장 가슴 림프 웰니스 바디 케어",
            "hero_p": "여성 및 피로한 현대인을 위한 품격 있는 웰니스 바디 프로그램",
            "section_h2": f"{region_title} 가슴 림프 & 상체 웰니스 테라피",
            "tag_suffix": "가슴 림프케어"
        },
        # 12. VIP 프리미엄 방문 테라피
        {
            "title": f"{region_title} 출장 VIP 프리미엄 방문 테라피 마사지 - {SITE_NAME}",
            "desc": f"{region_title} 출장 최고급 VIP 프리미엄 방문 마사지 서비스. {SITE_NAME}만의 차별화된 1:1 테라피 코스를 경험해보세요.",
            "h1_sub": "VIP 방문 테라피 마사지",
            "hero_h2": f"{region_title} 출장 VIP 프리미엄 1:1 방문 테라피",
            "hero_p": "차별화된 서비스와 감동을 선사하는 고품격 힐링 코스",
            "section_h2": f"{region_title} VIP 프리미엄 방문 케어 리스트",
            "tag_suffix": "VIP 테라피"
        },
        # 13. 전신 피로회복 딥티슈
        {
            "title": f"{region_title} 출장 전신 피로회복 딥티슈 마사지 - {SITE_NAME}",
            "desc": f"{region_title} 출장 피로회복 중심 딥티슈 테라피 마사지. 깊은 근육층까지 세심하게 케어하여 활력을 되찾아 드립니다.",
            "h1_sub": "피로회복 딥티슈 마사지",
            "hero_h2": f"{region_title} 출장 전신 피로회복 딥티슈 케어",
            "hero_p": "깊은 속근육까지 시원하게 케어하여 무거운 피로감을 해소합니다",
            "section_h2": f"{region_title} 만성 피로 해소 딥티슈 테라피 코스",
            "tag_suffix": "피로회복 케어"
        },
        # 14. 힐링 에스테틱 홈스파
        {
            "title": f"{region_title} 출장 힐링 에스테틱 홈스파 마사지 - {SITE_NAME}",
            "desc": f"{region_title} 출장 홈스파 & 에스테틱 감성 마사지. 집에서 즐기는 럭셔리 힐링 타임을 {SITE_NAME}과 함께하세요.",
            "h1_sub": "에스테틱 홈스파 마사지",
            "hero_h2": f"{region_title} 출장 프라이빗 에스테틱 홈스파",
            "hero_p": "에스테틱 샵의 감동을 고객님의 방 안에서 그대로 재현합니다",
            "section_h2": f"{region_title} 에스테틱 홈스파 & 뷰티 바디 프로그램",
            "tag_suffix": "에스테틱 홈스파"
        },
        # 15. 상체 집중 릴렉스
        {
            "title": f"{region_title} 출장 상체 집중 릴렉스 테라피 마사지 - {SITE_NAME}",
            "desc": f"{region_title} 출장 목, 어깨, 상체 가슴 집중 릴렉스 마사지. 굳은 상체 근육을 부드럽게 풀어 가벼운 몸을 만들어 드립니다.",
            "h1_sub": "상체 집중 릴렉스 마사지",
            "hero_h2": f"{region_title} 출장 목·어깨·상체 집중 릴렉스",
            "hero_p": "오랜 좌식 생활로 굳은 상체 라인을 부드럽게 이완합니다",
            "section_h2": f"{region_title} 상체 집중 릴렉싱 바디 케어 안내",
            "tag_suffix": "상체 릴렉스"
        },
        # 16. 건전 힐링 아로마
        {
            "title": f"{region_title} 출장 건전 힐링 아로마 테라피 마사지 - {SITE_NAME}",
            "desc": f"{region_title} 출장 건전 지향 아로마 테라피 마사지. 최고급 천연 오일을 사용하여 피부 보습과 릴렉스를 동시에 관리합니다.",
            "h1_sub": "건전 아로마 테라피 마사지",
            "hero_h2": f"{region_title} 출장 안심 건전 천연 아로마 케어",
            "hero_p": "은은한 아로마 향기와 함께 편안한 휴식의 시간을 선물합니다",
            "section_h2": f"{region_title} 건전 아로마 테라피 & 힐링 프로그램",
            "tag_suffix": "아로마 테라피"
        },
        # 17. 1:1 방문 맞춤 컨디셔닝
        {
            "title": f"{region_title} 출장 1:1 방문 맞춤 컨디셔닝 마사지 - {SITE_NAME}",
            "desc": f"{region_title} 출장 체형 맞춤 컨디셔닝 바디 마사지. 개개인의 신체 컨디션에 맞춘 최적의 테라피 솔루션을 제공합니다.",
            "h1_sub": "맞춤 컨디셔닝 마사지",
            "hero_h2": f"{region_title} 출장 1:1 맞춤 바디 컨디셔닝",
            "hero_p": "당신의 바디 컨디션에 최적화된 맞춤형 힐링 플랜",
            "section_h2": f"{region_title} 1:1 맞춤 컨디셔닝 바디 테라피",
            "tag_suffix": "맞춤 컨디셔닝"
        },
        # 18. 소프트 감성 스웨디시
        {
            "title": f"{region_title} 출장 소프트 감성 힐링 스웨디시 마사지 - {SITE_NAME}",
            "desc": f"{region_title} 출장 소프트 힐링 스웨디시 테라피 마사지. 부드럽고 섬세한 터치감으로 긴장된 하루의 스트레스를 완화합니다.",
            "h1_sub": "감성 힐링 스웨디시 마사지",
            "hero_h2": f"{region_title} 출장 소프트 감성 스웨디시 케어",
            "hero_p": "섬세한 감성 터칭으로 깊은 안정감과 휴식을 선사합니다",
            "section_h2": f"{region_title} 감성 스웨디시 테라피 전문 안내",
            "tag_suffix": "감성 스웨디시"
        },
        # 19. 바디 밸런스 림프
        {
            "title": f"{region_title} 출장 바디 밸런스 림프 순환 마사지 - {SITE_NAME}",
            "desc": f"{region_title} 출장 전신 및 가슴 림프 순환 마사지. 몸의 균형을 되찾아주는 프라이빗 테라피스트의 정성 가득한 방문 케어.",
            "h1_sub": "바디 밸런스 림프 마사지",
            "hero_h2": f"{region_title} 출장 바디 밸런스 & 림프 순환 케어",
            "hero_p": "무너진 신체 밸런스를 건강하게 되찾아 드립니다",
            "section_h2": f"{region_title} 전신 림프 순환 & 바디 밸런싱 코스",
            "tag_suffix": "바디 밸런스"
        },
        # 20. 프리미엄 홈타이 힐링
        {
            "title": f"{region_title} 출장 프리미엄 홈타이 힐링 테라피 마사지 - {SITE_NAME}",
            "desc": f"{region_title} 출장 24시 프리미엄 홈타이 힐링 마사지. 깔끔하고 정돈된 전문 홈케어 서비스로 완벽한 휴식을 약속합니다.",
            "h1_sub": "프리미엄 홈타이 마사지",
            "hero_h2": f"{region_title} 출장 프리미엄 홈타이 힐링 케어",
            "hero_p": "언제 어디서든 가장 편안하게 누리는 고품격 홈타이",
            "section_h2": f"{region_title} 프리미엄 홈타이 & 바디 힐링 매장",
            "tag_suffix": "홈타이 힐링"
        }
    ]
    return random.choice(templates)

# 5개 업체 데이터
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

# 서울 / 경기 / 인천 전체 지역 및 동 데이터
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
    "suwon": {"name": "경기 수원시", "dongs": ["인계동", "매탄동", "광교동", "영통동", "세류동", "권선동", "정자동", "조원동", "화서동"]},
    "seongnam": {"name": "경기 성남시", "dongs": ["서현동", "야탑동", "정자동", "판교동", "수내동", "금곡동", "구미동", "상대원동", "신흥동"]},
    "goyang": {"name": "경기 고양시", "dongs": ["백석동", "마두동", "주엽동", "화정동", "행신동", "삼송동", "식사동", "탄현동", "대화동"]},
    "yongin": {"name": "경기 용인시", "dongs": ["풍덕천동", "죽전동", "동백동", "신갈동", "보정동", "상현동", "역북동", "김량장동", "구갈동"]},
    "bucheon": {"name": "경기 부천시", "dongs": ["원미동", "심곡동", "중동", "상동", "소사본동", "괴안동", "오정동", "역곡동", "송내동"]},
    "ansan": {"name": "경기 안산시", "dongs": ["고잔동", "중앙동", "초지동", "본오동", "선부동", "와동", "사동", "월피동", "일동"]},
    "anyang": {"name": "경기 안양시", "dongs": ["평촌동", "범계동", "비산동", "안양동", "석수동", "호계동", "관양동", "박달동"]},
    "namyangju": {"name": "경기 남양주시", "dongs": ["다산동", "별내동", "와부읍", "진접읍", "화도읍", "평내동", "호평동", "오남읍", "퇴계원읍"]},
    "hwaseong": {"name": "경기 화성시", "dongs": ["동탄동", "반송동", "청계동", "영천동", "향남읍", "남양읍", "봉담읍", "병점동", "진안동"]},
    "pyeongtaek": {"name": "경기 평택시", "dongs": ["고덕동", "비전동", "세교동", "안중읍", "포승읍", "송탄동", "서정동", "동삭동", "용이동"]},
    "uijeongbu": {"name": "경기 의정부시", "dongs": ["의정부동", "호원동", "장암동", "신곡동", "송산동", "자금동", "가능동", "민락동", "낙양동"]},
    "siheung": {"name": "경기 시흥시", "dongs": ["정왕동", "배곧동", "은계동", "목감동", "신천동", "대야동", "은행동", "장현동", "능곡동"]},
    "paju": {"name": "경기 파주시", "dongs": ["운정동", "교하동", "금촌동", "문산읍", "야당동", "동패동", "와동동", "목동동", "다율동"]},
    "gimpo": {"name": "경기 김포시", "dongs": ["구래동", "장기동", "운양동", "사우동", "풍무동", "걸포동", "마산동", "북변동", "고촌읍"]},
    "gwangmyeong": {"name": "경기 광명시", "dongs": ["철산동", "하안동", "소하동", "일직동", "광명동", "옥길동", "학온동"]},
    "gwangju-gy": {"name": "경기 광주시", "dongs": ["경안동", "송정동", "태전동", "오포읍", "초월읍", "곤지암읍", "역동", "쌍령동"]},
    "gunpo": {"name": "경기 군포시", "dongs": ["산본동", "금정동", "당동", "당정동", "대야미동", "부곡동", "도마교동"]},
    "hanam": {"name": "경기 하남시", "dongs": ["미사동", "위례동", "신장동", "덕풍동", "감일동", "풍산동", "망월동", "선동"]},
    "osan": {"name": "경기 오산시", "dongs": ["원동", "궐동", "오산동", "세교동", "수청동", "갈곶동", "금암동", "은계동"]},
    "icheon": {"name": "경기 이천시", "dongs": ["창전동", "관고동", "증포동", "부발읍", "안흥동", "송정동", "갈산동"]},

    # [인천 주요 구]
    "bupyeong": {"name": "인천 부평구", "dongs": ["부평동", "십정동", "산곡동", "청천동", "삼산동", "갈산동", "부개동", "일신동"]},
    "namdong": {"name": "인천 남동구", "dongs": ["구월동", "간석동", "만수동", "논현동", "서창동", "도림동", "고잔동", "장수동"]},
    "incheon-seo": {"name": "인천 서구", "dongs": ["청라동", "가정동", "석남동", "검암동", "당하동", "원당동", "검단동", "마전동", "신현동"]},
    "yeonsu": {"name": "인천 연수구", "dongs": ["송도동", "연수동", "동춘동", "옥련동", "청학동", "선학동"]},
    "michuhol": {"name": "인천 미추홀구", "dongs": ["주안동", "도화동", "숭의동", "용현동", "학익동", "관교동", "문학동"]},
    "incheon-jung": {"name": "인천 중구", "dongs": ["영종동", "운서동", "중산동", "운남동", "신포동", "연안동", "북성동", "신흥동"]},
    "gyeyang": {"name": "인천 계양구", "dongs": ["계산동", "작전동", "효성동", "임학동", "박촌동", "동양동", "서운동", "병방동"]},
    "incheon-dong": {"name": "인천 동구", "dongs": ["송림동", "송현동", "화수동", "만석동", "화평동", "금곡동"]}
}

def generate_sub_html(display_title, folder_name, is_dong=False, dongs_data=[], current_dong=""):
    """구/시 및 동별 페이지 생성 함수 ('출장 [완충단어] 마사지' 적용)"""
    tpl = get_seo_template(display_title)
    shuffled_vendors = random.sample(VENDORS, len(VENDORS))
    
    vendor_html_blocks = []
    for idx, vendor in enumerate(shuffled_vendors, start=1):
        tagline_formatted = vendor["tagline"].format(region_title=display_title)
        features_formatted = vendor["features"].format(region_title=display_title)
        clean_phone = vendor['phone'].replace("-", "")
        
        block = f"""
        <!-- 업체 {idx}: {vendor['name']} -->
        <div class="vendor-card">
            <img src="{vendor['image']}" alt="{display_title} {vendor['name']} 힐링 바디 테라피" class="vendor-img" loading="lazy">
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
                <a href="tel:{clean_phone}" class="call-btn">📞 전화 문의 : {vendor['phone']}</a>
            </div>
        </div>"""
        vendor_html_blocks.append(block)

    vendors_rendered = "\n".join(vendor_html_blocks)

    # 동 목록 링크 (완충 키워드 접미사 적용)
    dong_links = []
    for d in dongs_data:
        active_style = ' style="border-color:#d4af37; color:#d4af37; font-weight:bold;"' if d == current_dong else ''
        dong_links.append(f'<a href="/{folder_name}/{d}.html" class="dong-tag"{active_style}>{d} {tpl["tag_suffix"]}</a>')
    
    dong_wrap_html = "\n                ".join(dong_links)
    
    # URL 및 뒤로가기 링크
    canonical_url = f"{BASE_URL}/{folder_name}/{current_dong}.html" if is_dong else f"{BASE_URL}/{folder_name}/"
    parent_link = f'/{folder_name}/' if is_dong else '/'
    parent_text = '← 구/시 메인으로' if is_dong else '← 전체 홈으로'

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{tpl['title']}</title>
    <meta name="description" content="{tpl['desc']}">
    <meta name="keywords" content="{display_title} 출장 홈케어, {display_title} 홈타이 테라피, {display_title} 스웨디시, 24시 방문 힐링">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{canonical_url}">
    
    <meta property="og:type" content="website">
    <meta property="og:title" content="{tpl['title']}">
    <meta property="og:description" content="{tpl['desc']}">
    <meta property="og:image" content="{shuffled_vendors[0]['image']}">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;600;700&display=swap" rel="stylesheet">

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
        .dong-tag {{ background: #1f2330; border: 1px solid #32384a; color: #e1e3e8; padding: 6px 12px; border-radius: 20px; font-size: 0.82rem; transition: 0.2s; }}
        .dong-tag:hover {{ border-color: #d4af37; color: #d4af37; }}
        .back-btn {{ display: inline-block; background: #222634; color: #bbb; padding: 8px 16px; border-radius: 6px; font-size: 0.85rem; margin-top: 20px; }}
        footer {{ text-align: center; padding: 20px; font-size: 0.8rem; color: #777; border-top: 1px solid #2a2d37; margin-top: 30px; }}
    </style>
</head>
<body>
    <header>
        <h1>{display_title} <span>{tpl['h1_sub']}</span></h1>
    </header>

    <div class="hero">
        <h2>{tpl['hero_h2']}</h2>
        <p>{tpl['hero_p']}</p>
    </div>

    <div class="container">
        
        <h2 class="section-title">{tpl['section_h2']}</h2>

{vendors_rendered}

        <!-- 세부 동 바로가기 링크 카드 -->
        <div class="card">
            <h3>{display_title} 주변 세부 동별 안내 (클릭 시 이동)</h3>
            <p>원하시는 동을 클릭하시면 해당 지역 전용 상세 안내 페이지로 이동합니다.</p>
            <div class="dong-wrap">
                {dong_wrap_html}
            </div>
        </div>

        <div style="text-align: center;">
            <a href="{parent_link}" class="back-btn">{parent_text}</a>
        </div>
    </div>

    <footer>
        <p>© {SITE_NAME}. All rights reserved.</p>
    </footer>
</body>
</html>
"""

def generate_clean_root_index():
    """
    루트 메인 페이지 (index.html)
    - '출장' 및 '마사지' 키워드를 100% 배제하고 순수 1:1 방문 홈케어 & 웰니스 테라피로 구성
    """
    region_links = []
    for folder, data in REGIONS.items():
        region_links.append(f'<a href="/{folder}/" class="dong-tag">{data["name"]} 홈케어</a>')
    
    region_links_html = "\n                ".join(region_links)
    
    root_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>수도권 24시 방문 홈케어 & 1:1 프라이빗 바디 테라피 - {SITE_NAME}</title>
    <meta name="description" content="서울, 경기, 인천 전 지역 신속 1:1 방문 홈케어 및 안심 힐링 에스테틱 전문 {SITE_NAME}. 24시간 언제나 편안한 공간에서 맞춤 바디 테라피를 누려보세요.">
    <meta name="keywords" content="수도권 방문 홈케어, 24시 홈타이 테라피, 스웨디시 힐링, 프라이빗 에스테틱, 바디 컨디셔닝">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{BASE_URL}/">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;600;700&display=swap" rel="stylesheet">

    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Noto Sans KR', sans-serif; }}
        body {{ background-color: #0f1117; color: #e1e3e8; line-height: 1.6; padding-bottom: 40px; }}
        a {{ text-decoration: none; color: inherit; }}
        header {{ background: #161821; padding: 18px 20px; text-align: center; border-bottom: 2px solid #d4af37; position: sticky; top: 0; z-index: 100; }}
        header h1 {{ font-size: 1.3rem; color: #ffffff; }}
        header h1 span {{ color: #d4af37; }}
        .hero {{ background: linear-gradient(rgba(15,17,23,0.8), rgba(15,17,23,0.9)), url('https://images.unsplash.com/photo-1544161515-4ab6ce6db874?auto=format&fit=crop&w=1200&q=80') center/cover; padding: 50px 20px; text-align: center; border-bottom: 1px solid #2a2d37; }}
        .hero h2 {{ font-size: 1.6rem; color: #fff; margin-bottom: 10px; }}
        .hero p {{ font-size: 0.95rem; color: #d4af37; }}
        .container {{ max-width: 850px; margin: 0 auto; padding: 25px 15px; }}
        .card {{ background: #161821; border: 1px solid #2a2d37; border-radius: 12px; padding: 22px; margin-top: 20px; }}
        .card h3 {{ color: #d4af37; font-size: 1.15rem; margin-bottom: 12px; border-left: 4px solid #d4af37; padding-left: 10px; }}
        .dong-wrap {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 15px; }}
        .dong-tag {{ background: #1f2330; border: 1px solid #32384a; color: #e1e3e8; padding: 8px 14px; border-radius: 20px; font-size: 0.85rem; transition: 0.2s; }}
        .dong-tag:hover {{ border-color: #d4af37; color: #d4af37; }}
        footer {{ text-align: center; padding: 20px; font-size: 0.8rem; color: #777; border-top: 1px solid #2a2d37; margin-top: 40px; }}
    </style>
</head>
<body>
    <header>
        <h1>수도권 프리미엄 <span>{SITE_NAME} 방문 홈케어</span></h1>
    </header>

    <div class="hero">
        <h2>수도권 24시 프라이빗 1:1 방문 홈케어</h2>
        <p>서울 · 경기 · 인천 어디서나 고객님이 계신 곳으로 전문 테라피스트가 찾아갑니다</p>
    </div>

    <div class="container">
        <div class="card">
            <h3>서비스 제공 지역 안내</h3>
            <p>원하시는 지역을 선택하시면 해당 구·시의 상세 안내 페이지로 이동합니다.</p>
            <div class="dong-wrap">
                {region_links_html}
            </div>
        </div>
    </div>

    <footer>
        <p>© {SITE_NAME}. All rights reserved.</p>
    </footer>
</body>
</html>
"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(root_html)
    print("🏠 [클린 메인 생성 완료] 루트 index.html (출장/마사지 키워드 100% 배제)")

def generate_all():
    gu_count = 0
    dong_count = 0

    # 1. 루트 클린 메인 index.html 생성
    generate_clean_root_index()

    # 2. 구/시 및 동별 세부 페이지 생성 ('출장 [완충단어] 마사지' 적용)
    for folder, data in REGIONS.items():
        os.makedirs(folder, exist_ok=True)
        region_title = data["name"]
        dongs = data["dongs"]

        # 구/시 메인 페이지 생성 (index.html)
        gu_html = generate_sub_html(region_title, folder, is_dong=False, dongs_data=dongs)
        with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
            f.write(gu_html)
        gu_count += 1

        # 각 동별 세부 페이지 생성 (동이름.html)
        for dong in dongs:
            dong_title = f"{region_title} {dong}"
            dong_html = generate_sub_html(dong_title, folder, is_dong=True, dongs_data=dongs, current_dong=dong)
            with open(os.path.join(folder, f"{dong}.html"), "w", encoding="utf-8") as f:
                f.write(dong_html)
            dong_count += 1

    print(f"\n🎉 [전체 완료] 루트 클린 메인 1개 + {gu_count}개 시·구 페이지 + {dong_count}개 동 페이지 생성이 완료되었습니다!")

if __name__ == "__main__":
    generate_all()