# Google Calendar API 자동화 스크립트
- Python의 Unittest와 Google Calendar Open API 를 이용한 자동화 스크립트 관리 레포지토리



### Tools
- Python
- Unittest
- Google Library

### 실행 프로세스
1. insert API 를 통해 캘린더를 생성합니다. (calendar_id 를 txt 파일로 반환합니다.)
2. calendar_id.txt 파일을 호출하고 get API 를 통해 생성한 캘린더를 조회합니다.
3. calendar_id.txt 파일을 호출하고update API 를 통해 생성한 캘린더에 대한 정보를 수정합니다.
4. calendar_id.txt 파일을 호출하고patch API 를 통해 생성한 캘린더에 대한 정보를 수정합니다.
5. clear API 를 통해 기본 캘린더에 대한 이벤트를 삭제합니다.
6. calendar_id.txt 파일을 호출하고 delete API 를 통해 생성한 캘린더를 삭제합니다.

### 실행 방법
- `source venv/bin/activate` 명령어로 파이썬 가상 환경을 활성화합니다.
- `pip install -r requirements.txt` 명령어로 필요한 구글 라이브러리를 설치합니다.
- authorize > authorization.py 모듈에 하드코딩된 token 값을 추가합니다. 토큰 값은 아래 스크린샷에서 참조 가능합니다.
- 포커스된 토큰 값을 사용합니다. Google Account API 는 프로젝트를 생성해야 획득할 수 있는 번거로움이 있어, 하드코딩으로 대체하였습니다.
- Root 디렉토리에서 아래 명령어를 입력합니다.
  - `./test_run.sh`
- 실행 시 scripts 디렉토리 내의 api_test_run.py 파일을 실행하고, 해당 파일은 모든 스크립트를 순차적으로 실행합니다.

### 실행 결과
- 터미널 로그에서 실행 결과를 확인할 수 있습니다.