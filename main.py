from utils import calculate_stats, format_message

def main():
    print("🚀 Running Python Script on GitHub Actions!")
    
    # Test calculations
    numbers = [10, 20, 30, 40, 50]
    stats = calculate_stats(numbers)
    
    # Display results
    message = format_message("Calculation Results", stats)
    print(message)
    
    # Simple file operation
    with open("output.txt", "w") as f:
        f.write(f"Results: {stats}")
    
    print("✅ Script completed successfully!")
    return stats

if __name__ == "__main__":
    result = main()
    print(f"Final result: {result}")