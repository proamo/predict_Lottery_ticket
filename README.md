# 雙色球彩券號碼預測

項目較簡單，僅作為娛樂項目，但沒想到關注人比預期多，特此感謝大家關注，祝大家都能發大財！
因為專案本身涉及爬蟲，機器學習，後端服務技術，而且是面向開發者的，我默認大家有這方面技術背景且能解決一些常識問題，故沒有做太多細節說明，特此表示抱歉。
項目只是拋磚引玉，很多地方都不是絕對的，目的是為了有興趣的朋友可以自訂調試。

## Update
之前有issue反應，因為不同紅球模型預測會有重複號碼出現，所以將紅球序列整體作為一個序列模型看待，推翻之前紅球之間相互獨立設定，
因為序列模型預測要引入crf層，相關API必須在 tf.compat.v1.disable_eager_execution()下，故整個模型採用 1.x 建構和訓練模式，
在 2.x 的tensorflow中 tf.compat.v1.XXX 保留了 1.x 的介面方式。


## Getting Started
執行 python get_train_data.py 用於取得訓練數據，
如果出現解析錯誤，應該看看網頁 http://datachart.500.com/ssq/history/newinc/history.php 是否可以正常訪問

執行 python train_model.py 開始模型訓練，先訓練紅球模型，再訓練藍球模型，模型參數和超參數在 config.py 檔案中自行配置
具體訓練時間消耗與模型參數和超參數相關。

執行 python run_api.py 啟動一個微服務，取得每天預測號碼，取得預測訪問url為: http://127.0.0.1:5000/predict_api
服務部署在後台，可以直接在瀏覽器上每日取得預測結果。

### Installing

python3.6 環境，相關函式庫和版本在 requirements.txt 下

pip install -r requirement.txt

若安裝有問題，可手動依序安裝，具體安裝庫產生問題，需自行解決


## Running the tests

![avatar](img/001.png)

![avatar](img/002.png)

![avatar](img/003.png)
