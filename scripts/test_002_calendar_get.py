import unittest

from authorize.authorization import get_token
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class TestCalendarGet(unittest.TestCase):

    def setUp(self):
        """
        테스트 전에 실행되어 필요한 설정을 수행함.
        Google Calendar API 가 필요하므로, auth 셋업을 위해 OAuth 2 Token 값을 가져옴.
        """
        self.token = get_token()
        credentials = Credentials(self.token)
        self.service = build('calendar', 'v3', credentials=credentials)

    # 보조 캘린더 목록을 조회하는 API TestCase
    def test_TC_CALENDAR_003(self):
        """
        현재 로그인된 계정 기본 캘린더의 메타데이터 확인하기
        insert API 를 통해 생성한 calendarId 사용
        :return:
        """
        try:
            # insert API 를 통해 생성한 캘린더의 calendarId 가져옴
            with open("../calendar_id.txt", "r") as file:
                calendar_id = file.read().strip()
            # get API 호출 (구글 라이브러리 사용)
            calendar = self.service.calendars().get(calendarId=calendar_id).execute()
            # calendarId 를 통해 캘린더 호출 시, 각 리소스 필드 (kind, etag, id, summary) 가 존재하는 지 확인
            self.assertIn("kind", calendar, "\"kind\" 필드가 존재하지 않음")
            self.assertIn("etag", calendar, "\"etag\" 필드가 존재하지 않음")
            self.assertIn("id", calendar, "\"id\" 필드가 존재하지 않음")
            self.assertIn("summary", calendar, "\"summary\" 필드가 존재하지 않음")
            print("TC_CALENDAR_003 : Passed")
        except HttpError as error:
            print("TC_CALENDAR_003 : Failed")
            self.fail(f"{error} 발생")
        except Exception as error:
            print("TC_CALENDAR_003 : Failed")
            self.fail(f"{error} 발생")

    def test_TC_CALENDAR_004(self):
        """
        유효하지 않은 타입의 calendarId 를 입력하여 해당 계정의 기본 캘린더 메타데이터 확인하기
        이 케이스는 예외 케이스로, 캘린더 조회 시 HttpError 가 발생하는 경우를 검증
        캘린더 조회가 성공적으로 수행되지 않을 때 Passed 처리
        :return:
        """
        try:
            invalid_calendar_id = "1"
            # HttpError 발생할 것을 예상하고, 이를 통해 예외 처리 로직 검증
            with self.assertRaises(HttpError) as error_context:
                self.service.calendars().get(calendarId=invalid_calendar_id).execute()
            # HttpError 예외가 발생했고, 그 상태 코드가 404인지 확인
            self.assertEqual(error_context.exception.resp.status, 404, "404 응답 코드 반환")
            print("TC_CALENDAR_004 : Passed")
        except HttpError as error:
            print("TC_CALENDAR_004 : Failed")
            self.fail(f"{error} 발생")
        except Exception as error:
            print("TC_CALENDAR_004 : Failed")
            self.fail(str(error))


if __name__ == "__main__":
    unittest.main()
