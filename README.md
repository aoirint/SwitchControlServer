# SwitchControlServer

一時的に[tokoroten-lab/joycon-python](https://github.com/tokoroten-lab/joycon-python)
を使ってJoyConとの通信を実装している。
この実装は新しくSwitchControlClientとして分離して、
このソフトウェアはWebSocketサーバにする予定。
JoyConとPCをペアリングして実験できる。

## Linux
udevに設定を追加する。

https://www.reddit.com/r/Stadia/comments/egcvpq/using_nintendo_switch_pro_controller_on_linux/fc5s7qm/

/etc/udev/rules.d/50-nintendo-switch.rules
```udev
# Switch Joy-con (L) (Bluetooth only)
KERNEL=="hidraw*", SUBSYSTEM=="hidraw", KERNELS=="0005:057E:2006.*", MODE="0666"

# Switch Joy-con (R) (Bluetooth only)
KERNEL=="hidraw*", SUBSYSTEM=="hidraw", KERNELS=="0005:057E:2007.*", MODE="0666"

# Switch Pro controller (USB and Bluetooth)
KERNEL=="hidraw*", SUBSYSTEM=="hidraw", ATTRS{idVendor}=="057e", ATTRS{idProduct}=="2009", MODE="0666"
KERNEL=="hidraw*", SUBSYSTEM=="hidraw", KERNELS=="0005:057E:2009.*", MODE="0666"

# Switch Joy-con charging grip (USB only)
KERNEL=="hidraw*", SUBSYSTEM=="hidraw", ATTRS{idVendor}=="057e", ATTRS{idProduct}=="200e", MODE="0666"
```

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```
