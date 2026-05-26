
choice = 0
account_name = 'h'
hashtag = '#'.split(",")
dec_video = 'sói cô độc'

while choice != 5:
    choice = input('''
+==============================================+                  
|       HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK       |
+==============================================+
|1. Nhập và phân tích thông tin video          |
|2. Chuẩn hóa tên tài khoản                    |
|3. Kiểm tra tính hợp lệ của hashtag           |
|4. Tìm kiếm và thay thê từ khóa trong mô tả   |
|5. Thoát chương trình                         |
+==============================================+
> Mời bạn chọn chức năng (1-5): ''')
    
    if choice.isdigit() != True:
        print("mời nhập số nguyên 1-5")
    else:
        choice = int(choice)

        match choice:
            case 1:
                while True: 
                    account_name = input("Nhập tên tài khoản người đăng: ")
                    title_video = input("Nhập tiêu đề video: ")
                    dec_video = input("Nhập mô tả video: ")
                    hashtag = input("Nhập hashtag (cách nhau bằng dấu ,): ").split(",")

                    if account_name == "":
                        print("Lỗi tên đăng nhập không được rỗng")
                        continue

                    if title_video == "":
                        print("Lỗi tiêu đề không được rỗng")
                        continue

                    if dec_video == "":
                        print("Lỗi mô tả không được rỗng")
                        continue

                    print("=== Thông xin in ra ===")
                    print(f"Tên tài khoản: {account_name.strip()}")
                    print(f"Tiêu đề      : {title_video.strip()}")
                    print(f"Mô tả        : {dec_video.strip()}")

                    print(f"Độ dài mô tả video: {len(dec_video)}")
                    print(f"Số lượng từ trong mô tả video: {len(dec_video.split())}")

                    print("Danh sách hashtag:", end=" ")
                    for i in range(len(hashtag)):
                        print(f"[{hashtag[i].strip()}]", end="")

                    print(f"\nSố lượng hashtag: {len(hashtag)}")

                    print(f"{dec_video.strip().lower()}")
                    print(f"{dec_video.strip().upper()}")

                    break
            case 2:
                if account_name == 'h':
                    account_name = input("Nhập tên tài khoản người đăng: ")
                    print("Tên sau khi chuẩn hóa: ", end="")
                    print("@" + account_name)
                else:
                    print("Tên sau khi chuẩn hóa: ", end="")
                    print("@" + account_name)

            case 3:
                
                while True:
                    add_hashtag = input("Thêm hashtag: ").strip()

                    isTrue = True
                    error_hashtag = ""

                    for i in range(len(add_hashtag)):
                        if add_hashtag == "":
                            isTrue = False
                            error_hashtag = "hashtag không được rỗng"
                        
                        if add_hashtag[0] != "#":
                            isTrue = False
                            error_hashtag = "hashtag phải bắt đầu bằng #"

                        if " " in add_hashtag:
                            isTrue = False
                            error_hashtag = "hashtag không được chứa khoảng trắng"

                        if len(add_hashtag) < 2:
                            isTrue = False
                            error_hashtag = "hashtag không được ít hơn 2 kí tự"

                        if not (add_hashtag[i].isalnum() or add_hashtag[i] == "_" or add_hashtag[0] == "#"):
                            isTrue = False
                            error_hashtag = "hashtag chỉ chứa chữ, số, _ hoặc #"

                    if isTrue == True:
                        print("Hashtag hợp lệ")
                        hashtag.append(add_hashtag)
                        break
                    else:
                        print("Hashtag không hợp lệ")
                        print(error_hashtag)
                    
            case 4:
                search_input = input("Nhập từ khóa cần tìm: ")
                new_dec = input("Nhập từ khóa thay thế: ")
                
                is_find = dec_video.find(search_input)

                if is_find != -1:
                    old_dec = dec_video[is_find : is_find + len(search_input)]
                    dec_video = dec_video.replace(search_input, new_dec)

                    print(f"Mô tả mới: {dec_video}")
                else:
                    print("Không tìm thấy từ khóa mà bạn nhập: ")


            case 5:
                print("thoát chương trình")
                break
            case _:
                print("Nhập không đúng mời nhập lại")