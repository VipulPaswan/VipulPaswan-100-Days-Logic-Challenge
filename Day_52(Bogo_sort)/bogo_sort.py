import random
import time

def is_sorted(data):
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True  

def bogo_sort(data):
    print("--- Starting Bogo Sort (may take time!) ---")
    attempts = 0
    start_time = time.time()

    while not is_sorted(data):
        random.shuffle(data)
        attempts += 1

        if attempts > 10_000_000:
            print("Reached Max Attempts (10,000,000).")
            break

    end_time = time.time()
    t = end_time - start_time

    if is_sorted(data):
        print(f"{attempts} attempts in {t:.4f} seconds.")

    return data

if __name__ == "__main__":
    list_bogo = [3, 1, 10, 4, 8, 2, 9, 7, 6, 5]
    print("\nOriginal List (Bogo):", list_bogo)

    sorted_bogo = bogo_sort(list_bogo)

    print("\nSorted List (Bogo):", sorted_bogo)
