# Lab 03 Hàm băm và chữ ký số

**Nhóm 16 · NT101.R11.2 · UIT**  
Hà Nguyễn Hiếu An (24520043), Nguyễn Hữu Nghĩa (24521144)

## Phạm vi

Chỉ thực hiện **Nhiệm vụ 2.1 Mã hóa khóa công khai RSA** trong đề Lab03:

1. Tính ba cặp khóa công khai và khóa riêng từ các bộ p, q, e đã cho.
2. Minh họa hai chiều RSA với M = 5 theo yêu cầu bảo mật và xác thực của đề.
3. Mã hóa `The University of Information Technology` bằng cả ba khóa và biểu diễn Base64.
4. Khôi phục bốn bản mã Base64, Hex và nhị phân trong đề.

Không triển khai Nhiệm vụ 2.2, 2.3 và 2.4.

## Tệp thực hành

| Tệp | Nội dung |
|---|---|
| [Lab3_Task2.1.ipynb](Lab3_Task2.1.ipynb) | Notebook độc lập gồm lý thuyết, thuật toán, ví dụ, nhập liệu tùy chọn, kiểm thử và nhận xét |

## Cách chạy

- Python **3.10 trở lên**. Thuật toán chỉ dùng thư viện chuẩn, không cần PyCryptodome hay dữ liệu ngoài.
- Mở notebook bằng VS Code Python/Jupyter hoặc JupyterLab, chọn kernel Python rồi **Restart Kernel and Run All**.
- Chạy được từ gốc repository hoặc thư mục Lab3. Chạy thuật toán không cần mạng.
- Nếu cần môi trường Jupyter:

  ```powershell
  python -m pip install jupyter ipykernel
  ```

- `RSA_INTERACTIVE = False` mặc định. Đổi thành `True` và chạy riêng cell nhập liệu để thử thông điệp số hoặc chuỗi. Bỏ trống p, q, e để sinh khóa 2048 bit; có thể bỏ trống riêng từng tham số. Dùng tiền tố `0x` khi nhập số Hex.
- Có thể gọi `generate_key(bits=2048)` với kích thước khác. Số nguyên Python có độ dài tùy ý nên không có khóa “lớn nhất”; kích thước được lựa chọn theo tài nguyên. Sinh khóa và thời gian chạy thay đổi giữa các lần thực thi.

## Quy ước dữ liệu và kết quả

- Khóa: `PU = (e, n)`, `PR = (d, n)`; `d` là nghịch đảo của e theo φ(n). Sinh nguyên tố bằng `secrets` và Miller–Rabin 64 vòng, là kiểm tra nguyên tố xác suất.
- Số nguyên đầu vào phải thuộc `[0, n)`. Khóa 1 cho `5 → 146 → 5` ở chiều bảo mật và `5 → 180 → 5` ở chiều xác thực theo đề.
- Chuỗi: UTF-8; đọc số nguyên và ghi byte theo **little-endian**. Khối rõ và khối mã của ba khóa có độ rộng `(1, 1)`, `(20, 21)`, `(31, 32)` byte. Gói dữ liệu giữ độ dài gốc để bảo toàn khối cuối và byte 0.
- Khóa 1 có n = 187, chỉ nhận byte < 187. Chuỗi đề là ASCII nên dùng được; văn bản tiếng Việt dùng khóa 2, 3 hoặc khóa sinh mới.
- Bốn bản mã của đề cho các kết quả:

  | Mẫu | Khóa | Bản rõ |
  |---|---|---|
  | 1 | 2 | `Ron Rivest, Adi Shamir and Leonard Adleman` |
  | 2 | 2 | `Meet-in-the-middle` |
  | 3 | 1 | `Vietnam National University - Ho Chi Minh City` |
  | 4 | 2 | `Man-in-the-middle` |

- Mẫu Hex số 2 có 20 byte, ngắn hơn khối mã 21 byte của khóa 2. Đọc little-endian tương đương bổ sung byte `00` ở cuối. Bộ dò ứng viên giả thiết văn bản ASCII in được; không phải phương pháp nhận diện khóa hay xác thực tổng quát.

## Kiểm chứng

Đã chạy toàn bộ notebook bằng kernel Jupyter mới trên Python **3.12.14**; lưu đầu ra trực tiếp trong notebook. **16 kiểm thử đạt**, gồm ba khóa đã biết, M = 5, toàn bộ 187 phần tử của khóa 1 ở cả hai chiều, bốn bản mã đề, UTF-8, byte 0, dữ liệu rỗng, ranh giới khối, đầu vào lỗi và sinh tham số còn thiếu. Thử sinh n đúng 2048 bit và khôi phục số, chuỗi thành công.

Chương trình dùng RSA thuần túy để học tập. Base64 là biểu diễn byte; phép biến đổi khóa riêng trong bài là mô hình toán học theo đề. Không dùng cấu hình này để thay thế RSA-OAEP hoặc chữ ký RSA-PSS trong ứng dụng thực tế.

## Tài liệu tham khảo

- Đề NT101 Lab03, Nhiệm vụ 2.1, trang PDF 3–7, tài liệu được cung cấp trong học phần.
- [RFC 8017](https://www.rfc-editor.org/rfc/rfc8017.html), mục 4, 5, 7 và 8.
- Python: [pow](https://docs.python.org/3/library/functions.html#pow), [secrets](https://docs.python.org/3/library/secrets.html).
