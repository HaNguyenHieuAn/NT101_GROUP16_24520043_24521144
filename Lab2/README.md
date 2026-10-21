# Lab 02: Mật mã học hiện đại (Modern Cryptography)

> **Môn học:** An toàn mạng máy tính (NT101)  
> **Khoa:** Mạng máy tính và Truyền thông  
> **Trường:** Đại học Công nghệ Thông tin – ĐHQG-HCM (UIT)  
> **Nhóm 16 – NT101.R11.2:** Hà Nguyễn Hiếu An (24520043), Nguyễn Hữu Nghĩa (24521144)

## Mục tiêu

Hoàn thành Nhiệm vụ 2.1 và 2.2 theo đề `NT101_Lab02__Modern_Cryptography.pdf`:
- Tự cài đặt Feistel 8 bit, theo dõi trạng thái và khoảng cách Hamming từng vòng.
- Quan sát khối lặp khi mã hóa AES-ECB/AES-CBC; thử các chế độ AES còn lại trong PyCryptodome.
- Phân biệt mã hóa bảo mật, xác thực, IV/nonce, padding và bọc khóa.

Mỗi notebook độc lập, theo format Lab1: thông tin nhóm, yêu cầu/lý thuyết, hàm xử lý, ví dụ, nhận xét, nhập liệu tùy chọn, kiểm thử và tài liệu tham khảo. Báo cáo Word/PDF nộp riêng, không sao chép tài liệu học phần vào repository.

## Cấu trúc thư mục

```text
Lab2/
├── README.md
├── requirements.txt
├── requirements-visualization.txt  # Thư viện vẽ sơ đồ, tùy chọn
├── Lab2_Task2.1.ipynb               # Feistel và sự lan truyền thay đổi
├── Lab2_Task2.2.ipynb               # Các chế độ hoạt động của AES
├── Lab2_Task2.1_Flowchart.ipynb     # Sơ đồ logic dùng Matplotlib/Seaborn
└── figures/
    ├── Lab2_Task2.1_Flowchart.png   # PNG 300 DPI để chèn report
    └── Lab2_Task2.1_Flowchart.svg   # Bản vector
```

| Nhiệm vụ | Nội dung |
|---|---|
| 2.1 | `F`, `feistel_round`, khóa con, mã hóa/giải mã, trạng thái `(L, R)`, so sánh Hamming, cặp khác đúng 1 bit |
| 2.2 | ECB, CBC, CFB-8/128, OFB, CTR, OPENPGP; EAX, GCM, CCM, OCB, SIV; KW/KWP; padding và kiểm tra dữ liệu bị sửa |

## Môi trường và cách chạy

- Python 3.10 trở lên; dùng `int.bit_count()` cho Nhiệm vụ 2.1.
- VS Code với extension Python/Jupyter hoặc JupyterLab.
- Thuật toán Feistel chỉ dùng thư viện chuẩn. AES dùng `pycryptodome>=3.23,<4` để có cả KW/KWP; không cần `numpy`, `sympy`, `matplotlib` cho hai nhiệm vụ này.

1. Mở terminal tại thư mục gốc repository và cài thư viện:

   ```powershell
   python -m pip install -r "Lab2/requirements.txt"
   python -m pip install jupyter ipykernel
   ```

2. Mở notebook, chọn kernel Python vừa cài thư viện, chọn **Restart Kernel and Run All**. Không cần chạy notebook khác trước; chạy được từ thư mục gốc hoặc thư mục Lab2, không đọc file dữ liệu hay truy cập mạng.
3. Kết quả mẫu và kiểm thử hiển thị ngay trong notebook. Cell kiểm thử phát sinh lỗi nếu có test thất bại.
4. Nhập liệu: đổi `FEISTEL_INTERACTIVE` hoặc `AES_INTERACTIVE` thành `True`, chạy riêng cell tương ứng. Đặt về `False` trước khi chạy toàn bộ không tương tác.
5. Nếu sai môi trường và báo `No module named 'Crypto'`, chạy `%pip install "pycryptodome>=3.23,<4"` trong notebook rồi khởi động lại kernel. Không cài gói `crypto` hoặc `pycrypto` thay cho PyCryptodome.

## Sơ đồ logic Task 2.1 cho report

- Mở [notebook vẽ sơ đồ](Lab2_Task2.1_Flowchart.ipynb), chọn **Run All**. Cần thư viện vẽ riêng, không ảnh hưởng yêu cầu của hai notebook thuật toán:

  ```powershell
  python -m pip install -r "Lab2/requirements-visualization.txt"
  ```

