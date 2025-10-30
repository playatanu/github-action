import json
import requests
from typing import List, Dict, Any

def read_json_file(file_path: str) -> Dict[str, Any]:
    """Read and parse JSON file"""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise ValueError(f"Error reading JSON file: {e}")

def calculate_average(numbers: List[float]) -> float:
    """Calculate average of a list of numbers"""
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)

def format_name(first: str, last: str) -> str:
    """Format full name from first and last name"""
    return f"{first} {last}".title()

async def mock_api_call():
    """Simulate an async API call"""
    import asyncio
    await asyncio.sleep(0.1)
    return {"status": "success", "data": [1, 2, 3, 4, 5]}