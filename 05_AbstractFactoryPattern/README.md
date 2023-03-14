# Abstract Factory Pattern
利用 [Abstract Factory Pattern - Design Patterns](https://www.youtube.com/watch?v=v-GiuMmsXj4&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=5) 學習設計模式 **Abstract Factory Pattern**，並利用 Python 撰寫 sample code.

簡而言之， Factory Method Pattern 描述的是定義製作者(Creator)和產品(Product)間的關係 ， Abstract Factory Pattern 則是一種將多個製作者(Creator) 群組化的關係；

**Abstract Factory Pattern** 是基於 **Factory Method Pattern** 建構而成的一種設計模式，因此需要先理解 Factory Method Pattern 的核心精神與設計方式
[Factory Method Pattern](https://github.com/zhweiliu/design-pattern-study/tree/master/04_FactoryMethodPattern)

在[影片](https://www.youtube.com/watch?v=v-GiuMmsXj4&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=5)中提供的案例是應用程式的 UI 設計 :

當一組應用程式的 UI 控制項固定後，每個控制項功能背後要達成的目的是固定的，但依據作業系統的不同，如: Windows、Mac OS 、 Linux，控制項功能需要有不同的實作方式，如: 呼叫不同的 driver 或 kernel APIs，以達成目的，而 Factory Method Pattern 恰好適合解決這個問題；

因此，透過宣告 Abstract Factory Pattern，將每個控制項功能當作一種產品(Product)，透過不同的製作者(Creator)來產生控制項，並將適用於同一種作業系統的製作者(Creator)整合成一個群組，當 **需要渲染出符合當前作業系統的UI 時，只要採納對應的群組生成控制項功能就能達成目的**，這也表達了 Abstract Factory Pattern 的設計理念

![](https://blog.zhengweiliu.com/images/design-pattern/abstract-factory-pattern/01-definition.png)


在本文的示例中所採用的編成架構，將各項具體單品(產品)、具體生產者，以及套餐組合進行分層，並且讓每一層只專注自己的變動，如 :
- 產品層只需要關注單品的參數，如名稱、售價，且單品參數的改變並不影響生產者層和套餐組合層的處理方式，以此為產品層異動保留了極大的彈性

- 生產者層同樣只考慮該如何生產出具體的產品，圍繞著建構子傳遞的肉類或尺寸的既有資訊進行拓展，而不是去改變肉類或尺寸的資訊

- 套餐組合層也僅考慮選用哪些具體生產者，來定義套餐組合的內容

未來無論是要增加新的套餐組合或是新的產品，不會(或非常小)對於現有的程式碼與軟體架構造成改動。 

我覺得這是一個，很好的闡述了鬆散耦合軟體框架的範例 。

詳細文章發表在[我的blog](https://blog.zhengweiliu.com/posts/design-pattern/abstract-factory-pattern/)