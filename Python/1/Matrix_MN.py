"""Matrix_MN"""
def matrix():
    """Matrix_MN"""
    row = int(input())
    col = int(input())
    list_out = []
    for _ in range(row):
        sub_list = []    #สร้าง Sub_List ใหม่
        for _ in range(col):
            sub_list.append(int(input()))   #เก็บข้อมูลรอบ Sub_List
        list_out.append(sub_list)      #เก็บข้อมูลเข้า List_Out
    for i in range(len(list_out)): #Print แยกบรรทัด
        print(*list_out[i])      #Printตามตำแหน่ง [i]
matrix()
