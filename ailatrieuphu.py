import random

BO_CAU_HOI_LIST = [
    'Có câu thành ngữ: "Đi mây về ..." gì? --- ⬥ A: Mây\t⬥ B: Núi\t⬥ C: Biển\t⬥ D: Gió\n',
    'Đâu là một cách nói ví von về những trường hợp gặp vận hạn, rủi ro? --- ⬥ A: Sao quả cân\t⬥ B: Sao quả tạ\t⬥ C: Sao quả tấn\t⬥ D: Sao quả yến\n',
    'Gỗ mun có màu gì? --- ⬥ A: Vàng\t⬥ B: Nâu\t⬥ C: Đen\t⬥ D: Xanh\n',
    'Câu nào chỉ tình cảnh đơn độc, yếu thế không có chỗ dựa? --- ⬥ A: Thân tàn ma dại\t⬥ B: Thân cô thế cô\t⬥ C: Thân lừa ưa nặng\t⬥ D: Thân làm tội đời\n',
    'Đâu là tên một loại đồ chơi dân gian của trẻ em? --- ⬥ A: Tò he\t⬥ B: Tò mò\t⬥ C: Tò vò\t⬥ D: Tến tò\n',
    'Đâu là tên một bãi biển ở Quảng Bình? --- ⬥ A: Đá Lăn\t⬥ B: Đá Nhảy\t⬥ C: Đá Chạy\t⬥ D: Đá Bò\n',
    'Đâu là tên một loại chợ? --- ⬥ A: Ếch\t⬥ B: Nhái\t⬥ C: Thằn lằn\t⬥ D: Cóc\n',
    'Tượng đài Chiến thắng Điện Biên Phủ được dựng trên ngọn đồi nào? --- ⬥ A: D1\t⬥ B: C1\t⬥ C: A1\t⬥ D: E1\n',
    'Nhà văn Kim Dung (Trung Quốc) nổi tiếng với thể loại văn học gì? --- ⬥ A: Truyện trinh thám\t⬥ B: Tiểu thuyết kiếm hiệp\t⬥ C: Sử thi\t⬥ D: Thơ lãng mạn\n',
    'Bộ phim "Chị Dậu" được chuyển thể từ tác phẩm nào? --- ⬥ A: Người mẹ cầm súng\t⬥ B: Vợ chồng A Phủ\t⬥ C: Tắt đèn\t⬥ D: Tuổi thơ dữ dội\n',
    'Loại cá nào bé hơn cả? --- ⬥ A: Voi\t⬥ B: Bống\t⬥ C: Mập\t⬥ D: Heo\n',
    'Giọng khàn khàn còn được ví với gì? --- ⬥ A: Thiên nga\t⬥ B: Vịt đực\t⬥ C: Ngan xiêm\t⬥ D: Ngỗng\n',
    'Sầu riêng Cái Mơn là đặc sản của tỉnh nào? --- ⬥ A: Tiền Giang\t⬥ B: Cà Mau\t⬥ C: Bến Tre\t⬥ D: Đồng Tháp\n',
    'Loại củ nào sau đây có thể giúp cho vết thương mau lành và ít để lại sẹo? --- ⬥ A: Giềng\t⬥ B: Hành tây\t⬥ C: Gừng\t⬥ D: Nghệ\n',
    'Cướp biển còn được gọi với tên khác là gì? --- ⬥ A: Đạo tặc\t⬥ B: Lâm tặc\t⬥ C: Tin tặc\t⬥ D: Hải tặc\n',
    'Hoa hậu Hòa bình Quốc tế 2017 dự kiến sẽ được tổ chức tại quốc gia nào? --- ⬥ A: Thái Lan\t⬥ B: Việt Nam\t⬥ C: Lào\t⬥ D: Campuchia\n',
    'Vườn quốc gia nào hiện không nằm trong danh sách Vườn di sản ASEAN? --- ⬥ A: Vườn quốc gia Kon Ka Kinh\t⬥ B: Vườn quốc gia Tam Đảo\t⬥ C: Vườn quốc gia Chư Mom Ray\t⬥ D: Vườn quốc gia Bái Tử Long\n',
    'Nhạc sĩ nào là người phổ nhạc ca khúc "Cây đàn sinh viên"? --- ⬥ A: Bảo Chấn\t⬥ B: Trịnh Công Sơn\t⬥ C: Quốc An\t⬥ D: Trần Tiến\n',
    'Đâu không phải là một tác phẩm của họa sĩ Trần Văn Cẩn? --- ⬥ A: Đôi bạn\t⬥ B: Mẹ tôi\t⬥ C: Em Thúy\t⬥ D: Em gái tôi'
]

