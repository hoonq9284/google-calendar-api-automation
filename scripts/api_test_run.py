import unittest
import sys
import os

# 현재 스크립트의 디렉토리를 기준으로 상위 디렉토리 경로를 sys.path에 추가
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


if __name__ == "__main__":
    # Test loader를 설정하여 scripts 디렉토리 내의 모든 테스트를 자동으로 찾아서 실행
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='.', pattern='*.py')  # 현재 디렉토리와 모든 .py 파일 검색
    runner = unittest.TextTestRunner()
    runner.run(suite)
