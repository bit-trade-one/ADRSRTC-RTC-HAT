# ADRSRTC-リアルタイムクロック拡張ボード

ラズベリーパイ（以下ラズパイ）にリアルタイムクロック（RTC)機能を追加するための拡張ボード。  
ADRSRTCのリポジトリです。

### *製品ページは[こちら](https://bit-trade-one.co.jp/adrsrtc/)*

## ファイルリスト
- Readme.md                       ［本文書］
- FAQ.md                           [FAQ］
- Switch-LED-Buzz2021-07-28.py     [サンプルプログラム］

## 前提条件
本動作確認は「RaspberryPI OS 32bit Bullseye 2022-04-04 Release」をイントールした後、2022年5月時点で最新版にupgradeした状態で実行しております。  
I2C・SPIインタフェースは、あらかじめraspi-configで許可した状態です。  

## RTC機能初期設定  

・RTC機能インストール  

1. /boot/config.txtに追記  

```
  dtparam=i2c_arm=on
  dtoverlay=i2c-rtc,ds3231
```

2. NTPを停止  

以下のコマンドを実行して下さい  
```
$  sudo systemctl stop systemd-timesyncd
$  sudo systemctl disable systemd-timesyncd
```

3. fake-hwlockを削除  

以下のコマンドを実行して下さい  
```
$  sudo apt-get -y remove fake-hwclock
$  sudo update-rc.d -f fake-hwclock remove
$  sudo systemctl disable fake-hwclock
```

4. 現在時刻をRTCに書き込みして再起動  

以下のコマンドを実行して下さい  
```
$  sudo hwclock -w
$  sudo reboot
```

5. 起動時RTCを読み込む設定  

・/etc/default/hwclock  
ファイル内の以下の行の先頭の'#'を削除してコメントアウトを解除してください。
記述がない場合は、追記してください。
```
#HCTOSYS_DEVICE=rtc0
```

・/lib/udev/hwclock-set  
ファイル内の以下の行すべての先頭に'#'を記入してコメントアウトしてください。
```
if [ -e /run/systemd/system ] ; then
    exit 0
fi
```

## OLED機能初期設定  

1. ライブラリのインストール  
```
$  git clone https://github.com/adafruit/Adafruit_CircuitPython_SSD1306
$  cd Adafruit_CircuitPython_SSD1306/
$  sudo python3 setup.py install
```

2. サンプルプログラムでOLED表示を確認  
```
$  cd examples
$  python3 ssd1306_stats.py
#  終了はCtrl-Cを押下
```
## スイッチ・LED・ブザーサンプルプログラム(Switch-LED-Buzz2021-07-28.py)

スイッチを押すと同じ並びのLEDが点灯します。  
4つ全部押すとブザーが鳴動します。  
```
$  sudo apt install pigpio
$  sudo pigpiod
$  python3 Switch-LED-Buzz2021-07-28.py
#  終了はCtrl-Cを押下
```
<!--
# -ADXXXXX-Template

## ここに見出し

![タイトル画像のURLを右のカッコに]()

「●●●●●」はほにゃららするためのなんちゃらボード。  
この製品を使用する事でもにょもにょがぺけぺけできる。  

<!--
改行する場合、文末に半角スペース2個を置く

リンクの貼り方
[リンクになる文章](URL)
exp.
[Google](https://www.google.co.jp/)

画像の貼り方
![画像が読めない時に表示されるテキスト](画像のURL)
exp.
![bit-trade-one](https://bit-trade-one.co.jp/wp/wp-content/uploads/tcd-w/logo.png)
※先頭の"!"を忘れないこと


見出しの付け方

# 見出し1

## 見出し1-1

###　見出し1-2

# 見出し2

"#"を増やすと下位の見出しになる


-- >


<!--
以下のURL内の"-ADXXXXX-Template"をリポジトリ名/ファイル名に変更 

製品によって無い情報(ライブラリへのリンクなど)は削除すること

ソフトの使い方、ライブラリの使い方などがWordなどである場合は、
各情報フォルダにMarkdown形式に起こし"Readme.md"という名前で保存すること
-- >

# [製品の詳細はこちら](http://bit-trade-one.co.jp/) 

## [マニュアルはこちら](https://github.com/bit-trade-one/-ADXXXXX-Template/raw/master/Manual)

## [アプリケーションソフトはこちら](https://github.com/bit-trade-one/-ADXXXXX-Template/raw/master/App/)  

## [ファームウェアはこちら](https://github.com/bit-trade-one/-ADXXXXX-Template/raw/master/Firmware/)

## [Q&A](https://github.com/bit-trade-one/-ADXXXXX-Template/blob/master/FAQ.md)

### [ライブラリはこちら](https://github.com/bit-trade-one/-ADXXXXX-Template/raw/master/Library)  

### [サンプルコードはこちら](https://github.com/bit-trade-one/-ADXXXXX-Template/raw/master/Sample)  

### [アプリケーションソースはこちら](https://github.com/bit-trade-one/-ADXXXXX-Template/raw/master/App_source/)  

### [ファームウェアソースはこちら](https://github.com/bit-trade-one/-ADXXXXX-Template/raw/master/Firmware_source/)

### [基板図](https://github.com/bit-trade-one/-ADXXXXX-Template/blob/master/Dimensions/-ADXXXXX-Template-Dimensions.pdf)

### [回路図](https://github.com/bit-trade-one/-ADXXXXX-Templateo/blob/master/Schematics/-ADXXXXX-Template-Schematics.pdf)

### [部品表](https://github.com/bit-trade-one-ADXXXXX-Templateo/blob/master/Partslist/-ADXXXXX-Template-Partslist.md)


## 作例

[BTO公式]()  
[Twitter作例1]()  
[Twitter作例2]()  
[ブログ作例1]()  
[ブログ作例1]()  

## 雑誌掲載情報

[ラズパイマガジンXX年Y月号]()  
[Pc Watch]()

## 製品仕様
    【対応OS】Windows7以降
    【サイズ】W16×D20×H5mm
    【重量】約1g
    【入力点数】12(デジタル)
    【コネクタ】USBマイクロB
    【電源】5V (USBマイクロB)
    【使用温度】0 ～ 40℃（結露なきこと）
    【保証期間】 1年間
    【付属品】保証書 1部
    【生産国】Made in Japan
-->
