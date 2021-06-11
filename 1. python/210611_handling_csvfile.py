"""
    csv = comma separate value
        - csv, 필드를 쉼표로 구분한 텍스트 파일
        - 엑셀 양식의 데이터를 프로그램과 상관없이 쓰기 위한 데이터 형식
        - 탭(TSV), 빈칸(SSV)등으로 구분해서 만들기도 함
        - 통칭하여 Character-separated values (CSV) 라 부름
        - 엑셀에서는 "다른 이름으로 저장" 기능으로 csv 파일 생성 가능
"""

line_counter = 0  # 파일의 총 개수를 세는 변수
data_header = []  # 데이터의 필드값을 저장하는 리스트
employee = []
customer_USA_only_list = []
customer = None

with open("customer.csv", "r") as customer_data:
    while True:
        data = customer_data.readline()  # customer.csv를 한줄씩 읽어오기
        if not data:
            break  # 데이터가 없을 때 loop 종료
        if line_counter == 0:  # 첫 번째 데이터는 데이터의 필드값
            data_header = data.split(",")  # 데이터의 필드값은 ","로 분리하여 data_header에 저장
        else:
            customer = data.split(",")  # 일반 데이터는 ","로 분리
            if customer[10] == "USA":
                customer_USA_only_list.append(customer)
        line_counter += 1

print("Header :\t", data_header)  # 데이터 필드값 출력
for i in range(10):  # 데이터 샘플 총 10개 출력
    print("Data", i, "\t\t", customer_USA_only_list[i])
print(len(customer_USA_only_list))  # 전체 데이터 크기 출력

with open("customer_USA_only.csv", "w") as customer_USA_only_csv:
    for customer in customer_USA_only_list:
        customer_USA_only_csv.write(",".join(customer).strip("\n") + "\n")
