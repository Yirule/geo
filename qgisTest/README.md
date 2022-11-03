# QGIS
- QGIS 26.3 기준
## 플러그인 설치
- AnotherDXFImporter
## 지도 준비하기
- world.svg에서  영토 레이어만 남기고 나머지 삭제
- 최상위 그룹 풀기
- .dxf로 내보내기
## 좌표계 정의하기
- 상단 툴바 > `설정` > `사용자 정의 좌표계`
- `+`
- `이름`: 'ZELI-B'
- `포맷`: `Proj 문자열 (레거시 - 비추천)`
- `파라미터`: 아래 참조
### 파라미터
- 참조: https://gis.stackexchange.com/questions/310212/get-correct-measurements-for-fantasy-world-map
```
+proj=eqc
+a=2704464.91491671
+b=2701536.2023632993
+units=m
+no_defs
```
- eqc: 등장방형도법
- a: 긴반지름 (적도지름/2)
- b: 짧은반지름 (극지름/2)
- 단위는 m
    - 광부위키에는 km으로 작성되어 있으므로 *1000하기
- no_defs: 기본값 적용 금지
## 좌표계 적용
- 우하단 > `EPSG:어쩌구` > `ZELI-B`로 변경
## DXF 불러오기
- 상단 툴바 > `벡터` > `DXF Import/Convert` > `Import or Convert`
- `Browse` > 아까 내보낸 dxf 파일 선택
- `Use Color attribut from DXF` > `Polygon` 체크
- `Use coordinate transformation` 체크

### 좌표 변환
- `Transformation settings` > `Type of input` > `Indentical Points` 선택
- 드롭다운 > `3 point (GeoRef)` 선택
- 값 입력
    - 원본 X, 원본 Y, 대상 X, 대상 Y
    - 0, 2160, 0, 90
    - 1920, 0, 180, -90
    - 0, 0, 0, -90
- `Import`
### 도형 오류 확인
- 참조: https://urbn-ds.tistory.com/24
- 안 해도 상관 없음
- 상단 툴바 > `공간 처리` > `툴박스`
- `벡터 도형` > `무결성 검증`
### 도형 오류 수정
- 참조(댓글): https://gis.stackexchange.com/questions/391094/how-to-use-v-clean-in-qgis-to-fix-polygon-topology#comment640636_391098
- 상단 툴바 > `공간 처리` > `툴박스`
- `벡터 도형` > `도형 수정`
- `입력 레이어` > '폴리곤(U+B808 어쩌구)' 선택
- `실행`
- 레이어에 '수정한 도형'이 추가됨
### 색상 별로 병합
- 상단 툴바 > `공간 처리` > `툴박스`
- `벡터 도형` > `디졸브`
- `입력 레이어` > '`수정한 도형`' 선택
- `디졸브 필드` > `fcolor` 선택
- `실행`
- 레이어에 '산출물'이 추가됨
- 각 레이어 옆의 체크 박스를 해제해 숨길 수 있다.
- '산출물' 빼고 다 숨겨주자.
#### 잘 됐는지 확인
- 좌하단 `레이어` > '`수정한 도형`' > 우클릭 > `속성`
- `정보` > `객체 개수`: 약 340
- 산출물의 `객체 개수`(약 68)와 비교
### 레이어에 좌표계 적용
- 좌하단 `레이어` > 그룹 레이어 선택 > 우클릭 > `그룹 좌표계 설정`
- `ZELI-B` 선택 > `확인`
## 라벨 추가
- 좌하단 `레이어` > '`산출물`' > 우클릭 > `속성`
- `라벨` > 상단 드롭다운 (`라벨 없음`) > `단일 라벨` 선택
- `값` ('`Layer`') > '`concat(round($area/1000000), '㎢')`'
    - `$area`: 각 폴리곤의 넓이
    - `/1000000`: m^2 -> km^2
    - `round`: 반올림
    - `concat`: 문자열 결합
- `확인`
## 색상 적용
- 좌하단 `레이어` > '`산출물`' > 우클릭 > `속성`
- `심볼` > 채우기 색상 > 우측의 아이콘 > `편집...`
- `"fcolor"` 입력 > `확인`