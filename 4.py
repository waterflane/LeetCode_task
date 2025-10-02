def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    all_len = (len(nums1)+len(nums2))
    med_is_fraction = True if all_len%2 == 0 else False
    list_med = []

    nums2.append(9223372036854775807)
    nums1.append(9223372036854775807)

    i_1, i_2 = 0, 0
    for i in range(all_len):
        if int(all_len/2)+1==i+1 and med_is_fraction == False:
            return min(nums1[i_1], nums2[i_2])
        elif (int(all_len/2) == i+1 or int(all_len/2)+1 == i+1) and med_is_fraction == True:
            if list_med: 
                list_med.append(min(nums1[i_1], nums2[i_2]))
                return (list_med[0]+list_med[1])/2
            list_med.append(min(nums1[i_1], nums2[i_2]))
        if nums1[i_1]>nums2[i_2]: 
            i_2=i_2+1 if i_2 != len(nums2)-1 else i_2+1
            nums2.append(9223372036854775807)
        else: 
            i_1=i_1+1 if i_1 != len(nums1)-1 else i_1+1
            nums1.append(9223372036854775807)

print(findMedianSortedArrays([1,3], [2]))
print(findMedianSortedArrays([1,2], [3,4]))
print(findMedianSortedArrays([1], []))
print(findMedianSortedArrays([2,2,4,4], [2,2,4,4]))
