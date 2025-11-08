# 💍 WeddingFinancePro  
**심화 프로그래밍 결혼식 예산 관리 프로젝트 입니다.**  

> Flask 기반 결혼식 예산 관리 및 축의금 통계 웹 애플리케이션  
> 결혼식을 준비하는 사용자가 **지출(비용)** 과 **수입(축의금)** 을 체계적으로 기록하고,  
> 대시보드를 통해 **손익을 시각화**할 수 있는 프로그램입니다.

---

## 📌 프로젝트 개요

### 🎯 목적
- 결혼식 비용(웨딩홀, 식대, 드레스 등)을 항목별로 관리  
- 하객별 축의금 데이터를 신랑측 / 신부측으로 분리하여 관리  
- 손익 계산 및 시각화(막대그래프, 원그래프)를 통해 직관적으로 재정 현황 파악  

### 🧩 개발 환경
| 항목 | 내용 |
|------|------|
| 언어 | Python 3.x |
| 프레임워크 | Flask |
| 데이터베이스 | SQLite (Flask-SQLAlchemy ORM) |
| 프론트엔드 | HTML, Bootstrap5, Chart.js |
| 실행 환경 | 로컬 데스크톱 (웹 브라우저 기반) |

---

## ⚙️ 주요 기능

| 기능 | 설명 |
|------|------|
| 💰 **지출 관리 (Expenses)** | 결혼식 관련 비용(웨딩홀, 스드메, 식대 등) 입력 및 합계 자동 계산 |
| 🎁 **축의금 관리 (Guests)** | 신랑측 / 신부측 하객 축의금 관리, 이름별 검색 가능 |
| 📊 **대시보드 (Dashboard)** | 총 수입 vs 지출, 신랑 vs 신부 비중, 지출 항목별 비율 시각화 |
| 🔄 **데이터 초기화** *(선택)* | wedding_budget.db 삭제 또는 `/reset-db` 경로로 초기화 가능 |

---

## 🗂️ 프로젝트 구조

```bash
WeddingFinancePro/
│
├── app.py                  # 메인 실행 파일
├── models.py               # DB 모델 정의
├── dashboard_routes.py     # 대시보드 관련 라우트
├── expenses_routes.py      # 지출 관련 라우트
├── guests_routes.py        # 축의금 관련 라우트
│
├── templates/              # HTML 템플릿 (Jinja2)
│   ├── base.html
│   ├── index.html
│   ├── expenses.html
│   └── guests.html
│
├── static/
│   └── style.css           # CSS 스타일
│
├── requirements.txt        # 패키지 의존성
└── README.md
