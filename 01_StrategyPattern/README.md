# Strategy Pattern
利用 [Strategy Pattern - Design Patterns](https://www.youtube.com/watch?v=v9ejT8FO-7I&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc) 學習設計模式 **Strategy Pattern**，並利用 Python 撰寫 sample code.

## Strategy Pattern Definition
相對於**繼承(inherit)**， Strategy Pattern 則是**組合優於繼承(composition over inheritance)** 的精神。

假設有一個薪水計算器要給兩個不同的客戶使用 : 速食業客戶以每小時時薪和工時來核算薪水，外送業客戶以每單獎金和總外送單數來核算薪水。

薪水計算器需要提供給不同業者不同核算薪水的方法， Strategy Pattern 則提供了一種方式，使得不同業者可以使用同一個計算器，並選擇不同的核算方式，來獲取薪水計算的結果。

用 Python 撰寫 Strategy Pattern 的示例。
![](https://blog.zhengweiliu.com/images/design-pattern/strategy-pattern/03_demo.png)

詳細文章發表在[我的blog](https://blog.zhengweiliu.com/posts/design-pattern/strategy-pattern/)