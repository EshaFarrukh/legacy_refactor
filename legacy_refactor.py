def read_numbers_from_file(filename):
    """Reads integers from a file, one per line."""
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    numbers.append(int(line))
    except FileNotFoundError:
        raise FileNotFoundError("Error: File not found.")
    except ValueError:
        raise ValueError("Error: File contains non-integer values.")
    return numbers


def compute_statistics(numbers):
    """Computes total, sum, average, min, and max from a list of integers."""
    if not numbers:
        return {
            "total": 0,
            "sum": 0,
            "average": 0,
            "min": None,
            "max": None
        }

    total = len(numbers)
    total_sum = sum(numbers)
    average = round(total_sum / total)
    return {
        "total": total,
        "sum": total_sum,
        "average": average,
        "min": min(numbers),
        "max": max(numbers)
    }


def display_statistics(stats):
    """Prints the computed statistics."""
    print(f"Total = {stats['total']}")
    print(f"Summation = {stats['sum']}")
    print(f"Average = {stats['average']}")
    print(f"Minimum = {stats['min']}")
    print(f"Maximum = {stats['max']}")


if __name__ == "__main__":
    try:
        numbers = read_numbers_from_file("random_nums.txt")
        stats = compute_statistics(numbers)
        display_statistics(stats)
    except Exception as e:
        print(str(e))
