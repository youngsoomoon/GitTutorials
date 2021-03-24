index = open("poketmon_index.txt",'rt', encoding='UTF8')
data = open("poketmon_data.txt",'rt', encoding='UTF8')

poketmon_list = list()

#poketmon에 포켓몬이름 리스트 형태로 저장 (\n 까지 포함됨)
poketmon = index.readlines() 
print(poketmon)

#poketmon_list에 \n 제거된 원소들 append
for i in poketmon:
    poketmon_list.append(i.strip())
print(poketmon_list)

index.close()

poketmon_count_list = list()

#poketmon_count_list에 poketmon_list 원소 수 만큼 0으로 채우기
for i in poketmon_list:
    poketmon_count_list.append(0)

print(poketmon_count_list)

#all_poketmonData_list에 포켓몬 데이터 리스트형태로 저장(\n 까지 포함됨)
all_poketmonData_list = data.readlines()

#each_poketmon에 포켓몬 데이터 \n빼고 저장
for each in all_poketmonData_list :
    each_poketmon = each.strip()
    #target_index에 poketmon_list에 있는 각 포켓몬의 인덱스를 저장
    target_index = poketmon_list.index(each_poketmon)
    #poketmon_count_list에 target_index로부터 들어오는 인덱스 들어올때마다 1씩 증가
    poketmon_count_list[target_index] += 1

print(poketmon_list)
print(poketmon_count_list)

#결과 예쁘게 출력하기
for i in range(len(poketmon_list)):
    print(poketmon_list[i],':', poketmon_count_list[i])
data.close()