- [PNG 300 DPI](figures/Lab2_Task2.1_Flowchart.png): chèn vào Word. [SVG](figures/Lab2_Task2.1_Flowchart.svg): phóng to không vỡ nét.
- Matplotlib vẽ khối và mũi tên; Seaborn tạo bảng màu và heatmap Hamming. Sơ đồ gồm luồng chính, vòng lặp Feistel và nhận xét; không đưa kiểm thử hoặc kiểm tra đầu vào vào sơ đồ.
- Notebook vẽ đọc riêng định nghĩa hàm trong cell `feistel-core` của Task 2.1 để tính số liệu; không chạy ví dụ/nhập liệu/kiểm thử và không sửa notebook thuật toán. Chạy từ thư mục gốc hoặc Lab2.
- Hai lời gọi tuần tự M1 rồi M2 được gộp bằng vòng lặp minh họa, không đổi thứ tự xử lý. Giải mã là bước bổ sung; `compare_avalanche` tính lại hai trace theo mã hiện tại.

## Kết quả và lưu ý quan trọng

### Nhiệm vụ 2.1

- Giữ đúng `F(R, K) = (R XOR K) & 0x0F` và bốn khóa con trong scaffold; không đổi chỗ thêm sau vòng cuối.
- Với khóa `0x12`: `0xAB` mã hóa thành `0x94`; `0xAC` thành `0xE3`.
- Đề ghi cặp này khác 1 bit, nhưng thực tế khác **3 bit**: `0xAB XOR 0xAC = 0x07`.
- Khoảng cách Hamming từ khởi tạo đến vòng 4: **3, 6, 3, 3, 6**. Cặp bổ sung `0xAB/0xAA` khác đúng 1 bit cho **1, 2, 1, 1, 2**.
- Không có xu hướng tăng đều: hàm vòng tuyến tính không trộn vị trí bit, sai khác có chu kỳ 3 vòng. Notebook giải thích hạn chế thay vì khẳng định hiệu ứng thác đổ mạnh.
- Kiểm thử gồm toàn bộ **65.536 cặp bản rõ/khóa**, xác minh mã hóa/giải mã và tính hoán vị.

### Nhiệm vụ 2.2

- Đúng bản rõ 32 byte và khóa ASCII 16 byte trong đề. IV CBC cố định là `b'0000000000000000'` (Hex `30` lặp 16 lần), không phải `bytes(16)`.
- Ví dụ chính không padding: hai khối ECB trùng; hai khối CBC khác trong mẫu. Phần padding minh họa PKCS#7: 32 byte thành 48 byte.
- CFB thử rõ `segment_size=8` và `128`; mặc định thư viện là 8. OPENPGP tách 18 byte IV đã mã hóa khỏi ciphertext dữ liệu khi so sánh khối.
- EAX/GCM/CCM/OCB/SIV có tag, xác thực AAD; sửa ciphertext, tag, AAD, nonce hoặc dùng sai khóa phải bị từ chối. SIV dùng khóa 32 byte riêng, thử thêm trường hợp không nonce.
- KW/KWP thử riêng với dữ liệu khóa: dùng `seal/unseal`, không coi là mã hóa văn bản. Có vector kiểm thử FIPS 197 và RFC 3394.

**An toàn:** Feistel mẫu và khóa/IV/nonce cố định chỉ phục vụ học tập. Không dùng cấu hình mẫu cho dữ liệu thực tế. Tránh ECB; ưu tiên AEAD như AES-GCM/EAX, quản lý khóa đúng cách và không lặp nonce với cùng khóa. Các chế độ cổ điển không tự xác thực dữ liệu; bỏ padding thành công không chứng minh dữ liệu nguyên vẹn.

## Kiểm chứng

- Đã chạy độc lập cả hai notebook bằng kernel Jupyter mới trên Python 3.13.9, PyCryptodome 3.24.1; lưu output trong notebook.
- Nhiệm vụ 2.1: **10 kiểm thử đạt**; Nhiệm vụ 2.2: **16 kiểm thử đạt**. Các phương thức kiểm thử có thêm nhiều trường hợp con và vòng lặp kiểm tra.
- Các cờ nhập liệu giữ `False`; chạy toàn bộ không chờ người dùng nhập.

## Tài liệu tham khảo

- Đề học phần, Nhiệm vụ 2.1–2.2; nguồn chi tiết ghi trong từng notebook.
- [AES API](https://www.pycryptodome.org/src/cipher/aes).
- [Chế độ cổ điển](https://www.pycryptodome.org/src/cipher/classic).
- [AEAD và bọc khóa](https://www.pycryptodome.org/src/cipher/modern).
