# Decorator Pattern
利用 [Decorator Pattern - Design Patterns](https://www.youtube.com/watch?v=GCraGHx6gso&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=3) 學習設計模式 **Decorator Pattern**，並利用 Python 撰寫 sample code.

Decorator Pattern 透過修改已定義的行為，以擴展或變更其功能，而不需透過繼承和覆寫。 使用組合 (composition) 替代繼承 (inherit)，可動態地添加或移除行為，且不需要在繼承關係中堆疊子類別。 Decorator模式更具靈活性和可維護性，因此被廣泛地應用於軟體開發領域中。

Decorator Pattern 則透過包裹 (wrapper) 方式來達成組合目的。

![](https://blog.zhengweiliu.com/images/design-pattern/decorator-pattern/02_decorators.png)

若 decorator 修改執行 behavior 的參數，或是修改了 behavior 的執行結果，則會依據 decorator 的包覆順序做出對應的改變 : 
- 若有多個 decorator 對同一個 behavior 的傳入參數進行修改，則傳入參數的改變會從 outer decorator 影響 inner decorator ，最終影響 component 執性 behavior 時的傳入參數
- 若有多個 decorator 對同一個 behavior 的執行結果進行修改，則從 component 回傳的執行結果開始，由 inner decorator 的修改影響 outer decorator 的修改，直至最外層的 outer decorator 回覆執行結果。

依據先前的說明整理出幾點資訊
- 需要定義出 **元件 (component)** 和 **附加描述 (Decorator)**
- 執行 behavior 是由外層 decorate 到內層 component ， behavior 的 signature 需統一，可判斷**附加描述是元件的一種(is-a)**
- 附加描述可以疊加、 outer decorator 需要呼叫 inner decorator ，可判斷**附加描述應具備 inner decorator 或 component**

再依據上述三點描述，以廣告文案投放至不同渠道的議題為例，用 Decorator Pattern 方式設計類別之間的關係，如下圖所示

![](https://blog.zhengweiliu.com/images/design-pattern/decorator-pattern/03_design.png)

令 Decorator 繼承 Component 類，並在 Decorator 的建構方法傳入 component 實體 ( object | instance ) ， 使 decorator 具備包裹 (wrapper) 其他 decorator 和 component 的能力。

用 Python 撰寫 Decorator Pattern 的 4 種示例。  
[Source code](https://github.com/zhweiliu/design-pattern-study/blob/master/03_DecoratorPattern/Demo.py)

詳細文章發表在[我的blog](https://blog.zhengweiliu.com/posts/design-pattern/decorator-pattern/)