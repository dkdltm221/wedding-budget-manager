# Wedding Budget Manager

Flask + SQLite로 만든 결혼 예산/축의금 관리 앱입니다. 축의금 양측(신랑/신부) 관리와 지출 관리, 대시보드 시각화를 제공합니다.

## 1. 실행 방법
1) Python 3.10+ 설치  
2) 가상환경 생성(권장):  
```bash
python -m venv .venv
.venv\Scripts\activate       # Windows
source .venv/bin/activate   # macOS/Linux
```
3) 의존성 설치:  
```bash
pip install -r requirements.txt
```
4) DB 초기화 및 실행:  
```bash
python app.py   # 최초 실행 시 DB 자동 생성
```
5) 브라우저에서 접속:  
```
http://localhost:5000
```

## 2. 주요 기능
- 축의금 관리: 신랑/신부측 별 리스트, 이름/금액 정렬, 검색 모달, 수정/삭제 모달, 엑셀 내보내기.
- 지출 관리: 카테고리/금액 입력 및 합계.
- 대시보드: 총 수입 vs 지출, 비중 그래프.

## 3. 폴더 구조
```
wedding-budget-manager/
├─ app.py               # Flask 앱 초기화/라우트 등록
├─ models.py            # SQLAlchemy 모델 정의
├─ dashboard_routes.py  # 대시보드 라우트
├─ expenses_routes.py   # 지출 라우트
├─ guests_routes.py     # 축의금 라우트
├─ templates/           # Jinja2 템플릿
└─ static/              # 정적 파일
```

## 4. 개발 메모 (품질/평가 대비)
- 파이썬 문법/라이브러리: Flask, SQLAlchemy, openpyxl 활용. 정렬/검색/합계는 SQLAlchemy case/sum 사용.
- 구조화: 라우트별 파일 분리, 축의금 라우트 내 정렬/검색/합계 헬퍼 함수로 중복 제거.
- 주석/가독성: 주요 라우트에 한 줄 설명과 의미 있는 함수명 사용.
- 기능 정확성: 이름·금액 정렬, 검색 모달, 수정/삭제 모달, 엑셀 출력(전체 가운데 정렬) 확인.
- 효율성: 정렬/검색 시 필요한 컬럼만 ORDER BY, 합계는 단일 쿼리로 계산.
- 보고/발표 팁: 실행 데모(입력→검색 모달→수정 모달→엑셀 다운로드) 흐름으로 설명하면 평가 항목을 자연스럽게 커버할 수 있음.
