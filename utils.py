def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def calculate_stats(numbers):
    if not numbers:
        return {}
    
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    return {
        "total": total,
        "average": average,
        "max": maximum,
        "min": minimum,
        "count": len(numbers)
    }

def format_message(title, data):
    message = f"\n📊 {title}:\n"
    for key, value in data.items():
        message += f"   {key}: {value}\n"
    return message

def process_data(data_list):
    processed = []
    for item in data_list:
        if isinstance(item, (int, float)):
            processed.append(item * 2)
        elif isinstance(item, str):
            processed.append(item.upper())
    return processed