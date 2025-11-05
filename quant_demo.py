import pandas as pd

# 讀取歷史資料（假設有 Date, Close 欄位）
data = pd.read_csv("price.csv")

# 計算移動平均線
data["MA5"] = data["Close"].rolling(window=5).mean()
data["MA20"] = data["Close"].rolling(window=20).mean()

# 建立交易訊號（短期>長期 → 買進；短期<長期 → 賣出）
data["Signal"] = 0
data.loc[data["MA5"] > data["MA20"], "Signal"] = 1
data.loc[data["MA5"] < data["MA20"], "Signal"] = -1

# 計算每日報酬率
data["Return"] = data["Close"].pct_change()
data["Strategy"] = data["Signal"].shift(1) * data["Return"]

# 計算總報酬率
total_return = (1 + data["Strategy"].fillna(0)).prod() - 1
print(f"策略總報酬率：約 {total_return*100:.2f}%")

# 若想看結果，可取消註解以下兩行
# import matplotlib.pyplot as plt
# data["Close"].plot(title="Price Trend (5MA vs 20MA)", figsize=(8,4)); plt.show()
