安装iverilog与gtkwave
sudo apt-get install iverilog
sudo apt-get install gtkwave

编译与仿真
将AES.v与AES_tb.v置于同一目录下，在该目录下打开终端，依此执行下述指令：

iverilog AES.v AES_tb.v //在当前路径下编译生成生成a.out文件
./a.out //在当前路径下生成wave.vcd文件
gtkwave wave.vcd //使用gtkwave打开仿真波形
