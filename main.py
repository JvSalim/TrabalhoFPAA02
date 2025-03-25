def max_min_select(arr, low, high):
    if low == high:
        return (arr[low], arr[low])  # Apenas 1 elemento

    if high == low + 1:
        return (arr[low], arr[high]) if arr[low] < arr[high] else (arr[high], arr[low])  # 1 comparação

    mid = (low + high) // 2

    min_left, max_left = max_min_select(arr, low, mid)
    min_right, max_right = max_min_select(arr, mid + 1, high)

    overall_min = min(min_left, min_right)
    overall_max = max(max_left, max_right)

    return (overall_min, overall_max)

if __name__ == "__main__":
    arr = [7, 12, 14, 3, 9, 6, 4, 1]
    min_val, max_val = max_min_select(arr, 0, len(arr) - 1)
    print("Array:", arr)
    print("Máximo:", max_val)
    print("Mínimo:", min_val)
