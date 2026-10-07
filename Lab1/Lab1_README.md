# Lab 01: Mật mã học Cổ điển (Classical Cryptography)

> **Môn học:** An toàn mạng máy tính (NT101)  
> **Khoa:** Mạng máy tính và Truyền thông  
> **Trường:** Đại học Công nghệ Thông tin – ĐHQG-HCM (UIT)

---

## 📑 Mục lục
- [Giới thiệu & Mục tiêu](#-giới-thiệu--mục-tiêu)
- [Cấu trúc thư mục](#-cấu-trúc-thư-mục)
- [Danh sách nhiệm vụ](#-danh-sách-nhiệm-vụ)
- [Yêu cầu môi trường & Cài đặt](#-yêu-cầu-môi-trường--cài-đặt)
- [Hướng dẫn thực thi](#-hướng-dẫn-thực-thi)
- [Báo cáo chi tiết](#-báo-cáo-chi-tiết)

---

## 🎯 Giới thiệu & Mục tiêu

Bài thực hành giúp làm quen với các khái niệm nền tảng trong mật mã hóa khóa đối xứng/cổ điển, cơ chế hoạt động của các thuật toán thay thế và hoán vị, cùng các phương pháp thám mã (cryptanalysis):
* Hiểu và cài đặt các hệ mật mã cổ điển: Caesar, Mono-alphabetic Substitution, Playfair, Vigenère.
* Ứng dụng kỹ thuật phân tích tần suất (Frequency Analysis) và các độ đo thống kê (Index of Coincidence, Kasiski Examination, n-gram).
* Xây dựng các thuật toán tìm kiếm tối ưu (Hill Climbing / Simulated Annealing) để tự động phá mã khi chỉ biết ciphertext (Ciphertext-only attack).

---

## 📂 Cấu trúc thư mục

```text
Lab1/
├── Lab1_README.md
├── task2_1_caesar.ipynb        # Caesar
├── task2_3_auto_mono.ipynb     # Tự động giải mã thay thế đơn bảng
├── task2_4_playfair.ipynb      # Playfair
├── task2_5_vigenere.ipynb      # Vigenère
├── Lab1_Task2.2.ipynb         # Phân tích tần suất thay thế đơn bảng
├── Lab1_Task2.6.ipynb         # Thám mã Vigenère
├── Lab1_Task2.7.ipynb         # Affine
├── cipher2.2.txt             # Ciphertext cho Task 2.2
└── task2_3_data/              # Dữ liệu cần để Task 2.3 chạy offline
    ├── cipher2_2.txt
    ├── english_quadgrams.txt
    ├── english_words.txt
    └── sources.json
```

## Danh sách nhiệm vụ

| Nhiệm vụ | Nội dung | Trạng thái |
|---|---|---|
| 2.1 | Caesar: mã hóa, giải mã, tự chọn khóa bằng brute-force | Có trong notebook |
| 2.2 | Phân tích tần suất thay thế đơn bảng | Có trong `Lab1_Task2.2.ipynb` |
| 2.3 | Tự động phá mã thay thế đơn bảng | Có trong `task2_3_auto_mono.ipynb` |
| 2.4 | Playfair: mã hóa, giải mã, hiển thị ma trận 5 × 5 | Có trong notebook |
| 2.5 | Vigenère: mã hóa và giải mã | Có trong `task2_5_vigenere.ipynb` |
| 2.6 | Phá mã Vigenère | Có trong `Lab1_Task2.6.ipynb` |
| 2.7 | Affine | Có trong `Lab1_Task2.7.ipynb` |

**Lưu ý:** nhiệm vụ 2.4 là Playfair, khác mục 2.4 Vigenère trong đề.

## Yêu cầu môi trường & Cài đặt

- Python 3; notebook được kiểm thử trên Python 3.13.9.
- VS Code với extension Python/Jupyter, hoặc Jupyter Notebook/JupyterLab.
- Chọn kernel Python có `ipykernel`. Nếu chưa có môi trường notebook:

```powershell
python -m pip install jupyter ipykernel
```

Mã thuật toán chỉ dùng thư viện chuẩn Python. Caesar/Playfair chứa ciphertext đề trong notebook; Task 2.3 đọc dữ liệu từ `task2_3_data`. Không cần Word/PDF, script `.py` hoặc mạng khi chạy.

## Hướng dẫn thực thi

1. Mở notebook cần chạy, chọn kernel Python 3. Chạy từ thư mục Lab1 hoặc gốc repository để Task 2.3 tìm đúng dữ liệu.
2. Các notebook độc lập; không cần chạy task khác trước. Chọn **Run All** để chạy hàm, ví dụ và kiểm thử có trong từng notebook.
3. Các cờ nhập liệu: `CAESAR_INTERACTIVE`, `MONO_INTERACTIVE`, `PLAYFAIR_INTERACTIVE`, `VIGENERE_INTERACTIVE`. Đặt `True` và chạy riêng cell nhập liệu để nhập input.
4. Đặt các cờ về `False` trước khi Run All không tương tác. Một số notebook đang lưu cờ `True`, nên Run All có thể chờ input.
5. Task 2.2: chạy từ thư mục `Lab1`, giữ `cipher2.2.txt` bên cạnh notebook.
6. Task 2.6: nhập ciphertext khi được hỏi. Task 2.7: chọn `1` mã hóa, `2` giải mã, `3` chạy ví dụ; `0` thoát.

Mỗi notebook gồm một nhiệm vụ với các cell lý thuyết, hàm xử lý, ví dụ, nhập liệu, kiểm thử và nhận xét. Tạo notebook riêng theo tên `task2_<số>_<thuật_toán>.ipynb` cho các bài khác.

### Quy ước và giới hạn

- Caesar giữ chữ hoa/thường, dấu câu và ký tự ngoài ASCII. Brute-force thử `0..25`, chọn một ứng viên theo điểm tiếng Anh; không bảo đảm đúng với mọi chuỗi ngắn hoặc ngôn ngữ khác.
- Playfair chỉ giữ chữ cái ASCII, chuyển chữ hoa, gộp `J/I`; đệm `X`, hoặc `Q` khi chữ đang xử lý là `X`.
- Giải mã Playfair giữ ký tự đệm; không khôi phục khoảng trắng, dấu câu hay phân biệt `I/J` ban đầu.
- Ciphertext Playfair có số chữ lẻ hoặc cặp trùng bị từ chối theo quy ước notebook.
- Caesar/Playfair không an toàn để bảo vệ dữ liệu thực tế.

## Task 2.3 — Tự động giải mã thay thế đơn bảng

- Mở `task2_3_auto_mono.ipynb`, chọn Python 3, Run All. Notebook độc lập, mã dùng thư viện chuẩn; cần giữ thư mục `task2_3_data` đi kèm. Không cần mạng.
- `MONO_INTERACTIVE = False` mặc định. Đổi `True`, chạy riêng cell nhập liệu: `1` nhập ciphertext, `2` đọc file UTF-8. Ví dụ file: `task2_3_data/cipher2_2.txt` khi chạy từ Lab1.
- Có thể tăng `restarts`, `iterations`, đổi `seed` để tìm thêm; không bảo đảm đúng mọi văn bản, đặc biệt chuỗi ngắn hoặc không phải tiếng Anh.
- Phương pháp: điểm quadgram + tần suất từ, simulated annealing nhiều lần khởi động, hill-climbing. IC chỉ hiển thị, không dùng chọn khóa.
- Run All giải ciphertext đề và thử nghiệm văn bản dài/ngắn; kết quả hiển thị ngay trong notebook.
- Script tạo báo cáo/kiểm chứng, kết quả JSON sinh ra và Word/PDF đã chuyển ngoài repository; không cần chúng để chạy notebook.
- Ciphertext Task 2.2 và bản rõ tham chiếu trong Word không nhất quán ở 3 vị trí Q/X. Kết quả tự động khớp 4575/4578 chữ (99,9345%); không sửa tay bản rõ.
- Nguồn mô hình và SHA-256: `task2_3_data/sources.json`. Quadgram lấy từ 3 tác phẩm Gutenberg; mô hình từ lấy từ Peter Norvig, không dùng bản rõ đề để huấn luyện.

## Báo cáo chi tiết

Notebook chứa phương pháp, kết quả chạy và kiểm thử để phục vụ viết báo cáo. Repository không lưu Word/PDF hoặc ảnh báo cáo. Báo cáo nộp riêng theo yêu cầu giảng viên; chỉ nộp mã nguồn không thay thế phần báo cáo.

Không đưa PDF đề vào kho mã nguồn. Tuân thủ yêu cầu giảng viên về phạm vi chia sẻ tài liệu và bài làm.
