# filename.py
import os

class Filename:
    """Directory and Filename"""
    @staticmethod
    def test_file(year):
        """Sets test filename"""
        base_dir = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__))), 'data/test_data')
        
        # Check if diretory exists
        os.makedirs(base_dir, exist_ok=True)

        return os.path.join(base_dir, f'test_{year}.json')
    
    @staticmethod
    def filename(year):
        """Sets filename"""
        base_dir = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__))), 'data')
        
        # Check if directory exists
        os.makedirs(base_dir, exist_ok=True)

        return os.path.join(base_dir, f'{year}_entry.json')