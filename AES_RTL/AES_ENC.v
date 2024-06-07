`timescale 1ns / 1ps


//AES加密
module AES_ENC(Din, Key, Dout, Drdy, Krdy, RSTn, EN, CLK, BSY, Dvld);
input  [127:0] Din;  // Data input，128位明文
input  [127:0] Key;  // Key input，128位密钥
output [127:0] Dout; // Data output，128位密文

input  Drdy;         // Data input ready
input  Krdy;         // Key input ready
input  RSTn;         // Reset (Low active)
input  EN;           // AES circuit enable
input  CLK;          // System clock
output BSY;          // Busy signal
output Dvld;         // Data output valid

reg  [127:0] Drg;    // Data register，当前状态矩阵
reg  [127:0] Krg;    // Key register
reg  [127:0] KrgX;   // Temporary key Register，当前轮密钥
reg  [9:0]   Rrg;    // Round counter，当前加密轮数，10位表示10轮加密
reg  Dvldrg, BSYrg;
wire [127:0] Dnext, Knext;//下一轮状态矩阵，下一轮轮密钥

EncCore EC (Drg, KrgX, Rrg, Dnext, Knext);//参数依次当前状态矩阵、当前轮密钥、当前加密轮数、下一轮状态矩阵、下一轮轮密钥

assign Dvld = Dvldrg;
assign Dout = Drg;
assign BSY  = BSYrg;

always @(posedge CLK) begin//CLK上升沿触发
  if (RSTn == 0) begin//初始化
    Rrg    <= 10'b0000000001;//轮数为1
    Dvldrg <= 0;//无最终输出
    BSYrg  <= 0;//标志轮加密是否开始
  end//if (RSTn == 0)
  
  else if (EN == 1) begin
  
     //还未开始10轮加密的准备
     if (BSYrg == 0) begin
      //key input ready=1
      if (Krdy == 1) begin
        Krg    <= Key;//key register=初始密钥
        KrgX   <= Key;//初始轮密钥
        Dvldrg <= 0;//无最终输出
      end//if (Krdy == 1)
      //data input valid
      else if (Drdy == 1) begin
        Rrg    <= {Rrg[8:0], Rrg[9]};//轮数+1
        KrgX   <= Knext;
        Drg    <= Din ^ Krg;//初始时进行轮密钥加
        Dvldrg <= 0;
        BSYrg  <= 1;//置1,类似于flag,标志10轮加密开始
      end//else if (Drdy == 1)
    end//if (BSYrg == 0)
    
    //开始10轮加密
    else begin
      Drg <= Dnext;//输出的状态矩阵作为下一轮的输入
      if (Rrg[0] == 1) begin//如果是第10轮
        KrgX   <= Krg;//轮密钥变为初始密钥
        Dvldrg <= 1;//有最终输出，Dvld = Dvldrg，data output valid
        BSYrg  <= 0;//加密结束flag重置为0
      end//if (Rrg[0] == 1)
      else begin//第1～9轮
        Rrg    <= {Rrg[8:0], Rrg[9]};//轮数+1
        KrgX   <= Knext;//输出轮密钥作为下一轮的输入
      end
    end
    
  end//else if (EN == 1)
  
end//always @(posedge CLK) begin
endmodule
