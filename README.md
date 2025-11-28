# Wedding Budget Manager

Flask + SQLite 기반의 예산/축의금 관리 웹앱입니다. 축의금(신랑/신부 측)과 지출을 기록·검색·통계로 확인할 수 있습니다.

## 1. 실행 방법
1) 패키지 설치  
```bash
pip install -r requirements.txt
```
2) DB 초기화 & 실행  
```bash
python app.py   # 첫 실행 시 DB 자동 생성
```
3) 접속  
```
http://localhost:5000
```

## 2. 주요 기능
- 축의금: 신랑/신부 측별 리스트, 금액/메모, 검색/정렬, PDF/엑셀 내보내기, 수정/삭제.
- 지출: 항목/설명/금액 입력, 리스트/총합 확인, 수정/삭제.
- 대시보드: 총 수입/지출/손익/커버율, 수입 vs 지출 그래프, 지출 항목별 비중.

## 3. 프로젝트 구조 (요약)
```
wedding-budget-manager/
├─ app.py                  # Flask 앱 초기화/블루프린트 등록
├─ models.py               # SQLAlchemy 모델 정의
├─ dashboard_routes.py     # 대시보드 뷰
├─ expenses_routes.py      # 지출 뷰 (락/언락 포함)
├─ guests_routes.py        # 축의금 뷰
├─ services/               # 서비스 레이어
│   ├─ dashboard_service.py
│   ├─ expenses_service.py
│   ├─ expenses_view.py
│   ├─ guests_service.py
│   └─ guests_view.py
├─ forms.py                # WTForms (축의금/지출 입력 검증)
├─ utils/
│   ├─ formatting.py       # 금액 포매팅
│   └─ params.py           # 정수/페이지 파싱
├─ view_models.py          # 템플릿 컨텍스트용 dataclass
├─ templates/
│   ├─ layouts/base.html   # 공통 레이아웃
│   ├─ index.html          # 대시보드 (컴포넌트 include)
│   ├─ guests.html         # 축의금 (컴포넌트 include)
│   ├─ expenses.html       # 지출 (컴포넌트 include)
│   ├─ expenses_edit.html  # 지출 수정
│   └─ components/
│       ├─ dashboard/{hero,cards,charts}.html
│       ├─ guests/{hero,stats,form_search,tables,modals}.html
│       └─ expenses/{header,form,list}.html
├─ static/
│   ├─ css/
│   │   ├─ base.css        # 공통 스타일
│   │   ├─ guests.css      # 축의금 전용
│   │   └─ expenses.css    # 지출 전용
│   └─ js/
│       ├─ charts.js       # 대시보드 차트 초기화
│       ├─ guests.js       # 축의금 모달/검색/진행바
│       └─ expenses.js     # 지출 삭제 확인 등
├─ tests/
│   └─ test_utils.py       # 유틸/파싱/검증 테스트
└─ requirements.txt
```

## 4. 개발 메모
- 폼 검증: WTForms(`forms.py`)로 필수값/금액(0 이상) 검증.
- 뷰모델: `view_models.py` dataclass를 뷰에서 사용해 템플릿 컨텍스트를 구조화.
- 서비스 레이어: 데이터 조회/집계/정렬/검색, 페이징 파싱 등을 서비스/뷰 빌더로 분리해 뷰 함수는 렌더링에 집중.
- 차트/JS: 대시보드 차트(`static/js/charts.js`), 축의금 UI(`static/js/guests.js`), 지출 삭제 확인(`static/js/expenses.js`)로 분리.
- 테스트: `python -m unittest discover -s tests` 로 유틸/파싱 로직 확인.
