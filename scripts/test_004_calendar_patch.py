import unittest

from authorize.authorization import get_token
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class TestCalendarPatch(unittest.TestCase):

    def setUp(self):
        """
        테스트 전에 실행되어 필요한 설정을 수행함.
        Google Calendar API 가 필요하므로, auth 셋업을 위해 OAuth 2 Token 값을 가져옴.
        """
        self.token = get_token()
        credentials = Credentials(self.token)
        self.service = build('calendar', 'v3', credentials=credentials)

    def test_TC_CALENDAR_012(self):
        """
        현재 로그인된 계정의 캘린더 summary 필드 업데이트하기
        insert API 를 통해 생성한 calendarId 사용
        :return:
        """
        try:
            # insert API 를 통해 생성한 캘린더의 calendarId 가져옴
            with open("../calendar_id.txt", "r") as file:
                calendar_id = file.read().strip()
            # 지정한 calendarId 를 인자로 전달한 get API 호출 (구글 라이브러리 사용)
            calendar = self.service.calendars().get(calendarId=calendar_id).execute()
            # summary 필드를 'Patch Summary' 로 수정
            calendar['summary'] = 'Patch Summary'
            # patch API 호출 (구글 라이브러리 사용)
            self.service.calendars().patch(calendarId=calendar['id'], body=calendar).execute()
            print("TC_CALENDAR_012 : Passed")
        except HttpError as error:
            print("TC_CALENDAR_012 : Failed")
            self.fail(f"{error} 발생")
        except Exception as error:
            print("TC_CALENDAR_012 : Failed")
            self.fail(f"{error} 발생")

    def test_TC_CALENDAR_013(self):
        """
        현재 로그인된 계정의 캘린더 description 필드 업데이트하기
        insert API 를 통해 생성한 calendarId 사용
        :return:
        """
        try:
            # insert API 를 통해 생성한 캘린더의 calendarId 가져옴
            with open("../calendar_id.txt", "r") as file:
                calendar_id = file.read().strip()
            # 지정한 calendarId 를 인자로 전달한 get API 호출 (구글 라이브러리 사용)
            calendar = self.service.calendars().get(calendarId=calendar_id).execute()
            # description 필드를 'Patch Description' 으로 수정
            calendar['description'] = 'Patch Description'
            # patch API 호출 (구글 라이브러리 사용)
            self.service.calendars().patch(calendarId=calendar['id'], body=calendar).execute()
            print("TC_CALENDAR_013 : Passed")
        except HttpError as error:
            print("TC_CALENDAR_013 : Failed")
            self.fail(f"{error} 발생")
        except Exception as error:
            print("TC_CALENDAR_013 : Failed")
            self.fail(f"{error} 발생")

    def test_TC_CALENDAR_014(self):
        """
        현재 로그인된 계정의 캘린더 location 필드 업데이트하기
        insert API 를 통해 생성한 calendarId 사용
        :return:
        """
        try:
            # insert API 를 통해 생성한 캘린더의 calendarId 가져옴
            with open("../calendar_id.txt", "r") as file:
                calendar_id = file.read().strip()
            # 지정한 calendarId 를 인자로 전달한 get API 호출 (구글 라이브러리 사용)
            calendar = self.service.calendars().get(calendarId=calendar_id).execute()
            # location 필드를 'Patch Location' 으로 수정
            calendar['location'] = 'Patch Location'
            # patch API 호출 (구글 라이브러리 사용)
            self.service.calendars().patch(calendarId=calendar['id'], body=calendar).execute()
            print("TC_CALENDAR_014 : Passed")
        except HttpError as error:
            print("TC_CALENDAR_014 : Failed")
            self.fail(f"{error} 발생")
        except Exception as error:
            print("TC_CALENDAR_014 : Failed")
            self.fail(f"{error} 발생")

    def test_TC_CALENDAR_015(self):
        """
        현재 로그인된 계정의 캘린더 timeZone 필드 업데이트하기
        insert API 를 통해 생성한 calendarId 사용
        :return:
        """
        try:
            # insert API 를 통해 생성한 캘린더의 calendarId 가져옴
            with open("../calendar_id.txt", "r") as file:
                calendar_id = file.read().strip()
            # 지정한 calendarId 를 인자로 전달한 get API 호출 (구글 라이브러리 사용)
            calendar = self.service.calendars().get(calendarId=calendar_id).execute()
            # timeZone 필드를 'Europe/Zurich' 으로 수정
            calendar['timeZone'] = 'Europe/Zurich'
            # patch API 호출 (구글 라이브러리 사용)
            self.service.calendars().patch(calendarId=calendar['id'], body=calendar).execute()
            print("TC_CALENDAR_015 : Passed")
        except HttpError as error:
            print("TC_CALENDAR_015 : Failed")
            self.fail(f"{error} 발생")
        except Exception as error:
            print("TC_CALENDAR_015 : Failed")
            self.fail(f"{error} 발생")

    def test_TC_CALENDAR_016(self):
        """
        현재 로그인된 계정의 캘린더 timeZone 비유효한 값으로 업데이트하기
        이 케이스는 예외 케이스로, 캘린더 업데이트 시 HttpError 가 발생하는 경우를 검증
        캘린더 업데이트가 성공적으로 수행되지 않을 때 Passed 처리
        :return:
        """
        try:
            # insert API 를 통해 생성한 캘린더의 calendarId 가져옴
            with open("../calendar_id.txt", "r") as file:
                calendar_id = file.read().strip()
            # 지정한 calendarId 를 인자로 전달한 get API 호출 (구글 라이브러리 사용)
            calendar = self.service.calendars().get(calendarId=calendar_id).execute()
            # timeZone 필드를 'Patch Test Timezone' 으로 수정
            calendar['timeZone'] = 'Patch Test Timezone'
            # HttpError 발생할 것을 예상하고, 이를 통해 예외 처리 로직 검증
            with self.assertRaises(HttpError) as error_context:
                self.service.calendars().update(calendarId=calendar['id'], body=calendar).execute()
            # HttpError 예외가 발생했고, 그 상태 코드가 400인지 확인
            self.assertEqual(error_context.exception.resp.status, 400, "400 응답 코드 반환")
            print("TC_CALENDAR_016 : Passed")
        except HttpError as error:
            print("TC_CALENDAR_016 : Failed")
            self.fail(f"{error} 발생")
        except Exception as error:
            print("TC_CALENDAR_016 : Failed")
            self.fail(f"{error} 발생")


if __name__ == "__main__":
    unittest.main()
