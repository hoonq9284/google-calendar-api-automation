import unittest

from authorize.authorization import get_token
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class TestCalendarClear(unittest.TestCase):

    def setUp(self):
        """
        테스트 전에 실행되어 필요한 설정을 수행함.
        Google Calendar API 가 필요하므로, auth 셋업을 위해 OAuth 2 Token 값을 가져옴.
        """
        self.token = get_token()
        credentials = Credentials(self.token)
        self.service = build('calendar', 'v3', credentials=credentials)

    def test_TC_CALENDAR_017(self):
        """
        현재 로그인된 계정 primary 캘린더 모든 일정 삭제하기
        primary 키워드를 사용함
        :return:
        """
        try:
            calendar_id = 'primary'
            # clear API 호출 (구글 라이브러리 사용)
            self.service.calendars().clear(calendarId=calendar_id).execute()
            print("TC_CALENDAR_017 : Passed")
        except HttpError as error:
            print("TC_CALENDAR_017 : Failed")
            self.fail(f"{error} 발생")
        except Exception as error:
            print("TC_CALENDAR_017 : Failed")
            self.fail(f"{error} 발생")

    def test_TC_CALENDAR_018(self):
        """
        유효하지 않은 타입의 calendarId 를 입력하여 해당 계정의 캘린더 모든 일정 삭제하기
        이 케이스는 예외 케이스로, 캘린더 일정 삭제 시 HttpError 가 발생하는 경우를 검증
        캘린더 일정 삭제가 성공적으로 수행되지 않을 때 Passed 처리
        :return:
        """
        try:
            calendar_id = '123'
            # HttpError 발생할 것을 예상하고, 이를 통해 예외 처리 로직 검증
            with self.assertRaises(HttpError) as error_context:
                self.service.calendars().clear(calendarId=calendar_id).execute()
            # HttpError 예외가 발생했고, 그 상태 코드가 404인지 확인
            self.assertEqual(error_context.exception.resp.status, 404, "404 응답 코드 반환")
            print("TC_CALENDAR_018 : Passed")
        except HttpError as error:
            print("TC_CALENDAR_018 : Failed")
            self.fail(f"{error} 발생")
        except Exception as error:
            print("TC_CALENDAR_018 : Failed")
            self.fail(f"{error} 발생")


if __name__ == "__main__":
    unittest.main()
