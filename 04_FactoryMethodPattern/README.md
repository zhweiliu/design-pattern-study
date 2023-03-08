# Factory Method Pattern
利用 [Factory Method Pattern - Design Patterns](https://www.youtube.com/watch?v=EcFVTgRHJLM&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=4) 學習設計模式 **Factory Method Pattern**，並利用 Python 撰寫 sample code.

Factory Method Pattern 簡明扼要的說，就是定義 **製作者(Creator)** 和 **產品(Product)** 間的關係

- 定義製作者可生產的產品，需要產品的時候才讓製作者生產出產品
- 不同的製作者可以有不同的製作方式，但統一使用**生產 (produce)** 來明確要求進行產品產出的行為

依據上述兩點可以得知 :
- 為產品定義一個基礎類別，並將同類型的 **具體產品(Concrete Product)** 繼承該基礎類別
- 為製作者定義一個基礎類別，並將產出同類型產品的 **具體製作者(Concrete Creator)** 繼承該基礎類別
- 不同類型的具體產品，應有不同的基礎產品類別
- 產出不同類型產品的具體製作者，應有不同的基礎製作者類類別

![](https://blog.zhengweiliu.com/images/design-pattern/factory-method-pattern/01-definition.png)

當需要某一特定產品時，委託可生產該產品的製作者進行生產並交付；

```
我們並不需要在意具體是哪個製作者生產產品，
也不需要在意製作者用何種方式生產特定產品，
因為我們關注的部分為，是否可拿到特定產品。
```

*註:在 《Design Pattern》書中有給出明確的定義和說明。我覺得太過繞口，所以用自己的想法來表達*
