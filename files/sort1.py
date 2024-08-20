def insertion_sort(arr):
    # เริ่มจาก index ที่ 1 เพราะ index 0 ถือว่าเรียงลำดับแล้ว
    for i in range(1, len(arr)):
        key = arr[i]  # เก็บค่าขององค์ประกอบที่กำลังพิจารณา
        j = i - 1

        # เลื่อนค่าของ arr[j] ที่มากกว่า key ไปข้างหน้า
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # วาง key ในตำแหน่งที่ถูกต้อง
        arr[j + 1] = key

    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # สถานะว่าไม่มีการสลับกันในรอบนี้
        swapped = False
        
        # ลูปผ่าน array จาก 0 ถึง n-i-1
        for j in range(0, n-i-1):
            # ถ้า element ปัจจุบันมากกว่าถัดไป ให้สลับกัน
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # ถ้าไม่มีการสลับกันในรอบนี้ แสดงว่า array เรียงลำดับแล้ว
        if not swapped:
            break
    
    return arr

def quick_sort(arr):
    # ฐานของ recursion: ถ้า array มีขนาด 1 หรือน้อยกว่า ถือว่าเรียงลำดับแล้ว
    if len(arr) <= 1:
        return arr

    # เลือก pivot โดยปกติแล้วเลือกตัวสุดท้ายของ array
    pivot = arr[-1]
    
    # แบ่ง array ออกเป็นสองส่วน: น้อยกว่าและมากกว่า pivot
    less_than_pivot = [x for x in arr[:-1] if x <= pivot]
    greater_than_pivot = [x for x in arr[:-1] if x > pivot]
    
    # เรียกใช้ quick sort แบบ recursive
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# ตัวอย่างการใช้งาน
arr = [12, 11, 13, 5, 6]
sorted_arr1 = insertion_sort(arr)
sorted_arr2 = bubble_sort(arr)
sorted_arr3 = quick_sort(arr)
print("Insertion Sorted array:", sorted_arr1)
print("Bubble Sorted array:", sorted_arr2)
print("Quick Sorted array:", sorted_arr3)
