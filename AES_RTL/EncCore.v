`timescale 1ns / 1ps

//加密核
module EncCore(di, ki, Rrg, do, ko);//参数依次为128位明文、轮密钥、当前加密轮数、下一轮状态矩阵、下一轮轮密钥
input  [127:0] di;//当前状态矩阵
input  [127:0] ki;//当前轮密钥
input  [9:0]   Rrg;//当前加密轮数
output [127:0] do;//下一轮状态矩阵
output [127:0] ko;//下一轮轮密钥

wire   [127:0] sb, sr, mx;//中间值，依次保存状态矩阵字节代换、行移位、列混合后的结果
wire   [31:0]  so;//中间值，保存密钥扩展中函数T行移位与字节代换后的结果

//加密流程为：S和字节代换，行移位，列混合，轮密钥加
SubBytes SB3 (di[127:96], sb[127:96]);
SubBytes SB2 (di[ 95:64], sb[ 95:64]);
SubBytes SB1 (di[ 63:32], sb[ 63:32]);
SubBytes SB0 (di[ 31: 0], sb[ 31: 0]);//sb保存字节代换后的结果

assign sr = {sb[127:120], sb[ 87: 80], sb[ 47: 40], sb[  7:  0],
             sb[ 95: 88], sb[ 55: 48], sb[ 15:  8], sb[103: 96],
             sb[ 63: 56], sb[ 23: 16], sb[111:104], sb[ 71: 64],
             sb[ 31: 24], sb[119:112], sb[ 79: 72], sb[ 39: 32]};//sr保存行移位后的结果
             
MixColumns MX3 (sr[127:96], mx[127:96]);
MixColumns MX2 (sr[ 95:64], mx[ 95:64]);
MixColumns MX1 (sr[ 63:32], mx[ 63:32]);
MixColumns MX0 (sr[ 31: 0], mx[ 31: 0]);//mx保存列混合后的结果

assign do = ((Rrg[0] == 1)? sr: mx) ^ ki;//判断是否为第10轮，若是，则跳过列混合使用sr轮密钥加，否则使用mx轮密钥加
//以上过程完成一轮加密获得下一轮状态矩阵do

function [7:0] rcon;//生成密钥扩展中的T函数中的rcon[j]
input [9:0] x;//x对应当前加密轮数
  casex (x)
    10'bxxxxxxxxx1: rcon = 8'h01;
    10'bxxxxxxxx1x: rcon = 8'h02;
    10'bxxxxxxx1xx: rcon = 8'h04;
    10'bxxxxxx1xxx: rcon = 8'h08;
    10'bxxxxx1xxxx: rcon = 8'h10;
    10'bxxxx1xxxxx: rcon = 8'h20;
    10'bxxx1xxxxxx: rcon = 8'h40;
    10'bxx1xxxxxxx: rcon = 8'h80;
    10'bx1xxxxxxxx: rcon = 8'h1b;
    10'b1xxxxxxxxx: rcon = 8'h36;
  endcase
endfunction

SubBytes SBK ({ki[23:16], ki[15:8], ki[7:0], ki[31:24]}, so);//字循环后S盒字节代换，结果保存在so中

assign ko[127:96] = ki[127:96] ^ {so[31:24] ^ rcon(Rrg), so[23: 0]};//对于W[4i]的扩展
assign ko[ 95:64] = ki[ 95:64] ^ ko[127:96];//W[4i+1],W[4i+2],w[4i+3]
assign ko[ 63:32] = ki[ 63:32] ^ ko[ 95:64];
assign ko[ 31: 0] = ki[ 31: 0] ^ ko[ 63:32];
//以上过程生成下一轮加密的轮密钥
endmodule
