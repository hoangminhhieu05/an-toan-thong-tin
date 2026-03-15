# Tìm nghịch đảo trong GF(2^10)

Cài đặt thuật toán **Euclidean mở rộng** để tìm nghịch đảo nhân trong trường GF(2^10).

Đa thức tối giản sử dụng:
m(x) = x^10 + x^3 + 1

Test vector:
a = 523  
b = 1015  

Chương trình thực hiện:
- Chia đa thức trên GF(2)
- Áp dụng thuật toán Euclid mở rộng
- In các giá trị trung gian (q, r, t) ở từng bước
- Tính nghịch đảo của a và b

Kết quả:
523^-1 = 798  
1015^-1 = 709

Kiểm tra lại:
523 * 798 mod m(x) = 1  
1015 * 709 mod m(x) = 1