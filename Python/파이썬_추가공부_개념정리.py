sorted(list(set(test_list)))와 list(set(sorted(test_list)))의 차이점

sorted(list(set(test_list)))
-> 중복 제거 후 정렬된 리스트를 얻음
list(set(sorted(test_list)))
-> 정렬된 후 중복 제거된 리스트를 얻지만, 결과는 정렬되지 않은 리스트임
-> set -> list 변환 되는 과정에서 정렬된 순서로 변환되는것이 보장 되지 않음
