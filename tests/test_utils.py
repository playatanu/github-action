import pytest
import json
import tempfile
import os
import asyncio
from src.utils import read_json_file, calculate_average, format_name, mock_api_call


class TestUtils:
    def test_calculate_average(self):
        assert calculate_average([1, 2, 3, 4, 5]) == 3.0
        assert calculate_average([10, 20, 30]) == 20.0

    def test_calculate_average_empty_list(self):
        with pytest.raises(ValueError, match="Cannot calculate average of empty list"):
            calculate_average([])

    def test_format_name(self):
        assert format_name("john", "doe") == "John Doe"
        assert format_name("alice", "smith") == "Alice Smith"

    def test_read_json_file(self):
        # Create temporary JSON file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump({"name": "test", "value": 123}, f)
            temp_path = f.name

        try:
            data = read_json_file(temp_path)
            assert data == {"name": "test", "value": 123}
        finally:
            os.unlink(temp_path)

    def test_read_json_file_not_found(self):
        with pytest.raises(ValueError, match="Error reading JSON file"):
            read_json_file("nonexistent.json")

    @pytest.mark.asyncio
    async def test_mock_api_call(self):
        result = await mock_api_call()
        assert result["status"] == "success"
        assert result["data"] == [1, 2, 3, 4, 5]