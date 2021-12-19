from file_process import file_copy_to_list
from file_process import file_copy_to_list_exclude_enter
from file_process import list_copy_to_file_exclude_enter
from frequency_analysis import descending_order_sort
from frequency_analysis import frequency_analysis_decode

# 암호문 읽어오기
# output : listed text
# 암호문을 다시 listed_encode_text 에 읽음
listed_encode_text = file_copy_to_list("C:\\Users\\gunma\\Documents\\encoded_text.txt")

# file 로 저장된 Key(빈도 수) 읽어오기
# output: listed text
key_list = file_copy_to_list_exclude_enter("C:\\Users\\gunma\\Documents\\key(count).txt")

# Key(빈도 수)를 내림차순으로 정렬한 문자열 구하기
# output : listed_text(내림차순으로 정렬된 빈도수에 대응하는 문자열)
sort_by_char_list = descending_order_sort(key_list)

# 복호화
# output : listed text
listed_decode_text = frequency_analysis_decode(listed_encode_text, sort_by_char_list)

# 복호문 저장
# output : file(모든 문자를 그대로 입력)
list_copy_to_file_exclude_enter(listed_decode_text, "C:\\Users\\gunma\\Documents\\decoded_text.txt")
