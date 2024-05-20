import unittest

from authorize.authorization import get_token
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class TestCalendarInsert(unittest.TestCase):

    def setUp(self):
        """
        테스트 전에 실행되어 필요한 설정을 수행함.
        Google Calendar API 가 필요하므로, auth 셋업을 위해 OAuth 2 Token 값을 가져옴.
        """
        self.token = get_token()
        credentials = Credentials(self.token)
        self.service = build('calendar', 'v3', credentials=credentials)

    # 보조 캘린더를 생성하는 API TestCase
    def test_TC_CALENDAR_001(self):
        """
        현재 로그인된 계정의 보조 캘린더 생성하기
        실제 생성한 캘린더의 calendarId 를 txt 파일로 생성하여 다른 API 에서 사용할 수 있도록 처리
        :return:
        """
        try:
            # 생성할 캘린더에 추가할 필드 (summary, timeZone)
            calendar = {
                "summary": "test calendar",
                "timeZone": "Asia/Seoul"
            }
            # insert API 호출 (구글 라이브러리 사용)
            created_calendar = self.service.calendars().insert(body=calendar).execute()
            print("생성된 calendarId : " + created_calendar["id"])
            # 생성된 캘린더의 calendarId 를 .txt 파일로 저장, 다른 API 에서 인자로 사용할 수 있도록 설계
            with open("../calendar_id.txt", "w") as file:
                file.write(created_calendar["id"])
            # id 필드, summary 필드가 존재하는지 검증
            self.assertIsNotNone(created_calendar.get("id"))
            self.assertIn("id", created_calendar, "\"id\" 필드가 존재하지 않음")
            self.assertIn("summary", created_calendar, "\"summary\" 필드가 존재하지 않음")
            print("TC_CALENDAR_001 : Passed")
        except HttpError as error:
            print("TC_CALENDAR_001 : Failed")
            self.fail(f"{error} 발생")
        except Exception as error:
            print("TC_CALENDAR_001 : Failed")
            self.fail(f"{error} 발생")

    def test_TC_CALENDAR_002(self):
        """
        summary 필드를 누락한 상태로 현재 로그인된 계정의 보조 캘린더 생성하기
        이 케이스는 예외 케이스로, 캘린더 생성 시 HttpError 가 발생하는 경우를 검증
        캘린더 생성이 성공적으로 수행되지 않을 때 Passed 처리
        :return:
        """
        try:
            calendar = {
                "summary": "",
                "timeZone": "Asia/Seoul"
            }
            # HttpError 발생할 것을 예상하고, 이를 통해 예외 처리 로직 검증
            with self.assertRaises(HttpError) as context:
                self.service.calendars().insert(body=calendar).execute()
            # HttpError 예외가 발생했고, 그 상태 코드가 400인지 확인
            self.assertEqual(context.exception.resp.status, 400, "400 응답 코드 반환")
            print("TC_CALENDAR_002 : Passed")
        except HttpError as error:
            print("TC_CALENDAR_002 : Failed")
            self.fail(f"{error} 발생")
        except Exception as error:
            print("TC_CALENDAR_002 : Failed")
            self.fail(f"{error} 발생")


if __name__ == "__main__":
    unittest.main()
