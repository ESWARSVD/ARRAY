# Rotate the array by N times

n=int(input("Enter the number:"))

arr=input("Enter the array:").split()  #Enter the space separated values

len_arr=len(arr)

rotation=n%len_arr

#using slicing to rotate the array
first_part=arr[-rotation:]

second_part=arr[:-rotation]

rotated_array=first_part+second_part
#print rotated arrays
print("Rotated array:")
print(*rotated_array)