groups = ['HOT', 'Seventeen', 'Black Pink', 'NJZ']
ratings = [1, 2, 4, 3]


groups_rating = list(zip(groups, ratings))
# zip 함수는 대응되는 인덱스 끼리 묶어 튜플로 반환 (두 인덱스의 크기가 다를땐 작은 크기 만큼 생성)
print(groups_rating)
