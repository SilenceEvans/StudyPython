i = 0
while i <= 5:
    i += 1
    print("*" * i)

# 实现同样功能在Java中代码如下
# public class LittleStar {
#     public static void main(String[] args) {
#         for (int i = 0; i <= 5; i++) {
#             for (int j = 0; j <= i; j++) {
#                 System.out.print("*"); 注意此处用的是print函数，使用print函数不换行
#             }
#             System.out.println();
#         }
#     }
# }

i = 0
while i < 5:
    n = 0
    while n <= i:
        print("*", end="")
        n += 1
    print()
    i += 1

# 以上两段代码其实完成了同样的功能
