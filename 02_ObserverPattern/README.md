# Observer Pattern
利用 [Observer Pattern - Design Patterns](https://www.youtube.com/watch?v=_BpmfnqjgzQ&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=2) 學習設計模式 **Observer Pattern**，並利用 Python 撰寫 sample code.

## Observer Pattern Definition
當有 A 、 B 兩類實體，其中實體 B 類實體為了某些原因，需要得知 A 類的某些狀態是否有改變；
若在 Server-Client 的架構中，假設 Server 為 A 類、Client 為 B 類 ，最簡單的想法是讓 Client 定期去問 Server 狀態是否已經改變，這樣的方式稱為**輪詢(Polling)**
![](https://blog.zhengweiliu.com/images/design-pattern/observer-pattern/01_polling.png)

然而，輪詢有些顯而易見的缺點：
- 大多時候輪詢的答案都是狀態未改變，屬於**無效的輪詢**
- 若同時有多個 Client 實體對 Server 進行輪詢，**會降低 Server 的處理效能**

讓 Server 主動**推送(Push)**狀態變更的信號給 Client，可以有效的改善上述的缺點
![](https://blog.zhengweiliu.com/images/design-pattern/observer-pattern/02_push.png)

因此在 Observer Pattern 中，將會明確定義出兩種角色 :
- **IObservable** : 被觀察者，如上述的 Server (A類)
- **IObserver** : 觀察者，如上述的 Client (B類)

用 Python 撰寫 Observer Pattern 的示例。  
[Source code](https://github.com/zhweiliu/design-pattern-study/blob/master/02_ObserverPattern/Demo.py)
![](https://blog.zhengweiliu.com/images/design-pattern/observer-pattern/04_demo_pattern.png)

詳細文章發表在[我的blog](https://blog.zhengweiliu.com/posts/design-pattern/observer-pattern/)