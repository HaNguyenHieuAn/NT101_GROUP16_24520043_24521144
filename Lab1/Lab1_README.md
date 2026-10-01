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
├── task2_1_caesar.ipynb        # Nhiệm vụ 2.1 — Caesar, chạy độc lập
├── task2_4_playfair.ipynb      # Nhiệm vụ 2.4 — Playfair, chạy độc lập
├── Lab1_Group16_Report.pdf     # File báo cáo hiện có, cần hoàn thiện riêng
└── Lab1_README.md              # Hướng dẫn bài Lab 1
```

## Danh sách nhiệm vụ

| Nhiệm vụ | Nội dung | Trạng thái |
|---|---|---|
| 2.1 | Caesar: mã hóa, giải mã, tự chọn khóa bằng brute-force | Có trong notebook |
| 2.2 | Phân tích tần suất thay thế đơn bảng | Chưa thực hiện |
| 2.3 | Tự động phá mã thay thế đơn bảng | Chưa thực hiện |
| 2.4 | Playfair: mã hóa, giải mã, hiển thị ma trận 5 × 5 | Có trong notebook |
| 2.5 | Vigenère: mã hóa và giải mã | Chưa thực hiện |
| 2.6 | Phá mã Vigenère | Chưa thực hiện |
| 2.7 | Thuật toán cổ điển khác | Chưa thực hiện |

**Lưu ý:** nhiệm vụ 2.4 là Playfair, khác mục 2.4 Vigenère trong đề.

## Yêu cầu môi trường & Cài đặt

- Python 3; notebook được kiểm thử trên Python 3.13.9.
- VS Code với extension Python/Jupyter, hoặc Jupyter Notebook/JupyterLab.
- Chọn kernel Python có `ipykernel`. Nếu chưa có môi trường notebook:

```powershell
python -m pip install jupyter ipykernel
```

Mã thuật toán chỉ dùng thư viện chuẩn Python. Ciphertext đề nằm trong notebook; không cần PDF hoặc mạng khi chạy.

## Hướng dẫn thực thi

1. Mở `task2_1_caesar.ipynb` hoặc `task2_4_playfair.ipynb`, chọn kernel Python 3.
2. Chọn **Run All** trong từng file để chạy hàm, giải mã ciphertext của bài đó và kiểm thử. Hai notebook chạy độc lập, không cần chạy file còn lại.
3. Để nhập dữ liệu Caesar, đổi `CAESAR_INTERACTIVE = True` trong notebook Caesar rồi chạy riêng cell nhập liệu.
4. Để nhập dữ liệu Playfair, đổi `PLAYFAIR_INTERACTIVE = True` trong notebook Playfair rồi chạy riêng cell nhập liệu.
5. Trả cờ nhập liệu về `False` trước khi Run All không tương tác.

Mỗi notebook gồm một nhiệm vụ với các cell lý thuyết, hàm xử lý, ví dụ, nhập liệu, kiểm thử và nhận xét. Tạo notebook riêng theo tên `task2_<số>_<thuật_toán>.ipynb` cho các bài khác.

### Quy ước và giới hạn

- Caesar giữ chữ hoa/thường, dấu câu và ký tự ngoài ASCII. Brute-force thử `0..25`, chọn một ứng viên theo điểm tiếng Anh; không bảo đảm đúng với mọi chuỗi ngắn hoặc ngôn ngữ khác.
- Playfair chỉ giữ chữ cái ASCII, chuyển chữ hoa, gộp `J/I`; đệm `X`, hoặc `Q` khi chữ đang xử lý là `X`.
- Giải mã Playfair giữ ký tự đệm; không khôi phục khoảng trắng, dấu câu hay phân biệt `I/J` ban đầu.
- Ciphertext Playfair có số chữ lẻ hoặc cặp trùng bị từ chối theo quy ước notebook.
- Caesar/Playfair không an toàn để bảo vệ dữ liệu thực tế.

## Báo cáo chi tiết

Notebook chứa phương pháp, kết quả chạy và kiểm thử để phục vụ viết báo cáo. File PDF báo cáo hiện có chưa được hoàn thiện bởi tác vụ này. Báo cáo cần trình bày phương pháp, phân tích và hình minh chứng; chỉ nộp mã nguồn không đủ yêu cầu đề.

Không đưa PDF đề vào kho mã nguồn. Tuân thủ yêu cầu giảng viên về phạm vi chia sẻ tài liệu và bài làm.