CAU_TRA_LOI_LIST = ['D\n', 'B\n', 'C\n', 'B\n', 'A\n', 'B\n', 'D\n', 'C\n', 'B\n', 'C\n', 'B\n', 'B\n', 'C\n', 'D\n', 'D\n', 'B\n', 'B\n', 'C\n', 'A']
GIAI_THUONG_LIST = ['   100.000  \n', '150.000\n', '300.000\n', '600.000\n', '1.000.000\n', '2.500.000\n', '6.000.000\n', '11.000.000\n', '22.000.000\n', '35.000.000\n', '66.000.000\n', '99.000.000\n', '120.000.000\n', '250.000.000\n', '500.000.000']

CAU_TRA_LOI_LIST_ADJUST = [i.strip() for i in CAU_TRA_LOI_LIST]
GIAI_THUONG_LIST_ADJUST = [j.strip() for j in GIAI_THUONG_LIST]

CAU_HOI_DA_RA = []
SO_THU_TU = 0
QUYEN_TRO_GIUP = [1, 2]

while True:
    if SO_THU_TU == 15:
        print("Chúc mừng bạn đã chiến thắng!")
        break

    print("Câu hỏi thứ {}".format(SO_THU_TU + 1))

    # Chọn câu hỏi ngẫu nhiên chưa xuất hiện
    while True:
        VI_TRI_CAU_HOI = random.randint(0, len(BO_CAU_HOI_LIST) - 1)
        if VI_TRI_CAU_HOI not in CAU_HOI_DA_RA:
            CAU_HOI_DA_RA.append(VI_TRI_CAU_HOI)
            break

    print(BO_CAU_HOI_LIST[VI_TRI_CAU_HOI])

    # Xử lý quyền trợ giúp
    if (1 in QUYEN_TRO_GIUP) or (2 in QUYEN_TRO_GIUP):
        if 1 in QUYEN_TRO_GIUP and 2 in QUYEN_TRO_GIUP:
            quyen_tro_giup = int(input("""
            Bạn có muốn nhận được quyền trợ giúp dưới đây:
                1. 50/50
                2. Khảo sát khán giả trường quay
                3. Không cần trợ giúp
            """))
        elif 1 in QUYEN_TRO_GIUP:
            quyen_tro_giup = int(input("""
            Bạn có muốn nhận được quyền trợ giúp dưới đây:
                1. 50/50
                3. Không cần trợ giúp
            """))
        elif 2 in QUYEN_TRO_GIUP:
            quyen_tro_giup = int(input("""
            Bạn có muốn nhận được quyền trợ giúp dưới đây:
                2. Khảo sát khán giả trường quay
                3. Không cần trợ giúp
            """))

        if quyen_tro_giup == 1:
            print("Bạn đã chọn quyền trợ giúp 50/50.")
            dap_an_1 = CAU_TRA_LOI_LIST_ADJUST[VI_TRI_CAU_HOI]
            dap_an_2 = chr(random.randint(65, 68))
            while dap_an_2.lower() == dap_an_1.lower():
                dap_an_2 = chr(random.randint(65, 68))
            dap_an_list = [dap_an_1, dap_an_2]
            random.shuffle(dap_an_list)
            print("Đáp án còn lại: {} và {}".format(dap_an_list[0], dap_an_list[1]))
            QUYEN_TRO_GIUP.remove(1)
        elif quyen_tro_giup == 2:
            print("Bạn đã chọn quyền trợ giúp khảo sát khán giả.")
            # Code cho quyền trợ giúp khảo sát khán giả có thể thêm vào sau
            QUYEN_TRO_GIUP.remove(2)
        else:
            print("Bạn đã không chọn quyền trợ giúp.")

    # Nhập câu trả lời
    user_answer = input("Nhập vào câu trả lời của bạn: ").strip()

    # Kiểm tra đáp án
    if user_answer.lower() == CAU_TRA_LOI_LIST_ADJUST[VI_TRI_CAU_HOI].lower():
        print(f"Chúc mừng bạn đã trả lời đúng! ---> Giải thưởng của bạn hiện tại là {GIAI_THUONG_LIST_ADJUST[SO_THU_TU]} đồng.")
        SO_THU_TU += 1
        if SO_THU_TU == len(GIAI_THUONG_LIST_ADJUST):
            print("Chúc mừng bạn đã hoàn thành trò chơi với tổng giải thưởng cao nhất!")
            break
    else:
        print(f"Rất tiếc, bạn đã trả lời sai. Bạn nhận được {GIAI_THUONG_LIST_ADJUST[max(SO_THU_TU - 1, 0)]} đồng.")
        break
