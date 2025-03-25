import multiprocessing


def square_number(number: int) -> int:
    """
    Square a single number.
    
    :param number: Input number to be squared
    :return: Squared result
    """
    return number ** 2


def process_with_pool(numbers: list[int]) -> list[int]:
    """
    Process numbers using multiprocessing Pool.
    
    :return: List of processed numbers
    """
    # Create a pool of worker processes
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # Map the square_number function to all numbers
        results = pool.map(square_number, numbers)
    
    return results


if __name__ == "__main__":
    n = [x for x in range(1, 25 + 1)]

    pool_results = process_with_pool(n)

    print(f"Original list: {n}")
    print(f"Squared numbers: {pool_results}")
