## Cài đặt thuật toán RC4 để sinh dòng khóa và mã hóa chuỗi "cybersecurity" bằng phép XOR.

## Input
- S = [0,1,2,3,4,5,6,7,8,9]  
- K = [2,4,1,7]  
- m = "cybersecurity" (ASCII)  
- N = 10  

## Thuật toán
- KSA: trộn mảng S theo khóa K  
- PRGA: sinh dòng khóa  
- XOR: C = m XOR key  

## Output
- S sau KSA:  
  [6, 1, 8, 5, 9, 0, 2, 3, 7, 4]
- Dòng khóa:  
  8 4 5 9 5 9 2 0 8 3 1 8 0
- Bản mã:  
  k}glwzgc}qh|y