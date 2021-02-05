import ccxt
import re
import imaplib
import email
import time, threading
import asyncio
from bs4 import BeautifulSoup
import bs4 as bs
import sys 
import os
from termcolor import *
import numpy
import colorama
import numpy as np
# import tulipy as ti
# from irc_class import *
import os
import random
import requests
from termcolor import colored
os.system('color')
from pynput import keyboard
from playsound import playsound
from operator import itemgetter
# import pymysql.cursors
import csv
from datetime import datetime
# import urllib.request
import json



StartGrid=0
BiDirectionalGrid=0
SellDirectinalGrid=0
BuyDirectinalGrid=0
BotType="SUPERTREND-LONG"	  # ##	"SHORT-WAVES-TREND" , "SUPERTREND-LONG" , "SUPERTREND-SHORT" , "LONG-WAVES-ALL", "SHORT-WAVES-ALL" , "LONG-MACD-ALL" , "SHORT-MACD-ALL"
MACDType=0	   # ######## MACD TYPE For the 15 Func Only 
PostionSizeAccordingtoIndicator=60
SecondPostionSizeAccordingtoIndicator=60
Version=4.1
GlobalProfit=2.5
LongerTimeFrame="NONE"
ShorterTimeFrame="NONE"
print("GlobalProfit",GlobalProfit)

if(BotType=="SUPERTREND-LONG" or BotType=="SUPERTREND-SHORT"  or BotType=="LONG-MACD-ALL"  or BotType=="SHORT-MACD-ALL"	 ):
	MACDType=1
	PostionSizeAccordingtoIndicator=60

if(BotType=="SUPERTREND-LONG"  or BotType=="LONG-MACD-ALL"	or BotType=="LONG-WAVES-ALL" or	  BotType=="LONG-WAVES-TREND" ):
	SellDirectinalGrid=0
	BuyDirectinalGrid=1
if(BotType=="SUPERTREND-SHORT"	or BotType=="SHORT-MACD-ALL"  or BotType=="SHORT-WAVES-ALL" or	 BotType=="SHORT-WAVES-TREND" ):
	SellDirectinalGrid=1
	BuyDirectinalGrid=0
	


if(BuyDirectinalGrid==1 and SellDirectinalGrid==0  and	BotType=="SUPERTREND-LONG"):				 # #   sobh bot 1
	ResultFile='drive01/SUPERTREND-LONG.csv'
if(SellDirectinalGrid==1 and BuyDirectinalGrid==0	and	 BotType=="SUPERTREND-SHORT"):			 # #   sobh bot 2
	ResultFile='drive01/SUPERTREND-SHORT.csv'

print('CCXT version:', ccxt.__version__)
print('MACDType:',MACDType)
print('BotType:',BotType)
print('PostionSizeAccordingtoIndicator:',PostionSizeAccordingtoIndicator)
# ##############################################################################################################################################################################
# ##############################################################################################################################################################################
# ##############################################################################################################################################################################
# #######################################################		 THIS IS SOBH BOT LIVE ACCOUNT		  ##########################################################################
# ##############################################################################################################################################################################
# ##############################################################################################################################################################################
# ##############################################################################################################################################################################

if(BuyDirectinalGrid==1 and SellDirectinalGrid==0  and	BotType=="SUPERTREND-LONG"):
	binance = ccxt.binance({
		# 'apiKey': '',	## MSOBH
		# 'secret': '',	## MSOBH
		'apiKey': '',	## SOBH.BOT
		'secret': '',	## SOBH.BOT 
		'enableRateLimit': True,
		'options': {
			'defaultType': 'future',  # requires CCXT version > 1.20.31
			'adjustForTimeDifference': True,
			'recvWindow': 10000000
		},
	})
	
if(SellDirectinalGrid==1 and BuyDirectinalGrid==0  and	BotType=="SUPERTREND-SHORT"):
	binance = ccxt.binance({
		'apiKey': '',	## SOBH.BOT
		'secret': '',	## SOBH.BOT 
		'enableRateLimit': True,
		'options': {
			'defaultType': 'future',  # requires CCXT version > 1.20.31
			'adjustForTimeDifference': True,
			'recvWindow': 10000000
		},
	})	





symbol = 'BTC/USDT'	 #bitmex symbol
Subject='NONE'
SubjectManual='NONE'
OrderActionTakenGlobal='NONE'
AmountGlobal=0
SubjectGlobal='NONE'
profitLock=0
profitLockKey=0
i=0
RealProfitWithUnRealizedProfit=0
VolumePriceTICKSUSDT=0
priceList=[]
totalUnrealizedProfitBalanceList=[]
currentPrice=0
previousPrice=0
CurrentProffit=0
previousProfit=0
profitlockArray=[]
ClosesArrayFor14=[]
LowArrayFor14=[]
HighArrayFor14=[]
currentProfitLockArray=0
previousProfitLockArray=0
currentPosition='NONE'
TheDynaimicProfitPercent=0
previousDynaimicProfitPercent=0
totalWalletBalance=0
totalUnrealizedProfitBalance=0
totalUnrealizedProfitBalanceInPercent=0
LastPriceTICKS=0
currentPriceOneMin=0
previousPriceOneMin=0
CurrentProffitOneMin=0
previousProfitOneMin=0
priceListOneMin=[]
totalUnrealizedProfitBalanceOneMinListOneMin=[]
totalWalletBalanceOneMin=0
SL=4
ProfitPercentDynamic=0
GridArray=[]
LocakPrecentToBeUsedAfterProfitPercentDynamic=2
LocakPrecentToBeUsedAfterGridArray=[]
SELLNOW='NONE'
PrecentProfitLock=0
OpenedPostition=99
PositionPrice=0
CurrentPositionProfit=0
CurrentPositionProfitArray=[]
PreviousPositionProfit=0
PreviousPositionProfitArray=[]
StopLossPricePercent=0
StopLossPriceFull=0
ClosesFor200P1HArray=[]
ClosesFor50P1HArray=[]
Margin=125
TradeBotUsedMargin=125
MI=0
CI=0
AArray=[]
ManualEntryPrice=0
ManualSize=0
ManualPositionDirection='NONE'
totalPositionInitialMargin=0
walletBalance=0
maxWithdrawAmount=0
totalUnrealizedProfit=0
RunForOneTimeOnly=0
Tradedamount=0
TottalIntiatedMarginManual=0
TottalIntiatedMarginAuto=0
CurrentPositionProfitPercent=0
inPostion=0
StartTrading=1
ATRValueOpenPostionTime=0
previousProfitLock=0
FirstpreviousProfitLock=0
KeyPressedToBuy=0
KeyPressedToSell=0
NextProfitPrice=0
IncreasedNumber=0
ProfitCount=0
SLUsingATR=0
ProfitUsingATR=0
AutoATRVALUEToProfitLock=0
A=0
UseATRForTrading=13
UsingEmailedStaticPercent=0
PositionPriceIndollars=0
FeesMarket=0
TheFirstpreviousProfit=0
SafeFirstpreviousProfitLock=0
LastProfitGain=0
ProfitLevel=0
NewManualTrade=1
LocakedNewManualTrade=0
manualBalance15M=10000
inSHORT15M=0
inLong15M=0
OrderActionTakenGlobal15M='NONE'
AmountGlobal15M=0
profitLockKey15M=0
CurrentPositionProfit15M=0
FeesMarket15M=0
PositionPrice15M=0
Ordertype15M='NONE'
OrderActionWas15M='NONE'
ExitSL15M=0
ExitPR15M=0
MI15M=0
CI15M=0
A15M=0
ProfitPercentDynamic15M=0
currentPosition15M=0
GridArray15M=[]
CurrentPositionProfitPercent15M=0
TottalIntiatedMarginAuto15M=0
StopLossPricePercent15M=0
StopLossPriceFull15M=0	   
SELLNOW15M='NONE'
SN15M=1 
SL15M=0
PR15M=0
id=0
Buy_start=0
Buy_end=0
target1=0
stop_loss=0
exchange1="NONE"
currency="NONE"
coin="NONE"
countto10=0	
StopGettingSignals="NONE"
grid=[]
x=0
ii=0
grid0BuyPrice=0
grid0SellPrice=0	
grid1BuyPrice=0
grid1SellPrice=0
grid2BuyPrice=0
grid2SellPrice=0
grid3BuyPrice=0
grid3SellPrice=0
grid4BuyPrice=0
grid4SellPrice=0
grid5BuyPrice=0
grid5SellPrice=0
grid6BuyPrice=0
grid6SellPrice=0
grid7BuyPrice=0
grid7SellPrice=0
grid8BuyPrice=0
grid8SellPrice=0
grid9BuyPrice=0
grid9SellPrice=0
grid10BuyPrice=0
grid10SellPrice=0
grid11BuyPrice=0
grid11SellPrice=0
grid12BuyPrice=0
grid12SellPrice=0
grid13BuyPrice=0
grid13SellPrice=0
grid14BuyPrice=0
grid14SellPrice=0
grid15BuyPrice=0
grid15SellPrice=0
grid16BuyPrice=0
grid16SellPrice=0
grid17BuyPrice=0
grid17SellPrice=0
grid18BuyPrice=0
grid18SellPrice=0
grid19BuyPrice=0
grid19SellPrice=0
grid20BuyPrice=0
grid20SellPrice=0
grid21BuyPrice=0
grid21SellPrice=0
grid22BuyPrice=0
grid22SellPrice=0
grid23BuyPrice=0
grid23SellPrice=0
grid24BuyPrice=0
grid24SellPrice=0
grid25BuyPrice=0
grid25SellPrice=0
grid26BuyPrice=0
grid26SellPrice=0
grid27BuyPrice=0
grid27SellPrice=0
grid28BuyPrice=0
grid28SellPrice=0
grid29BuyPrice=0
grid29SellPrice=0
grid30BuyPrice=0
grid30SellPrice=0
grid0BuyPostion=0
grid0SellPostion=0	
grid1BuyPostion=0
grid1SellPostion=0
grid2BuyPostion=0
grid2SellPostion=0
grid3BuyPostion=0
grid3SellPostion=0
grid4BuyPostion=0
grid4SellPostion=0
grid5BuyPostion=0
grid5SellPostion=0
grid6BuyPostion=0
grid6SellPostion=0
grid7BuyPostion=0
grid7SellPostion=0
grid8BuyPostion=0
grid8SellPostion=0
grid9BuyPostion=0
grid9SellPostion=0
grid10BuyPostion=0
grid10SellPostion=0
grid11BuyPostion=0
grid11SellPostion=0
grid12BuyPostion=0
grid12SellPostion=0
grid13BuyPostion=0
grid13SellPostion=0
grid14BuyPostion=0
grid14SellPostion=0
grid15BuyPostion=0
grid15SellPostion=0
grid16BuyPostion=0
grid16SellPostion=0
grid17BuyPostion=0
grid17SellPostion=0
grid18BuyPostion=0
grid18SellPostion=0
grid19BuyPostion=0
grid19SellPostion=0
grid20BuyPostion=0
grid20SellPostion=0
grid21BuyPostion=0
grid21SellPostion=0
grid22BuyPostion=0
grid22SellPostion=0
grid23BuyPostion=0
grid23SellPostion=0
grid24BuyPostion=0
grid24SellPostion=0
grid25BuyPostion=0
grid25SellPostion=0
grid26BuyPostion=0
grid26SellPostion=0
grid27BuyPostion=0
grid27SellPostion=0
grid28BuyPostion=0
grid28SellPostion=0
grid29BuyPostion=0
grid29SellPostion=0
grid30BuyPostion=0
grid30SellPostion=0


GridBuy0PriceMovePercent =	0.1		# 0.25
GridBuy1PriceMovePercent =	0.3		# 0.5
GridBuy2PriceMovePercent =	0.5		# 0.75
GridBuy3PriceMovePercent =	0.7		# 1
GridBuy4PriceMovePercent =	0.9		# 1.25
GridBuy5PriceMovePercent =	1.1		# 1.5
GridBuy6PriceMovePercent =	1.3		# 1.75
GridBuy7PriceMovePercent =	1.5		# 2
GridBuy8PriceMovePercent =	1.7		# 2.25
GridBuy9PriceMovePercent =	1.9		# 2.5
GridBuy10PriceMovePercent=	2.1		# 2.75
GridBuy11PriceMovePercent=	2.3		# 3.25
GridBuy12PriceMovePercent=	2.5		# 3.75
GridBuy13PriceMovePercent=	2.7		# 4.25
GridBuy14PriceMovePercent=	2.9		# 4.75
GridBuy15PriceMovePercent=	3.1		# 5.25
GridBuy16PriceMovePercent=	3.3		# 5.75
GridBuy17PriceMovePercent=	3.5		# 6.25
GridBuy18PriceMovePercent=	3.7		# 6.75
GridBuy19PriceMovePercent=	3.9		# 7.25
GridBuy20PriceMovePercent=	4.1		# 7.5
GridBuy21PriceMovePercent=	4.3		# 8.25
GridBuy22PriceMovePercent=	4.5		# 9
GridBuy23PriceMovePercent=	4.7		# 9.75
GridBuy24PriceMovePercent=	4.9		# 10.5
GridBuy25PriceMovePercent=	5.1		# 11.25
GridBuy26PriceMovePercent=	5.3		# 12
GridBuy27PriceMovePercent=	5.5		# 12.75
GridBuy28PriceMovePercent=	5.7		# 13.5
GridBuy29PriceMovePercent=	5.9		# 14.25
GridBuy30PriceMovePercent=	6.1		# 15.25
AcualDollarMainAccountProfitSinceGridStart=0


GridBuy0Func = 0
GridBuy1Func = 0
GridBuy2Func = 0
GridBuy3Func = 0
GridBuy4Func = 0
GridBuy5Func = 0
GridBuy6Func = 0
GridBuy7Func = 0
GridBuy8Func = 0
GridBuy9Func = 0
GridBuy10Func= 0
GridBuy11Func= 0
GridBuy12Func= 0
GridBuy13Func= 0
GridBuy14Func= 0
GridBuy15Func= 0
GridBuy16Func= 0
GridBuy17Func= 0
GridBuy18Func= 0
GridBuy19Func= 0
GridBuy20Func= 0
GridBuy21Func= 0
GridBuy22Func= 0
GridBuy23Func= 0
GridBuy24Func= 0
GridBuy25Func= 0
GridBuy26Func= 0
GridBuy27Func= 0
GridBuy28Func= 0
GridBuy29Func= 0
GridBuy30Func= 0

GridSell0Func = 0
GridSell1Func = 0
GridSell2Func = 0
GridSell3Func = 0
GridSell4Func = 0
GridSell5Func = 0
GridSell6Func = 0
GridSell7Func = 0
GridSell8Func = 0
GridSell9Func = 0
GridSell10Func= 0
GridSell11Func= 0
GridSell12Func= 0
GridSell13Func= 0
GridSell14Func= 0
GridSell15Func= 0
GridSell16Func= 0
GridSell17Func= 0
GridSell18Func= 0
GridSell19Func= 0
GridSell20Func= 0
GridSell21Func= 0
GridSell22Func= 0
GridSell23Func= 0
GridSell24Func= 0
GridSell25Func= 0
GridSell26Func= 0
GridSell27Func= 0
GridSell28Func= 0
GridSell29Func= 0
GridSell30Func= 0


Buy0OrderID=0
Buy0OrderStatus="NONE"
Buy0OrderSide='NONE'
Buy0cost=0
Buy0OrderType='NONE'
Buy1OrderID=0
Buy1OrderStatus="NONE"
Buy1OrderSide='NONE'
Buy1cost=0
Buy1OrderType='NONE'
Buy2OrderID=0
Buy2OrderStatus="NONE"
Buy2OrderSide='NONE'
Buy2cost=0
Buy2OrderType='NONE'
Buy3OrderID=0
Buy3OrderStatus="NONE"
Buy3OrderSide='NONE'
Buy3cost=0
Buy3OrderType='NONE'
Buy4OrderID=0
Buy4OrderStatus="NONE"
Buy4OrderSide='NONE'
Buy4cost=0
Buy4OrderType='NONE'
Buy5OrderID=0
Buy5OrderStatus="NONE"
Buy5OrderSide='NONE'
Buy5cost=0
Buy5OrderType='NONE'
Buy6OrderID=0
Buy6OrderStatus="NONE"
Buy6OrderSide='NONE'
Buy6cost=0
Buy6OrderType='NONE'
Buy7OrderID=0
Buy7OrderStatus="NONE"
Buy7OrderSide='NONE'
Buy7cost=0
Buy7OrderType='NONE'
Buy8OrderID=0
Buy8OrderStatus="NONE"
Buy8OrderSide='NONE'
Buy8cost=0
Buy8OrderType='NONE'
Buy9OrderID=0
Buy9OrderStatus="NONE"
Buy9OrderSide='NONE'
Buy9cost=0
Buy9OrderType='NONE'
Buy10OrderID=0
Buy10OrderStatus="NONE"
Buy10OrderSide='NONE'
Buy10cost=0
Buy10OrderType='NONE'
Buy11OrderID=0
Buy11OrderStatus="NONE"
Buy11OrderSide='NONE'
Buy11cost=0
Buy11OrderType='NONE'
Buy12OrderID=0
Buy12OrderStatus="NONE"
Buy12OrderSide='NONE'
Buy12cost=0
Buy12OrderType='NONE'
Buy13OrderID=0
Buy13OrderStatus="NONE"
Buy13OrderSide='NONE'
Buy13cost=0
Buy13OrderType='NONE'
Buy14OrderID=0
Buy14OrderStatus="NONE"
Buy14OrderSide='NONE'
Buy14cost=0
Buy14OrderType='NONE'
Buy15OrderID=0
Buy15OrderStatus="NONE"
Buy15OrderSide='NONE'
Buy15cost=0
Buy15OrderType='NONE'
Buy16OrderID=0
Buy16OrderStatus="NONE"
Buy16OrderSide='NONE'
Buy16cost=0
Buy16OrderType='NONE'
Buy17OrderID=0
Buy17OrderStatus="NONE"
Buy17OrderSide='NONE'
Buy17cost=0
Buy17OrderType='NONE'
Buy18OrderID=0
Buy18OrderStatus="NONE"
Buy18OrderSide='NONE'
Buy18cost=0
Buy18OrderType='NONE'
Buy19OrderID=0
Buy19OrderStatus="NONE"
Buy19OrderSide='NONE'
Buy19cost=0
Buy19OrderType='NONE'
Buy20OrderID=0
Buy20OrderStatus="NONE"
Buy20OrderSide='NONE'
Buy20cost=0
Buy20OrderType='NONE'
Buy21OrderID=0
Buy21OrderStatus="NONE"
Buy21OrderSide='NONE'
Buy21cost=0
Buy21OrderType='NONE'
Buy22OrderID=0
Buy22OrderStatus="NONE"
Buy22OrderSide='NONE'
Buy22cost=0
Buy22OrderType='NONE'
Buy23OrderID=0
Buy23OrderStatus="NONE"
Buy23OrderSide='NONE'
Buy23cost=0
Buy23OrderType='NONE'
Buy24OrderID=0
Buy24OrderStatus="NONE"
Buy24OrderSide='NONE'
Buy24cost=0
Buy24OrderType='NONE'
Buy25OrderID=0
Buy25OrderStatus="NONE"
Buy25OrderSide='NONE'
Buy25cost=0
Buy25OrderType='NONE'
Buy26OrderID=0
Buy26OrderStatus="NONE"
Buy26OrderSide='NONE'
Buy26cost=0
Buy26OrderType='NONE'
Buy27OrderID=0
Buy27OrderStatus="NONE"
Buy27OrderSide='NONE'
Buy27cost=0
Buy27OrderType='NONE'
Buy28OrderID=0
Buy28OrderStatus="NONE"
Buy28OrderSide='NONE'
Buy28cost=0
Buy28OrderType='NONE'
Buy29OrderID=0
Buy29OrderStatus="NONE"
Buy29OrderSide='NONE'
Buy29cost=0
Buy29OrderType='NONE'
Buy0OrderID=0
Buy0OrderStatus="NONE"
Buy0OrderSide='NONE'
Buy0cost=0
Buy0OrderType='NONE'
Buy0OrderID=0
Buy0OrderStatus="NONE"
Buy0OrderSide='NONE'
Buy0cost=0
Buy0OrderType='NONE'
Buy0OrderID=0
Buy0OrderStatus="NONE"
Buy0OrderSide='NONE'
Buy0cost=0
Buy0OrderType='NONE'
Buy0OrderID=0
Buy0OrderStatus="NONE"
Buy0OrderSide='NONE'
Buy0cost=0
Buy0OrderType='NONE'
Buy0OrderID=0
Buy0OrderStatus="NONE"
Buy0OrderSide='NONE'
Buy0cost=0
Buy0OrderType='NONE'
GridCountToRestTheDynProfirForGrid=0
Sell0OrderID=0
Sell0OrderAmount=0
Sell0OrderSide='NONE'
Sell0cost=0
Sell0OrderType='NONE'
Sell1OrderID=0
Sell1OrderStatus="NONE"
Sell1OrderSide='NONE'
Sell1cost=0
Sell1OrderType='NONE'
Sell2OrderID=0
Sell2OrderStatus="NONE"
Sell2OrderSide='NONE'
Sell2cost=0
Sell2OrderType='NONE'
Sell3OrderID=0
Sell3OrderStatus="NONE"
Sell3OrderSide='NONE'
Sell3cost=0
Sell3OrderType='NONE'
Sell4OrderID=0
Sell4OrderStatus="NONE"
Sell4OrderSide='NONE'
Sell4cost=0
Sell4OrderType='NONE'
Sell5OrderID=0
Sell5OrderStatus="NONE"
Sell5OrderSide='NONE'
Sell5cost=0
Sell5OrderType='NONE'
Sell6OrderID=0
Sell6OrderStatus="NONE"
Sell6OrderSide='NONE'
Sell6cost=0
Sell6OrderType='NONE'
Sell7OrderID=0
Sell7OrderStatus="NONE"
Sell7OrderSide='NONE'
Sell7cost=0
Sell7OrderType='NONE'
Sell8OrderID=0
Sell8OrderStatus="NONE"
Sell8OrderSide='NONE'
Sell8cost=0
Sell8OrderType='NONE'
Sell9OrderID=0
Sell9OrderStatus="NONE"
Sell9OrderSide='NONE'
Sell9cost=0
Sell9OrderType='NONE'
Sell10OrderID=0
Sell10OrderStatus="NONE"
Sell10OrderSide='NONE'
Sell10cost=0
Sell10OrderType='NONE'
Sell11OrderID=0
Sell11OrderStatus="NONE"
Sell11OrderSide='NONE'
Sell11cost=0
Sell11OrderType='NONE'
Sell12OrderID=0
Sell12OrderStatus="NONE"
Sell12OrderSide='NONE'
Sell12cost=0
Sell12OrderType='NONE'
Sell13OrderID=0
Sell13OrderStatus="NONE"
Sell13OrderSide='NONE'
Sell13cost=0
Sell13OrderType='NONE'
Sell14OrderID=0
Sell14OrderStatus="NONE"
Sell14OrderSide='NONE'
Sell14cost=0
Sell14OrderType='NONE'
Sell15OrderID=0
Sell15OrderStatus="NONE"
Sell15OrderSide='NONE'
Sell15cost=0
Sell15OrderType='NONE'
Sell16OrderID=0
Sell16OrderStatus="NONE"
Sell16OrderSide='NONE'
Sell16cost=0
Sell16OrderType='NONE'
Sell17OrderID=0
Sell17OrderStatus="NONE"
Sell17OrderSide='NONE'
Sell17cost=0
Sell17OrderType='NONE'
Sell18OrderID=0
Sell18OrderStatus="NONE"
Sell18OrderSide='NONE'
Sell18cost=0
Sell18OrderType='NONE'
Sell19OrderID=0
Sell19OrderStatus="NONE"
Sell19OrderSide='NONE'
Sell19cost=0
Sell19OrderType='NONE'
Sell20OrderID=0
Sell20OrderStatus="NONE"
Sell20OrderSide='NONE'
Sell20cost=0
Sell20OrderType='NONE'
Sell21OrderID=0
Sell21OrderStatus="NONE"
Sell21OrderSide='NONE'
Sell21cost=0
Sell21OrderType='NONE'
Sell22OrderID=0
Sell22OrderStatus="NONE"
Sell22OrderSide='NONE'
Sell22cost=0
Sell22OrderType='NONE'
Sell23OrderID=0
Sell23OrderStatus="NONE"
Sell23OrderSide='NONE'
Sell23cost=0
Sell23OrderType='NONE'
Sell24OrderID=0
Sell24OrderStatus="NONE"
Sell24OrderSide='NONE'
Sell24cost=0
Sell24OrderType='NONE'
Sell25OrderID=0
Sell25OrderStatus="NONE"
Sell25OrderSide='NONE'
Sell25cost=0
Sell25OrderType='NONE'
Sell26OrderID=0
Sell26OrderStatus="NONE"
Sell26OrderSide='NONE'
Sell26cost=0
Sell26OrderType='NONE'
Sell27OrderID=0
Sell27OrderStatus="NONE"
Sell27OrderSide='NONE'
Sell27cost=0
Sell27OrderType='NONE'
Sell28OrderID=0
Sell28OrderStatus="NONE"
Sell28OrderSide='NONE'
Sell28cost=0
Sell28OrderType='NONE'
Sell29OrderID=0
Sell29OrderStatus="NONE"
Sell29OrderSide='NONE'
Sell29cost=0
Sell29OrderType='NONE'
Sell0OrderID=0
Sell0OrderStatus="NONE"
Sell0OrderSide='NONE'
Sell0cost=0
Sell0OrderType='NONE'
Sell0OrderID=0
Sell0OrderStatus="NONE"
Sell0OrderSide='NONE'
Sell0cost=0
Sell0OrderType='NONE'
Sell0OrderID=0
Sell0OrderStatus="NONE"
Sell0OrderSide='NONE'
Sell0cost=0
Sell0OrderType='NONE'
Sell0OrderID=0
Sell0OrderStatus="NONE"
Sell0OrderSide='NONE'
Sell0cost=0
Sell0OrderType='NONE'
Sell0OrderID=0
Sell0OrderStatus="NONE"
Sell0OrderSide='NONE'
Sell0cost=0
Sell0OrderType='NONE'
MovingGridUpBuy0=0




GridSell0PriceMovePercent=	0.1
GridSell1PriceMovePercent=	0.3
GridSell2PriceMovePercent=	0.5
GridSell3PriceMovePercent=	0.7
GridSell4PriceMovePercent=	0.9
GridSell5PriceMovePercent=	1.1
GridSell6PriceMovePercent=	1.3
GridSell7PriceMovePercent=	1.5
GridSell8PriceMovePercent=	1.7
GridSell9PriceMovePercent=	1.9
GridSell10PriceMovePercent= 2.1
GridSell11PriceMovePercent= 2.3
GridSell12PriceMovePercent= 2.5
GridSell13PriceMovePercent= 2.7
GridSell14PriceMovePercent= 2.9
GridSell15PriceMovePercent= 3.1
GridSell16PriceMovePercent= 3.3
GridSell17PriceMovePercent= 3.5
GridSell18PriceMovePercent= 3.7
GridSell19PriceMovePercent= 3.9
GridSell20PriceMovePercent= 4.1
GridSell21PriceMovePercent= 4.3
GridSell22PriceMovePercent= 4.5
GridSell23PriceMovePercent= 4.7
GridSell24PriceMovePercent= 4.9
GridSell25PriceMovePercent= 5.1
GridSell26PriceMovePercent= 5.3
GridSell27PriceMovePercent= 5.5
GridSell28PriceMovePercent= 5.7
GridSell29PriceMovePercent= 5.9
GridSell30PriceMovePercent= 6.1







FixSellMove=0
BTCBalanceFree=0
BTCBalanceLocked=0
ETHBalanceFree=0
ETHBalanceLocked=0
GridBuyProfit0Percent = GlobalProfit
GridBuyProfit1Percent = GlobalProfit
GridBuyProfit2Percent = GlobalProfit
GridBuyProfit3Percent = GlobalProfit
GridBuyProfit4Percent = GlobalProfit
GridBuyProfit5Percent = GlobalProfit
GridBuyProfit6Percent = GlobalProfit
GridBuyProfit7Percent = GlobalProfit
GridBuyProfit8Percent = GlobalProfit
GridBuyProfit9Percent = GlobalProfit
GridBuyProfit10Percent=GlobalProfit
GridBuyProfit11Percent=GlobalProfit
GridBuyProfit12Percent=GlobalProfit
GridBuyProfit13Percent=GlobalProfit
GridBuyProfit14Percent=GlobalProfit
GridBuyProfit15Percent=GlobalProfit
GridBuyProfit16Percent=GlobalProfit
GridBuyProfit17Percent=GlobalProfit
GridBuyProfit18Percent=GlobalProfit
GridBuyProfit19Percent=GlobalProfit
GridBuyProfit20Percent=GlobalProfit
GridBuyProfit21Percent=GlobalProfit
GridBuyProfit22Percent=GlobalProfit
GridBuyProfit23Percent=GlobalProfit
GridBuyProfit24Percent=GlobalProfit
GridBuyProfit25Percent=GlobalProfit
GridBuyProfit26Percent=GlobalProfit
GridBuyProfit27Percent=GlobalProfit
GridBuyProfit28Percent=GlobalProfit
GridBuyProfit29Percent=GlobalProfit
GridBuyProfit30Percent=GlobalProfit


GridBuyProfit0Price = 0
GridBuyProfit1Price = 0
GridBuyProfit2Price = 0
GridBuyProfit3Price = 0
GridBuyProfit4Price = 0
GridBuyProfit5Price = 0
GridBuyProfit6Price = 0
GridBuyProfit7Price = 0
GridBuyProfit8Price = 0
GridBuyProfit9Price = 0
GridBuyProfit10Price= 0
GridBuyProfit11Price= 0
GridBuyProfit12Price= 0
GridBuyProfit13Price= 0
GridBuyProfit14Price= 0
GridBuyProfit15Price= 0
GridBuyProfit16Price= 0
GridBuyProfit17Price= 0
GridBuyProfit18Price= 0
GridBuyProfit19Price= 0
GridBuyProfit20Price= 0
GridBuyProfit21Price= 0
GridBuyProfit22Price= 0
GridBuyProfit23Price= 0
GridBuyProfit24Price= 0
GridBuyProfit25Price= 0
GridBuyProfit26Price= 0
GridBuyProfit27Price= 0
GridBuyProfit28Price= 0
GridBuyProfit29Price= 0
GridBuyProfit30Price= 0

GridBuyProfit0PriceCount =	GlobalProfit
GridBuyProfit1PriceCount =	GlobalProfit
GridBuyProfit2PriceCount =	GlobalProfit
GridBuyProfit3PriceCount =	GlobalProfit
GridBuyProfit4PriceCount =	GlobalProfit
GridBuyProfit5PriceCount =	GlobalProfit
GridBuyProfit6PriceCount =	GlobalProfit
GridBuyProfit7PriceCount =	GlobalProfit
GridBuyProfit8PriceCount =	GlobalProfit
GridBuyProfit9PriceCount =	GlobalProfit
GridBuyProfit10PriceCount= GlobalProfit
GridBuyProfit11PriceCount= GlobalProfit
GridBuyProfit12PriceCount= GlobalProfit
GridBuyProfit13PriceCount= GlobalProfit
GridBuyProfit14PriceCount= GlobalProfit
GridBuyProfit15PriceCount= GlobalProfit
GridBuyProfit16PriceCount= GlobalProfit
GridBuyProfit17PriceCount= GlobalProfit
GridBuyProfit18PriceCount= GlobalProfit
GridBuyProfit19PriceCount= GlobalProfit
GridBuyProfit20PriceCount= GlobalProfit
GridBuyProfit21PriceCount= GlobalProfit
GridBuyProfit22PriceCount= GlobalProfit
GridBuyProfit23PriceCount= GlobalProfit
GridBuyProfit24PriceCount= GlobalProfit
GridBuyProfit25PriceCount= GlobalProfit
GridBuyProfit26PriceCount= GlobalProfit
GridBuyProfit27PriceCount= GlobalProfit
GridBuyProfit28PriceCount= GlobalProfit
GridBuyProfit29PriceCount= GlobalProfit
GridBuyProfit30PriceCount= GlobalProfit




PreviousGridBuyProfit0Price = 0
PreviousGridBuyProfit1Price = 0
PreviousGridBuyProfit2Price = 0
PreviousGridBuyProfit3Price = 0
PreviousGridBuyProfit4Price = 0
PreviousGridBuyProfit5Price = 0
PreviousGridBuyProfit6Price = 0
PreviousGridBuyProfit7Price = 0
PreviousGridBuyProfit8Price = 0
PreviousGridBuyProfit9Price = 0
PreviousGridBuyProfit10Price= 0
PreviousGridBuyProfit11Price= 0
PreviousGridBuyProfit12Price= 0
PreviousGridBuyProfit13Price= 0
PreviousGridBuyProfit14Price= 0
PreviousGridBuyProfit15Price= 0
PreviousGridBuyProfit16Price= 0
PreviousGridBuyProfit17Price= 0
PreviousGridBuyProfit18Price= 0
PreviousGridBuyProfit19Price= 0
PreviousGridBuyProfit20Price= 0
PreviousGridBuyProfit21Price= 0
PreviousGridBuyProfit22Price= 0
PreviousGridBuyProfit23Price= 0
PreviousGridBuyProfit24Price= 0
PreviousGridBuyProfit25Price= 0
PreviousGridBuyProfit26Price= 0
PreviousGridBuyProfit27Price= 0
PreviousGridBuyProfit28Price= 0
PreviousGridBuyProfit29Price= 0
PreviousGridBuyProfit30Price= 0



LOCKPreviousGridBuyProfit0Price = 0
LOCKPreviousGridBuyProfit1Price = 0
LOCKPreviousGridBuyProfit2Price = 0
LOCKPreviousGridBuyProfit3Price = 0
LOCKPreviousGridBuyProfit4Price = 0
LOCKPreviousGridBuyProfit5Price = 0
LOCKPreviousGridBuyProfit6Price = 0
LOCKPreviousGridBuyProfit7Price = 0
LOCKPreviousGridBuyProfit8Price = 0
LOCKPreviousGridBuyProfit9Price = 0
LOCKPreviousGridBuyProfit10Price= 0
LOCKPreviousGridBuyProfit11Price= 0
LOCKPreviousGridBuyProfit12Price= 0
LOCKPreviousGridBuyProfit13Price= 0
LOCKPreviousGridBuyProfit14Price= 0
LOCKPreviousGridBuyProfit15Price= 0
LOCKPreviousGridBuyProfit16Price= 0
LOCKPreviousGridBuyProfit17Price= 0
LOCKPreviousGridBuyProfit18Price= 0
LOCKPreviousGridBuyProfit19Price= 0
LOCKPreviousGridBuyProfit20Price= 0
LOCKPreviousGridBuyProfit21Price= 0
LOCKPreviousGridBuyProfit22Price= 0
LOCKPreviousGridBuyProfit23Price= 0
LOCKPreviousGridBuyProfit24Price= 0
LOCKPreviousGridBuyProfit25Price= 0
LOCKPreviousGridBuyProfit26Price= 0
LOCKPreviousGridBuyProfit27Price= 0
LOCKPreviousGridBuyProfit28Price= 0
LOCKPreviousGridBuyProfit29Price= 0
LOCKPreviousGridBuyProfit30Price= 0


GridSellProfit0Percent=	 GlobalProfit
GridSellProfit1Percent=	 GlobalProfit
GridSellProfit2Percent=	 GlobalProfit
GridSellProfit3Percent=	 GlobalProfit
GridSellProfit4Percent=	 GlobalProfit
GridSellProfit5Percent=	 GlobalProfit
GridSellProfit6Percent=	 GlobalProfit
GridSellProfit7Percent=	 GlobalProfit
GridSellProfit8Percent=	 GlobalProfit
GridSellProfit9Percent=	 GlobalProfit
GridSellProfit10Percent= GlobalProfit
GridSellProfit11Percent= GlobalProfit
GridSellProfit12Percent= GlobalProfit
GridSellProfit13Percent= GlobalProfit
GridSellProfit14Percent= GlobalProfit
GridSellProfit15Percent= GlobalProfit
GridSellProfit16Percent= GlobalProfit
GridSellProfit17Percent= GlobalProfit
GridSellProfit18Percent= GlobalProfit
GridSellProfit19Percent= GlobalProfit
GridSellProfit20Percent= GlobalProfit
GridSellProfit21Percent= GlobalProfit
GridSellProfit22Percent= GlobalProfit
GridSellProfit23Percent= GlobalProfit
GridSellProfit24Percent= GlobalProfit
GridSellProfit25Percent= GlobalProfit
GridSellProfit26Percent= GlobalProfit
GridSellProfit27Percent= GlobalProfit
GridSellProfit28Percent= GlobalProfit
GridSellProfit29Percent= GlobalProfit
GridSellProfit30Percent= GlobalProfit

GridSellProfit0Price = 0
GridSellProfit1Price = 0
GridSellProfit2Price = 0
GridSellProfit3Price = 0
GridSellProfit4Price = 0
GridSellProfit5Price = 0
GridSellProfit6Price = 0
GridSellProfit7Price = 0
GridSellProfit8Price = 0
GridSellProfit9Price = 0
GridSellProfit10Price= 0
GridSellProfit11Price= 0
GridSellProfit12Price= 0
GridSellProfit13Price= 0
GridSellProfit14Price= 0
GridSellProfit15Price= 0
GridSellProfit16Price= 0
GridSellProfit17Price= 0
GridSellProfit18Price= 0
GridSellProfit19Price= 0
GridSellProfit20Price= 0
GridSellProfit21Price= 0
GridSellProfit22Price= 0
GridSellProfit23Price= 0
GridSellProfit24Price= 0
GridSellProfit25Price= 0
GridSellProfit26Price= 0
GridSellProfit27Price= 0
GridSellProfit28Price= 0
GridSellProfit29Price= 0
GridSellProfit30Price= 0

GridSellProfit0PriceCount = GlobalProfit
GridSellProfit1PriceCount = GlobalProfit
GridSellProfit2PriceCount = GlobalProfit
GridSellProfit3PriceCount = GlobalProfit
GridSellProfit4PriceCount = GlobalProfit
GridSellProfit5PriceCount = GlobalProfit
GridSellProfit6PriceCount = GlobalProfit
GridSellProfit7PriceCount = GlobalProfit
GridSellProfit8PriceCount = GlobalProfit
GridSellProfit9PriceCount = GlobalProfit
GridSellProfit10PriceCount=GlobalProfit
GridSellProfit11PriceCount=GlobalProfit
GridSellProfit12PriceCount=GlobalProfit
GridSellProfit13PriceCount=GlobalProfit
GridSellProfit14PriceCount=GlobalProfit
GridSellProfit15PriceCount=GlobalProfit
GridSellProfit16PriceCount=GlobalProfit
GridSellProfit17PriceCount=GlobalProfit
GridSellProfit18PriceCount=GlobalProfit
GridSellProfit19PriceCount=GlobalProfit
GridSellProfit20PriceCount=GlobalProfit
GridSellProfit21PriceCount=GlobalProfit
GridSellProfit22PriceCount=GlobalProfit
GridSellProfit23PriceCount=GlobalProfit
GridSellProfit24PriceCount=GlobalProfit
GridSellProfit25PriceCount=GlobalProfit
GridSellProfit26PriceCount=GlobalProfit
GridSellProfit27PriceCount=GlobalProfit
GridSellProfit28PriceCount=GlobalProfit
GridSellProfit29PriceCount=GlobalProfit
GridSellProfit30PriceCount=GlobalProfit






PreviousGridSellProfit0Price = 0
PreviousGridSellProfit1Price = 0
PreviousGridSellProfit2Price = 0
PreviousGridSellProfit3Price = 0
PreviousGridSellProfit4Price = 0
PreviousGridSellProfit5Price = 0
PreviousGridSellProfit6Price = 0
PreviousGridSellProfit7Price = 0
PreviousGridSellProfit8Price = 0
PreviousGridSellProfit9Price = 0
PreviousGridSellProfit10Price= 0
PreviousGridSellProfit11Price= 0
PreviousGridSellProfit12Price= 0
PreviousGridSellProfit13Price= 0
PreviousGridSellProfit14Price= 0
PreviousGridSellProfit15Price= 0
PreviousGridSellProfit16Price= 0
PreviousGridSellProfit17Price= 0
PreviousGridSellProfit18Price= 0
PreviousGridSellProfit19Price= 0
PreviousGridSellProfit20Price= 0
PreviousGridSellProfit21Price= 0
PreviousGridSellProfit22Price= 0
PreviousGridSellProfit23Price= 0
PreviousGridSellProfit24Price= 0
PreviousGridSellProfit25Price= 0
PreviousGridSellProfit26Price= 0
PreviousGridSellProfit27Price= 0
PreviousGridSellProfit28Price= 0
PreviousGridSellProfit29Price= 0
PreviousGridSellProfit30Price= 0

LOCKPreviousGridSellProfit0Price = 0
LOCKPreviousGridSellProfit1Price = 0
LOCKPreviousGridSellProfit2Price = 0
LOCKPreviousGridSellProfit3Price = 0
LOCKPreviousGridSellProfit4Price = 0
LOCKPreviousGridSellProfit5Price = 0
LOCKPreviousGridSellProfit6Price = 0
LOCKPreviousGridSellProfit7Price = 0
LOCKPreviousGridSellProfit8Price = 0
LOCKPreviousGridSellProfit9Price = 0
LOCKPreviousGridSellProfit10Price= 0
LOCKPreviousGridSellProfit11Price= 0
LOCKPreviousGridSellProfit12Price= 0
LOCKPreviousGridSellProfit13Price= 0
LOCKPreviousGridSellProfit14Price= 0
LOCKPreviousGridSellProfit15Price= 0
LOCKPreviousGridSellProfit16Price= 0
LOCKPreviousGridSellProfit17Price= 0
LOCKPreviousGridSellProfit18Price= 0
LOCKPreviousGridSellProfit19Price= 0
LOCKPreviousGridSellProfit20Price= 0
LOCKPreviousGridSellProfit21Price= 0
LOCKPreviousGridSellProfit22Price= 0
LOCKPreviousGridSellProfit23Price= 0
LOCKPreviousGridSellProfit24Price= 0
LOCKPreviousGridSellProfit25Price= 0
LOCKPreviousGridSellProfit26Price= 0
LOCKPreviousGridSellProfit27Price= 0
LOCKPreviousGridSellProfit28Price= 0
LOCKPreviousGridSellProfit29Price= 0
LOCKPreviousGridSellProfit30Price= 0

GridSellFlag0  =0
GridSellFlag1  =0
GridSellFlag2  =0
GridSellFlag3  =0
GridSellFlag4  =0
GridSellFlag5  =0
GridSellFlag6  =0
GridSellFlag7  =0
GridSellFlag8  =0
GridSellFlag9  =0
GridSellFlag10 =0
GridSellFlag11 =0
GridSellFlag12 =0
GridSellFlag13 =0
GridSellFlag14 =0
GridSellFlag15 =0
GridSellFlag16 =0
GridSellFlag17 =0
GridSellFlag18 =0
GridSellFlag19 =0
GridSellFlag20 =0
GridSellFlag21 =0
GridSellFlag22 =0
GridSellFlag23 =0
GridSellFlag24 =0
GridSellFlag25 =0
GridSellFlag26 =0
GridSellFlag27 =0
GridSellFlag28 =0
GridSellFlag29 =0
GridSellFlag30 =0

GridBuyFlag0  =0
GridBuyFlag1  =0
GridBuyFlag2  =0
GridBuyFlag3  =0
GridBuyFlag4  =0
GridBuyFlag5  =0
GridBuyFlag6  =0
GridBuyFlag7  =0
GridBuyFlag8  =0
GridBuyFlag9  =0
GridBuyFlag10 =0
GridBuyFlag11 =0
GridBuyFlag12 =0
GridBuyFlag13 =0
GridBuyFlag14 =0
GridBuyFlag15 =0
GridBuyFlag16 =0
GridBuyFlag17 =0
GridBuyFlag18 =0
GridBuyFlag19 =0
GridBuyFlag20 =0
GridBuyFlag21 =0
GridBuyFlag22 =0
GridBuyFlag23 =0
GridBuyFlag24 =0
GridBuyFlag25 =0
GridBuyFlag26 =0
GridBuyFlag27 =0
GridBuyFlag28 =0
GridBuyFlag29 =0
GridBuyFlag30 =0

TradedamountBuy0=0
TradedamountBuy1=0
TradedamountBuy2 =0
TradedamountBuy3 =0
TradedamountBuy4 =0
TradedamountBuy5 =0
TradedamountBuy6 =0
TradedamountBuy7 =0
TradedamountBuy8 =0
TradedamountBuy9 =0
TradedamountBuy10=0
TradedamountBuy11=0
TradedamountBuy12=0
TradedamountBuy13=0
TradedamountBuy14=0
TradedamountBuy15=0
TradedamountBuy16=0
TradedamountBuy17=0
TradedamountBuy18=0
TradedamountBuy19=0
TradedamountBuy20=0
TradedamountBuy21=0
TradedamountBuy22=0
TradedamountBuy23=0
TradedamountBuy24=0
TradedamountBuy25=0
TradedamountBuy26=0
TradedamountBuy27=0
TradedamountBuy28=0
TradedamountBuy29=0
TradedamountBuy30=0

TradedamountSell0=0
TradedamountSell1=0
TradedamountSell2 =0
TradedamountSell3 =0
TradedamountSell4 =0
TradedamountSell5 =0
TradedamountSell6 =0
TradedamountSell7 =0
TradedamountSell8 =0
TradedamountSell9 =0
TradedamountSell10=0
TradedamountSell11=0
TradedamountSell12=0
TradedamountSell13=0
TradedamountSell14=0
TradedamountSell15=0
TradedamountSell16=0
TradedamountSell17=0
TradedamountSell18=0
TradedamountSell19=0
TradedamountSell20=0
TradedamountSell21=0
TradedamountSell22=0
TradedamountSell23=0
TradedamountSell24=0
TradedamountSell25=0
TradedamountSell26=0
TradedamountSell27=0
TradedamountSell28=0
TradedamountSell29=0
TradedamountSell30=0

GridBuy0ProfitFuncHandle=0
GridSell0ProfitFuncHandle=0

FullOpenOrderDetailsRAW="NONE"
FullOpenOrderDetailsLength=0
AAAATestPrice=0


MainPositionAmount=0
MainPostionSide="NONE"
MainPostionProfit=0
MainPostionLiquidationPrice=0
MainPostionEntryPrice=0


GridPriceMovePercent=.25
FirstIntiatedWalletBalance=0
DynamicFirstIntiatedWalletBalanceForGrid=0
FirstIntiatedWalletBalanceIncreaseCount=0
StopBuyFunc=0
StopSellFunc=0
PostionFullInfo="NONE"
PostionFullInfoRequest="NONE"
doubledAcountAmount=0
MainAccountProfitSinceGridStart=0
SN1M=0

MainPositionLiquidationPrice=0
MainPositionEntryPrice=0
MainPositionAmount=0
leverage=0
GridNumberCount=0
Buy0OrderID=0
PostionunRealizedProfit=0
RacingPriceFunc=0
HowManyTimesMoveFuncTriggeredSell=0
SHORTGridWithIndicator=0
SHORTGridWithIndicator0=0
SHORTGridWithIndicator1=0
SHORTGridWithIndicator2=0
SHORTGridWithIndicator3=0
SHORTGridWithIndicator4=0
SHORTGridWithIndicator5=0
SHORTGridWithIndicator6=0
SHORTGridWithIndicator7=0
SHORTGridWithIndicator8=0
SHORTGridWithIndicator9=0
SHORTGridWithIndicator10=0
SHORTGridWithIndicator11=0
SHORTGridWithIndicator12=0
SHORTGridWithIndicator13=0
SHORTGridWithIndicator14=0
SHORTGridWithIndicator15=0
SHORTGridWithIndicator16=0
SHORTGridWithIndicator17=0
SHORTGridWithIndicator18=0
SHORTGridWithIndicator19=0
SHORTGridWithIndicator20=0
SHORTGridWithIndicator21=0
SHORTGridWithIndicator22=0
SHORTGridWithIndicator23=0
SHORTGridWithIndicator24=0
SHORTGridWithIndicator25=0
SHORTGridWithIndicator26=0
SHORTGridWithIndicator27=0
SHORTGridWithIndicator28=0
SHORTGridWithIndicator29=0
SHORTGridWithIndicator30=0
LongGridWithIndicator0=0
LongGridWithIndicator1=0
LongGridWithIndicator2=0
LongGridWithIndicator3=0
LongGridWithIndicator4=0
LongGridWithIndicator5=0
LongGridWithIndicator6=0
LongGridWithIndicator7=0
LongGridWithIndicator8=0
LongGridWithIndicator9=0
LongGridWithIndicator10=0
LongGridWithIndicator11=0
LongGridWithIndicator12=0
LongGridWithIndicator13=0
LongGridWithIndicator14=0
LongGridWithIndicator15=0
LongGridWithIndicator16=0
LongGridWithIndicator17=0
LongGridWithIndicator18=0
LongGridWithIndicator19=0
LongGridWithIndicator20=0
LongGridWithIndicator21=0
LongGridWithIndicator22=0
LongGridWithIndicator23=0
LongGridWithIndicator24=0
LongGridWithIndicator25=0
LongGridWithIndicator26=0
LongGridWithIndicator27=0
LongGridWithIndicator28=0
LongGridWithIndicator29=0
LongGridWithIndicator30=0

ProfitPercentDynamic0  =10
ProfitPercentDynamic1  =11
ProfitPercentDynamic2  =12
ProfitPercentDynamic3  =13
ProfitPercentDynamic4  =14
ProfitPercentDynamic5  =15
ProfitPercentDynamic6  =16
ProfitPercentDynamic7  =17
ProfitPercentDynamic8  =18
ProfitPercentDynamic9  =19
ProfitPercentDynamic10 =20
ProfitPercentDynamic11 =21
ProfitPercentDynamic12 =22
ProfitPercentDynamic13 =23
ProfitPercentDynamic14 =24
ProfitPercentDynamic15 =25
ProfitPercentDynamic16 =26
ProfitPercentDynamic17 =27
ProfitPercentDynamic18 =28
ProfitPercentDynamic19 =29
ProfitPercentDynamic20 =30
ProfitPercentDynamic21 =31
ProfitPercentDynamic22 =32
ProfitPercentDynamic23 =33
ProfitPercentDynamic24 =34
ProfitPercentDynamic25 =35
ProfitPercentDynamic26 =36
ProfitPercentDynamic27 =37
ProfitPercentDynamic28 =38
ProfitPercentDynamic29 =39
ProfitPercentDynamic30 =40
lockProfit1=0 
lockProfit2=0 
lockProfit3=0 
lockProfit4=0 
lockProfit5=0 
lockProfit6=0 
lockProfit7=0 
lockProfit8=0 
lockProfit9=0 
lockProfit10=0
lockProfit11=0
lockProfit12=0
lockProfit13=0
lockProfit14=0	
lockProfit15=0
lockProfit16=0
lockProfit17=0
lockProfit18=0	
lockProfit19=0
lockProfit20=0
lockProfit21=0
DynamicFirstIntiatedWalletBalanceForAmountPostion=0
PercentBetweenFirstBalanceAndCurrentBalance=0

# # extra params and overrides if needed
params = {
	'test': True,  # test if it's valid, but don't actually place it
}





start_time = time.time()
StartNowTimeAndDate=datetime.now() 
# # closing all open orders from previous grid ##############################################################################
# binance.cancel_all_orders(symbol=symbol)
# # closing open postion from previous grid ##############################################################################
# PostionFullInfo=binance.fapiPrivateGetPositionRisk ()
# MainPositionAmount=float(PostionFullInfo[0].get('positionAmt'))
# MainPositionEntryPrice=float(PostionFullInfo[0].get('entryPrice'))
# MainPositionLiquidationPrice=float(PostionFullInfo[0].get('liquidationPrice'))
# MainPostionProfit=float(PostionFullInfo[0].get('unRealizedProfit'))
# leverage=PostionFullInfo[0].get('leverage')
	
# print("----PostionAmount----",MainPositionAmount,"----entryPrice----",MainPositionEntryPrice,'---liquidationPrice----',MainPositionLiquidationPrice,'----leverage----',leverage)


# if(MainPositionAmount!=0):
	# print("CLOSING THIS POSTION BE READY =========================================================================================================================================")	
	# if(MainPositionAmount > 0 and MainPositionEntryPrice !=0 ):
		# MainPostionSide='long'
	# if(MainPositionAmount < 0	 and MainPositionEntryPrice !=0 ):
		# MainPostionSide='SHORT'	
	# TickersInfo=binance.fetchTicker (symbol)
	# LastPriceTICKS=TickersInfo.get("last")
	# if(MainPostionSide=='long' ):
		# print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Closing LONG Postion NOW USING MARKET ORDER <<<<<<<<<<<<<<<<<<<<<<<<','green'))
		# Ordertype='Sell'
		# Orderside='market'
		# Orderprice=LastPriceTICKS
		# Orderamount=MainPositionAmount
		# binance.createOrder (symbol,Orderside,Ordertype,Orderamount)
	# if(MainPostionSide=='SHORT'):
		# print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Closing SHORT Postion NOW USING MARKET ORDER <<<<<<<<<<<<<<<<<<<<<<<<','red'))
		# Ordertype='Buy'
		# Orderside='market'
		# Orderprice=LastPriceTICKS
		# Orderamount=-(MainPositionAmount)
		# binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	


# ################################################################################### TICKS AND WALLET FUNC SECTION ###########################################################################################################
# ################################################################################### TICKS AND WALLET FUNC SECTION ###########################################################################################################
# ################################################################################### TICKS AND WALLET FUNC SECTION ###########################################################################################################
# ################################################################################### TICKS AND WALLET FUNC SECTION ###########################################################################################################
# ################################################################################### TICKS AND WALLET FUNC SECTION ###########################################################################################################	
# ################################### EMPTY INBOX FIRST ###############################################

if(BuyDirectinalGrid==1 and SellDirectinalGrid==0  and	BotType=="SUPERTREND-LONG"):
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login('sobh@gmail.com', '')
	mail.list() 
	mail.select('inbox') 
	result, data = mail.uid('search', None, "ALL")
	if data!=[b'']:
		i = len(data[0].split()) 
		for x in range(i):
				latest_email_uid = data[0].split()[x] 
				result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
				raw_email = email_data[0][1]
		raw_email_string = raw_email.decode('utf-8')
		FullEmailMSG=str(email.message_from_string(raw_email_string))
		email_message = email.message_from_string(raw_email_string)
		Subject = FullEmailMSG[FullEmailMSG.find("TradingView Alert:")+len(Subject):].split()[2]
		SubjectManual = FullEmailMSG[FullEmailMSG.find("")+len(Subject):].split()[0]
		print("Subject=",Subject,"SubjectGlobal=",SubjectGlobal,"SubjectManual=",SubjectManual)
		mail.uid('STORE', latest_email_uid, '+X-GM-LABELS', '\\Trash')	 # Move to Trash 
# # ################################### EMPTY INBOX FIRST ###############################################
# ################################### EMPTY INBOX FIRST ###############################################
if(SellDirectinalGrid==1 and BuyDirectinalGrid==0  and	BotType=="SUPERTREND-SHORT"):
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login('sobh@gmail.com', '')
	mail.list() 
	mail.select('inbox') 
	result, data = mail.uid('search', None, "ALL")
	if data!=[b'']:
		i = len(data[0].split()) 
		for x in range(i):
				latest_email_uid = data[0].split()[x] 
				result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
				raw_email = email_data[0][1]
		raw_email_string = raw_email.decode('utf-8')
		FullEmailMSG=str(email.message_from_string(raw_email_string))
		email_message = email.message_from_string(raw_email_string)
		Subject = FullEmailMSG[FullEmailMSG.find("TradingView Alert:")+len(Subject):].split()[2]
		SubjectManual = FullEmailMSG[FullEmailMSG.find("")+len(Subject):].split()[0]
		print("Subject=",Subject,"SubjectGlobal=",SubjectGlobal,"SubjectManual=",SubjectManual)
		mail.uid('STORE', latest_email_uid, '+X-GM-LABELS', '\\Trash')	 # Move to Trash 
	# ################################### EMPTY INBOX FIRST ###############################################




def SUPERTRENDLONG():
	global SubjectGlobal
	global Subject
	global SubjectManual
	global ATRValueOpenPostionTime
	global FullEmailMSG
	global UsingEmailedStaticPercent
	try:
		mail = imaplib.IMAP4_SSL('imap.gmail.com')
		mail.login('sobh@gmail.com', '')
		mail.list() 
		mail.select('inbox') 
		result, data = mail.uid('search', None, "ALL")
		if data!=[b'']:
			Subject='WHATEVER'
			ATRValueOpenPostionTime='WHATEVER'
			i = len(data[0].split()) 
			for x in range(i):
			 latest_email_uid = data[0].split()[x] 
			 result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
			 raw_email = email_data[0][1]

			raw_email_string = raw_email.decode('utf-8')
			FullEmailMSG=str(email.message_from_string(raw_email_string))
			Subject = FullEmailMSG[FullEmailMSG.find("TradingView Alert:")+len(Subject):].split()[2]
			Subject= Subject.split(',')[0]
			ATRValueOpenPostionTime = FullEmailMSG[FullEmailMSG.find("TradingView Alert:")+len(Subject):].split()[2]
			ATRValueOpenPostionTime = ATRValueOpenPostionTime.split(',')[1]
			ATRValueOpenPostionTime = ATRValueOpenPostionTime.split('=')[1]
			ATRValueOpenPostionTime=float(ATRValueOpenPostionTime)
			UsingEmailedStaticPercent=ATRValueOpenPostionTime
			SubjectGlobal=Subject
			SubjectManual = FullEmailMSG[FullEmailMSG.find("Subject:")+len(Subject):].split()[1]
			# print("Subject=",Subject,"SubjectGlobalMain=",SubjectGlobal,"SubjectManual=",SubjectManual)
			# print("ATRValueOpenPostionTime=",str(ATRValueOpenPostionTime))
			email_message = email.message_from_string(raw_email_string)
			mail.uid('STORE', latest_email_uid, '+X-GM-LABELS', '\\Trash')	 # Move to Trash 
			for part in email_message.walk():
			 if part.get_content_type() == "text/plain": 
			  body = part.get_payload(decode=True)
			 else:
			  continue
		  
		  
	except:
			print("Err in GMAIL")
			
	threading.Timer(1, SUPERTRENDLONG).start()	


def SUPERTRENDSHORT():
	global SubjectGlobal
	global Subject
	global SubjectManual
	global ATRValueOpenPostionTime
	global FullEmailMSG
	global UsingEmailedStaticPercent
	try:
		mail = imaplib.IMAP4_SSL('imap.gmail.com')
		mail.login('sobh@gmail.com', '')
		mail.list() 
		mail.select('inbox') 
		result, data = mail.uid('search', None, "ALL")
		if data!=[b'']:
			Subject='WHATEVER'
			ATRValueOpenPostionTime='WHATEVER'
			i = len(data[0].split()) 
			for x in range(i):
			 latest_email_uid = data[0].split()[x] 
			 result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
			 raw_email = email_data[0][1]

			raw_email_string = raw_email.decode('utf-8')
			FullEmailMSG=str(email.message_from_string(raw_email_string))
			Subject = FullEmailMSG[FullEmailMSG.find("TradingView Alert:")+len(Subject):].split()[2]
			Subject= Subject.split(',')[0]
			ATRValueOpenPostionTime = FullEmailMSG[FullEmailMSG.find("TradingView Alert:")+len(Subject):].split()[2]
			ATRValueOpenPostionTime = ATRValueOpenPostionTime.split(',')[1]
			ATRValueOpenPostionTime = ATRValueOpenPostionTime.split('=')[1]
			ATRValueOpenPostionTime=float(ATRValueOpenPostionTime)
			UsingEmailedStaticPercent=ATRValueOpenPostionTime
			SubjectGlobal=Subject
			SubjectManual = FullEmailMSG[FullEmailMSG.find("Subject:")+len(Subject):].split()[1]
			# print("Subject=",Subject,"SubjectGlobalMain=",SubjectGlobal,"SubjectManual=",SubjectManual)
			# print("ATRValueOpenPostionTime=",str(ATRValueOpenPostionTime))
			email_message = email.message_from_string(raw_email_string)
			mail.uid('STORE', latest_email_uid, '+X-GM-LABELS', '\\Trash')	 # Move to Trash 
			for part in email_message.walk():
			 if part.get_content_type() == "text/plain": 
			  body = part.get_payload(decode=True)
			 else:
			  continue
		  
		  
	except:
			print("Err in GMAIL")					
	threading.Timer(1, SUPERTRENDSHORT).start()	


































# ################################################################################### MAIN FUNC SECTION ###########################################################################################################
# ################################################################################### MAIN FUNC SECTION ###########################################################################################################
# ################################################################################### MAIN FUNC SECTION ###########################################################################################################
# ################################################################################### MAIN FUNC SECTION ###########################################################################################################
# ################################################################################### MAIN FUNC SECTION ###########################################################################################################	
def TICKSFunc():
	
	global	AArray
	global	ClosesFor200P1HArray
	global price
	global i
	global totalUnrealizedProfitBalanceList
	global currentPrice
	global previousPrice
	global CurrentProffit
	global previousProfit
	global currentProfitLockArray	
	global previousProfitLockArray	
	global currentPosition
	global TheDynaimicProfitPercent
	global OrderActionTakenGlobal
	global AmountGlobal
	global SubjectGlobal
	global Subject
	global SubjectGlobal15M
	global Subject15M
	global profitLock
	global profitLockKey
	global SubjectManual
	global previousDynaimicProfitPercent
	global totalWalletBalance
	global totalUnrealizedProfitBalance
	global totalUnrealizedProfitBalanceInPercent
	global LastPriceTICKS
	global ProfitPercentDynamic
	global SELLNOW
	global PrecentProfitLock
	global PositionPrice
	global SL
	global StopLossPricePercent
	global StopLossPriceFull
	global ClosesArrayFor14
	global LowArrayFor14
	global HighArrayFor14	
	global ClosesFor50P1HArray
	global Margin	
	global TradeBotUsedMargin
	global LocakPrecentToBeUsedAfterProfitPercentDynamic
	global MI
	global GridArray
	global LocakPrecentToBeUsedAfterGridArray
	global CI
	global CurrentPositionProfit
	global currentPriceOneMin
	global previousPriceOneMin
	global CurrentProffitOneMin
	global previousProfitOneMin
	global totalWalletBalanceOneMin
	global CurrentPositionProfitArray
	global PreviousPositionProfitArray
	global ManualEntryPrice
	global ManualSize
	global ManualPositionDirection
	global totalPositionInitialMargin
	global walletBalance
	global maxWithdrawAmount
	global totalUnrealizedProfit
	global RunForOneTimeOnly
	global Tradedamount
	global TottalIntiatedMarginManual
	global TottalIntiatedMarginAuto
	global CurrentPositionProfitPercent
	global inPostion
	global StartTrading
	global ATRValueOpenPostionTime
	global previousProfitLock
	global FirstpreviousProfitLock
	global KeyPressedToSell
	global KeyPressedToBuy
	global NextProfitPrice
	global IncreasedNumber
	global ProfitCount
	global SLUsingATR
	global ProfitUsingATR
	global AutoATRVALUEToProfitLock
	global A
	global UseATRForTrading
	global UsingEmailedStaticPercent
	global PositionPriceIndollars
	global FeesMarket
	global TheFirstpreviousProfit
	global SafeFirstpreviousProfitLock
	global LastProfitGain
	global ProfitLevel
	global NewManualTrade
	global LocakedNewManualTrade
	global manualBalance
	global manualBalance15M
	global FeesMarket15M	
	global inSHORT15M
	global inLong15M
	global OrderActionTakenGlobal15M
	global AmountGlobal15M
	global profitLockKey15M
	global CurrentPositionProfit15M
	global FeesMarket15M
	global PositionPrice15M
	global Ordertype15M
	global OrderActionWas15M
	global ExitSL15M
	global ExitPR15M
	global MI15M
	global CI15M
	global A15M
	global ProfitPercentDynamic15M
	global currentPosition15M
	global GridArray15M
	global CurrentPositionProfitPercent15M
	global TottalIntiatedMarginAuto15M
	global StopLossPricePercent15M
	global StopLossPriceFull15M
	global SELLNOW15M
	global SN15M
	global SL15M
	global PR15M
	global MoveEmailToTrash15M
	global id
	global Buy_start
	global Buy_end
	global target1
	global stop_loss
	global exchange1
	global currency
	global coin
	global countto10
	global StopGettingSignals
	global grid
	global x
	global grid0BuyPrice
	global grid0SellPrice
	global grid1BuyPrice
	global grid1SellPrice
	global grid2BuyPrice
	global grid2SellPrice
	global grid3BuyPrice
	global grid3SellPrice
	global grid4BuyPrice
	global grid4SellPrice
	global grid5BuyPrice
	global grid5SellPrice
	global grid6BuyPrice
	global grid6SellPrice
	global grid7BuyPrice
	global grid7SellPrice
	global grid8BuyPrice
	global grid8SellPrice
	global grid9BuyPrice
	global grid9SellPrice
	global grid10BuyPrice
	global grid10SellPrice
	global grid11BuyPrice
	global grid11SellPrice
	global grid12BuyPrice
	global grid12SellPrice
	global grid13BuyPrice
	global grid13SellPrice
	global grid14BuyPrice
	global grid14SellPrice
	global grid15BuyPrice
	global grid15SellPrice
	global grid16BuyPrice
	global grid16SellPrice
	global grid17BuyPrice
	global grid17SellPrice
	global grid18BuyPrice
	global grid18SellPrice
	global grid19BuyPrice
	global grid19SellPrice
	global grid20BuyPrice
	global grid20SellPrice
	global grid21BuyPrice
	global grid21SellPrice
	global grid22BuyPrice
	global grid22SellPrice
	global grid23BuyPrice
	global grid23SellPrice
	global grid24BuyPrice
	global grid24SellPrice
	global grid25BuyPrice
	global grid25SellPrice
	global grid26BuyPrice
	global grid26SellPrice
	global grid27BuyPrice
	global grid27SellPrice
	global grid28BuyPrice
	global grid28SellPrice
	global grid29BuyPrice
	global grid29SellPrice
	global grid30BuyPrice
	global grid30SellPrice
	global grid0BuyPostion
	global grid0SellPostion
	global grid1BuyPostion
	global grid1SellPostion
	global grid2BuyPostion
	global grid2SellPostion
	global grid3BuyPostion
	global grid3SellPostion
	global grid4BuyPostion
	global grid4SellPostion
	global grid5BuyPostion
	global grid5SellPostion
	global grid6BuyPostion
	global grid6SellPostion
	global grid7BuyPostion
	global grid7SellPostion
	global grid8BuyPostion
	global grid8SellPostion
	global grid9BuyPostion
	global grid9SellPostion
	global grid10BuyPostion
	global grid10SellPostion
	global grid11BuyPostion
	global grid11SellPostion
	global grid12BuyPostion
	global grid12SellPostion
	global grid13BuyPostion
	global grid13SellPostion
	global grid14BuyPostion
	global grid14SellPostion
	global grid15BuyPostion
	global grid15SellPostion
	global grid16BuyPostion
	global grid16SellPostion
	global grid17BuyPostion
	global grid17SellPostion
	global grid18BuyPostion
	global grid18SellPostion
	global grid19BuyPostion
	global grid19SellPostion
	global grid20BuyPostion
	global grid20SellPostion
	global grid21BuyPostion
	global grid21SellPostion
	global grid22BuyPostion
	global grid22SellPostion
	global grid23BuyPostion
	global grid23SellPostion
	global grid24BuyPostion
	global grid24SellPostion
	global grid25BuyPostion
	global grid25SellPostion
	global grid26BuyPostion
	global grid26SellPostion
	global grid27BuyPostion
	global grid27SellPostion
	global grid28BuyPostion
	global grid28SellPostion
	global grid29BuyPostion
	global grid29SellPostion
	global grid30BuyPostion
	global grid30SellPostion
	global StartGrid
	global BiDirectionalGrid
	global SellDirectinalGrid
	global BuyDirectinalGrid
	global GridPriceMovePercent
	global FixSellMove
	global BTCBalanceFree
	global ETHBalanceFree
	global ETHBalanceLocked
	global BTCBalanceLocked
	global TradedamountBuy0
	global TradedamountBuy1
	global TradedamountBuy2 
	global TradedamountBuy3 
	global TradedamountBuy4 
	global TradedamountBuy5 
	global TradedamountBuy6 
	global TradedamountBuy7 
	global TradedamountBuy8 
	global TradedamountBuy9 
	global TradedamountBuy10
	global TradedamountBuy11
	global TradedamountBuy12
	global TradedamountBuy13
	global TradedamountBuy14
	global TradedamountBuy15
	global TradedamountBuy16
	global TradedamountBuy17
	global TradedamountBuy18
	global TradedamountBuy19
	global TradedamountBuy20
	global TradedamountBuy21
	global TradedamountBuy22
	global TradedamountBuy23
	global TradedamountBuy24
	global TradedamountBuy25
	global TradedamountBuy26
	global TradedamountBuy27
	global TradedamountBuy28
	global TradedamountBuy29
	global TradedamountBuy30
	global TradedamountSell0
	global TradedamountSell1
	global TradedamountSell2 
	global TradedamountSell3 
	global TradedamountSell4 
	global TradedamountSell5 
	global TradedamountSell6 
	global TradedamountSell7 
	global TradedamountSell8 
	global TradedamountSell9 
	global TradedamountSell10
	global TradedamountSell11
	global TradedamountSell12
	global TradedamountSell13
	global TradedamountSell14
	global TradedamountSell15
	global TradedamountSell16
	global TradedamountSell17
	global TradedamountSell18
	global TradedamountSell19
	global TradedamountSell20
	global TradedamountSell21
	global TradedamountSell22
	global TradedamountSell23
	global TradedamountSell24
	global TradedamountSell25
	global TradedamountSell26
	global TradedamountSell27
	global TradedamountSell28
	global TradedamountSell29
	global TradedamountSell30
	global GridBuyProfit0Price 
	global GridBuyProfit1Price 
	global GridBuyProfit2Price 
	global GridBuyProfit3Price 
	global GridBuyProfit4Price 
	global GridBuyProfit5Price 
	global GridBuyProfit6Price 
	global GridBuyProfit7Price 
	global GridBuyProfit8Price 
	global GridBuyProfit9Price 
	global GridBuyProfit10Price
	global GridBuyProfit11Price
	global GridBuyProfit12Price
	global GridBuyProfit13Price
	global GridBuyProfit14Price
	global GridBuyProfit15Price
	global GridBuyProfit16Price
	global GridBuyProfit17Price
	global GridBuyProfit18Price
	global GridBuyProfit19Price
	global GridBuyProfit20Price
	global GridBuyProfit21Price
	global GridBuyProfit22Price
	global GridBuyProfit23Price
	global GridBuyProfit24Price
	global GridBuyProfit25Price
	global GridBuyProfit26Price
	global GridBuyProfit27Price
	global GridBuyProfit28Price
	global GridBuyProfit29Price
	global GridBuyProfit30Price
	global GridBuyProfit0Percent 
	global GridBuyProfit1Percent 
	global GridBuyProfit2Percent 
	global GridBuyProfit3Percent 
	global GridBuyProfit4Percent 
	global GridBuyProfit5Percent 
	global GridBuyProfit6Percent 
	global GridBuyProfit7Percent 
	global GridBuyProfit8Percent 
	global GridBuyProfit9Percent 
	global GridBuyProfit10Percent
	global GridBuyProfit11Percent
	global GridBuyProfit12Percent
	global GridBuyProfit13Percent
	global GridBuyProfit14Percent
	global GridBuyProfit15Percent
	global GridBuyProfit16Percent
	global GridBuyProfit17Percent
	global GridBuyProfit18Percent
	global GridBuyProfit19Percent
	global GridBuyProfit20Percent
	global GridBuyProfit21Percent
	global GridBuyProfit22Percent
	global GridBuyProfit23Percent
	global GridBuyProfit24Percent
	global GridBuyProfit25Percent
	global GridBuyProfit26Percent
	global GridBuyProfit27Percent
	global GridBuyProfit28Percent
	global GridBuyProfit29Percent
	global GridBuyProfit30Percent
	global GridSellProfit0Percent
	global GridSellProfit1Percent
	global GridSellProfit2Percent
	global GridSellProfit3Percent
	global GridSellProfit4Percent
	global GridSellProfit5Percent
	global GridSellProfit6Percent
	global GridSellProfit7Percent
	global GridSellProfit8Percent
	global GridSellProfit9Percent
	global GridSellProfit10Percent
	global GridSellProfit11Percent
	global GridSellProfit12Percent
	global GridSellProfit13Percent
	global GridSellProfit14Percent
	global GridSellProfit15Percent
	global GridSellProfit16Percent
	global GridSellProfit17Percent
	global GridSellProfit18Percent
	global GridSellProfit19Percent
	global GridSellProfit20Percent
	global GridSellProfit21Percent
	global GridSellProfit22Percent
	global GridSellProfit23Percent
	global GridSellProfit24Percent
	global GridSellProfit25Percent
	global GridSellProfit26Percent
	global GridSellProfit27Percent
	global GridSellProfit28Percent
	global GridSellProfit29Percent
	global GridSellProfit30Percent
	global GridSellProfit0Price 
	global GridSellProfit1Price 
	global GridSellProfit2Price 
	global GridSellProfit3Price 
	global GridSellProfit4Price 
	global GridSellProfit5Price 
	global GridSellProfit6Price 
	global GridSellProfit7Price 
	global GridSellProfit8Price 
	global GridSellProfit9Price 
	global GridSellProfit10Price
	global GridSellProfit11Price
	global GridSellProfit12Price
	global GridSellProfit13Price
	global GridSellProfit14Price
	global GridSellProfit15Price
	global GridSellProfit16Price
	global GridSellProfit17Price
	global GridSellProfit18Price
	global GridSellProfit19Price
	global GridSellProfit20Price
	global GridSellProfit21Price
	global GridSellProfit22Price
	global GridSellProfit23Price
	global GridSellProfit24Price
	global GridSellProfit25Price
	global GridSellProfit26Price
	global GridSellProfit27Price
	global GridSellProfit28Price
	global GridSellProfit29Price
	global GridSellProfit30Price
	global GridSellFlag0 
	global GridSellFlag1 
	global GridSellFlag2 
	global GridSellFlag3 
	global GridSellFlag4 
	global GridSellFlag5 
	global GridSellFlag6 
	global GridSellFlag7 
	global GridSellFlag8 
	global GridSellFlag9 
	global GridSellFlag10
	global GridSellFlag11
	global GridSellFlag12
	global GridSellFlag13
	global GridSellFlag14
	global GridSellFlag15
	global GridSellFlag16
	global GridSellFlag17
	global GridSellFlag18
	global GridSellFlag19
	global GridSellFlag20
	global GridSellFlag21
	global GridSellFlag22
	global GridSellFlag23
	global GridSellFlag24
	global GridSellFlag25
	global GridSellFlag26
	global GridSellFlag27
	global GridSellFlag28
	global GridSellFlag29
	global GridSellFlag30
	global GridBuyFlag0 
	global GridBuyFlag1 
	global GridBuyFlag2 
	global GridBuyFlag3 
	global GridBuyFlag4 
	global GridBuyFlag5 
	global GridBuyFlag6 
	global GridBuyFlag7 
	global GridBuyFlag8 
	global GridBuyFlag9 
	global GridBuyFlag10
	global GridBuyFlag11
	global GridBuyFlag12
	global GridBuyFlag13
	global GridBuyFlag14
	global GridBuyFlag15
	global GridBuyFlag16
	global GridBuyFlag17
	global GridBuyFlag18
	global GridBuyFlag19
	global GridBuyFlag20
	global GridBuyFlag21
	global GridBuyFlag22
	global GridBuyFlag23
	global GridBuyFlag24
	global GridBuyFlag25
	global GridBuyFlag26
	global GridBuyFlag27
	global GridBuyFlag28
	global GridBuyFlag29
	global GridBuyFlag30
	global GridBuy0PriceMovePercent 
	global GridBuy1PriceMovePercent 
	global GridBuy2PriceMovePercent 
	global GridBuy3PriceMovePercent 
	global GridBuy4PriceMovePercent 
	global GridBuy5PriceMovePercent 
	global GridBuy6PriceMovePercent 
	global GridBuy7PriceMovePercent 
	global GridBuy8PriceMovePercent 
	global GridBuy9PriceMovePercent 
	global GridBuy10PriceMovePercent
	global GridBuy11PriceMovePercent
	global GridBuy12PriceMovePercent
	global GridBuy13PriceMovePercent
	global GridBuy14PriceMovePercent
	global GridBuy15PriceMovePercent
	global GridBuy16PriceMovePercent
	global GridBuy17PriceMovePercent
	global GridBuy18PriceMovePercent
	global GridBuy19PriceMovePercent
	global GridBuy20PriceMovePercent
	global GridBuy21PriceMovePercent
	global GridBuy22PriceMovePercent
	global GridBuy23PriceMovePercent
	global GridBuy24PriceMovePercent
	global GridBuy25PriceMovePercent
	global GridBuy26PriceMovePercent
	global GridBuy27PriceMovePercent
	global GridBuy28PriceMovePercent
	global GridBuy29PriceMovePercent
	global GridBuy30PriceMovePercent
	global GridSell0PriceMovePercent
	global GridSell1PriceMovePercent
	global GridSell2PriceMovePercent
	global GridSell3PriceMovePercent
	global GridSell4PriceMovePercent
	global GridSell5PriceMovePercent
	global GridSell6PriceMovePercent
	global GridSell7PriceMovePercent
	global GridSell8PriceMovePercent
	global GridSell9PriceMovePercent
	global GridSell10PriceMovePercent
	global GridSell11PriceMovePercent
	global GridSell12PriceMovePercent
	global GridSell13PriceMovePercent
	global GridSell14PriceMovePercent
	global GridSell15PriceMovePercent
	global GridSell16PriceMovePercent
	global GridSell17PriceMovePercent
	global GridSell18PriceMovePercent
	global GridSell19PriceMovePercent
	global GridSell20PriceMovePercent
	global GridSell21PriceMovePercent
	global GridSell22PriceMovePercent
	global GridSell23PriceMovePercent
	global GridSell24PriceMovePercent
	global GridSell25PriceMovePercent
	global GridSell26PriceMovePercent
	global GridSell27PriceMovePercent
	global GridSell28PriceMovePercent
	global GridSell29PriceMovePercent
	global GridSell30PriceMovePercent
	global FullOpenOrderDetailsRAW
	global ii
	global FullOpenOrderDetailsLength
	global VolumePriceTICKSUSDT
	global GridSell0Func 
	global GridSell1Func 
	global GridSell2Func 
	global GridSell3Func 
	global GridSell4Func 
	global GridSell5Func 
	global GridSell6Func 
	global GridSell7Func 
	global GridSell8Func 
	global GridSell9Func 
	global GridSell10Func
	global GridSell11Func
	global GridSell12Func
	global GridSell13Func
	global GridSell14Func
	global GridSell15Func
	global GridSell16Func
	global GridSell17Func
	global GridSell18Func
	global GridSell19Func
	global GridSell20Func
	global GridSell21Func
	global GridSell22Func
	global GridSell23Func
	global GridSell24Func
	global GridSell25Func
	global GridSell26Func
	global GridSell27Func
	global GridSell28Func
	global GridSell29Func
	global GridSell30Func
	global GridBuy0Func 
	global GridBuy1Func 
	global GridBuy2Func 
	global GridBuy3Func 
	global GridBuy4Func 
	global GridBuy5Func 
	global GridBuy6Func 
	global GridBuy7Func 
	global GridBuy8Func 
	global GridBuy9Func 
	global GridBuy10Func
	global GridBuy11Func
	global GridBuy12Func
	global GridBuy13Func
	global GridBuy14Func
	global GridBuy15Func
	global GridBuy16Func
	global GridBuy17Func
	global GridBuy18Func
	global GridBuy19Func
	global GridBuy20Func
	global GridBuy21Func
	global GridBuy22Func
	global GridBuy23Func
	global GridBuy24Func
	global GridBuy25Func
	global GridBuy26Func
	global GridBuy27Func
	global GridBuy28Func
	global GridBuy29Func
	global GridBuy30Func
	global OrderIDBuy0
	global Buy0OrderID
	global Buy0OrderStatus
	global Buy0OrderSide
	global Buy0cost
	global Buy0OrderType
	global Buy1OrderID
	global Buy1OrderStatus
	global Buy1OrderSide
	global Buy1cost
	global Buy1OrderType
	global Buy2OrderID
	global Buy2OrderStatus
	global Buy2OrderSide
	global Buy2cost
	global Buy2OrderType
	global Buy3OrderID
	global Buy3OrderStatus
	global Buy3OrderSide
	global Buy3cost
	global Buy3OrderType
	global Buy4OrderID
	global Buy4OrderStatus
	global Buy4OrderSide
	global Buy4cost
	global Buy4OrderType
	global Buy5OrderID
	global Buy5OrderStatus
	global Buy5OrderSide
	global Buy5cost
	global Buy5OrderType
	global Buy6OrderID
	global Buy6OrderStatus
	global Buy6OrderSide
	global Buy6cost
	global Buy6OrderType
	global Buy7OrderID
	global Buy7OrderStatus
	global Buy7OrderSide
	global Buy7cost
	global Buy7OrderType
	global Buy8OrderID
	global Buy8OrderStatus
	global Buy8OrderSide
	global Buy8cost
	global Buy8OrderType
	global Buy9OrderID
	global Buy9OrderStatus
	global Buy9OrderSide
	global Buy9cost
	global Buy9OrderType
	global Buy10OrderID
	global Buy10OrderStatus
	global Buy10OrderSide
	global Buy10cost
	global Buy10OrderType
	global Buy11OrderID
	global Buy11OrderStatus
	global Buy11OrderSide
	global Buy11cost
	global Buy11OrderType
	global Buy12OrderID
	global Buy12OrderStatus
	global Buy12OrderSide
	global Buy12cost
	global Buy12OrderType
	global Buy13OrderID
	global Buy13OrderStatus
	global Buy13OrderSide
	global Buy13cost
	global Buy13OrderType
	global Buy14OrderID
	global Buy14OrderStatus
	global Buy14OrderSide
	global Buy14cost
	global Buy14OrderType
	global Buy15OrderID
	global Buy15OrderStatus
	global Buy15OrderSide
	global Buy15cost
	global Buy15OrderType
	global Buy16OrderID
	global Buy16OrderStatus
	global Buy16OrderSide
	global Buy16cost
	global Buy16OrderType
	global Buy17OrderID
	global Buy17OrderStatus
	global Buy17OrderSide
	global Buy17cost
	global Buy17OrderType
	global Buy18OrderID
	global Buy18OrderStatus
	global Buy18OrderSide
	global Buy18cost
	global Buy18OrderType
	global Buy19OrderID
	global Buy19OrderStatus
	global Buy19OrderSide
	global Buy19cost
	global Buy19OrderType
	global Buy20OrderID
	global Buy20OrderStatus
	global Buy20OrderSide
	global Buy20cost
	global Buy20OrderType
	global Buy21OrderID
	global Buy21OrderStatus
	global Buy21OrderSide
	global Buy21cost
	global Buy21OrderType
	global Buy22OrderID
	global Buy22OrderStatus
	global Buy22OrderSide
	global Buy22cost
	global Buy22OrderType
	global Buy23OrderID
	global Buy23OrderStatus
	global Buy23OrderSide
	global Buy23cost
	global Buy23OrderType
	global Buy24OrderID
	global Buy24OrderStatus
	global Buy24OrderSide
	global Buy24cost
	global Buy24OrderType
	global Buy25OrderID
	global Buy25OrderStatus
	global Buy25OrderSide
	global Buy25cost
	global Buy25OrderType
	global Buy26OrderID
	global Buy26OrderStatus
	global Buy26OrderSide
	global Buy26cost
	global Buy26OrderType
	global Buy27OrderID
	global Buy27OrderStatus
	global Buy27OrderSide
	global Buy27cost
	global Buy27OrderType
	global Buy28OrderID
	global Buy28OrderStatus
	global Buy28OrderSide
	global Buy28cost
	global Buy28OrderType
	global Buy29OrderID
	global Buy29OrderStatus
	global Buy29OrderSide
	global Buy29cost
	global Buy29OrderType
	global Buy30OrderID
	global Buy30OrderStatus
	global Buy30OrderSide
	global Buy30cost
	global Buy30OrderType
	global Sell0OrderID
	global Sell0OrderStatus
	global Sell0OrderSide
	global Sell0cost
	global Sell0OrderType
	global Sell1OrderID
	global Sell1OrderStatus
	global Sell1OrderSide
	global Sell1cost
	global Sell1OrderType
	global Sell2OrderID
	global Sell2OrderStatus
	global Sell2OrderSide
	global Sell2cost
	global Sell2OrderType
	global Sell3OrderID
	global Sell3OrderStatus
	global Sell3OrderSide
	global Sell3cost
	global Sell3OrderType
	global Sell4OrderID
	global Sell4OrderStatus
	global Sell4OrderSide
	global Sell4cost
	global Sell4OrderType
	global Sell5OrderID
	global Sell5OrderStatus
	global Sell5OrderSide
	global Sell5cost
	global Sell5OrderType
	global Sell6OrderID
	global Sell6OrderStatus
	global Sell6OrderSide
	global Sell6cost
	global Sell6OrderType
	global Sell7OrderID
	global Sell7OrderStatus
	global Sell7OrderSide
	global Sell7cost
	global Sell7OrderType
	global Sell8OrderID
	global Sell8OrderStatus
	global Sell8OrderSide
	global Sell8cost
	global Sell8OrderType
	global Sell9OrderID
	global Sell9OrderStatus
	global Sell9OrderSide
	global Sell9cost
	global Sell9OrderType
	global Sell10OrderID
	global Sell10OrderStatus
	global Sell10OrderSide
	global Sell10cost
	global Sell10OrderType
	global Sell11OrderID
	global Sell11OrderStatus
	global Sell11OrderSide
	global Sell11cost
	global Sell11OrderType
	global Sell12OrderID
	global Sell12OrderStatus
	global Sell12OrderSide
	global Sell12cost
	global Sell12OrderType
	global Sell13OrderID
	global Sell13OrderStatus
	global Sell13OrderSide
	global Sell13cost
	global Sell13OrderType
	global Sell14OrderID
	global Sell14OrderStatus
	global Sell14OrderSide
	global Sell14cost
	global Sell14OrderType
	global Sell15OrderID
	global Sell15OrderStatus
	global Sell15OrderSide
	global Sell15cost
	global Sell15OrderType
	global Sell16OrderID
	global Sell16OrderStatus
	global Sell16OrderSide
	global Sell16cost
	global Sell16OrderType
	global Sell17OrderID
	global Sell17OrderStatus
	global Sell17OrderSide
	global Sell17cost
	global Sell17OrderType
	global Sell18OrderID
	global Sell18OrderStatus
	global Sell18OrderSide
	global Sell18cost
	global Sell18OrderType
	global Sell19OrderID
	global Sell19OrderStatus
	global Sell19OrderSide
	global Sell19cost
	global Sell19OrderType
	global Sell20OrderID
	global Sell20OrderStatus
	global Sell20OrderSide
	global Sell20cost
	global Sell20OrderType
	global Sell21OrderID
	global Sell21OrderStatus
	global Sell21OrderSide
	global Sell21cost
	global Sell21OrderType
	global Sell22OrderID
	global Sell22OrderStatus
	global Sell22OrderSide
	global Sell22cost
	global Sell22OrderType
	global Sell23OrderID
	global Sell23OrderStatus
	global Sell23OrderSide
	global Sell23cost
	global Sell23OrderType
	global Sell24OrderID
	global Sell24OrderStatus
	global Sell24OrderSide
	global Sell24cost
	global Sell24OrderType
	global Sell25OrderID
	global Sell25OrderStatus
	global Sell25OrderSide
	global Sell25cost
	global Sell25OrderType
	global Sell26OrderID
	global Sell26OrderStatus
	global Sell26OrderSide
	global Sell26cost
	global Sell26OrderType
	global Sell27OrderID
	global Sell27OrderStatus
	global Sell27OrderSide
	global Sell27cost
	global Sell27OrderType
	global Sell28OrderID
	global Sell28OrderStatus
	global Sell28OrderSide
	global Sell28cost
	global Sell28OrderType
	global Sell29OrderID
	global Sell29OrderStatus
	global Sell29OrderSide
	global Sell29cost
	global Sell29OrderType
	global Sell0OrderID
	global Sell0OrderStatus
	global Sell0OrderSide
	global Sell0cost
	global Sell0OrderType
	global Sell0OrderID
	global Sell0OrderStatus
	global Sell0OrderSide
	global Sell0cost
	global Sell0OrderType
	global Sell0OrderID
	global Sell0OrderStatus
	global Sell0OrderSide
	global Sell0cost
	global Sell0OrderType
	global Sell0OrderID
	global Sell0OrderStatus
	global Sell0OrderSide
	global Sell0cost
	global Sell0OrderType
	global Sell0OrderID
	global Sell0OrderStatus
	global Sell0OrderSide
	global Sell0cost
	global Sell0OrderType
	global AAAATestPrice
	global FirstIntiatedWalletBalance
	global StopBuyFunc
	global StopSellFunc
	global MovingGridUpBuy0
	global PostionFullInfo
	global PostionFullInfoRequest
	global GridBuy0ProfitFuncHandle
	global GridSell0ProfitFuncHandle
	global FirstIntiatedWalletBalanceIncreaseCount
	global MainPositionAmount
	global MainPostionSide
	global MainPostionProfit
	global MainPostionLiquidationPrice
	global MainPostionEntryPrice
	global doubledAcountAmount 
	global MainAccountProfitSinceGridStart
	global SN1M
	global MainPositionLiquidationPrice
	global MainPositionEntryPrice
	global MainPositionAmount
	global leverage
	global GridNumberCount
	global Buy0OrderID
	global PostionunRealizedProfit
	global OpenPriceTICKS
	global LastPriceTICKS
	global HighPriceTICKS
	global LowPriceTICKS
	global VolumePriceTICKSBTC
	global VolumePriceTICKSUSDT
	global BalanceRes
	global totalWalletBalance
	global totalUnrealizedProfitBalance
	global totalPositionInitialMargin
	global walletBalance
	global maxWithdrawAmount
	global BTCBalanceFree
	global FirstIntiatedWalletBalanceIncreaseCount
	global FirstIntiatedWalletBalance
	global RacingPriceFunc
	global HowManyTimesMoveFuncTriggeredSell
	global RealProfitWithUnRealizedProfit
	global AcualDollarMainAccountProfitSinceGridStart
	global SHORTGridWithIndicator
	global SHORTGridWithIndicator0
	global SHORTGridWithIndicator1
	global SHORTGridWithIndicator2
	global SHORTGridWithIndicator3
	global SHORTGridWithIndicator4
	global SHORTGridWithIndicator5
	global SHORTGridWithIndicator6
	global SHORTGridWithIndicator7
	global SHORTGridWithIndicator8
	global SHORTGridWithIndicator9
	global SHORTGridWithIndicator10
	global SHORTGridWithIndicator11
	global SHORTGridWithIndicator12
	global SHORTGridWithIndicator13
	global SHORTGridWithIndicator14
	global SHORTGridWithIndicator15
	global SHORTGridWithIndicator16
	global SHORTGridWithIndicator17
	global SHORTGridWithIndicator18
	global SHORTGridWithIndicator19
	global SHORTGridWithIndicator20
	global SHORTGridWithIndicator21
	global SHORTGridWithIndicator22
	global SHORTGridWithIndicator23
	global SHORTGridWithIndicator24
	global SHORTGridWithIndicator25
	global SHORTGridWithIndicator26
	global SHORTGridWithIndicator27
	global SHORTGridWithIndicator28
	global SHORTGridWithIndicator29
	global SHORTGridWithIndicator30
	global LongGridWithIndicator0
	global LongGridWithIndicator1
	global LongGridWithIndicator2
	global LongGridWithIndicator3
	global LongGridWithIndicator4
	global LongGridWithIndicator5
	global LongGridWithIndicator6
	global LongGridWithIndicator7
	global LongGridWithIndicator8
	global LongGridWithIndicator9
	global LongGridWithIndicator10
	global LongGridWithIndicator11
	global LongGridWithIndicator12
	global LongGridWithIndicator13
	global LongGridWithIndicator14
	global LongGridWithIndicator15
	global LongGridWithIndicator16
	global LongGridWithIndicator17
	global LongGridWithIndicator18
	global LongGridWithIndicator19
	global LongGridWithIndicator20
	global LongGridWithIndicator21
	global LongGridWithIndicator22
	global LongGridWithIndicator23
	global LongGridWithIndicator24
	global LongGridWithIndicator25
	global LongGridWithIndicator26
	global LongGridWithIndicator27
	global LongGridWithIndicator28
	global LongGridWithIndicator29
	global LongGridWithIndicator30
	global ProfitPercentDynamic0 
	global ProfitPercentDynamic1 
	global ProfitPercentDynamic2 
	global ProfitPercentDynamic3 
	global ProfitPercentDynamic4 
	global ProfitPercentDynamic5 
	global ProfitPercentDynamic6 
	global ProfitPercentDynamic7 
	global ProfitPercentDynamic8 
	global ProfitPercentDynamic9 
	global ProfitPercentDynamic10
	global ProfitPercentDynamic11
	global ProfitPercentDynamic12
	global ProfitPercentDynamic13
	global ProfitPercentDynamic14
	global ProfitPercentDynamic15
	global ProfitPercentDynamic16
	global ProfitPercentDynamic17
	global ProfitPercentDynamic18
	global ProfitPercentDynamic19
	global ProfitPercentDynamic20
	global ProfitPercentDynamic21
	global ProfitPercentDynamic22
	global ProfitPercentDynamic23
	global ProfitPercentDynamic24
	global ProfitPercentDynamic25
	global ProfitPercentDynamic26
	global ProfitPercentDynamic27
	global ProfitPercentDynamic28
	global ProfitPercentDynamic29
	global ProfitPercentDynamic30
	global lockProfit1
	global lockProfit2
	global lockProfit3
	global lockProfit4
	global lockProfit5
	global lockProfit6
	global lockProfit7
	global lockProfit8
	global lockProfit9
	global lockProfit10
	global lockProfit11
	global lockProfit12
	global lockProfit13
	global lockProfit14
	global lockProfit15
	global lockProfit16
	global lockProfit17
	global lockProfit18
	global lockProfit19
	global lockProfit20
	global lockProfit21
	global GridBuyProfit0PriceCount 
	global GridBuyProfit1PriceCount 
	global GridBuyProfit2PriceCount 
	global GridBuyProfit3PriceCount 
	global GridBuyProfit4PriceCount 
	global GridBuyProfit5PriceCount 
	global GridBuyProfit6PriceCount 
	global GridBuyProfit7PriceCount 
	global GridBuyProfit8PriceCount 
	global GridBuyProfit9PriceCount 
	global GridBuyProfit10PriceCount
	global GridBuyProfit11PriceCount
	global GridBuyProfit12PriceCount
	global GridBuyProfit13PriceCount
	global GridBuyProfit14PriceCount
	global GridBuyProfit15PriceCount
	global GridBuyProfit16PriceCount
	global GridBuyProfit17PriceCount
	global GridBuyProfit18PriceCount
	global GridBuyProfit19PriceCount
	global GridBuyProfit20PriceCount
	global GridBuyProfit21PriceCount
	global GridBuyProfit22PriceCount
	global GridBuyProfit23PriceCount
	global GridBuyProfit24PriceCount
	global GridBuyProfit25PriceCount
	global GridBuyProfit26PriceCount
	global GridBuyProfit27PriceCount
	global GridBuyProfit28PriceCount
	global GridBuyProfit29PriceCount
	global GridBuyProfit30PriceCount
	global PreviousGridBuyProfit0Price 
	global PreviousGridBuyProfit1Price 
	global PreviousGridBuyProfit2Price 
	global PreviousGridBuyProfit3Price 
	global PreviousGridBuyProfit4Price 
	global PreviousGridBuyProfit5Price 
	global PreviousGridBuyProfit6Price 
	global PreviousGridBuyProfit7Price 
	global PreviousGridBuyProfit8Price 
	global PreviousGridBuyProfit9Price 
	global PreviousGridBuyProfit10Price
	global PreviousGridBuyProfit11Price
	global PreviousGridBuyProfit12Price
	global PreviousGridBuyProfit13Price
	global PreviousGridBuyProfit14Price
	global PreviousGridBuyProfit15Price
	global PreviousGridBuyProfit16Price
	global PreviousGridBuyProfit17Price
	global PreviousGridBuyProfit18Price
	global PreviousGridBuyProfit19Price
	global PreviousGridBuyProfit20Price
	global PreviousGridBuyProfit21Price
	global PreviousGridBuyProfit22Price
	global PreviousGridBuyProfit23Price
	global PreviousGridBuyProfit24Price
	global PreviousGridBuyProfit25Price
	global PreviousGridBuyProfit26Price
	global PreviousGridBuyProfit27Price
	global PreviousGridBuyProfit28Price
	global PreviousGridBuyProfit29Price
	global PreviousGridBuyProfit30Price
	global LOCKPreviousGridBuyProfit0Price 
	global LOCKPreviousGridBuyProfit1Price 
	global LOCKPreviousGridBuyProfit2Price 
	global LOCKPreviousGridBuyProfit3Price 
	global LOCKPreviousGridBuyProfit4Price 
	global LOCKPreviousGridBuyProfit5Price 
	global LOCKPreviousGridBuyProfit6Price 
	global LOCKPreviousGridBuyProfit7Price 
	global LOCKPreviousGridBuyProfit8Price 
	global LOCKPreviousGridBuyProfit9Price 
	global LOCKPreviousGridBuyProfit10Price
	global LOCKPreviousGridBuyProfit11Price
	global LOCKPreviousGridBuyProfit12Price
	global LOCKPreviousGridBuyProfit13Price
	global LOCKPreviousGridBuyProfit14Price
	global LOCKPreviousGridBuyProfit15Price
	global LOCKPreviousGridBuyProfit16Price
	global LOCKPreviousGridBuyProfit17Price
	global LOCKPreviousGridBuyProfit18Price
	global LOCKPreviousGridBuyProfit19Price
	global LOCKPreviousGridBuyProfit20Price
	global LOCKPreviousGridBuyProfit21Price
	global LOCKPreviousGridBuyProfit22Price
	global LOCKPreviousGridBuyProfit23Price
	global LOCKPreviousGridBuyProfit24Price
	global LOCKPreviousGridBuyProfit25Price
	global LOCKPreviousGridBuyProfit26Price
	global LOCKPreviousGridBuyProfit27Price
	global LOCKPreviousGridBuyProfit28Price
	global LOCKPreviousGridBuyProfit29Price
	global LOCKPreviousGridBuyProfit30Price
	global GridSellProfit0PriceCount 
	global GridSellProfit1PriceCount 
	global GridSellProfit2PriceCount 
	global GridSellProfit3PriceCount 
	global GridSellProfit4PriceCount 
	global GridSellProfit5PriceCount 
	global GridSellProfit6PriceCount 
	global GridSellProfit7PriceCount 
	global GridSellProfit8PriceCount 
	global GridSellProfit9PriceCount 
	global GridSellProfit10PriceCount
	global GridSellProfit11PriceCount
	global GridSellProfit12PriceCount
	global GridSellProfit13PriceCount
	global GridSellProfit14PriceCount
	global GridSellProfit15PriceCount
	global GridSellProfit16PriceCount
	global GridSellProfit17PriceCount
	global GridSellProfit18PriceCount
	global GridSellProfit19PriceCount
	global GridSellProfit20PriceCount
	global GridSellProfit21PriceCount
	global GridSellProfit22PriceCount
	global GridSellProfit23PriceCount
	global GridSellProfit24PriceCount
	global GridSellProfit25PriceCount
	global GridSellProfit26PriceCount
	global GridSellProfit27PriceCount
	global GridSellProfit28PriceCount
	global GridSellProfit29PriceCount
	global GridSellProfit30PriceCount
	global PreviousGridSellProfit0Price 
	global PreviousGridSellProfit1Price 
	global PreviousGridSellProfit2Price 
	global PreviousGridSellProfit3Price 
	global PreviousGridSellProfit4Price 
	global PreviousGridSellProfit5Price 
	global PreviousGridSellProfit6Price 
	global PreviousGridSellProfit7Price 
	global PreviousGridSellProfit8Price 
	global PreviousGridSellProfit9Price 
	global PreviousGridSellProfit10Price
	global PreviousGridSellProfit11Price
	global PreviousGridSellProfit12Price
	global PreviousGridSellProfit13Price
	global PreviousGridSellProfit14Price
	global PreviousGridSellProfit15Price
	global PreviousGridSellProfit16Price
	global PreviousGridSellProfit17Price
	global PreviousGridSellProfit18Price
	global PreviousGridSellProfit19Price
	global PreviousGridSellProfit20Price
	global PreviousGridSellProfit21Price
	global PreviousGridSellProfit22Price
	global PreviousGridSellProfit23Price
	global PreviousGridSellProfit24Price
	global PreviousGridSellProfit25Price
	global PreviousGridSellProfit26Price
	global PreviousGridSellProfit27Price
	global PreviousGridSellProfit28Price
	global PreviousGridSellProfit29Price
	global PreviousGridSellProfit30Price
	global LOCKPreviousGridSellProfit0Price 
	global LOCKPreviousGridSellProfit1Price 
	global LOCKPreviousGridSellProfit2Price 
	global LOCKPreviousGridSellProfit3Price 
	global LOCKPreviousGridSellProfit4Price 
	global LOCKPreviousGridSellProfit5Price 
	global LOCKPreviousGridSellProfit6Price 
	global LOCKPreviousGridSellProfit7Price 
	global LOCKPreviousGridSellProfit8Price 
	global LOCKPreviousGridSellProfit9Price 
	global LOCKPreviousGridSellProfit10Price
	global LOCKPreviousGridSellProfit11Price
	global LOCKPreviousGridSellProfit12Price
	global LOCKPreviousGridSellProfit13Price
	global LOCKPreviousGridSellProfit14Price
	global LOCKPreviousGridSellProfit15Price
	global LOCKPreviousGridSellProfit16Price
	global LOCKPreviousGridSellProfit17Price
	global LOCKPreviousGridSellProfit18Price
	global LOCKPreviousGridSellProfit19Price
	global LOCKPreviousGridSellProfit20Price
	global LOCKPreviousGridSellProfit21Price
	global LOCKPreviousGridSellProfit22Price
	global LOCKPreviousGridSellProfit23Price
	global LOCKPreviousGridSellProfit24Price
	global LOCKPreviousGridSellProfit25Price
	global LOCKPreviousGridSellProfit26Price
	global LOCKPreviousGridSellProfit27Price
	global LOCKPreviousGridSellProfit28Price
	global LOCKPreviousGridSellProfit29Price
	global LOCKPreviousGridSellProfit30Price
	global MACDType
	global BotType
	global GlobalProfit
	global DynamicFirstIntiatedWalletBalanceForGrid
	global GridCountToRestTheDynProfirForGrid
	global DynamicFirstIntiatedWalletBalanceForAmountPostion
	global SecondPostionSizeAccordingtoIndicator
	global PercentBetweenFirstBalanceAndCurrentBalance
	global LongerTimeFrame
	global ShorterTimeFrame

	
	try:
		TickersInfo=binance.fetchTicker (symbol)
		OpenPriceTICKS=TickersInfo.get("open")
		LastPriceTICKS=TickersInfo.get("last")
		HighPriceTICKS=TickersInfo.get("high")
		LowPriceTICKS=TickersInfo.get("low")
		VolumePriceTICKSBTC=TickersInfo.get("baseVolume")
		VolumePriceTICKSUSDT=(VolumePriceTICKSBTC*LastPriceTICKS)/1000000
		BalanceRes = binance.fetchBalance ()
		# print(BalanceRes)
		totalWalletBalance=BalanceRes.get("info").get("totalWalletBalance")
		totalWalletBalance=float(totalWalletBalance)
		totalUnrealizedProfitBalance=BalanceRes.get("info").get("totalUnrealizedProfit")
		totalPositionInitialMargin=BalanceRes.get("info").get("totalPositionInitialMargin")
		walletBalance=BalanceRes.get("info").get("walletBalance")
		maxWithdrawAmount=BalanceRes.get("info").get("maxWithdrawAmount")
		BTCBalanceFree=totalWalletBalance
		if(FirstIntiatedWalletBalanceIncreaseCount==0):
			FirstIntiatedWalletBalance=totalWalletBalance
			DynamicFirstIntiatedWalletBalanceForGrid=totalWalletBalance
			DynamicFirstIntiatedWalletBalanceForAmountPostion=totalWalletBalance
			FirstIntiatedWalletBalanceIncreaseCount=FirstIntiatedWalletBalanceIncreaseCount+1
		

		
		
		if(Subject=="LONGFRAME"):
			LongerTimeFrame="LONG"
		if(Subject=="SHORTFRAME"):
			LongerTimeFrame="SHORTNOTRADE"	
		
		def grid0BuyFunc():
			global LongGridWithIndicator0
			global TradedamountBuy0
			global GridBuy0ProfitFuncHandle
			global Buy0OrderID
			global Buy0OrderStatus
			global GridBuyProfit0Price
			global Buy0ProfitOrderStatus
			global GridBuyFlag0
			global GridBuy0Func
			global grid0BuyPrice
			Buy0ProfitOrderStatus="NONE"
			Buy0OrderStatus="NONE"
			Ordertype='Buy'
			Orderside='limit'
			grid0BuyPrice=LastPriceTICKS +1
			Orderprice=grid0BuyPrice
			TradedamountBuy0 = (((DynamicFirstIntiatedWalletBalanceForAmountPostion/PostionSizeAccordingtoIndicator)*Margin) / grid0BuyPrice  )
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy0
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator0=1 
			PositionPriceIndollars=(grid0BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			GridBuy0Func=1
			GridBuy0ProfitFuncHandle=0
			CheckPostionInfo=binance.fapiPrivateGetPositionRisk()
			a=(CheckPostionInfo[0].get('entryPrice'))
			b=(CheckPostionInfo[0].get('positionAmt'))
			a=int(float(a))
			b=int(float(b))
			c=a
			if(a==0 and b==0):
				FullOpenOrderDetailsRAW=binance.fetchOpenOrders(symbol)
				FullOpenOrderDetailsLength=len(FullOpenOrderDetailsRAW)
				FullOpenOrderDetailsLength=int(FullOpenOrderDetailsLength)
				Buy0OrderID=FullOpenOrderDetailsRAW[0]["info"]['orderId']
				Buy0OrderID=int(Buy0OrderID)
			if(c!=0 ):
				Buy0OrderID=binance.fetchClosedOrders(symbol = symbol)[-1].get("id")
				Buy0OrderID=int(Buy0OrderID)
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> TradedamountBuy0 NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree,"Buy0OrderID",Buy0OrderID)
		
		
		if(Buy0OrderID!=0):
			Buy0OrderStatus	=binance.fetchOrder(Buy0OrderID,  symbol = symbol).get("status")
		
		if(Buy0OrderStatus =="closed"	 and  grid0BuyPrice	 !=0  and TradedamountBuy0 !=0	):
			GridBuyFlag0=1
			
			
			
		def grid1BuyFunc():
			global LongGridWithIndicator1
			global grid1BuyPrice
			grid1BuyPrice=LastPriceTICKS +1	
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid1BuyPrice
			global TradedamountBuy1
			TradedamountBuy1 =( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid1BuyPrice	)
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy1
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator1=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid1BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy1Func
			global Buy1OrderID
			global Buy1OrderStatus
			GridBuy1Func=1
	
			
			
		def grid2BuyFunc():
			global LongGridWithIndicator2
			global grid2BuyPrice
			grid2BuyPrice=LastPriceTICKS +1		
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid2BuyPrice
			global TradedamountBuy2
			global Buy2OrderID
			global Buy2OrderStatus
			TradedamountBuy2 =( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid2BuyPrice	)
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy2
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator2=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid2BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy2Func
			GridBuy2Func=1
	
			
		def grid3BuyFunc():
			global LongGridWithIndicator3
			global grid3BuyPrice
			grid3BuyPrice=LastPriceTICKS +1		
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid3BuyPrice
			global TradedamountBuy3
			global Buy3OrderID
			global Buy3OrderStatus
			TradedamountBuy3 =( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid3BuyPrice	)
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy3
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator3=1
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid3BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy3Func
			GridBuy3Func=1
	
			
		def grid4BuyFunc():
			global LongGridWithIndicator4
			global grid4BuyPrice
			grid4BuyPrice=LastPriceTICKS +1		
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid4BuyPrice
			global TradedamountBuy4
			global Buy4OrderID
			global Buy4OrderStatus
			TradedamountBuy4 =( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid4BuyPrice	)
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy4
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator4=1
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid4BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy4Func
			GridBuy4Func=1
	
			
		def grid5BuyFunc():
			global LongGridWithIndicator5
			global grid5BuyPrice
			grid5BuyPrice=LastPriceTICKS +1		
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid5BuyPrice
			global TradedamountBuy5
			global Buy5OrderID
			global Buy5OrderStatus
			TradedamountBuy5 =( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid5BuyPrice	)
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy5
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator5=1
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid5BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy5Func
			GridBuy5Func=1
		
			
		def grid6BuyFunc():
			global LongGridWithIndicator6
			global grid6BuyPrice
			grid6BuyPrice=LastPriceTICKS +1		
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid6BuyPrice
			global TradedamountBuy6
			global Buy6OrderID
			global Buy6OrderStatus
			TradedamountBuy6 =( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid6BuyPrice	)
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy6
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator6=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid6BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			global GridBuy6Func			
			GridBuy6Func=1
		
			
		def grid7BuyFunc():
			global LongGridWithIndicator7
			global grid7BuyPrice
			grid7BuyPrice=LastPriceTICKS +1		
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid7BuyPrice
			global TradedamountBuy7
			global Buy7OrderID
			global Buy7OrderStatus
			TradedamountBuy7 =( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid7BuyPrice	)
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy7
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator7=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid7BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy7Func
			GridBuy7Func=1
	
			
		def grid8BuyFunc():
			global LongGridWithIndicator8
			global grid8BuyPrice
			grid8BuyPrice=LastPriceTICKS +1		
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid8BuyPrice
			global TradedamountBuy8
			global Buy8OrderID
			global Buy8OrderStatus
			TradedamountBuy8 =( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid8BuyPrice	)
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy8
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator8=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid8BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy8Func
			GridBuy8Func=1
		
			
		def grid9BuyFunc():
			global LongGridWithIndicator9
			global grid9BuyPrice
			grid9BuyPrice=LastPriceTICKS +1		
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid9BuyPrice
			global TradedamountBuy9
			global Buy9OrderID
			global Buy9OrderStatus
			TradedamountBuy9 =( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid9BuyPrice	)
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy9
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator9=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid9BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy9Func
			GridBuy9Func=1
		
			
		def grid10BuyFunc():
			global LongGridWithIndicator10
			global grid10BuyPrice
			grid10BuyPrice=LastPriceTICKS +1		
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid10BuyPrice
			global TradedamountBuy10
			global Buy10OrderID
			global Buy10OrderStatus
			TradedamountBuy10=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid10BuyPrice )
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy10
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator10=1
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid10BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy10Func
			GridBuy10Func=1
		
			
		def grid11BuyFunc():
			global LongGridWithIndicator11
			global grid11BuyPrice
			grid11BuyPrice=LastPriceTICKS +1		
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid11BuyPrice
			global TradedamountBuy11
			global Buy11OrderID
			global Buy11OrderStatus
			TradedamountBuy11=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid11BuyPrice )
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy11
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator11=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid11BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy11Func
			GridBuy11Func=1
		
			
		def grid12BuyFunc():
			global LongGridWithIndicator12
			global grid12BuyPrice
			grid12BuyPrice=LastPriceTICKS +1		
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid12BuyPrice
			global TradedamountBuy12
			global Buy12OrderID
			global Buy12OrderStatus
			TradedamountBuy12=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid12BuyPrice )
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy12
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator12=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid12BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy12Func
			GridBuy12Func=1
			
			
		def grid13BuyFunc():
			global LongGridWithIndicator13
			global grid13BuyPrice
			grid13BuyPrice=LastPriceTICKS +1		
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid13BuyPrice
			global TradedamountBuy13
			global Buy13OrderID
			global Buy13OrderStatus
			TradedamountBuy13=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid13BuyPrice )
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy13
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator13=1
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid13BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy13Func
			GridBuy13Func=1
			
			
		def grid14BuyFunc():
			global LongGridWithIndicator14
			global grid14BuyPrice
			grid14BuyPrice=LastPriceTICKS +1		
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid14BuyPrice
			global TradedamountBuy14
			global Buy14OrderID
			global Buy14OrderStatus
			TradedamountBuy14=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid14BuyPrice )
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy14
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator14=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid14BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy14Func
			GridBuy14Func=1
		
			
		def grid15BuyFunc():
			global LongGridWithIndicator15
			global grid15BuyPrice
			grid15BuyPrice=LastPriceTICKS +1		
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid15BuyPrice
			global TradedamountBuy15
			global Buy15OrderID
			global Buy15OrderStatus
			TradedamountBuy15=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid15BuyPrice )
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy15
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator15=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid15BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy15Func
			GridBuy15Func=1
		
			
		def grid16BuyFunc():
			global LongGridWithIndicator16
			global grid16BuyPrice
			grid16BuyPrice=LastPriceTICKS +1		
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid16BuyPrice
			global TradedamountBuy16
			global Buy16OrderID
			global Buy16OrderStatus
			TradedamountBuy16=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid16BuyPrice )
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy16
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator16=1
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid16BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy16Func
			GridBuy16Func=1
		
			
		def grid17BuyFunc():
			global LongGridWithIndicator17
			global grid17BuyPrice
			grid17BuyPrice=LastPriceTICKS	 +2	
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid17BuyPrice
			global TradedamountBuy17
			global Buy17OrderID
			global Buy17OrderStatus
			TradedamountBuy17=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid17BuyPrice )
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy17
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator17=1
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid17BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy17Func
			GridBuy17Func=1
		
			
		def grid18BuyFunc():
			global LongGridWithIndicator18
			global grid18BuyPrice
			grid18BuyPrice=LastPriceTICKS +1		
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid18BuyPrice
			global TradedamountBuy18
			global Buy18OrderID
			global Buy18OrderStatus
			TradedamountBuy18=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid18BuyPrice )
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy18
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator18=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid18BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy18Func
			GridBuy18Func=1
		
			
		def grid19BuyFunc():
			global LongGridWithIndicator19
			global grid19BuyPrice
			grid19BuyPrice=LastPriceTICKS	 +2	
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid19BuyPrice
			global TradedamountBuy19
			global Buy19OrderID
			global Buy19OrderStatus
			TradedamountBuy19=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid19BuyPrice )
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy19
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator19=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid19BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy19Func
			GridBuy19Func=1
		
			
		def grid20BuyFunc():
			global LongGridWithIndicator20
			global grid20BuyPrice
			grid20BuyPrice=LastPriceTICKS	 +2	
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid20BuyPrice
			global TradedamountBuy20
			global Buy20OrderID
			global Buy20OrderStatus
			TradedamountBuy20=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid20BuyPrice )
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy20
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator20=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid20BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy20Func
			GridBuy20Func=1
			
			
		def grid21BuyFunc():
			global LongGridWithIndicator21
			global grid21BuyPrice
			grid21BuyPrice=LastPriceTICKS	 +2	
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid21BuyPrice
			global TradedamountBuy21
			global Buy21OrderID
			global Buy21OrderStatus
			TradedamountBuy21=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid21BuyPrice )
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy21
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator21=1
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid21BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy21Func
			GridBuy21Func=1
		
			
		def grid22BuyFunc():
			global LongGridWithIndicator22
			global grid22BuyPrice
			grid22BuyPrice=LastPriceTICKS	 +2	
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid22BuyPrice
			global TradedamountBuy22
			global Buy22OrderID
			global Buy22OrderStatus
			TradedamountBuy22=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid22BuyPrice )
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy22
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator22=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid22BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy22Func
			GridBuy22Func=1
		
			
		def grid23BuyFunc():
			global LongGridWithIndicator23
			global grid23BuyPrice
			grid23BuyPrice=LastPriceTICKS	 +2	
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid23BuyPrice
			global TradedamountBuy23
			global Buy23OrderID
			global Buy23OrderStatus
			TradedamountBuy23=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid23BuyPrice )
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy23
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator23=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid23BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy23Func
			GridBuy23Func=1
		
			
		def grid24BuyFunc():
			global LongGridWithIndicator24
			global grid24BuyPrice
			grid24BuyPrice=LastPriceTICKS +1		
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid24BuyPrice
			global TradedamountBuy24
			global Buy24OrderID
			global Buy24OrderStatus
			TradedamountBuy24=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid24BuyPrice )
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy24
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator24=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid24BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy24Func
			GridBuy24Func=1
		
			
		def grid25BuyFunc():
			global LongGridWithIndicator25
			global grid25BuyPrice
			grid25BuyPrice=LastPriceTICKS	 +2	
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid25BuyPrice
			global TradedamountBuy25
			global Buy25OrderID
			global Buy25OrderStatus
			TradedamountBuy25=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid25BuyPrice )
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy25
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator25=1
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid25BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy25Func
			GridBuy25Func=1
		
			
		def grid26BuyFunc():
			global LongGridWithIndicator26
			global grid26BuyPrice
			grid26BuyPrice=LastPriceTICKS	 +2	
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid26BuyPrice
			global TradedamountBuy26
			global Buy26OrderID
			global Buy26OrderStatus
			TradedamountBuy26=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid26BuyPrice )
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy26
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator26=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid26BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy26Func
			GridBuy26Func=1
		
			
		def grid27BuyFunc():
			global LongGridWithIndicator27
			global grid27BuyPrice
			grid27BuyPrice=LastPriceTICKS	 +2	
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid27BuyPrice
			global TradedamountBuy27
			global Buy27OrderID
			global Buy27OrderStatus
			TradedamountBuy27=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid27BuyPrice )
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy27
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator27=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid27BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy27Func
			GridBuy27Func=1
	
			
		def grid28BuyFunc():
			global LongGridWithIndicator28
			global grid28BuyPrice
			grid28BuyPrice=LastPriceTICKS	 +2	
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid28BuyPrice
			global TradedamountBuy28
			global Buy28OrderID
			global Buy28OrderStatus
			TradedamountBuy28=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid28BuyPrice )
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy28
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator28=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid28BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridBuy28Func
			GridBuy28Func=1
		
			
		def grid29BuyFunc():
			global LongGridWithIndicator29
			global grid29BuyPrice
			grid29BuyPrice=LastPriceTICKS	 +2	
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid29BuyPrice
			global TradedamountBuy29
			global Buy29OrderID
			global Buy29OrderStatus
			TradedamountBuy29=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid29BuyPrice )
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy29
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator29=1
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid29BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			global	GridBuy29Func		
			GridBuy29Func=1
		
			
		def grid30BuyFunc():
			global LongGridWithIndicator30
			global grid30BuyPrice
			grid30BuyPrice=LastPriceTICKS	 +2	
			Ordertype='Buy'
			Orderside='limit'
			Orderprice=grid30BuyPrice
			global TradedamountBuy30
			global Buy30OrderID
			global Buy30OrderStatus
			TradedamountBuy30=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid30BuyPrice )
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountBuy30
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			LongGridWithIndicator30=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid30BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			global	GridBuy30Func
			GridBuy30Func=1
		

		
		def grid0SellFunc():
			global SHORTGridWithIndicator0
			global TradedamountSell0
			global GridSell0ProfitFuncHandle
			global Sell0OrderID
			global Sell0OrderStatus
			global GridSellProfit0Price
			global Sell0ProfitOrderStatus
			global GridSellFlag0
			global GridSell0Func
			global grid0SellPrice
			Sell0ProfitOrderStatus="NONE"
			Sell0OrderStatus="NONE"
			Ordertype='Sell'
			Orderside='limit'
			grid0SellPrice=LastPriceTICKS
			Orderprice=grid0SellPrice
			TradedamountSell0 = (((DynamicFirstIntiatedWalletBalanceForAmountPostion/PostionSizeAccordingtoIndicator)*Margin) / grid0SellPrice	 )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell0
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator0=1 
			PositionPriceIndollars=(grid0SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			GridSell0Func=1
			GridSell0ProfitFuncHandle=0
			CheckPostionInfo=binance.fapiPrivateGetPositionRisk()
			a=(CheckPostionInfo[0].get('entryPrice'))
			b=(CheckPostionInfo[0].get('positionAmt'))
			a=int(float(a))
			b=int(float(b))
			c=a
			if(a==0 and b==0):
				FullOpenOrderDetailsRAW=binance.fetchOpenOrders(symbol)
				FullOpenOrderDetailsLength=len(FullOpenOrderDetailsRAW)
				FullOpenOrderDetailsLength=int(FullOpenOrderDetailsLength)
				Sell0OrderID=FullOpenOrderDetailsRAW[0]["info"]['orderId']
				Sell0OrderID=int(Sell0OrderID)
			if(c!=0 ):
				Sell0OrderID=binance.fetchClosedOrders(symbol = symbol)[-1].get("id")
				Sell0OrderID=int(Sell0OrderID)
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> TradedamountSell0 NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree,"Sell0OrderID",Sell0OrderID)
		
		
		if(Sell0OrderID!=0):
			Sell0OrderStatus	=binance.fetchOrder(Sell0OrderID,  symbol = symbol).get("status")
		
		if(Sell0OrderStatus =="closed"	 and  grid0SellPrice	 !=0  and TradedamountSell0 !=0	):
			GridSellFlag0=1
			
			
			
		def grid1SellFunc():
			global SHORTGridWithIndicator1
			global grid1SellPrice
			grid1SellPrice=LastPriceTICKS	-2
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid1SellPrice
			global TradedamountSell1
			TradedamountSell1 =( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid1SellPrice	 )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell1
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator1=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid1SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell1Func
			global Sell1OrderID
			global Sell1OrderStatus
			GridSell1Func=1
	
			
			
		def grid2SellFunc():
			global SHORTGridWithIndicator2
			global grid2SellPrice
			grid2SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid2SellPrice
			global TradedamountSell2
			global Sell2OrderID
			global Sell2OrderStatus
			TradedamountSell2 =( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid2SellPrice	 )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell2
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator2=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid2SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell2Func
			GridSell2Func=1
	
			
		def grid3SellFunc():
			global SHORTGridWithIndicator3
			global grid3SellPrice
			grid3SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid3SellPrice
			global TradedamountSell3
			global Sell3OrderID
			global Sell3OrderStatus
			TradedamountSell3 =( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid3SellPrice	 )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell3
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator3=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid3SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell3Func
			GridSell3Func=1
	
			
		def grid4SellFunc():
			global SHORTGridWithIndicator4
			global grid4SellPrice
			grid4SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid4SellPrice
			global TradedamountSell4
			global Sell4OrderID
			global Sell4OrderStatus
			TradedamountSell4 =( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid4SellPrice	 )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell4
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator4=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid4SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell4Func
			GridSell4Func=1
	
			
		def grid5SellFunc():
			global SHORTGridWithIndicator5
			global grid5SellPrice
			grid5SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid5SellPrice
			global TradedamountSell5
			global Sell5OrderID
			global Sell5OrderStatus
			TradedamountSell5 =( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid5SellPrice	 )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell5
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator5=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid5SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell5Func
			GridSell5Func=1
		
			
		def grid6SellFunc():
			global SHORTGridWithIndicator6
			global grid6SellPrice
			grid6SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid6SellPrice
			global TradedamountSell6
			global Sell6OrderID
			global Sell6OrderStatus
			TradedamountSell6 =( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid6SellPrice	 )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell6
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator6=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid6SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			global GridSell6Func			
			GridSell6Func=1
		
			
		def grid7SellFunc():
			global SHORTGridWithIndicator7
			global grid7SellPrice
			grid7SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid7SellPrice
			global TradedamountSell7
			global Sell7OrderID
			global Sell7OrderStatus
			TradedamountSell7 =( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid7SellPrice	 )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell7
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator7=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid7SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell7Func
			GridSell7Func=1
	
			
		def grid8SellFunc():
			global SHORTGridWithIndicator8
			global grid8SellPrice
			grid8SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid8SellPrice
			global TradedamountSell8
			global Sell8OrderID
			global Sell8OrderStatus
			TradedamountSell8 =( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid8SellPrice	 )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell8
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator8=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid8SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell8Func
			GridSell8Func=1
		
			
		def grid9SellFunc():
			global SHORTGridWithIndicator9
			global grid9SellPrice
			grid9SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid9SellPrice
			global TradedamountSell9
			global Sell9OrderID
			global Sell9OrderStatus
			TradedamountSell9 =( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid9SellPrice	 )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell9
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator9=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid9SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell9Func
			GridSell9Func=1
		
			
		def grid10SellFunc():
			global SHORTGridWithIndicator10
			global grid10SellPrice
			grid10SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid10SellPrice
			global TradedamountSell10
			global Sell10OrderID
			global Sell10OrderStatus
			TradedamountSell10=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid10SellPrice )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell10
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator10=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid10SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell10Func
			GridSell10Func=1
		
			
		def grid11SellFunc():
			global SHORTGridWithIndicator11
			global grid11SellPrice
			grid11SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid11SellPrice
			global TradedamountSell11
			global Sell11OrderID
			global Sell11OrderStatus
			TradedamountSell11=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid11SellPrice )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell11
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator11=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid11SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell11Func
			GridSell11Func=1
		
			
		def grid12SellFunc():
			global SHORTGridWithIndicator12
			global grid12SellPrice
			grid12SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid12SellPrice
			global TradedamountSell12
			global Sell12OrderID
			global Sell12OrderStatus
			TradedamountSell12=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid12SellPrice )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell12
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator12=1
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid12SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell12Func
			GridSell12Func=1
			
			
		def grid13SellFunc():
			global SHORTGridWithIndicator13
			global grid13SellPrice
			grid13SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid13SellPrice
			global TradedamountSell13
			global Sell13OrderID
			global Sell13OrderStatus
			TradedamountSell13=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid13SellPrice )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell13
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator13=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid13SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell13Func
			GridSell13Func=1
			
			
		def grid14SellFunc():
			global SHORTGridWithIndicator14
			global grid14SellPrice
			grid14SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid14SellPrice
			global TradedamountSell14
			global Sell14OrderID
			global Sell14OrderStatus
			TradedamountSell14=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid14SellPrice )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell14
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator14=1
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid14SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell14Func
			GridSell14Func=1
		
			
		def grid15SellFunc():
			global SHORTGridWithIndicator15
			global grid15SellPrice
			grid15SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid15SellPrice
			global TradedamountSell15
			global Sell15OrderID
			global Sell15OrderStatus
			TradedamountSell15=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid15SellPrice )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell15
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator15=1
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid15SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell15Func
			GridSell15Func=1
		
			
		def grid16SellFunc():
			global SHORTGridWithIndicator16
			global grid16SellPrice
			grid16SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid16SellPrice
			global TradedamountSell16
			global Sell16OrderID
			global Sell16OrderStatus
			TradedamountSell16=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid16SellPrice )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell16
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator16=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid16SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell16Func
			GridSell16Func=1
		
			
		def grid17SellFunc():
			global SHORTGridWithIndicator17
			global grid17SellPrice
			grid17SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid17SellPrice
			global TradedamountSell17
			global Sell17OrderID
			global Sell17OrderStatus
			TradedamountSell17=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid17SellPrice )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell17
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator17=1
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid17SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell17Func
			GridSell17Func=1
		
			
		def grid18SellFunc():
			global SHORTGridWithIndicator18
			global grid18SellPrice
			grid18SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid18SellPrice
			global TradedamountSell18
			global Sell18OrderID
			global Sell18OrderStatus
			TradedamountSell18=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid18SellPrice )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell18
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator18=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid18SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell18Func
			GridSell18Func=1
		
			
		def grid19SellFunc():
			global SHORTGridWithIndicator19
			global grid19SellPrice
			grid19SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid19SellPrice
			global TradedamountSell19
			global Sell19OrderID
			global Sell19OrderStatus
			TradedamountSell19=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid19SellPrice )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell19
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator19=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid19SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell19Func
			GridSell19Func=1
		
			
		def grid20SellFunc():
			global SHORTGridWithIndicator20
			global grid20SellPrice
			grid20SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid20SellPrice
			global TradedamountSell20
			global Sell20OrderID
			global Sell20OrderStatus
			TradedamountSell20=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid20SellPrice )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell20
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator20=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid20SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell20Func
			GridSell20Func=1
			
			
		def grid21SellFunc():
			global SHORTGridWithIndicator21
			global grid21SellPrice
			grid21SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid21SellPrice
			global TradedamountSell21
			global Sell21OrderID
			global Sell21OrderStatus
			TradedamountSell21=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid21SellPrice )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell21
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator21=1
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid21SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell21Func
			GridSell21Func=1
		
			
		def grid22SellFunc():
			global SHORTGridWithIndicator22
			global grid22SellPrice
			grid22SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid22SellPrice
			global TradedamountSell22
			global Sell22OrderID
			global Sell22OrderStatus
			TradedamountSell22=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid22SellPrice )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell22
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator22=1
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid22SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell22Func
			GridSell22Func=1
		
			
		def grid23SellFunc():
			global SHORTGridWithIndicator23
			global grid23SellPrice
			grid23SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid23SellPrice
			global TradedamountSell23
			global Sell23OrderID
			global Sell23OrderStatus
			TradedamountSell23=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid23SellPrice )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell23
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator23=1
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid23SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell23Func
			GridSell23Func=1
		
			
		def grid24SellFunc():
			global SHORTGridWithIndicator24
			global grid24SellPrice
			grid24SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid24SellPrice
			global TradedamountSell24
			global Sell24OrderID
			global Sell24OrderStatus
			TradedamountSell24=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid24SellPrice )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell24
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator24=1
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid24SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell24Func
			GridSell24Func=1
		
			
		def grid25SellFunc():
			global SHORTGridWithIndicator25
			global grid25SellPrice
			grid25SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid25SellPrice
			global TradedamountSell25
			global Sell25OrderID
			global Sell25OrderStatus
			TradedamountSell25=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid25SellPrice )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell25
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator25=1
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid25SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell25Func
			GridSell25Func=1
		
			
		def grid26SellFunc():
			global SHORTGridWithIndicator26
			global grid26SellPrice
			grid26SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid26SellPrice
			global TradedamountSell26
			global Sell26OrderID
			global Sell26OrderStatus
			TradedamountSell26=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid26SellPrice )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell26
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator26=1
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid26SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell26Func
			GridSell26Func=1
		
			
		def grid27SellFunc():
			global SHORTGridWithIndicator27
			global grid27SellPrice
			grid27SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid27SellPrice
			global TradedamountSell27
			global Sell27OrderID
			global Sell27OrderStatus
			TradedamountSell27=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid27SellPrice )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell27
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator27=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid27SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell27Func
			GridSell27Func=1
	
			
		def grid28SellFunc():
			global SHORTGridWithIndicator28
			global grid28SellPrice
			grid28SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid28SellPrice
			global TradedamountSell28
			global Sell28OrderID
			global Sell28OrderStatus
			TradedamountSell28=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid28SellPrice )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell28
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator28=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid28SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100 
			global GridSell28Func
			GridSell28Func=1
		
			
		def grid29SellFunc():
			global SHORTGridWithIndicator29
			global grid29SellPrice
			grid29SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid29SellPrice
			global TradedamountSell29
			global Sell29OrderID
			global Sell29OrderStatus
			TradedamountSell29=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid29SellPrice )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell29
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator29=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid29SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			global	GridSell29Func		
			GridSell29Func=1
		
			
		def grid30SellFunc():
			global SHORTGridWithIndicator30
			global grid30SellPrice
			grid30SellPrice=LastPriceTICKS	-2	
			Ordertype='Sell'
			Orderside='limit'
			Orderprice=grid30SellPrice
			global TradedamountSell30
			global Sell30OrderID
			global Sell30OrderStatus
			TradedamountSell30=( ((DynamicFirstIntiatedWalletBalanceForAmountPostion/SecondPostionSizeAccordingtoIndicator)*Margin) / grid30SellPrice )
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountSell30
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)	 # working
			SHORTGridWithIndicator30=1 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid30SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			global	GridSell30Func
			GridSell30Func=1
			
		
		
	

		
		
		

	
		
			
		
			
		# ###############################START############################################ STARTING Buy GRID ONLY ############################################################################	
		if(StartGrid==0	 and BuyDirectinalGrid==1 and SellDirectinalGrid==0 and LastPriceTICKS!=0): 
			MainPostionSide=0
			MainPositionAmount=0
			MainPostionEntryPrice=0
			MainAccountProfitSinceGridStart=0
			StartGrid=1
			GridBuyFlag0	=0
			GridBuyFlag1	=0
			GridBuyFlag2	=0
			GridBuyFlag3	=0
			GridBuyFlag4	=0
			GridBuyFlag5	=0
			GridBuyFlag6	=0
			GridBuyFlag7	=0
			GridBuyFlag8	=0
			GridBuyFlag9	=0
			GridBuyFlag10	=0
			GridBuyFlag11	=0
			GridBuyFlag12	=0
			GridBuyFlag13	=0
			GridBuyFlag14	=0
			GridBuyFlag15	=0
			GridBuyFlag16	=0
			GridBuyFlag17	=0
			GridBuyFlag18	=0
			GridBuyFlag19	=0
			GridBuyFlag20	=0
			GridBuyFlag21	=0
			GridBuyFlag22	=0
			GridBuyFlag23	=0
			GridBuyFlag24	=0
			GridBuyFlag25	=0
			GridBuyFlag26	=0
			GridBuyFlag27	=0
			GridBuyFlag28	=0
			GridBuyFlag29	=0
			GridBuyFlag30	=0
			
			
			
			
		# ###############################END############################################ STARTING Buy GRID ONLY ############################################################################
		
		
		
		
		
		
		# ###############################START############################################ STARTING Sell GRID ONLY ############################################################################
		if(StartGrid==0	 and SellDirectinalGrid==1 and BiDirectionalGrid==0 and LastPriceTICKS!=0): 
			MainPostionSide=0
			MainPositionAmount=0
			MainPostionEntryPrice=0
			MainAccountProfitSinceGridStart=0
			StartGrid=1
			GridSellFlag0	=0
			GridSellFlag1	=0
			GridSellFlag2	=0
			GridSellFlag3	=0
			GridSellFlag4	=0
			GridSellFlag5	=0
			GridSellFlag6	=0
			GridSellFlag7	=0
			GridSellFlag8	=0
			GridSellFlag9	=0
			GridSellFlag10	=0
			GridSellFlag11	=0
			GridSellFlag12	=0
			GridSellFlag13	=0
			GridSellFlag14	=0
			GridSellFlag15	=0
			GridSellFlag16	=0
			GridSellFlag17	=0
			GridSellFlag18	=0
			GridSellFlag19	=0
			GridSellFlag20	=0
			GridSellFlag21	=0
			GridSellFlag22	=0
			GridSellFlag23	=0
			GridSellFlag24	=0
			GridSellFlag25	=0
			GridSellFlag26	=0
			GridSellFlag27	=0
			GridSellFlag28	=0
			GridSellFlag29	=0
			GridSellFlag30	=0
	
		
		if(LastPriceTICKS <	 grid0BuyPrice	 and  grid0BuyPrice		!=0 and GridBuy0Func ==1 and TradedamountBuy0 !=0):	GridBuyFlag0 =1
		if(LastPriceTICKS <	 grid1BuyPrice	 and  grid1BuyPrice		!=0 and GridBuy1Func ==1 and TradedamountBuy1 !=0):	GridBuyFlag1 =1
		if(LastPriceTICKS <	 grid2BuyPrice	 and  grid2BuyPrice		!=0 and GridBuy2Func ==1 and TradedamountBuy2 !=0):	GridBuyFlag2 =1
		if(LastPriceTICKS <	 grid3BuyPrice	 and  grid3BuyPrice		!=0 and GridBuy3Func ==1 and TradedamountBuy3 !=0):	GridBuyFlag3 =1
		if(LastPriceTICKS <	 grid4BuyPrice	 and  grid4BuyPrice		!=0 and GridBuy4Func ==1 and TradedamountBuy4 !=0):	GridBuyFlag4 =1
		if(LastPriceTICKS <	 grid5BuyPrice	 and  grid5BuyPrice		!=0 and GridBuy5Func ==1 and TradedamountBuy5 !=0):	GridBuyFlag5 =1
		if(LastPriceTICKS <	 grid6BuyPrice	 and  grid6BuyPrice		!=0 and GridBuy6Func ==1 and TradedamountBuy6 !=0):	GridBuyFlag6 =1
		if(LastPriceTICKS <	 grid7BuyPrice	 and  grid7BuyPrice		!=0 and GridBuy7Func ==1 and TradedamountBuy7 !=0):	GridBuyFlag7 =1
		if(LastPriceTICKS <	 grid8BuyPrice	 and  grid8BuyPrice		!=0 and GridBuy8Func ==1 and TradedamountBuy8 !=0):	GridBuyFlag8 =1
		if(LastPriceTICKS <	 grid9BuyPrice	 and  grid9BuyPrice		!=0 and GridBuy9Func ==1 and TradedamountBuy9 !=0):	GridBuyFlag9 =1
		if(LastPriceTICKS <	 grid10BuyPrice	 and  grid10BuyPrice !=0 and GridBuy10Func==1 and TradedamountBuy10!=0):	GridBuyFlag10=1
		if(LastPriceTICKS <	 grid11BuyPrice	 and  grid11BuyPrice !=0 and GridBuy11Func==1 and TradedamountBuy11!=0):	GridBuyFlag11=1
		if(LastPriceTICKS <	 grid12BuyPrice	 and  grid12BuyPrice !=0 and GridBuy12Func==1 and TradedamountBuy12!=0):	GridBuyFlag12=1
		if(LastPriceTICKS <	 grid13BuyPrice	 and  grid13BuyPrice !=0 and GridBuy13Func==1 and TradedamountBuy13!=0):	GridBuyFlag13=1
		if(LastPriceTICKS <	 grid14BuyPrice	 and  grid14BuyPrice !=0 and GridBuy14Func==1 and TradedamountBuy14!=0):	GridBuyFlag14=1
		if(LastPriceTICKS <	 grid15BuyPrice	 and  grid15BuyPrice !=0 and GridBuy15Func==1 and TradedamountBuy15!=0):	GridBuyFlag15=1
		if(LastPriceTICKS <	 grid16BuyPrice	 and  grid16BuyPrice !=0 and GridBuy16Func==1 and TradedamountBuy16!=0):	GridBuyFlag16=1
		if(LastPriceTICKS <	 grid17BuyPrice	 and  grid17BuyPrice !=0 and GridBuy17Func==1 and TradedamountBuy17!=0):	GridBuyFlag17=1
		if(LastPriceTICKS <	 grid18BuyPrice	 and  grid18BuyPrice !=0 and GridBuy18Func==1 and TradedamountBuy18!=0):	GridBuyFlag18=1
		if(LastPriceTICKS <	 grid19BuyPrice	 and  grid19BuyPrice !=0 and GridBuy19Func==1 and TradedamountBuy19!=0):	GridBuyFlag19=1
		if(LastPriceTICKS <	 grid20BuyPrice	 and  grid20BuyPrice !=0 and GridBuy20Func==1 and TradedamountBuy20!=0):	GridBuyFlag20=1
		if(LastPriceTICKS <	 grid21BuyPrice	 and  grid21BuyPrice !=0 and GridBuy21Func==1 and TradedamountBuy21!=0):	GridBuyFlag21=1
		if(LastPriceTICKS <	 grid22BuyPrice	 and  grid22BuyPrice !=0 and GridBuy22Func==1 and TradedamountBuy22!=0):	GridBuyFlag22=1
		if(LastPriceTICKS <	 grid23BuyPrice	 and  grid23BuyPrice !=0 and GridBuy23Func==1 and TradedamountBuy23!=0):	GridBuyFlag23=1
		if(LastPriceTICKS <	 grid24BuyPrice	 and  grid24BuyPrice !=0 and GridBuy24Func==1 and TradedamountBuy24!=0):	GridBuyFlag24=1
		if(LastPriceTICKS <	 grid25BuyPrice	 and  grid25BuyPrice !=0 and GridBuy25Func==1 and TradedamountBuy25!=0):	GridBuyFlag25=1
		if(LastPriceTICKS <	 grid26BuyPrice	 and  grid26BuyPrice !=0 and GridBuy26Func==1 and TradedamountBuy26!=0):	GridBuyFlag26=1
		if(LastPriceTICKS <	 grid27BuyPrice	 and  grid27BuyPrice !=0 and GridBuy27Func==1 and TradedamountBuy27!=0):	GridBuyFlag27=1
		if(LastPriceTICKS <	 grid28BuyPrice	 and  grid28BuyPrice !=0 and GridBuy28Func==1 and TradedamountBuy28!=0):	GridBuyFlag28=1
		if(LastPriceTICKS <	 grid29BuyPrice	 and  grid29BuyPrice !=0 and GridBuy29Func==1 and TradedamountBuy29!=0):	GridBuyFlag29=1
		if(LastPriceTICKS <	 grid30BuyPrice	 and  grid30BuyPrice !=0 and GridBuy30Func==1 and TradedamountBuy30!=0):	GridBuyFlag30=1
		
		
		if(GridBuyFlag0	 == 1  and TradedamountBuy0 !=0 ):	 GridBuyProfit0Price =	grid0BuyPrice  +((grid0BuyPrice	 *GridBuyProfit0Percent )/Margin)
		if(GridBuyFlag1	 == 1  and TradedamountBuy1 !=0 ):	 GridBuyProfit1Price =	grid1BuyPrice  +((grid1BuyPrice	 *GridBuyProfit1Percent )/Margin)
		if(GridBuyFlag2	 == 1  and TradedamountBuy2 !=0 ):	 GridBuyProfit2Price =	grid2BuyPrice  +((grid2BuyPrice	 *GridBuyProfit2Percent )/Margin)
		if(GridBuyFlag3	 == 1  and TradedamountBuy3 !=0 ):	 GridBuyProfit3Price =	grid3BuyPrice  +((grid3BuyPrice	 *GridBuyProfit3Percent )/Margin)
		if(GridBuyFlag4	 == 1  and TradedamountBuy4 !=0 ):	 GridBuyProfit4Price =	grid4BuyPrice  +((grid4BuyPrice	 *GridBuyProfit4Percent )/Margin)
		if(GridBuyFlag5	 == 1  and TradedamountBuy5 !=0 ):	 GridBuyProfit5Price =	grid5BuyPrice  +((grid5BuyPrice	 *GridBuyProfit5Percent )/Margin)
		if(GridBuyFlag6	 == 1  and TradedamountBuy6 !=0 ):	 GridBuyProfit6Price =	grid6BuyPrice  +((grid6BuyPrice	 *GridBuyProfit6Percent )/Margin)
		if(GridBuyFlag7	 == 1  and TradedamountBuy7 !=0 ):	 GridBuyProfit7Price =	grid7BuyPrice  +((grid7BuyPrice	 *GridBuyProfit7Percent )/Margin)
		if(GridBuyFlag8	 == 1  and TradedamountBuy8 !=0 ):	 GridBuyProfit8Price =	grid8BuyPrice  +((grid8BuyPrice	 *GridBuyProfit8Percent )/Margin)
		if(GridBuyFlag9	 == 1  and TradedamountBuy9 !=0 ):	 GridBuyProfit9Price =	grid9BuyPrice  +((grid9BuyPrice	 *GridBuyProfit9Percent )/Margin)
		if(GridBuyFlag10 == 1  and TradedamountBuy10!=0 ):	 GridBuyProfit10Price=	grid10BuyPrice +((grid10BuyPrice *GridBuyProfit10Percent)/Margin)
		if(GridBuyFlag11 == 1  and TradedamountBuy11!=0 ):	 GridBuyProfit11Price=	grid11BuyPrice +((grid11BuyPrice *GridBuyProfit11Percent)/Margin)
		if(GridBuyFlag12 == 1  and TradedamountBuy12!=0 ):	 GridBuyProfit12Price=	grid12BuyPrice +((grid12BuyPrice *GridBuyProfit12Percent)/Margin)
		if(GridBuyFlag13 == 1  and TradedamountBuy13!=0 ):	 GridBuyProfit13Price=	grid13BuyPrice +((grid13BuyPrice *GridBuyProfit13Percent)/Margin)
		if(GridBuyFlag14 == 1  and TradedamountBuy14!=0 ):	 GridBuyProfit14Price=	grid14BuyPrice +((grid14BuyPrice *GridBuyProfit14Percent)/Margin)
		if(GridBuyFlag15 == 1  and TradedamountBuy15!=0 ):	 GridBuyProfit15Price=	grid15BuyPrice +((grid15BuyPrice *GridBuyProfit15Percent)/Margin)
		if(GridBuyFlag16 == 1  and TradedamountBuy16!=0 ):	 GridBuyProfit16Price=	grid16BuyPrice +((grid16BuyPrice *GridBuyProfit16Percent)/Margin)
		if(GridBuyFlag17 == 1  and TradedamountBuy17!=0 ):	 GridBuyProfit17Price=	grid17BuyPrice +((grid17BuyPrice *GridBuyProfit17Percent)/Margin)
		if(GridBuyFlag18 == 1  and TradedamountBuy18!=0 ):	 GridBuyProfit18Price=	grid18BuyPrice +((grid18BuyPrice *GridBuyProfit18Percent)/Margin)
		if(GridBuyFlag19 == 1  and TradedamountBuy19!=0 ):	 GridBuyProfit19Price=	grid19BuyPrice +((grid19BuyPrice *GridBuyProfit19Percent)/Margin)
		if(GridBuyFlag20 == 1  and TradedamountBuy20!=0 ):	 GridBuyProfit20Price=	grid20BuyPrice +((grid20BuyPrice *GridBuyProfit20Percent)/Margin)
		if(GridBuyFlag21 == 1  and TradedamountBuy21!=0 ):	 GridBuyProfit21Price=	grid21BuyPrice +((grid21BuyPrice *GridBuyProfit21Percent)/Margin)
		if(GridBuyFlag22 == 1  and TradedamountBuy22!=0 ):	 GridBuyProfit22Price=	grid22BuyPrice +((grid22BuyPrice *GridBuyProfit22Percent)/Margin)
		if(GridBuyFlag23 == 1  and TradedamountBuy23!=0 ):	 GridBuyProfit23Price=	grid23BuyPrice +((grid23BuyPrice *GridBuyProfit23Percent)/Margin)
		if(GridBuyFlag24 == 1  and TradedamountBuy24!=0 ):	 GridBuyProfit24Price=	grid24BuyPrice +((grid24BuyPrice *GridBuyProfit24Percent)/Margin)
		if(GridBuyFlag25 == 1  and TradedamountBuy25!=0 ):	 GridBuyProfit25Price=	grid25BuyPrice +((grid25BuyPrice *GridBuyProfit25Percent)/Margin)
		if(GridBuyFlag26 == 1  and TradedamountBuy26!=0 ):	 GridBuyProfit26Price=	grid26BuyPrice +((grid26BuyPrice *GridBuyProfit26Percent)/Margin)
		if(GridBuyFlag27 == 1  and TradedamountBuy27!=0 ):	 GridBuyProfit27Price=	grid27BuyPrice +((grid27BuyPrice *GridBuyProfit27Percent)/Margin)
		if(GridBuyFlag28 == 1  and TradedamountBuy28!=0 ):	 GridBuyProfit28Price=	grid28BuyPrice +((grid28BuyPrice *GridBuyProfit28Percent)/Margin)
		if(GridBuyFlag29 == 1  and TradedamountBuy29!=0 ):	 GridBuyProfit29Price=	grid29BuyPrice +((grid29BuyPrice *GridBuyProfit29Percent)/Margin)
		if(GridBuyFlag30 == 1  and TradedamountBuy30!=0 ):	 GridBuyProfit30Price=	grid30BuyPrice +((grid30BuyPrice *GridBuyProfit30Percent)/Margin)
		
	
		if(LastPriceTICKS >	 grid0SellPrice	  and  grid0SellPrice  !=0 and GridSell0Func !=0 and TradedamountSell0 !=0):	GridSellFlag0 =1
		if(LastPriceTICKS >	 grid1SellPrice	  and  grid1SellPrice  !=0 and GridSell1Func !=0 and TradedamountSell1 !=0):	GridSellFlag1 =1
		if(LastPriceTICKS >	 grid2SellPrice	  and  grid2SellPrice  !=0 and GridSell2Func !=0 and TradedamountSell2 !=0):	GridSellFlag2 =1
		if(LastPriceTICKS >	 grid3SellPrice	  and  grid3SellPrice  !=0 and GridSell3Func !=0 and TradedamountSell3 !=0):	GridSellFlag3 =1
		if(LastPriceTICKS >	 grid4SellPrice	  and  grid4SellPrice  !=0 and GridSell4Func !=0 and TradedamountSell4 !=0):	GridSellFlag4 =1
		if(LastPriceTICKS >	 grid5SellPrice	  and  grid5SellPrice  !=0 and GridSell5Func !=0 and TradedamountSell5 !=0):	GridSellFlag5 =1
		if(LastPriceTICKS >	 grid6SellPrice	  and  grid6SellPrice  !=0 and GridSell6Func !=0 and TradedamountSell6 !=0):	GridSellFlag6 =1
		if(LastPriceTICKS >	 grid7SellPrice	  and  grid7SellPrice  !=0 and GridSell7Func !=0 and TradedamountSell7 !=0):	GridSellFlag7 =1
		if(LastPriceTICKS >	 grid8SellPrice	  and  grid8SellPrice  !=0 and GridSell8Func !=0 and TradedamountSell8 !=0):	GridSellFlag8 =1
		if(LastPriceTICKS >	 grid9SellPrice	  and  grid9SellPrice  !=0 and GridSell9Func !=0 and TradedamountSell9 !=0):	GridSellFlag9 =1
		if(LastPriceTICKS >	 grid10SellPrice  and  grid10SellPrice !=0 and GridSell10Func!=0 and TradedamountSell10!=0):	GridSellFlag10=1
		if(LastPriceTICKS >	 grid11SellPrice  and  grid11SellPrice !=0 and GridSell11Func!=0 and TradedamountSell11!=0):	GridSellFlag11=1
		if(LastPriceTICKS >	 grid12SellPrice  and  grid12SellPrice !=0 and GridSell12Func!=0 and TradedamountSell12!=0):	GridSellFlag12=1
		if(LastPriceTICKS >	 grid13SellPrice  and  grid13SellPrice !=0 and GridSell13Func!=0 and TradedamountSell13!=0):	GridSellFlag13=1
		if(LastPriceTICKS >	 grid14SellPrice  and  grid14SellPrice !=0 and GridSell14Func!=0 and TradedamountSell14!=0):	GridSellFlag14=1
		if(LastPriceTICKS >	 grid15SellPrice  and  grid15SellPrice !=0 and GridSell15Func!=0 and TradedamountSell15!=0):	GridSellFlag15=1
		if(LastPriceTICKS >	 grid16SellPrice  and  grid16SellPrice !=0 and GridSell16Func!=0 and TradedamountSell16!=0):	GridSellFlag16=1
		if(LastPriceTICKS >	 grid17SellPrice  and  grid17SellPrice !=0 and GridSell17Func!=0 and TradedamountSell17!=0):	GridSellFlag17=1
		if(LastPriceTICKS >	 grid18SellPrice  and  grid18SellPrice !=0 and GridSell18Func!=0 and TradedamountSell18!=0):	GridSellFlag18=1
		if(LastPriceTICKS >	 grid19SellPrice  and  grid19SellPrice !=0 and GridSell19Func!=0 and TradedamountSell19!=0):	GridSellFlag19=1
		if(LastPriceTICKS >	 grid20SellPrice  and  grid20SellPrice !=0 and GridSell20Func!=0 and TradedamountSell20!=0):	GridSellFlag20=1
		if(LastPriceTICKS >	 grid21SellPrice  and  grid21SellPrice !=0 and GridSell21Func!=0 and TradedamountSell21!=0):	GridSellFlag21=1
		if(LastPriceTICKS >	 grid22SellPrice  and  grid22SellPrice !=0 and GridSell22Func!=0 and TradedamountSell22!=0):	GridSellFlag22=1
		if(LastPriceTICKS >	 grid23SellPrice  and  grid23SellPrice !=0 and GridSell23Func!=0 and TradedamountSell23!=0):	GridSellFlag23=1
		if(LastPriceTICKS >	 grid24SellPrice  and  grid24SellPrice !=0 and GridSell24Func!=0 and TradedamountSell24!=0):	GridSellFlag24=1
		if(LastPriceTICKS >	 grid25SellPrice  and  grid25SellPrice !=0 and GridSell25Func!=0 and TradedamountSell25!=0):	GridSellFlag25=1
		if(LastPriceTICKS >	 grid26SellPrice  and  grid26SellPrice !=0 and GridSell26Func!=0 and TradedamountSell26!=0):	GridSellFlag26=1
		if(LastPriceTICKS >	 grid27SellPrice  and  grid27SellPrice !=0 and GridSell27Func!=0 and TradedamountSell27!=0):	GridSellFlag27=1
		if(LastPriceTICKS >	 grid28SellPrice  and  grid28SellPrice !=0 and GridSell28Func!=0 and TradedamountSell28!=0):	GridSellFlag28=1
		if(LastPriceTICKS >	 grid29SellPrice  and  grid29SellPrice !=0 and GridSell29Func!=0 and TradedamountSell29!=0):	GridSellFlag29=1
		if(LastPriceTICKS >	 grid30SellPrice  and  grid30SellPrice !=0 and GridSell30Func!=0 and TradedamountSell30!=0):	GridSellFlag30=1
		
		
		if(GridSellFlag0  == 1	and TradedamountSell0 !=0):	 GridSellProfit0Price =	 grid0SellPrice	 -((grid0SellPrice	*GridSellProfit0Percent )/Margin)
		if(GridSellFlag1  == 1	and TradedamountSell1 !=0):	 GridSellProfit1Price =	 grid1SellPrice	 -((grid1SellPrice	*GridSellProfit1Percent )/Margin)
		if(GridSellFlag2  == 1	and TradedamountSell2 !=0):	 GridSellProfit2Price =	 grid2SellPrice	 -((grid2SellPrice	*GridSellProfit2Percent )/Margin)
		if(GridSellFlag3  == 1	and TradedamountSell3 !=0):	 GridSellProfit3Price =	 grid3SellPrice	 -((grid3SellPrice	*GridSellProfit3Percent )/Margin)
		if(GridSellFlag4  == 1	and TradedamountSell4 !=0):	 GridSellProfit4Price =	 grid4SellPrice	 -((grid4SellPrice	*GridSellProfit4Percent )/Margin)
		if(GridSellFlag5  == 1	and TradedamountSell5 !=0):	 GridSellProfit5Price =	 grid5SellPrice	 -((grid5SellPrice	*GridSellProfit5Percent )/Margin)
		if(GridSellFlag6  == 1	and TradedamountSell6 !=0):	 GridSellProfit6Price =	 grid6SellPrice	 -((grid6SellPrice	*GridSellProfit6Percent )/Margin)
		if(GridSellFlag7  == 1	and TradedamountSell7 !=0):	 GridSellProfit7Price =	 grid7SellPrice	 -((grid7SellPrice	*GridSellProfit7Percent )/Margin)
		if(GridSellFlag8  == 1	and TradedamountSell8 !=0):	 GridSellProfit8Price =	 grid8SellPrice	 -((grid8SellPrice	*GridSellProfit8Percent )/Margin)
		if(GridSellFlag9  == 1	and TradedamountSell9 !=0):	 GridSellProfit9Price =	 grid9SellPrice	 -((grid9SellPrice	*GridSellProfit9Percent )/Margin)
		if(GridSellFlag10 == 1	and TradedamountSell10!=0):	 GridSellProfit10Price=	 grid10SellPrice -((grid10SellPrice *GridSellProfit10Percent)/Margin)
		if(GridSellFlag11 == 1	and TradedamountSell11!=0):	 GridSellProfit11Price=	 grid11SellPrice -((grid11SellPrice *GridSellProfit11Percent)/Margin)
		if(GridSellFlag12 == 1	and TradedamountSell12!=0):	 GridSellProfit12Price=	 grid12SellPrice -((grid12SellPrice *GridSellProfit12Percent)/Margin)
		if(GridSellFlag13 == 1	and TradedamountSell13!=0):	 GridSellProfit13Price=	 grid13SellPrice -((grid13SellPrice *GridSellProfit13Percent)/Margin)
		if(GridSellFlag14 == 1	and TradedamountSell14!=0):	 GridSellProfit14Price=	 grid14SellPrice -((grid14SellPrice *GridSellProfit14Percent)/Margin)
		if(GridSellFlag15 == 1	and TradedamountSell15!=0):	 GridSellProfit15Price=	 grid15SellPrice -((grid15SellPrice *GridSellProfit15Percent)/Margin)
		if(GridSellFlag16 == 1	and TradedamountSell16!=0):	 GridSellProfit16Price=	 grid16SellPrice -((grid16SellPrice *GridSellProfit16Percent)/Margin)
		if(GridSellFlag17 == 1	and TradedamountSell17!=0):	 GridSellProfit17Price=	 grid17SellPrice -((grid17SellPrice *GridSellProfit17Percent)/Margin)
		if(GridSellFlag18 == 1	and TradedamountSell18!=0):	 GridSellProfit18Price=	 grid18SellPrice -((grid18SellPrice *GridSellProfit18Percent)/Margin)
		if(GridSellFlag19 == 1	and TradedamountSell19!=0):	 GridSellProfit19Price=	 grid19SellPrice -((grid19SellPrice *GridSellProfit19Percent)/Margin)
		if(GridSellFlag20 == 1	and TradedamountSell20!=0):	 GridSellProfit20Price=	 grid20SellPrice -((grid20SellPrice *GridSellProfit20Percent)/Margin)
		if(GridSellFlag21 == 1	and TradedamountSell21!=0):	 GridSellProfit21Price=	 grid21SellPrice -((grid21SellPrice *GridSellProfit21Percent)/Margin)
		if(GridSellFlag22 == 1	and TradedamountSell22!=0):	 GridSellProfit22Price=	 grid22SellPrice -((grid22SellPrice *GridSellProfit22Percent)/Margin)
		if(GridSellFlag23 == 1	and TradedamountSell23!=0):	 GridSellProfit23Price=	 grid23SellPrice -((grid23SellPrice *GridSellProfit23Percent)/Margin)
		if(GridSellFlag24 == 1	and TradedamountSell24!=0):	 GridSellProfit24Price=	 grid24SellPrice -((grid24SellPrice *GridSellProfit24Percent)/Margin)
		if(GridSellFlag25 == 1	and TradedamountSell25!=0):	 GridSellProfit25Price=	 grid25SellPrice -((grid25SellPrice *GridSellProfit25Percent)/Margin)
		if(GridSellFlag26 == 1	and TradedamountSell26!=0):	 GridSellProfit26Price=	 grid26SellPrice -((grid26SellPrice *GridSellProfit26Percent)/Margin)
		if(GridSellFlag27 == 1	and TradedamountSell27!=0):	 GridSellProfit27Price=	 grid27SellPrice -((grid27SellPrice *GridSellProfit27Percent)/Margin)
		if(GridSellFlag28 == 1	and TradedamountSell28!=0):	 GridSellProfit28Price=	 grid28SellPrice -((grid28SellPrice *GridSellProfit28Percent)/Margin)
		if(GridSellFlag29 == 1	and TradedamountSell29!=0):	 GridSellProfit29Price=	 grid29SellPrice -((grid29SellPrice *GridSellProfit29Percent)/Margin)
		if(GridSellFlag30 == 1	and TradedamountSell30!=0):	 GridSellProfit30Price=	 grid30SellPrice -((grid30SellPrice *GridSellProfit30Percent)/Margin)
		
		
		def GridBuyProfit0PriceFunc():
			global	LongGridWithIndicator0
			global	GridBuyFlag0
			global	TradedamountBuy0
			global	GridBuyProfit0Price
			global GridBuy0ProfitFuncHandle
			global SN1M
			global GridBuyProfit0PriceCount
			global LOCKPreviousGridBuyProfit0Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit0Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy0
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid0BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator0=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit0PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit0Price=0
			GridBuyFlag0=0
			TradedamountBuy0=0
			GridBuyProfit0Price=0
			GridBuy0ProfitFuncHandle=1
	
		def GridBuyProfit1PriceFunc():
			global	LongGridWithIndicator1
			global GridBuyFlag1
			global TradedamountBuy1
			global GridBuyProfit1Price
			global SN1M
			global GridBuyProfit1PriceCount
			global LOCKPreviousGridBuyProfit1Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit1Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy1
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid1BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator1=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit1PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit1Price=0
			GridBuyFlag1=0
			TradedamountBuy1=0
			GridBuyProfit1Price=0
	
		
		def GridBuyProfit2PriceFunc():
			global	LongGridWithIndicator2
			global GridBuyFlag2
			global TradedamountBuy2
			global GridBuyProfit2Price
			global SN1M
			global GridBuyProfit2PriceCount
			global LOCKPreviousGridBuyProfit2Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit2Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy2
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid2BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator2=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit2PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit2Price=0
			GridBuyFlag2=0
			TradedamountBuy2=0
			GridBuyProfit2Price=0
		
		def GridBuyProfit3PriceFunc():
			global	LongGridWithIndicator3
			global GridBuyFlag3
			global TradedamountBuy3
			global GridBuyProfit3Price
			global SN1M
			global GridBuyProfit3PriceCount
			global LOCKPreviousGridBuyProfit3Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit3Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy3
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid3BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator3=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit3PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit3Price=0
			GridBuyFlag3=0
			TradedamountBuy3=0
			GridBuyProfit3Price=0
	
		def GridBuyProfit4PriceFunc():
			global	LongGridWithIndicator4
			global	GridBuyFlag4
			global	TradedamountBuy4
			global	GridBuyProfit4Price
			global SN1M
			global GridBuyProfit4PriceCount
			global LOCKPreviousGridBuyProfit4Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit4Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy4
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid4BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator4=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit4PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit4Price=0
			GridBuyFlag4=0
			TradedamountBuy4=0
			GridBuyProfit4Price=0			
	
		def GridBuyProfit5PriceFunc():
			global	LongGridWithIndicator5
			global	GridBuyFlag5
			global	TradedamountBuy5
			global	GridBuyProfit5Price
			global SN1M
			global GridBuyProfit5PriceCount
			global LOCKPreviousGridBuyProfit5Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit5Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy5
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid5BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator5=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit5PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit5Price=0
			GridBuyFlag5=0
			TradedamountBuy5=0
			GridBuyProfit5Price=0
	
		def GridBuyProfit6PriceFunc():
			global	LongGridWithIndicator6
			global	GridBuyFlag6
			global	TradedamountBuy6
			global	GridBuyProfit6Price
			global SN1M
			global GridBuyProfit6PriceCount
			global LOCKPreviousGridBuyProfit6Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit6Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy6
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid6BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator6=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit6PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit6Price=0
			GridBuyFlag6=0
			TradedamountBuy6=0
			GridBuyProfit6Price=0
	
		
		def GridBuyProfit7PriceFunc():
			global	LongGridWithIndicator7
			global	GridBuyFlag7
			global	TradedamountBuy7
			global	GridBuyProfit7Price
			global SN1M
			global GridBuyProfit7PriceCount
			global LOCKPreviousGridBuyProfit7Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit7Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy7
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid7BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator7=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit7PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit7Price=0
			GridBuyFlag7=0
			TradedamountBuy7=0
			GridBuyProfit7Price=0
		
		def GridBuyProfit8PriceFunc():
			global	LongGridWithIndicator8
			global	GridBuyFlag8
			global	TradedamountBuy8
			global	GridBuyProfit8Price
			global SN1M
			global GridBuyProfit8PriceCount
			global LOCKPreviousGridBuyProfit8Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit8Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy8
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid8BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator8=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit8PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit8Price=0
			GridBuyFlag8=0
			TradedamountBuy8=0
			GridBuyProfit8Price=0
	
		def GridBuyProfit9PriceFunc():
			global	LongGridWithIndicator9
			global	GridBuyFlag9
			global	TradedamountBuy9
			global	GridBuyProfit9Price
			global SN1M
			global GridBuyProfit9PriceCount
			global LOCKPreviousGridBuyProfit9Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit9Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy9
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid9BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator9=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit9PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit9Price=0
			GridBuyFlag9=0
			TradedamountBuy9=0
			GridBuyProfit9Price=0			
	
		def GridBuyProfit10PriceFunc():
			global	LongGridWithIndicator10
			global	GridBuyFlag10
			global	TradedamountBuy10
			global	GridBuyProfit10Price
			global SN1M
			global GridBuyProfit10PriceCount
			global LOCKPreviousGridBuyProfit10Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit10Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy10
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid10BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator10=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit10PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit10Price=0
			GridBuyFlag10=0
			TradedamountBuy10=0
			GridBuyProfit10Price=0
	
		def GridBuyProfit11PriceFunc():
			global	LongGridWithIndicator11
			global	GridBuyFlag11
			global	TradedamountBuy11
			global	GridBuyProfit11Price
			global SN1M
			global GridBuyProfit11PriceCount
			global LOCKPreviousGridBuyProfit11Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit11Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy11
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid11BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator11=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit11PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit11Price=0
			GridBuyFlag11=0
			TradedamountBuy11=0
			GridBuyProfit11Price=0
	
		
		def GridBuyProfit12PriceFunc():
			global	LongGridWithIndicator12
			global	GridBuyFlag12
			global	TradedamountBuy12
			global	GridBuyProfit12Price
			global SN1M
			global GridBuyProfit12PriceCount
			global LOCKPreviousGridBuyProfit12Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit12Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy12
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid12BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator12=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit12PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit12Price=0
			GridBuyFlag12=0
			TradedamountBuy12=0
			GridBuyProfit12Price=0
		
		def GridBuyProfit13PriceFunc():
			global	LongGridWithIndicator13
			global	GridBuyFlag13
			global	TradedamountBuy13
			global	GridBuyProfit13Price
			global SN1M
			global GridBuyProfit13PriceCount
			global LOCKPreviousGridBuyProfit13Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit13Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy13
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid13BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator13=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit13PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit13Price=0
			GridBuyFlag13=0
			TradedamountBuy13=0
			GridBuyProfit13Price=0
	
		def GridBuyProfit14PriceFunc():
			global	LongGridWithIndicator14
			global	GridBuyFlag14
			global	TradedamountBuy14
			global	GridBuyProfit14Price
			global SN1M
			global GridBuyProfit14PriceCount
			global LOCKPreviousGridBuyProfit14Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit14Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy14
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid14BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator14=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit14PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit14Price=0
			GridBuyFlag14=0	
			TradedamountBuy14=0
			GridBuyProfit14Price=0
	
		def GridBuyProfit15PriceFunc():
			global	LongGridWithIndicator15
			global	GridBuyFlag15
			global	TradedamountBuy15
			global	GridBuyProfit15Price
			global SN1M
			global GridBuyProfit15PriceCount
			global LOCKPreviousGridBuyProfit15Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit15Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy15
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid15BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator15=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit15PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit15Price=0
			GridBuyFlag15=0
			TradedamountBuy15=0
			GridBuyProfit15Price=0
	
		def GridBuyProfit16PriceFunc():
			global	LongGridWithIndicator16
			global	GridBuyFlag16
			global	TradedamountBuy16
			global	GridBuyProfit16Price
			global SN1M
			global GridBuyProfit16PriceCount
			global LOCKPreviousGridBuyProfit16Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit16Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy16
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid16BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator16=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit16PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit16Price=0
			GridBuyFlag16=0
			TradedamountBuy16=0
			GridBuyProfit16Price=0
	
		
		def GridBuyProfit17PriceFunc():
			global	LongGridWithIndicator17
			global	GridBuyFlag17
			global	TradedamountBuy17
			global	GridBuyProfit17Price
			global SN1M
			global GridBuyProfit17PriceCount
			global LOCKPreviousGridBuyProfit17Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit17Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy17
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid17BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator17=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit17PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit17Price=0
			GridBuyFlag17=0
			TradedamountBuy17=0
			GridBuyProfit17Price=0
		
		def GridBuyProfit18PriceFunc():
			global	LongGridWithIndicator18
			global	GridBuyFlag18
			global	TradedamountBuy18
			global	GridBuyProfit18Price
			global SN1M
			global GridBuyProfit18PriceCount
			global LOCKPreviousGridBuyProfit18Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit18Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy18
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid18BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator18=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit18PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit18Price=0
			GridBuyFlag18=0
			TradedamountBuy18=0
			GridBuyProfit18Price=0
	
		def GridBuyProfit19PriceFunc():
			global	LongGridWithIndicator19
			global	GridBuyFlag19
			global	TradedamountBuy19
			global	GridBuyProfit19Price
			global SN1M
			global GridBuyProfit19PriceCount
			global LOCKPreviousGridBuyProfit19Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit19Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy19
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid19BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator19=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit19PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit19Price=0
			GridBuyFlag19=0
			TradedamountBuy19=0
			GridBuyProfit19Price=0			
	
		def GridBuyProfit20PriceFunc():
			global	LongGridWithIndicator20
			global	GridBuyFlag20
			global	TradedamountBuy20
			global	GridBuyProfit20Price
			global SN1M
			global GridBuyProfit20PriceCount
			global LOCKPreviousGridBuyProfit20Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit20Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy20
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid20BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator20=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit20PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit20Price=0
			GridBuyFlag20=0
			TradedamountBuy20=0
			GridBuyProfit20Price=0
	
		def GridBuyProfit21PriceFunc():
			global	LongGridWithIndicator21
			global	GridBuyFlag21
			global	TradedamountBuy21
			global	GridBuyProfit21Price
			global SN1M
			global GridBuyProfit21PriceCount
			global LOCKPreviousGridBuyProfit21Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit21Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy21
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid21BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator21=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit21PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit21Price=0
			GridBuyFlag21=0
			TradedamountBuy21=0
			GridBuyProfit21Price=0
	
		
		def GridBuyProfit22PriceFunc():
			global	LongGridWithIndicator22
			global	GridBuyFlag22
			global	TradedamountBuy22
			global	GridBuyProfit22Price
			global SN1M
			global GridBuyProfit22PriceCount
			global LOCKPreviousGridBuyProfit22Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit22Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy22
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid22BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator22=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit22PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit22Price=0
			GridBuyFlag22=0
			TradedamountBuy22=0
			GridBuyProfit22Price=0
		
		def GridBuyProfit23PriceFunc():
			global	LongGridWithIndicator23
			global	GridBuyFlag23
			global	TradedamountBuy23
			global	GridBuyProfit23Price
			global SN1M
			global GridBuyProfit23PriceCount
			global LOCKPreviousGridBuyProfit23Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit23Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy23
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid23BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator23=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit23PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit23Price=0
			GridBuyFlag23=0
			TradedamountBuy23=0
			GridBuyProfit23Price=0
	
		def GridBuyProfit24PriceFunc():
			global	LongGridWithIndicator24
			global	GridBuyFlag24
			global	TradedamountBuy24
			global	GridBuyProfit24Price
			global SN1M
			global GridBuyProfit24PriceCount
			global LOCKPreviousGridBuyProfit24Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit24Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy24
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid24BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator24=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit24PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit24Price=0
			GridBuyFlag24=0
			TradedamountBuy24=0
			GridBuyProfit24Price=0
	
		def GridBuyProfit25PriceFunc():
			global	LongGridWithIndicator25
			global	GridBuyFlag25
			global	TradedamountBuy25
			global	GridBuyProfit25Price
			global SN1M
			global GridBuyProfit25PriceCount
			global LOCKPreviousGridBuyProfit25Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit25Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy25
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid25BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator25=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit25PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit25Price=0
			GridBuyFlag25=0
			TradedamountBuy25=0
			GridBuyProfit25Price=0
	
		def GridBuyProfit26PriceFunc():
			global	LongGridWithIndicator26
			global	GridBuyFlag26
			global	TradedamountBuy26
			global	GridBuyProfit26Price
			global SN1M
			global GridBuyProfit26PriceCount
			global LOCKPreviousGridBuyProfit26Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit26Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy26
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid26BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator26=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit26PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit26Price=0
			GridBuyFlag26=0
			TradedamountBuy26=0
			GridBuyProfit26Price=0
	
		
		def GridBuyProfit27PriceFunc():
			global	LongGridWithIndicator27
			global	GridBuyFlag27
			global	TradedamountBuy27
			global	GridBuyProfit27Price
			global SN1M
			global GridBuyProfit27PriceCount
			global LOCKPreviousGridBuyProfit27Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit27Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy27
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid27BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator27=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit27PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit27Price=0
			GridBuyFlag27=0
			TradedamountBuy27=0
			GridBuyProfit27Price=0
		
		def GridBuyProfit28PriceFunc():
			global	LongGridWithIndicator28
			global	GridBuyFlag28
			global	TradedamountBuy28
			global	GridBuyProfit28Price
			global SN1M
			global GridBuyProfit28PriceCount
			global LOCKPreviousGridBuyProfit28Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit28Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy28
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid28BuyPrice*Orderamount)
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit28PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit28Price=0
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator28=0
			GridBuyFlag28=0
			TradedamountBuy28=0
			GridBuyProfit28Price=0
	
		def GridBuyProfit29PriceFunc():
			global	LongGridWithIndicator29
			global	GridBuyFlag29
			global	TradedamountBuy29
			global	GridBuyProfit29Price
			global SN1M
			global GridBuyProfit29PriceCount
			global LOCKPreviousGridBuyProfit29Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit29Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy29
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid29BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator29=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit29PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit29Price=0
			GridBuyFlag29=0
			TradedamountBuy29=0
			GridBuyProfit29Price=0
		
		def GridBuyProfit30PriceFunc():
			global	LongGridWithIndicator30
			global	GridBuyFlag30	
			global	TradedamountBuy30
			global	GridBuyProfit30Price
			global SN1M
			global GridBuyProfit30PriceCount
			global LOCKPreviousGridBuyProfit30Price
			Ordertype='Sell'
			Orderside='market'
			Orderprice=GridBuyProfit30Price
			OrderActionWas='Sell'
			OrderActionTakenGlobal="Sell"
			Orderamount=TradedamountBuy30
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid30BuyPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator30=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridBuyProfit30PriceCount=GlobalProfit
			LOCKPreviousGridBuyProfit30Price=0
			GridBuyFlag30=0	
			TradedamountBuy30=0
			GridBuyProfit30Price=0
	
	

		
		if(GridBuyFlag0	 == 1 and LastPriceTICKS > GridBuyProfit0Price	and GridBuyProfit0Price !=0 and TradedamountBuy0 !=0  ):	
			GridBuyProfit0PriceCount=GridBuyProfit0PriceCount+.5
			PreviousGridBuyProfit0Price=GridBuyProfit0Price
			GridBuyProfit0Price=grid0BuyPrice	 +((grid0BuyPrice	 *GridBuyProfit0PriceCount )/Margin)
			LOCKPreviousGridBuyProfit0Price=1															   
		if(LOCKPreviousGridBuyProfit0Price==1 and	LastPriceTICKS	<  PreviousGridBuyProfit0Price and PreviousGridBuyProfit0Price !=0):
			GridBuyProfit0PriceFunc()		
			#if(StopBuyFunc==0):grid0BuyFunc()
	
		if(GridBuyFlag1	 == 1 and LastPriceTICKS > GridBuyProfit1Price	and GridBuyProfit1Price !=0 and TradedamountBuy1 !=0  ):	
			GridBuyProfit1PriceCount=GridBuyProfit1PriceCount+.5
			PreviousGridBuyProfit1Price=GridBuyProfit1Price
			GridBuyProfit1Price=grid1BuyPrice	 +((grid1BuyPrice	 *GridBuyProfit1PriceCount )/Margin)
			LOCKPreviousGridBuyProfit1Price=1															   
		if(LOCKPreviousGridBuyProfit1Price==1 and	LastPriceTICKS	<  PreviousGridBuyProfit1Price	and PreviousGridBuyProfit1Price !=0):
			GridBuyProfit1PriceFunc()		
			#if(StopBuyFunc==0):grid1BuyFunc()
		
		
		if(GridBuyFlag2	 == 1  and LastPriceTICKS > GridBuyProfit2Price	and GridBuyProfit2Price !=0 and TradedamountBuy2 !=0  ):	
			GridBuyProfit2PriceCount=GridBuyProfit2PriceCount+.5
			PreviousGridBuyProfit2Price=GridBuyProfit2Price
			GridBuyProfit2Price=grid2BuyPrice	 +((grid2BuyPrice	 *GridBuyProfit2PriceCount )/Margin)
			LOCKPreviousGridBuyProfit2Price=1															   
		if(LOCKPreviousGridBuyProfit2Price==1 and	LastPriceTICKS	<  PreviousGridBuyProfit2Price	and PreviousGridBuyProfit2Price !=0):
			GridBuyProfit2PriceFunc()		
			#if(StopBuyFunc==0):grid2BuyFunc()
		
	
		if(GridBuyFlag3	 == 1  and LastPriceTICKS > GridBuyProfit3Price	and GridBuyProfit3Price !=0 and TradedamountBuy3 !=0  ):	
			GridBuyProfit3PriceCount=GridBuyProfit3PriceCount+.5
			PreviousGridBuyProfit3Price=GridBuyProfit3Price
			GridBuyProfit3Price=grid3BuyPrice	 +((grid3BuyPrice	 *GridBuyProfit3PriceCount )/Margin)
			LOCKPreviousGridBuyProfit3Price=1															   
		if(LOCKPreviousGridBuyProfit3Price==1 and	LastPriceTICKS	<  PreviousGridBuyProfit3Price	and PreviousGridBuyProfit3Price !=0):
			GridBuyProfit3PriceFunc()		
			#if(StopBuyFunc==0):grid3BuyFunc()
		
		if(GridBuyFlag4	 == 1  and LastPriceTICKS > GridBuyProfit4Price	and GridBuyProfit4Price !=0 and TradedamountBuy4 !=0  ):	
			GridBuyProfit4PriceCount=GridBuyProfit4PriceCount+.5
			PreviousGridBuyProfit4Price=GridBuyProfit4Price
			GridBuyProfit4Price=grid4BuyPrice	 +((grid4BuyPrice	 *GridBuyProfit4PriceCount )/Margin)
			LOCKPreviousGridBuyProfit4Price=1															   
		if(LOCKPreviousGridBuyProfit4Price==1 and	LastPriceTICKS	<  PreviousGridBuyProfit4Price	and PreviousGridBuyProfit4Price !=0):
			GridBuyProfit4PriceFunc()		
			#if(StopBuyFunc==0):grid4BuyFunc()


		if(GridBuyFlag5	 == 1  and LastPriceTICKS > GridBuyProfit5Price	and GridBuyProfit5Price !=0 and TradedamountBuy5 !=0  ):	
			GridBuyProfit5PriceCount=GridBuyProfit5PriceCount+.5
			PreviousGridBuyProfit5Price=GridBuyProfit5Price
			GridBuyProfit5Price=grid5BuyPrice	 +((grid5BuyPrice	 *GridBuyProfit5PriceCount )/Margin)
			LOCKPreviousGridBuyProfit5Price=1															   
		if(LOCKPreviousGridBuyProfit5Price==1 and	LastPriceTICKS	<  PreviousGridBuyProfit5Price	and PreviousGridBuyProfit5Price !=0):
			GridBuyProfit5PriceFunc()		
			#if(StopBuyFunc==0):grid5BuyFunc()
				 
				 
		if(GridBuyFlag6	 == 1  and LastPriceTICKS > GridBuyProfit6Price	and GridBuyProfit6Price !=0 and TradedamountBuy6 !=0  ):	
			GridBuyProfit6PriceCount=GridBuyProfit6PriceCount+.5
			PreviousGridBuyProfit6Price=GridBuyProfit6Price
			GridBuyProfit6Price=grid6BuyPrice	 +((grid6BuyPrice	 *GridBuyProfit6PriceCount )/Margin)
			LOCKPreviousGridBuyProfit6Price=1															   
		if(LOCKPreviousGridBuyProfit6Price==1 and	LastPriceTICKS	<  PreviousGridBuyProfit6Price	and PreviousGridBuyProfit6Price !=0):
			GridBuyProfit6PriceFunc()		
			#if(StopBuyFunc==0):grid6BuyFunc()

		if(GridBuyFlag7	 == 1  and LastPriceTICKS > GridBuyProfit7Price	and GridBuyProfit7Price !=0 and TradedamountBuy7 !=0  ):	
			GridBuyProfit7PriceCount=GridBuyProfit7PriceCount+.5
			PreviousGridBuyProfit7Price=GridBuyProfit7Price
			GridBuyProfit7Price=grid7BuyPrice	 +((grid7BuyPrice	 *GridBuyProfit7PriceCount )/Margin)
			LOCKPreviousGridBuyProfit7Price=1															   
		if(LOCKPreviousGridBuyProfit7Price==1 and	LastPriceTICKS	<  PreviousGridBuyProfit7Price	and PreviousGridBuyProfit7Price !=0):
			GridBuyProfit7PriceFunc()		
			#if(StopBuyFunc==0):grid7BuyFunc()

		if(GridBuyFlag8	 == 1  and LastPriceTICKS > GridBuyProfit8Price	and GridBuyProfit8Price !=0 and TradedamountBuy8 !=0  ):	
			GridBuyProfit8PriceCount=GridBuyProfit8PriceCount+.5
			PreviousGridBuyProfit8Price=GridBuyProfit8Price
			GridBuyProfit8Price=grid8BuyPrice	 +((grid8BuyPrice	 *GridBuyProfit8PriceCount )/Margin)
			LOCKPreviousGridBuyProfit8Price=1															   
		if(LOCKPreviousGridBuyProfit8Price==1 and	LastPriceTICKS	<  PreviousGridBuyProfit8Price	and PreviousGridBuyProfit8Price !=0):
			GridBuyProfit8PriceFunc()		
			#if(StopBuyFunc==0):grid8BuyFunc()					 

		if(GridBuyFlag9	 == 1  and LastPriceTICKS > GridBuyProfit9Price	and GridBuyProfit9Price !=0 and TradedamountBuy9 !=0  ):	
			GridBuyProfit9PriceCount=GridBuyProfit9PriceCount+.5
			PreviousGridBuyProfit9Price=GridBuyProfit9Price
			GridBuyProfit9Price=grid9BuyPrice	 +((grid9BuyPrice	 *GridBuyProfit9PriceCount )/Margin)
			LOCKPreviousGridBuyProfit9Price=1															   
		if(LOCKPreviousGridBuyProfit9Price==1 and	LastPriceTICKS	<  PreviousGridBuyProfit9Price	and PreviousGridBuyProfit9Price !=0):
			GridBuyProfit9PriceFunc()		
			#if(StopBuyFunc==0):grid9BuyFunc()
				 
				 
		if(GridBuyFlag10	 == 1  and LastPriceTICKS > GridBuyProfit10Price	and GridBuyProfit10Price !=0 and TradedamountBuy10!=0	 ):	
			GridBuyProfit10PriceCount=GridBuyProfit10PriceCount+.5
			PreviousGridBuyProfit10Price=GridBuyProfit10Price
			GridBuyProfit10Price=grid10BuyPrice	 +((grid10BuyPrice	 *GridBuyProfit10PriceCount )/Margin)
			LOCKPreviousGridBuyProfit10Price=1															   
		if(LOCKPreviousGridBuyProfit10Price==1 and	 LastPriceTICKS	 <	PreviousGridBuyProfit10Price  and PreviousGridBuyProfit10Price !=0):
			GridBuyProfit10PriceFunc()		
			#if(StopBuyFunc==0):grid10BuyFunc()
				 
		if(GridBuyFlag11	 == 1  and LastPriceTICKS > GridBuyProfit11Price	and GridBuyProfit11Price !=0 and TradedamountBuy11!=0	 ):	
			GridBuyProfit11PriceCount=GridBuyProfit11PriceCount+.5
			PreviousGridBuyProfit11Price=GridBuyProfit11Price
			GridBuyProfit11Price=grid11BuyPrice	 +((grid11BuyPrice	 *GridBuyProfit11PriceCount )/Margin)
			LOCKPreviousGridBuyProfit11Price=1															   
		if(LOCKPreviousGridBuyProfit11Price==1 and	 LastPriceTICKS	 <	PreviousGridBuyProfit11Price  and PreviousGridBuyProfit11Price !=0):
			GridBuyProfit11PriceFunc()		
			#if(StopBuyFunc==0):grid11BuyFunc()

		if(GridBuyFlag12	 == 1  and LastPriceTICKS > GridBuyProfit12Price	and GridBuyProfit12Price !=0 and TradedamountBuy12!=0	 ):	
			GridBuyProfit12PriceCount=GridBuyProfit12PriceCount+.5
			PreviousGridBuyProfit12Price=GridBuyProfit12Price
			GridBuyProfit12Price=grid12BuyPrice	 +((grid12BuyPrice	 *GridBuyProfit12PriceCount )/Margin)
			LOCKPreviousGridBuyProfit12Price=1															   
		if(LOCKPreviousGridBuyProfit12Price==1 and	 LastPriceTICKS	 <	PreviousGridBuyProfit12Price  and PreviousGridBuyProfit12Price !=0):
			GridBuyProfit12PriceFunc()		
			#if(StopBuyFunc==0):grid12BuyFunc()

		if(GridBuyFlag13	 == 1  and LastPriceTICKS > GridBuyProfit13Price	and GridBuyProfit13Price !=0 and TradedamountBuy13!=0	 ):	
			GridBuyProfit13PriceCount=GridBuyProfit13PriceCount+.5
			PreviousGridBuyProfit13Price=GridBuyProfit13Price
			GridBuyProfit13Price=grid13BuyPrice	 +((grid13BuyPrice	 *GridBuyProfit13PriceCount )/Margin)
			LOCKPreviousGridBuyProfit13Price=1															   
		if(LOCKPreviousGridBuyProfit13Price==1 and	 LastPriceTICKS	 <	PreviousGridBuyProfit13Price  and PreviousGridBuyProfit13Price !=0):
			GridBuyProfit13PriceFunc()		
			#if(StopBuyFunc==0):grid13BuyFunc()

		if(GridBuyFlag14	 == 1  and LastPriceTICKS > GridBuyProfit14Price	and GridBuyProfit14Price !=0 and TradedamountBuy14!=0	 ):	
			GridBuyProfit14PriceCount=GridBuyProfit14PriceCount+.5
			PreviousGridBuyProfit14Price=GridBuyProfit14Price
			GridBuyProfit14Price=grid14BuyPrice	 +((grid14BuyPrice	 *GridBuyProfit14PriceCount )/Margin)
			LOCKPreviousGridBuyProfit14Price=1															   
		if(LOCKPreviousGridBuyProfit14Price==1 and	 LastPriceTICKS	 <	PreviousGridBuyProfit14Price  and PreviousGridBuyProfit14Price !=0):
			GridBuyProfit14PriceFunc()		
			#if(StopBuyFunc==0):grid14BuyFunc()
		
		if(GridBuyFlag15	 == 1  and LastPriceTICKS > GridBuyProfit15Price	and GridBuyProfit15Price !=0 and TradedamountBuy15!=0	 ):	
			GridBuyProfit15PriceCount=GridBuyProfit15PriceCount+.5
			PreviousGridBuyProfit15Price=GridBuyProfit15Price
			GridBuyProfit15Price=grid15BuyPrice	 +((grid15BuyPrice	 *GridBuyProfit15PriceCount )/Margin)
			LOCKPreviousGridBuyProfit15Price=1															   
		if(LOCKPreviousGridBuyProfit15Price==1 and	 LastPriceTICKS	 <	PreviousGridBuyProfit15Price  and PreviousGridBuyProfit15Price !=0):
			GridBuyProfit15PriceFunc()		
			#if(StopBuyFunc==0):grid15BuyFunc()

		if(GridBuyFlag16	 == 1  and LastPriceTICKS > GridBuyProfit16Price	and GridBuyProfit16Price !=0 and TradedamountBuy16!=0	 ):	
			GridBuyProfit16PriceCount=GridBuyProfit16PriceCount+.5
			PreviousGridBuyProfit16Price=GridBuyProfit16Price
			GridBuyProfit16Price=grid16BuyPrice	 +((grid16BuyPrice	 *GridBuyProfit16PriceCount )/Margin)
			LOCKPreviousGridBuyProfit16Price=1															   
		if(LOCKPreviousGridBuyProfit16Price==1 and	 LastPriceTICKS	 <	PreviousGridBuyProfit16Price  and PreviousGridBuyProfit16Price !=0):
			GridBuyProfit16PriceFunc()		
			#if(StopBuyFunc==0):grid16BuyFunc()

						 
		if(GridBuyFlag17	 == 1  and LastPriceTICKS > GridBuyProfit17Price	and GridBuyProfit17Price !=0 and TradedamountBuy17!=0	 ):	
			GridBuyProfit17PriceCount=GridBuyProfit17PriceCount+.5
			PreviousGridBuyProfit17Price=GridBuyProfit17Price
			GridBuyProfit17Price=grid17BuyPrice	 +((grid17BuyPrice	 *GridBuyProfit17PriceCount )/Margin)
			LOCKPreviousGridBuyProfit17Price=1															   
		if(LOCKPreviousGridBuyProfit17Price==1 and	 LastPriceTICKS	 <	PreviousGridBuyProfit17Price  and PreviousGridBuyProfit17Price !=0):
			GridBuyProfit17PriceFunc()		
			#if(StopBuyFunc==0):grid17BuyFunc()


		if(GridBuyFlag18	 == 1  and LastPriceTICKS > GridBuyProfit18Price	and GridBuyProfit18Price !=0 and TradedamountBuy18!=0	 ):	
			GridBuyProfit18PriceCount=GridBuyProfit18PriceCount+.5
			PreviousGridBuyProfit18Price=GridBuyProfit18Price
			GridBuyProfit18Price=grid18BuyPrice	 +((grid18BuyPrice	 *GridBuyProfit18PriceCount )/Margin)
			LOCKPreviousGridBuyProfit18Price=1															   
		if(LOCKPreviousGridBuyProfit18Price==1 and	 LastPriceTICKS	 <	PreviousGridBuyProfit18Price  and PreviousGridBuyProfit18Price !=0):
			GridBuyProfit18PriceFunc()		
			#if(StopBuyFunc==0):grid18BuyFunc()
				 
		
		if(GridBuyFlag19	 == 1  and LastPriceTICKS > GridBuyProfit19Price	and GridBuyProfit19Price !=0 and TradedamountBuy19!=0	 ):	
			GridBuyProfit19PriceCount=GridBuyProfit19PriceCount+.5
			PreviousGridBuyProfit19Price=GridBuyProfit19Price
			GridBuyProfit19Price=grid19BuyPrice	 +((grid19BuyPrice	 *GridBuyProfit19PriceCount )/Margin)
			LOCKPreviousGridBuyProfit19Price=1															   
		if(LOCKPreviousGridBuyProfit19Price==1 and	 LastPriceTICKS	 <	PreviousGridBuyProfit19Price  and PreviousGridBuyProfit19Price !=0):
			GridBuyProfit19PriceFunc()		
			#if(StopBuyFunc==0):grid19BuyFunc()		


		if(GridBuyFlag20	 == 1  and LastPriceTICKS > GridBuyProfit20Price	and GridBuyProfit20Price !=0 and TradedamountBuy20!=0	 ):	
			GridBuyProfit20PriceCount=GridBuyProfit20PriceCount+.5
			PreviousGridBuyProfit20Price=GridBuyProfit20Price
			GridBuyProfit20Price=grid20BuyPrice	 +((grid20BuyPrice	 *GridBuyProfit20PriceCount )/Margin)
			LOCKPreviousGridBuyProfit20Price=1															   
		if(LOCKPreviousGridBuyProfit20Price==1 and	 LastPriceTICKS	 <	PreviousGridBuyProfit20Price  and PreviousGridBuyProfit20Price !=0):
			GridBuyProfit20PriceFunc()		
			#if(StopBuyFunc==0):grid20BuyFunc()
				 
				 

		if(GridBuyFlag21	 == 1  and LastPriceTICKS > GridBuyProfit21Price	and GridBuyProfit21Price !=0 and TradedamountBuy21!=0	 ):	
			GridBuyProfit21PriceCount=GridBuyProfit21PriceCount+.5
			PreviousGridBuyProfit21Price=GridBuyProfit21Price
			GridBuyProfit21Price=grid21BuyPrice	 +((grid21BuyPrice	 *GridBuyProfit21PriceCount )/Margin)
			LOCKPreviousGridBuyProfit21Price=1															   
		if(LOCKPreviousGridBuyProfit21Price==1 and	 LastPriceTICKS	 <	PreviousGridBuyProfit21Price  and PreviousGridBuyProfit21Price !=0):
			GridBuyProfit21PriceFunc()		
			#if(StopBuyFunc==0):grid21BuyFunc()
				 
				 
		if(GridBuyFlag22	 == 1  and LastPriceTICKS > GridBuyProfit22Price	and GridBuyProfit22Price !=0 and TradedamountBuy22!=0	 ):	
			GridBuyProfit22PriceCount=GridBuyProfit22PriceCount+.5
			PreviousGridBuyProfit22Price=GridBuyProfit22Price
			GridBuyProfit22Price=grid22BuyPrice	 +((grid22BuyPrice	 *GridBuyProfit22PriceCount )/Margin)
			LOCKPreviousGridBuyProfit22Price=1															   
		if(LOCKPreviousGridBuyProfit22Price==1 and	 LastPriceTICKS	 <	PreviousGridBuyProfit22Price  and PreviousGridBuyProfit22Price !=0):
			GridBuyProfit22PriceFunc()		
			#if(StopBuyFunc==0):grid22BuyFunc()
				 
		if(GridBuyFlag23	 == 1  and LastPriceTICKS > GridBuyProfit23Price	and GridBuyProfit23Price !=0 and TradedamountBuy23!=0	 ):	
			GridBuyProfit23PriceCount=GridBuyProfit23PriceCount+.5
			PreviousGridBuyProfit23Price=GridBuyProfit23Price
			GridBuyProfit23Price=grid23BuyPrice	 +((grid23BuyPrice	 *GridBuyProfit23PriceCount )/Margin)
			LOCKPreviousGridBuyProfit23Price=1															   
		if(LOCKPreviousGridBuyProfit23Price==1 and	 LastPriceTICKS	 <	PreviousGridBuyProfit23Price  and PreviousGridBuyProfit23Price !=0):
			GridBuyProfit23PriceFunc()		
			#if(StopBuyFunc==0):grid23BuyFunc()

		if(GridBuyFlag24	 == 1  and LastPriceTICKS > GridBuyProfit24Price	and GridBuyProfit24Price !=0 and TradedamountBuy24!=0	 ):	
			GridBuyProfit24PriceCount=GridBuyProfit24PriceCount+.5
			PreviousGridBuyProfit24Price=GridBuyProfit24Price
			GridBuyProfit24Price=grid24BuyPrice	 +((grid24BuyPrice	 *GridBuyProfit24PriceCount )/Margin)
			LOCKPreviousGridBuyProfit24Price=1															   
		if(LOCKPreviousGridBuyProfit24Price==1 and	 LastPriceTICKS	 <	PreviousGridBuyProfit24Price  and PreviousGridBuyProfit24Price !=0):
			GridBuyProfit24PriceFunc()		
			#if(StopBuyFunc==0):grid24BuyFunc()

		if(GridBuyFlag25	 == 1  and LastPriceTICKS > GridBuyProfit25Price	and GridBuyProfit25Price !=0 and TradedamountBuy25!=0	 ):	
			GridBuyProfit25PriceCount=GridBuyProfit25PriceCount+.5
			PreviousGridBuyProfit25Price=GridBuyProfit25Price
			GridBuyProfit25Price=grid25BuyPrice	 +((grid25BuyPrice	 *GridBuyProfit25PriceCount )/Margin)
			LOCKPreviousGridBuyProfit25Price=1															   
		if(LOCKPreviousGridBuyProfit25Price==1 and	 LastPriceTICKS	 <	PreviousGridBuyProfit25Price  and PreviousGridBuyProfit25Price !=0):
			GridBuyProfit25PriceFunc()		
			#if(StopBuyFunc==0):grid25BuyFunc()

		if(GridBuyFlag26	 == 1  and LastPriceTICKS > GridBuyProfit26Price	and GridBuyProfit26Price !=0 and TradedamountBuy26!=0	 ):	
			GridBuyProfit26PriceCount=GridBuyProfit26PriceCount+.5
			PreviousGridBuyProfit26Price=GridBuyProfit26Price
			GridBuyProfit26Price=grid26BuyPrice	 +((grid26BuyPrice	 *GridBuyProfit26PriceCount )/Margin)
			LOCKPreviousGridBuyProfit26Price=1															   
		if(LOCKPreviousGridBuyProfit26Price==1 and	 LastPriceTICKS	 <	PreviousGridBuyProfit26Price  and PreviousGridBuyProfit26Price !=0):
			GridBuyProfit26PriceFunc()		
			#if(StopBuyFunc==0):grid26BuyFunc()

		if(GridBuyFlag27	 == 1  and LastPriceTICKS > GridBuyProfit27Price	and GridBuyProfit27Price !=0 and TradedamountBuy27!=0	 ):	
			GridBuyProfit27PriceCount=GridBuyProfit27PriceCount+.5
			PreviousGridBuyProfit27Price=GridBuyProfit27Price
			GridBuyProfit27Price=grid27BuyPrice	 +((grid27BuyPrice	 *GridBuyProfit27PriceCount )/Margin)
			LOCKPreviousGridBuyProfit27Price=1															   
		if(LOCKPreviousGridBuyProfit27Price==1 and	 LastPriceTICKS	 <	PreviousGridBuyProfit27Price  and PreviousGridBuyProfit27Price !=0):
			GridBuyProfit27PriceFunc()		
			#if(StopBuyFunc==0):grid27BuyFunc()

		if(GridBuyFlag28	 == 1  and LastPriceTICKS > GridBuyProfit28Price	and GridBuyProfit28Price !=0 and TradedamountBuy28!=0	 ):	
			GridBuyProfit28PriceCount=GridBuyProfit28PriceCount+.5
			PreviousGridBuyProfit28Price=GridBuyProfit28Price
			GridBuyProfit28Price=grid28BuyPrice	 +((grid28BuyPrice	 *GridBuyProfit28PriceCount )/Margin)
			LOCKPreviousGridBuyProfit28Price=1															   
		if(LOCKPreviousGridBuyProfit28Price==1 and	 LastPriceTICKS	 <	PreviousGridBuyProfit28Price  and PreviousGridBuyProfit28Price !=0):
			GridBuyProfit28PriceFunc()		
			#if(StopBuyFunc==0):grid28BuyFunc()

		if(GridBuyFlag29	 == 1  and LastPriceTICKS > GridBuyProfit29Price	and GridBuyProfit29Price !=0 and TradedamountBuy29!=0	 ):	
			GridBuyProfit29PriceCount=GridBuyProfit29PriceCount+.5
			PreviousGridBuyProfit29Price=GridBuyProfit29Price
			GridBuyProfit29Price=grid29BuyPrice	 +((grid29BuyPrice	 *GridBuyProfit29PriceCount )/Margin)
			LOCKPreviousGridBuyProfit29Price=1															   
		if(LOCKPreviousGridBuyProfit29Price==1 and	 LastPriceTICKS	 <	PreviousGridBuyProfit29Price  and PreviousGridBuyProfit29Price !=0):
			GridBuyProfit29PriceFunc()		
			#if(StopBuyFunc==0):grid29BuyFunc()

		if(GridBuyFlag30	 == 1  and LastPriceTICKS > GridBuyProfit30Price	and GridBuyProfit30Price !=0 and TradedamountBuy30!=0	 ):	
			GridBuyProfit30PriceCount=GridBuyProfit30PriceCount+.5
			PreviousGridBuyProfit30Price=GridBuyProfit30Price
			GridBuyProfit30Price=grid30BuyPrice	 +((grid30BuyPrice	 *GridBuyProfit30PriceCount )/Margin)
			LOCKPreviousGridBuyProfit30Price=1															   
		if(LOCKPreviousGridBuyProfit30Price==1 and	 LastPriceTICKS	 <	PreviousGridBuyProfit30Price  and PreviousGridBuyProfit30Price !=0):
			GridBuyProfit30PriceFunc()		
			#if(StopBuyFunc==0):grid30BuyFunc()			 

		# # ########################	  ######################## ######################## ######################## ######################## ########################	SHORTING		 
		
		def GridSellProfit0PriceFunc():
			global	LongGridWithIndicator0
			global	GridSellFlag0
			global	TradedamountSell0
			global	GridSellProfit0Price
			global GridSell0ProfitFuncHandle
			global SN1M
			global GridSellProfit0PriceCount
			global LOCKPreviousGridSellProfit0Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit0Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell0
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid0SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator0=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit0PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit0Price=0
			GridSellFlag0=0
			TradedamountSell0=0
			GridSellProfit0Price=0
			GridSell0ProfitFuncHandle=1
	
		def GridSellProfit1PriceFunc():
			global	LongGridWithIndicator1
			global GridSellFlag1
			global TradedamountSell1
			global GridSellProfit1Price
			global SN1M
			global GridSellProfit1PriceCount
			global LOCKPreviousGridSellProfit1Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit1Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell1
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid1SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator1=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit1PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit1Price=0
			GridSellFlag1=0
			TradedamountSell1=0
			GridSellProfit1Price=0
	
		
		def GridSellProfit2PriceFunc():
			global	LongGridWithIndicator2
			global GridSellFlag2
			global TradedamountSell2
			global GridSellProfit2Price
			global SN1M
			global GridSellProfit2PriceCount
			global LOCKPreviousGridSellProfit2Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit2Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell2
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid2SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator2=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit2PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit2Price=0
			GridSellFlag2=0
			TradedamountSell2=0
			GridSellProfit2Price=0
		
		def GridSellProfit3PriceFunc():
			global	LongGridWithIndicator3
			global GridSellFlag3
			global TradedamountSell3
			global GridSellProfit3Price
			global SN1M
			global GridSellProfit3PriceCount
			global LOCKPreviousGridSellProfit3Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit3Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell3
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid3SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator3=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit3PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit3Price=0
			GridSellFlag3=0
			TradedamountSell3=0
			GridSellProfit3Price=0
	
		def GridSellProfit4PriceFunc():
			global	LongGridWithIndicator4
			global	GridSellFlag4
			global	TradedamountSell4
			global	GridSellProfit4Price
			global SN1M
			global GridSellProfit4PriceCount
			global LOCKPreviousGridSellProfit4Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit4Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell4
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid4SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator4=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit4PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit4Price=0
			GridSellFlag4=0
			TradedamountSell4=0
			GridSellProfit4Price=0			
	
		def GridSellProfit5PriceFunc():
			global	LongGridWithIndicator5
			global	GridSellFlag5
			global	TradedamountSell5
			global	GridSellProfit5Price
			global SN1M
			global GridSellProfit5PriceCount
			global LOCKPreviousGridSellProfit5Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit5Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell5
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid5SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator5=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit5PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit5Price=0
			GridSellFlag5=0
			TradedamountSell5=0
			GridSellProfit5Price=0
	
		def GridSellProfit6PriceFunc():
			global	LongGridWithIndicator6
			global	GridSellFlag6
			global	TradedamountSell6
			global	GridSellProfit6Price
			global SN1M
			global GridSellProfit6PriceCount
			global LOCKPreviousGridSellProfit6Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit6Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell6
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid6SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator6=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit6PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit6Price=0
			GridSellFlag6=0
			TradedamountSell6=0
			GridSellProfit6Price=0
	
		
		def GridSellProfit7PriceFunc():
			global	LongGridWithIndicator7
			global	GridSellFlag7
			global	TradedamountSell7
			global	GridSellProfit7Price
			global SN1M
			global GridSellProfit7PriceCount
			global LOCKPreviousGridSellProfit7Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit7Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell7
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid7SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator7=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit7PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit7Price=0
			GridSellFlag7=0
			TradedamountSell7=0
			GridSellProfit7Price=0
		
		def GridSellProfit8PriceFunc():
			global	LongGridWithIndicator8
			global	GridSellFlag8
			global	TradedamountSell8
			global	GridSellProfit8Price
			global SN1M
			global GridSellProfit8PriceCount
			global LOCKPreviousGridSellProfit8Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit8Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell8
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid8SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator8=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit8PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit8Price=0
			GridSellFlag8=0
			TradedamountSell8=0
			GridSellProfit8Price=0
	
		def GridSellProfit9PriceFunc():
			global	LongGridWithIndicator9
			global	GridSellFlag9
			global	TradedamountSell9
			global	GridSellProfit9Price
			global SN1M
			global GridSellProfit9PriceCount
			global LOCKPreviousGridSellProfit9Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit9Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell9
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid9SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator9=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit9PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit9Price=0
			GridSellFlag9=0
			TradedamountSell9=0
			GridSellProfit9Price=0			
	
		def GridSellProfit10PriceFunc():
			global	LongGridWithIndicator10
			global	GridSellFlag10
			global	TradedamountSell10
			global	GridSellProfit10Price
			global SN1M
			global GridSellProfit10PriceCount
			global LOCKPreviousGridSellProfit10Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit10Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell10
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid10SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator10=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit10PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit10Price=0
			GridSellFlag10=0
			TradedamountSell10=0
			GridSellProfit10Price=0
	
		def GridSellProfit11PriceFunc():
			global	LongGridWithIndicator11
			global	GridSellFlag11
			global	TradedamountSell11
			global	GridSellProfit11Price
			global SN1M
			global GridSellProfit11PriceCount
			global LOCKPreviousGridSellProfit11Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit11Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell11
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid11SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator11=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit11PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit11Price=0
			GridSellFlag11=0
			TradedamountSell11=0
			GridSellProfit11Price=0
	
		
		def GridSellProfit12PriceFunc():
			global	LongGridWithIndicator12
			global	GridSellFlag12
			global	TradedamountSell12
			global	GridSellProfit12Price
			global SN1M
			global GridSellProfit12PriceCount
			global LOCKPreviousGridSellProfit12Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit12Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell12
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid12SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator12=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit12PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit12Price=0
			GridSellFlag12=0
			TradedamountSell12=0
			GridSellProfit12Price=0
		
		def GridSellProfit13PriceFunc():
			global	LongGridWithIndicator13
			global	GridSellFlag13
			global	TradedamountSell13
			global	GridSellProfit13Price
			global SN1M
			global GridSellProfit13PriceCount
			global LOCKPreviousGridSellProfit13Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit13Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell13
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid13SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator13=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit13PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit13Price=0
			GridSellFlag13=0
			TradedamountSell13=0
			GridSellProfit13Price=0
	
		def GridSellProfit14PriceFunc():
			global	LongGridWithIndicator14
			global	GridSellFlag14
			global	TradedamountSell14
			global	GridSellProfit14Price
			global SN1M
			global GridSellProfit14PriceCount
			global LOCKPreviousGridSellProfit14Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit14Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell14
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid14SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator14=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit14PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit14Price=0
			GridSellFlag14=0	
			TradedamountSell14=0
			GridSellProfit14Price=0
	
		def GridSellProfit15PriceFunc():
			global	LongGridWithIndicator15
			global	GridSellFlag15
			global	TradedamountSell15
			global	GridSellProfit15Price
			global SN1M
			global GridSellProfit15PriceCount
			global LOCKPreviousGridSellProfit15Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit15Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell15
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid15SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator15=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit15PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit15Price=0
			GridSellFlag15=0
			TradedamountSell15=0
			GridSellProfit15Price=0
	
		def GridSellProfit16PriceFunc():
			global	LongGridWithIndicator16
			global	GridSellFlag16
			global	TradedamountSell16
			global	GridSellProfit16Price
			global SN1M
			global GridSellProfit16PriceCount
			global LOCKPreviousGridSellProfit16Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit16Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell16
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid16SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator16=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit16PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit16Price=0
			GridSellFlag16=0
			TradedamountSell16=0
			GridSellProfit16Price=0
	
		
		def GridSellProfit17PriceFunc():
			global	LongGridWithIndicator17
			global	GridSellFlag17
			global	TradedamountSell17
			global	GridSellProfit17Price
			global SN1M
			global GridSellProfit17PriceCount
			global LOCKPreviousGridSellProfit17Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit17Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell17
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid17SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator17=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit17PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit17Price=0
			GridSellFlag17=0
			TradedamountSell17=0
			GridSellProfit17Price=0
		
		def GridSellProfit18PriceFunc():
			global	LongGridWithIndicator18
			global	GridSellFlag18
			global	TradedamountSell18
			global	GridSellProfit18Price
			global SN1M
			global GridSellProfit18PriceCount
			global LOCKPreviousGridSellProfit18Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit18Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell18
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid18SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator18=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit18PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit18Price=0
			GridSellFlag18=0
			TradedamountSell18=0
			GridSellProfit18Price=0
	
		def GridSellProfit19PriceFunc():
			global	LongGridWithIndicator19
			global	GridSellFlag19
			global	TradedamountSell19
			global	GridSellProfit19Price
			global SN1M
			global GridSellProfit19PriceCount
			global LOCKPreviousGridSellProfit19Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit19Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell19
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid19SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator19=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit19PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit19Price=0
			GridSellFlag19=0
			TradedamountSell19=0
			GridSellProfit19Price=0			
	
		def GridSellProfit20PriceFunc():
			global	LongGridWithIndicator20
			global	GridSellFlag20
			global	TradedamountSell20
			global	GridSellProfit20Price
			global SN1M
			global GridSellProfit20PriceCount
			global LOCKPreviousGridSellProfit20Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit20Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell20
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid20SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator20=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit20PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit20Price=0
			GridSellFlag20=0
			TradedamountSell20=0
			GridSellProfit20Price=0
	
		def GridSellProfit21PriceFunc():
			global	LongGridWithIndicator21
			global	GridSellFlag21
			global	TradedamountSell21
			global	GridSellProfit21Price
			global SN1M
			global GridSellProfit21PriceCount
			global LOCKPreviousGridSellProfit21Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit21Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell21
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid21SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator21=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit21PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit21Price=0
			GridSellFlag21=0
			TradedamountSell21=0
			GridSellProfit21Price=0
	
		
		def GridSellProfit22PriceFunc():
			global	LongGridWithIndicator22
			global	GridSellFlag22
			global	TradedamountSell22
			global	GridSellProfit22Price
			global SN1M
			global GridSellProfit22PriceCount
			global LOCKPreviousGridSellProfit22Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit22Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell22
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid22SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator22=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit22PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit22Price=0
			GridSellFlag22=0
			TradedamountSell22=0
			GridSellProfit22Price=0
		
		def GridSellProfit23PriceFunc():
			global	LongGridWithIndicator23
			global	GridSellFlag23
			global	TradedamountSell23
			global	GridSellProfit23Price
			global SN1M
			global GridSellProfit23PriceCount
			global LOCKPreviousGridSellProfit23Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit23Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell23
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid23SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator23=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit23PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit23Price=0
			GridSellFlag23=0
			TradedamountSell23=0
			GridSellProfit23Price=0
	
		def GridSellProfit24PriceFunc():
			global	LongGridWithIndicator24
			global	GridSellFlag24
			global	TradedamountSell24
			global	GridSellProfit24Price
			global SN1M
			global GridSellProfit24PriceCount
			global LOCKPreviousGridSellProfit24Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit24Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell24
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid24SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator24=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit24PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit24Price=0
			GridSellFlag24=0
			TradedamountSell24=0
			GridSellProfit24Price=0
	
		def GridSellProfit25PriceFunc():
			global	LongGridWithIndicator25
			global	GridSellFlag25
			global	TradedamountSell25
			global	GridSellProfit25Price
			global SN1M
			global GridSellProfit25PriceCount
			global LOCKPreviousGridSellProfit25Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit25Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell25
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid25SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator25=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit25PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit25Price=0
			GridSellFlag25=0
			TradedamountSell25=0
			GridSellProfit25Price=0
	
		def GridSellProfit26PriceFunc():
			global	LongGridWithIndicator26
			global	GridSellFlag26
			global	TradedamountSell26
			global	GridSellProfit26Price
			global SN1M
			global GridSellProfit26PriceCount
			global LOCKPreviousGridSellProfit26Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit26Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell26
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid26SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator26=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit26PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit26Price=0
			GridSellFlag26=0
			TradedamountSell26=0
			GridSellProfit26Price=0
	
		
		def GridSellProfit27PriceFunc():
			global	LongGridWithIndicator27
			global	GridSellFlag27
			global	TradedamountSell27
			global	GridSellProfit27Price
			global SN1M
			global GridSellProfit27PriceCount
			global LOCKPreviousGridSellProfit27Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit27Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell27
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid27SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator27=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit27PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit27Price=0
			GridSellFlag27=0
			TradedamountSell27=0
			GridSellProfit27Price=0
		
		def GridSellProfit28PriceFunc():
			global	LongGridWithIndicator28
			global	GridSellFlag28
			global	TradedamountSell28
			global	GridSellProfit28Price
			global SN1M
			global GridSellProfit28PriceCount
			global LOCKPreviousGridSellProfit28Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit28Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell28
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid28SellPrice*Orderamount)
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit28PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit28Price=0
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator28=0
			GridSellFlag28=0
			TradedamountSell28=0
			GridSellProfit28Price=0
	
		def GridSellProfit29PriceFunc():
			global	LongGridWithIndicator29
			global	GridSellFlag29
			global	TradedamountSell29
			global	GridSellProfit29Price
			global SN1M
			global GridSellProfit29PriceCount
			global LOCKPreviousGridSellProfit29Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit29Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell29
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid29SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator29=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit29PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit29Price=0
			GridSellFlag29=0
			TradedamountSell29=0
			GridSellProfit29Price=0
		
		def GridSellProfit30PriceFunc():
			global	LongGridWithIndicator30
			global	GridSellFlag30	
			global	TradedamountSell30
			global	GridSellProfit30Price
			global SN1M
			global GridSellProfit30PriceCount
			global LOCKPreviousGridSellProfit30Price
			Ordertype='Buy'
			Orderside='market'
			Orderprice=GridSellProfit30Price
			OrderActionWas='Buy'
			OrderActionTakenGlobal="Buy"
			Orderamount=TradedamountSell30
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'),Orderamount,"BTCBalanceFree",BTCBalanceFree)
			PositionPriceIndollars=(grid30SellPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.02)/100
			LongGridWithIndicator30=0
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			with open(ResultFile, 'a', newline='') as file:
				writer = csv.writer(file)
				writer.writerow([SN1M, dt_string1M,Ordertype,Orderamount,Orderprice,FeesMarket,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType])
				SN1M=SN1M+1
			GridSellProfit30PriceCount=GlobalProfit
			LOCKPreviousGridSellProfit30Price=0
			GridSellFlag30=0	
			TradedamountSell30=0
			GridSellProfit30Price=0
	
		# #####################################	 NEW GRID with Indicators
		if(BuyDirectinalGrid==1 and SellDirectinalGrid==0 and StartGrid==1	   and	MACDType==1 and LongerTimeFrame=="LONG"):		 # ######### Only 15 Times 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator0==0:
				grid0BuyFunc()				
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator1==0:
				grid1BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator2==0:
				grid2BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator3==0:
				grid3BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator4==0:
				grid4BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator5==0:
				grid5BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator6==0:
				grid6BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator7==0:
				grid7BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator8==0:
				grid8BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator9==0:
				grid9BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator10==0:
				grid10BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator11==0:
				grid11BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator12==0:
				grid12BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator13==0:
				grid13BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator14==0:
				grid14BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator15==0:
				grid15BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	 and LongGridWithIndicator16==0:
				grid16BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	 and LongGridWithIndicator17==0:
				grid17BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	 and LongGridWithIndicator18==0:
				grid18BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	 and LongGridWithIndicator19==0:
				grid19BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	 and LongGridWithIndicator20==0:
				grid20BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	and LongGridWithIndicator21==0:
				grid21BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	and LongGridWithIndicator22==0:
				grid22BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	and LongGridWithIndicator23==0:
				grid23BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	and LongGridWithIndicator24==0:
				grid24BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	and LongGridWithIndicator25==0:
				grid25BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	and LongGridWithIndicator26==0:
				grid26BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	and LongGridWithIndicator27==0:
				grid27BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	and LongGridWithIndicator28==0:
				grid28BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	and LongGridWithIndicator29==0:
				grid29BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	and LongGridWithIndicator30==0:
				grid30BuyFunc()
				SubjectGlobal="NONE"
		
			
		if(BuyDirectinalGrid==0 and SellDirectinalGrid==1 and StartGrid==1	  and  MACDType==1 and LongerTimeFrame=="SHORT"):	 # ######### Only 15 Times 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator0==0:
				grid0SellFunc()				
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator1==0:
				grid1SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator2==0:
				grid2SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator3==0:
				grid3SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator4==0:
				grid4SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator5==0:
				grid5SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator6==0:
				grid6SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator7==0:
				grid7SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator8==0:
				grid8SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator9==0:
				grid9SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator10==0:
				grid10SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator11==0:
				grid11SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator12==0:
				grid12SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator13==0:
				grid13SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator14==0:
				grid14SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator15==0:
				grid15SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator16==0:
				grid16SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator17==0:
				grid17SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator18==0:
				grid18SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator19==0:
				grid19SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator20==0:
				grid20SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	 and SHORTGridWithIndicator21==0:
				grid21SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	 and SHORTGridWithIndicator22==0:
				grid22SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	 and SHORTGridWithIndicator23==0:
				grid23SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	 and SHORTGridWithIndicator24==0:
				grid24SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	 and SHORTGridWithIndicator25==0:
				grid25SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	 and SHORTGridWithIndicator26==0:
				grid26SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	 and SHORTGridWithIndicator27==0:
				grid27SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	 and SHORTGridWithIndicator28==0:
				grid28SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	 and SHORTGridWithIndicator29==0:
				grid29SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	 and SHORTGridWithIndicator30==0:
				grid30SellFunc()
				SubjectGlobal="NONE"		
		
		# #####################################	 NEW GRID with Indicators
		if(BuyDirectinalGrid==1 and SellDirectinalGrid==0 and StartGrid==1		  and  MACDType==0 and LongerTimeFrame=="LONG"):		
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator0==0:
				grid0BuyFunc()				
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator1==0:
				grid1BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator2==0:
				grid2BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator3==0:
				grid3BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator4==0:
				grid4BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator5==0:
				grid5BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator6==0:
				grid6BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator7==0:
				grid7BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator8==0:
				grid8BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator9==0:
				grid9BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator10==0:
				grid10BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator11==0:
				grid11BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator12==0:
				grid12BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator13==0:
				grid13BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator14==0:
				grid14BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator15==0:
				grid15BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator16==0:
				grid16BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator17==0:
				grid17BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator18==0:
				grid18BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator19==0:
				grid19BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0  and LongGridWithIndicator20==0:
				grid20BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	and LongGridWithIndicator21==0:
				grid21BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	and LongGridWithIndicator22==0:
				grid22BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	and LongGridWithIndicator23==0:
				grid23BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	and LongGridWithIndicator24==0:
				grid24BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	and LongGridWithIndicator25==0:
				grid25BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	and LongGridWithIndicator26==0:
				grid26BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	and LongGridWithIndicator27==0:
				grid27BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	and LongGridWithIndicator28==0:
				grid28BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	and LongGridWithIndicator29==0:
				grid29BuyFunc()
				SubjectGlobal="NONE"														 
			if "LONG" == SubjectGlobal and totalWalletBalance !=0	and LongGridWithIndicator30==0:
				grid30BuyFunc()
				SubjectGlobal="NONE"
		
			
		if(BuyDirectinalGrid==0 and SellDirectinalGrid==1 and StartGrid==1			 and  MACDType==0 and LongerTimeFrame=="SHORT"):
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator0==0:
				grid0SellFunc()				
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator1==0:
				grid1SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator2==0:
				grid2SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator3==0:
				grid3SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator4==0:
				grid4SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator5==0:
				grid5SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator6==0:
				grid6SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator7==0:
				grid7SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator8==0:
				grid8SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator9==0:
				grid9SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator10==0:
				grid10SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator11==0:
				grid11SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator12==0:
				grid12SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator13==0:
				grid13SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator14==0:
				grid14SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator15==0:
				grid15SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator16==0:
				grid16SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator17==0:
				grid17SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator18==0:
				grid18SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator19==0:
				grid19SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	and SHORTGridWithIndicator20==0:
				grid20SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	 and SHORTGridWithIndicator21==0:
				grid21SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	 and SHORTGridWithIndicator22==0:
				grid22SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	 and SHORTGridWithIndicator23==0:
				grid23SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	 and SHORTGridWithIndicator24==0:
				grid24SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	 and SHORTGridWithIndicator25==0:
				grid25SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	 and SHORTGridWithIndicator26==0:
				grid26SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	 and SHORTGridWithIndicator27==0:
				grid27SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	 and SHORTGridWithIndicator28==0:
				grid28SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	 and SHORTGridWithIndicator29==0:
				grid29SellFunc()
				SubjectGlobal="NONE"														 
			if "SHORT" == SubjectGlobal and totalWalletBalance !=0	 and SHORTGridWithIndicator30==0:
				grid30SellFunc()
				SubjectGlobal="NONE"		
			





		if(GridSellFlag0	 == 1 and LastPriceTICKS  <	 GridSellProfit0Price	and GridSellProfit0Price !=0 and TradedamountSell0 !=0	):	
			GridSellProfit0PriceCount=GridSellProfit0PriceCount+.5
			PreviousGridSellProfit0Price=GridSellProfit0Price
			GridSellProfit0Price=grid0SellPrice	 -((grid0SellPrice*GridSellProfit0PriceCount )/Margin)
			LOCKPreviousGridSellProfit0Price=1															   
		if(LOCKPreviousGridSellProfit0Price==1 and	LastPriceTICKS	>	PreviousGridSellProfit0Price and PreviousGridSellProfit0Price !=0):
			GridSellProfit0PriceFunc()		
			#if(StopSellFunc==0):grid0SellFunc()
	
		if(GridSellFlag1	 == 1 and LastPriceTICKS  <	 GridSellProfit1Price	and GridSellProfit1Price !=0 and TradedamountSell1 !=0	):	
			GridSellProfit1PriceCount=GridSellProfit1PriceCount+.5
			PreviousGridSellProfit1Price=GridSellProfit1Price
			GridSellProfit1Price=grid1SellPrice	 -((grid1SellPrice	 *GridSellProfit1PriceCount )/Margin)
			LOCKPreviousGridSellProfit1Price=1															   
		if(LOCKPreviousGridSellProfit1Price==1 and	LastPriceTICKS	>	PreviousGridSellProfit1Price  and PreviousGridSellProfit1Price !=0):
			GridSellProfit1PriceFunc()		
			#if(StopSellFunc==0):grid1SellFunc()
		
		
		if(GridSellFlag2	 == 1  and LastPriceTICKS  <  GridSellProfit2Price	and GridSellProfit2Price !=0 and TradedamountSell2 !=0	):	
			GridSellProfit2PriceCount=GridSellProfit2PriceCount+.5
			PreviousGridSellProfit2Price=GridSellProfit2Price
			GridSellProfit2Price=grid2SellPrice	 -((grid2SellPrice	 *GridSellProfit2PriceCount )/Margin)
			LOCKPreviousGridSellProfit2Price=1															   
		if(LOCKPreviousGridSellProfit2Price==1 and	LastPriceTICKS	>	PreviousGridSellProfit2Price  and PreviousGridSellProfit2Price !=0):
			GridSellProfit2PriceFunc()		
			#if(StopSellFunc==0):grid2SellFunc()
		
	
		if(GridSellFlag3	 == 1  and LastPriceTICKS  <  GridSellProfit3Price	and GridSellProfit3Price !=0 and TradedamountSell3 !=0	):	
			GridSellProfit3PriceCount=GridSellProfit3PriceCount+.5
			PreviousGridSellProfit3Price=GridSellProfit3Price
			GridSellProfit3Price=grid3SellPrice	 -((grid3SellPrice	 *GridSellProfit3PriceCount )/Margin)
			LOCKPreviousGridSellProfit3Price=1															   
		if(LOCKPreviousGridSellProfit3Price==1 and	LastPriceTICKS	>	PreviousGridSellProfit3Price  and PreviousGridSellProfit3Price !=0):
			GridSellProfit3PriceFunc()		
			#if(StopSellFunc==0):grid3SellFunc()
		
		if(GridSellFlag4	 == 1  and LastPriceTICKS  <  GridSellProfit4Price	and GridSellProfit4Price !=0 and TradedamountSell4 !=0	):	
			GridSellProfit4PriceCount=GridSellProfit4PriceCount+.5
			PreviousGridSellProfit4Price=GridSellProfit4Price
			GridSellProfit4Price=grid4SellPrice	 -((grid4SellPrice	 *GridSellProfit4PriceCount )/Margin)
			LOCKPreviousGridSellProfit4Price=1															   
		if(LOCKPreviousGridSellProfit4Price==1 and	LastPriceTICKS	>	PreviousGridSellProfit4Price  and PreviousGridSellProfit4Price !=0):
			GridSellProfit4PriceFunc()		
			#if(StopSellFunc==0):grid4SellFunc()


		if(GridSellFlag5	 == 1  and LastPriceTICKS  <  GridSellProfit5Price	and GridSellProfit5Price !=0 and TradedamountSell5 !=0	):	
			GridSellProfit5PriceCount=GridSellProfit5PriceCount+.5
			PreviousGridSellProfit5Price=GridSellProfit5Price
			GridSellProfit5Price=grid5SellPrice	 -((grid5SellPrice	 *GridSellProfit5PriceCount )/Margin)
			LOCKPreviousGridSellProfit5Price=1															   
		if(LOCKPreviousGridSellProfit5Price==1 and	LastPriceTICKS	>	PreviousGridSellProfit5Price  and PreviousGridSellProfit5Price !=0):
			GridSellProfit5PriceFunc()		
			#if(StopSellFunc==0):grid5SellFunc()
				 
				 
		if(GridSellFlag6	 == 1  and LastPriceTICKS  <  GridSellProfit6Price	and GridSellProfit6Price !=0 and TradedamountSell6 !=0	):	
			GridSellProfit6PriceCount=GridSellProfit6PriceCount+.5
			PreviousGridSellProfit6Price=GridSellProfit6Price
			GridSellProfit6Price=grid6SellPrice	 -((grid6SellPrice	 *GridSellProfit6PriceCount )/Margin)
			LOCKPreviousGridSellProfit6Price=1															   
		if(LOCKPreviousGridSellProfit6Price==1 and	LastPriceTICKS	>	PreviousGridSellProfit6Price  and PreviousGridSellProfit6Price !=0):
			GridSellProfit6PriceFunc()		
			#if(StopSellFunc==0):grid6SellFunc()

		if(GridSellFlag7	 == 1  and LastPriceTICKS  <  GridSellProfit7Price	and GridSellProfit7Price !=0 and TradedamountSell7 !=0	):	
			GridSellProfit7PriceCount=GridSellProfit7PriceCount+.5
			PreviousGridSellProfit7Price=GridSellProfit7Price
			GridSellProfit7Price=grid7SellPrice	 -((grid7SellPrice	 *GridSellProfit7PriceCount )/Margin)
			LOCKPreviousGridSellProfit7Price=1															   
		if(LOCKPreviousGridSellProfit7Price==1 and	LastPriceTICKS	>	PreviousGridSellProfit7Price  and PreviousGridSellProfit7Price !=0):
			GridSellProfit7PriceFunc()		
			#if(StopSellFunc==0):grid7SellFunc()

		if(GridSellFlag8	 == 1  and LastPriceTICKS  <  GridSellProfit8Price	and GridSellProfit8Price !=0 and TradedamountSell8 !=0	):	
			GridSellProfit8PriceCount=GridSellProfit8PriceCount+.5
			PreviousGridSellProfit8Price=GridSellProfit8Price
			GridSellProfit8Price=grid8SellPrice	 -((grid8SellPrice	 *GridSellProfit8PriceCount )/Margin)
			LOCKPreviousGridSellProfit8Price=1															   
		if(LOCKPreviousGridSellProfit8Price==1 and	LastPriceTICKS	>	PreviousGridSellProfit8Price  and PreviousGridSellProfit8Price !=0):
			GridSellProfit8PriceFunc()		
			#if(StopSellFunc==0):grid8SellFunc()					 

		if(GridSellFlag9	 == 1  and LastPriceTICKS  <  GridSellProfit9Price	and GridSellProfit9Price !=0 and TradedamountSell9 !=0	):	
			GridSellProfit9PriceCount=GridSellProfit9PriceCount+.5
			PreviousGridSellProfit9Price=GridSellProfit9Price
			GridSellProfit9Price=grid9SellPrice	 -((grid9SellPrice	 *GridSellProfit9PriceCount )/Margin)
			LOCKPreviousGridSellProfit9Price=1															   
		if(LOCKPreviousGridSellProfit9Price==1 and	LastPriceTICKS	>	PreviousGridSellProfit9Price  and PreviousGridSellProfit9Price !=0):
			GridSellProfit9PriceFunc()		
			#if(StopSellFunc==0):grid9SellFunc()
				 
				 
		if(GridSellFlag10	 == 1  and LastPriceTICKS  <  GridSellProfit10Price	and GridSellProfit10Price !=0 and TradedamountSell10!=0	 ):	
			GridSellProfit10PriceCount=GridSellProfit10PriceCount+.5
			PreviousGridSellProfit10Price=GridSellProfit10Price
			GridSellProfit10Price=grid10SellPrice  -((grid10SellPrice	 *GridSellProfit10PriceCount )/Margin)
			LOCKPreviousGridSellProfit10Price=1															   
		if(LOCKPreviousGridSellProfit10Price==1 and	 LastPriceTICKS	 >	PreviousGridSellProfit10Price  and PreviousGridSellProfit10Price !=0):
			GridSellProfit10PriceFunc()		
			#if(StopSellFunc==0):grid10SellFunc()
				 
		if(GridSellFlag11	 == 1  and LastPriceTICKS  <  GridSellProfit11Price	and GridSellProfit11Price !=0 and TradedamountSell11!=0	 ):	
			GridSellProfit11PriceCount=GridSellProfit11PriceCount+.5
			PreviousGridSellProfit11Price=GridSellProfit11Price
			GridSellProfit11Price=grid11SellPrice  -((grid11SellPrice	 *GridSellProfit11PriceCount )/Margin)
			LOCKPreviousGridSellProfit11Price=1															   
		if(LOCKPreviousGridSellProfit11Price==1 and	 LastPriceTICKS	 >	PreviousGridSellProfit11Price  and PreviousGridSellProfit11Price !=0):
			GridSellProfit11PriceFunc()		
			#if(StopSellFunc==0):grid11SellFunc()

		if(GridSellFlag12	 == 1  and LastPriceTICKS  <  GridSellProfit12Price	and GridSellProfit12Price !=0 and TradedamountSell12!=0	 ):	
			GridSellProfit12PriceCount=GridSellProfit12PriceCount+.5
			PreviousGridSellProfit12Price=GridSellProfit12Price
			GridSellProfit12Price=grid12SellPrice  -((grid12SellPrice	 *GridSellProfit12PriceCount )/Margin)
			LOCKPreviousGridSellProfit12Price=1															   
		if(LOCKPreviousGridSellProfit12Price==1 and	 LastPriceTICKS	 >	PreviousGridSellProfit12Price  and PreviousGridSellProfit12Price !=0):
			GridSellProfit12PriceFunc()		
			#if(StopSellFunc==0):grid12SellFunc()

		if(GridSellFlag13	 == 1  and LastPriceTICKS  <  GridSellProfit13Price	and GridSellProfit13Price !=0 and TradedamountSell13!=0	 ):	
			GridSellProfit13PriceCount=GridSellProfit13PriceCount+.5
			PreviousGridSellProfit13Price=GridSellProfit13Price
			GridSellProfit13Price=grid13SellPrice  -((grid13SellPrice	 *GridSellProfit13PriceCount )/Margin)
			LOCKPreviousGridSellProfit13Price=1															   
		if(LOCKPreviousGridSellProfit13Price==1 and	 LastPriceTICKS	 >	PreviousGridSellProfit13Price  and PreviousGridSellProfit13Price !=0):
			GridSellProfit13PriceFunc()		
			#if(StopSellFunc==0):grid13SellFunc()

		if(GridSellFlag14	 == 1  and LastPriceTICKS  <  GridSellProfit14Price	and GridSellProfit14Price !=0 and TradedamountSell14!=0	 ):	
			GridSellProfit14PriceCount=GridSellProfit14PriceCount+.5
			PreviousGridSellProfit14Price=GridSellProfit14Price
			GridSellProfit14Price=grid14SellPrice  -((grid14SellPrice	 *GridSellProfit14PriceCount )/Margin)
			LOCKPreviousGridSellProfit14Price=1															   
		if(LOCKPreviousGridSellProfit14Price==1 and	 LastPriceTICKS	 >	PreviousGridSellProfit14Price  and PreviousGridSellProfit14Price !=0):
			GridSellProfit14PriceFunc()		
			#if(StopSellFunc==0):grid14SellFunc()
		
		if(GridSellFlag15	 == 1  and LastPriceTICKS  <  GridSellProfit15Price	and GridSellProfit15Price !=0 and TradedamountSell15!=0	 ):	
			GridSellProfit15PriceCount=GridSellProfit15PriceCount+.5
			PreviousGridSellProfit15Price=GridSellProfit15Price
			GridSellProfit15Price=grid15SellPrice  -((grid15SellPrice	 *GridSellProfit15PriceCount )/Margin)
			LOCKPreviousGridSellProfit15Price=1															   
		if(LOCKPreviousGridSellProfit15Price==1 and	 LastPriceTICKS	 >	PreviousGridSellProfit15Price  and PreviousGridSellProfit15Price !=0):
			GridSellProfit15PriceFunc()		
			#if(StopSellFunc==0):grid15SellFunc()

		if(GridSellFlag16	 == 1  and LastPriceTICKS  <  GridSellProfit16Price	and GridSellProfit16Price !=0 and TradedamountSell16!=0	 ):	
			GridSellProfit16PriceCount=GridSellProfit16PriceCount+.5
			PreviousGridSellProfit16Price=GridSellProfit16Price
			GridSellProfit16Price=grid16SellPrice  -((grid16SellPrice	 *GridSellProfit16PriceCount )/Margin)
			LOCKPreviousGridSellProfit16Price=1															   
		if(LOCKPreviousGridSellProfit16Price==1 and	 LastPriceTICKS	 >	PreviousGridSellProfit16Price  and PreviousGridSellProfit16Price !=0):
			GridSellProfit16PriceFunc()		
			#if(StopSellFunc==0):grid16SellFunc()

						 
		if(GridSellFlag17	 == 1  and LastPriceTICKS  <  GridSellProfit17Price	and GridSellProfit17Price !=0 and TradedamountSell17!=0	 ):	
			GridSellProfit17PriceCount=GridSellProfit17PriceCount+.5
			PreviousGridSellProfit17Price=GridSellProfit17Price
			GridSellProfit17Price=grid17SellPrice  -((grid17SellPrice	 *GridSellProfit17PriceCount )/Margin)
			LOCKPreviousGridSellProfit17Price=1															   
		if(LOCKPreviousGridSellProfit17Price==1 and	 LastPriceTICKS	 >	PreviousGridSellProfit17Price  and PreviousGridSellProfit17Price !=0):
			GridSellProfit17PriceFunc()		
			#if(StopSellFunc==0):grid17SellFunc()


		if(GridSellFlag18	 == 1  and LastPriceTICKS  <  GridSellProfit18Price	and GridSellProfit18Price !=0 and TradedamountSell18!=0	 ):	
			GridSellProfit18PriceCount=GridSellProfit18PriceCount+.5
			PreviousGridSellProfit18Price=GridSellProfit18Price
			GridSellProfit18Price=grid18SellPrice  -((grid18SellPrice	 *GridSellProfit18PriceCount )/Margin)
			LOCKPreviousGridSellProfit18Price=1															   
		if(LOCKPreviousGridSellProfit18Price==1 and	 LastPriceTICKS	 >	PreviousGridSellProfit18Price  and PreviousGridSellProfit18Price !=0):
			GridSellProfit18PriceFunc()		
			#if(StopSellFunc==0):grid18SellFunc()
				 
		
		if(GridSellFlag19	 == 1  and LastPriceTICKS  <  GridSellProfit19Price	and GridSellProfit19Price !=0 and TradedamountSell19!=0	 ):	
			GridSellProfit19PriceCount=GridSellProfit19PriceCount+.5
			PreviousGridSellProfit19Price=GridSellProfit19Price
			GridSellProfit19Price=grid19SellPrice  -((grid19SellPrice	 *GridSellProfit19PriceCount )/Margin)
			LOCKPreviousGridSellProfit19Price=1															   
		if(LOCKPreviousGridSellProfit19Price==1 and	 LastPriceTICKS	 >	PreviousGridSellProfit19Price  and PreviousGridSellProfit19Price !=0):
			GridSellProfit19PriceFunc()		
			#if(StopSellFunc==0):grid19SellFunc()		


		if(GridSellFlag20	 == 1  and LastPriceTICKS  <  GridSellProfit20Price	and GridSellProfit20Price !=0 and TradedamountSell20!=0	 ):	
			GridSellProfit20PriceCount=GridSellProfit20PriceCount+.5
			PreviousGridSellProfit20Price=GridSellProfit20Price
			GridSellProfit20Price=grid20SellPrice  -((grid20SellPrice	 *GridSellProfit20PriceCount )/Margin)
			LOCKPreviousGridSellProfit20Price=1															   
		if(LOCKPreviousGridSellProfit20Price==1 and	 LastPriceTICKS	 >	PreviousGridSellProfit20Price  and PreviousGridSellProfit20Price !=0):
			GridSellProfit20PriceFunc()		
			#if(StopSellFunc==0):grid20SellFunc()
				 
				 

		if(GridSellFlag21	 == 1  and LastPriceTICKS  <  GridSellProfit21Price	and GridSellProfit21Price !=0 and TradedamountSell21!=0	 ):	
			GridSellProfit21PriceCount=GridSellProfit21PriceCount+.5
			PreviousGridSellProfit21Price=GridSellProfit21Price
			GridSellProfit21Price=grid21SellPrice  -((grid21SellPrice	 *GridSellProfit21PriceCount )/Margin)
			LOCKPreviousGridSellProfit21Price=1															   
		if(LOCKPreviousGridSellProfit21Price==1 and	 LastPriceTICKS	 >	PreviousGridSellProfit21Price  and PreviousGridSellProfit21Price !=0):
			GridSellProfit21PriceFunc()		
			#if(StopSellFunc==0):grid21SellFunc()
				 
				 
		if(GridSellFlag22	 == 1  and LastPriceTICKS  <  GridSellProfit22Price	and GridSellProfit22Price !=0 and TradedamountSell22!=0	 ):	
			GridSellProfit22PriceCount=GridSellProfit22PriceCount+.5
			PreviousGridSellProfit22Price=GridSellProfit22Price
			GridSellProfit22Price=grid22SellPrice  -((grid22SellPrice	 *GridSellProfit22PriceCount )/Margin)
			LOCKPreviousGridSellProfit22Price=1															   
		if(LOCKPreviousGridSellProfit22Price==1 and	 LastPriceTICKS	 >	PreviousGridSellProfit22Price  and PreviousGridSellProfit22Price !=0):
			GridSellProfit22PriceFunc()		
			#if(StopSellFunc==0):grid22SellFunc()
				 
		if(GridSellFlag23	 == 1  and LastPriceTICKS  <  GridSellProfit23Price	and GridSellProfit23Price !=0 and TradedamountSell23!=0	 ):	
			GridSellProfit23PriceCount=GridSellProfit23PriceCount+.5
			PreviousGridSellProfit23Price=GridSellProfit23Price
			GridSellProfit23Price=grid23SellPrice  -((grid23SellPrice	 *GridSellProfit23PriceCount )/Margin)
			LOCKPreviousGridSellProfit23Price=1															   
		if(LOCKPreviousGridSellProfit23Price==1 and	 LastPriceTICKS	 >	PreviousGridSellProfit23Price  and PreviousGridSellProfit23Price !=0):
			GridSellProfit23PriceFunc()		
			#if(StopSellFunc==0):grid23SellFunc()

		if(GridSellFlag24	 == 1  and LastPriceTICKS  <  GridSellProfit24Price	and GridSellProfit24Price !=0 and TradedamountSell24!=0	 ):	
			GridSellProfit24PriceCount=GridSellProfit24PriceCount+.5
			PreviousGridSellProfit24Price=GridSellProfit24Price
			GridSellProfit24Price=grid24SellPrice  -((grid24SellPrice	 *GridSellProfit24PriceCount )/Margin)
			LOCKPreviousGridSellProfit24Price=1															   
		if(LOCKPreviousGridSellProfit24Price==1 and	 LastPriceTICKS	 >	PreviousGridSellProfit24Price  and PreviousGridSellProfit24Price !=0):
			GridSellProfit24PriceFunc()		
			#if(StopSellFunc==0):grid24SellFunc()

		if(GridSellFlag25	 == 1  and LastPriceTICKS  <  GridSellProfit25Price	and GridSellProfit25Price !=0 and TradedamountSell25!=0	 ):	
			GridSellProfit25PriceCount=GridSellProfit25PriceCount+.5
			PreviousGridSellProfit25Price=GridSellProfit25Price
			GridSellProfit25Price=grid25SellPrice  -((grid25SellPrice	 *GridSellProfit25PriceCount )/Margin)
			LOCKPreviousGridSellProfit25Price=1															   
		if(LOCKPreviousGridSellProfit25Price==1 and	 LastPriceTICKS	 >	PreviousGridSellProfit25Price  and PreviousGridSellProfit25Price !=0):
			GridSellProfit25PriceFunc()		
			#if(StopSellFunc==0):grid25SellFunc()

		if(GridSellFlag26	 == 1  and LastPriceTICKS  <  GridSellProfit26Price	and GridSellProfit26Price !=0 and TradedamountSell26!=0	 ):	
			GridSellProfit26PriceCount=GridSellProfit26PriceCount+.5
			PreviousGridSellProfit26Price=GridSellProfit26Price
			GridSellProfit26Price=grid26SellPrice  -((grid26SellPrice	 *GridSellProfit26PriceCount )/Margin)
			LOCKPreviousGridSellProfit26Price=1															   
		if(LOCKPreviousGridSellProfit26Price==1 and	 LastPriceTICKS	 >	PreviousGridSellProfit26Price  and PreviousGridSellProfit26Price !=0):
			GridSellProfit26PriceFunc()		
			#if(StopSellFunc==0):grid26SellFunc()

		if(GridSellFlag27	 == 1  and LastPriceTICKS  <  GridSellProfit27Price	and GridSellProfit27Price !=0 and TradedamountSell27!=0	 ):	
			GridSellProfit27PriceCount=GridSellProfit27PriceCount+.5
			PreviousGridSellProfit27Price=GridSellProfit27Price
			GridSellProfit27Price=grid27SellPrice  -((grid27SellPrice	 *GridSellProfit27PriceCount )/Margin)
			LOCKPreviousGridSellProfit27Price=1															   
		if(LOCKPreviousGridSellProfit27Price==1 and	 LastPriceTICKS	 >	PreviousGridSellProfit27Price  and PreviousGridSellProfit27Price !=0):
			GridSellProfit27PriceFunc()		
			#if(StopSellFunc==0):grid27SellFunc()

		if(GridSellFlag28	 == 1  and LastPriceTICKS  <  GridSellProfit28Price	and GridSellProfit28Price !=0 and TradedamountSell28!=0	 ):	
			GridSellProfit28PriceCount=GridSellProfit28PriceCount+.5
			PreviousGridSellProfit28Price=GridSellProfit28Price
			GridSellProfit28Price=grid28SellPrice  -((grid28SellPrice	 *GridSellProfit28PriceCount )/Margin)
			LOCKPreviousGridSellProfit28Price=1															   
		if(LOCKPreviousGridSellProfit28Price==1 and	 LastPriceTICKS	 >	PreviousGridSellProfit28Price  and PreviousGridSellProfit28Price !=0):
			GridSellProfit28PriceFunc()		
			#if(StopSellFunc==0):grid28SellFunc()

		if(GridSellFlag29	 == 1  and LastPriceTICKS  <  GridSellProfit29Price	and GridSellProfit29Price !=0 and TradedamountSell29!=0	 ):	
			GridSellProfit29PriceCount=GridSellProfit29PriceCount+.5
			PreviousGridSellProfit29Price=GridSellProfit29Price
			GridSellProfit29Price=grid29SellPrice  -((grid29SellPrice	 *GridSellProfit29PriceCount )/Margin)
			LOCKPreviousGridSellProfit29Price=1															   
		if(LOCKPreviousGridSellProfit29Price==1 and	 LastPriceTICKS	 >	PreviousGridSellProfit29Price  and PreviousGridSellProfit29Price !=0):
			GridSellProfit29PriceFunc()		
			#if(StopSellFunc==0):grid29SellFunc()

		if(GridSellFlag30	 == 1  and LastPriceTICKS  <  GridSellProfit30Price	and GridSellProfit30Price !=0 and TradedamountSell30!=0	 ):	
			GridSellProfit30PriceCount=GridSellProfit30PriceCount+.5
			PreviousGridSellProfit30Price=GridSellProfit30Price
			GridSellProfit30Price=grid30SellPrice  -((grid30SellPrice	 *GridSellProfit30PriceCount )/Margin)
			LOCKPreviousGridSellProfit30Price=1															   
		if(LOCKPreviousGridSellProfit30Price==1 and	 LastPriceTICKS	 >	PreviousGridSellProfit30Price  and PreviousGridSellProfit30Price !=0):
			GridSellProfit30PriceFunc()		
			#if(StopSellFunc==0):grid30SellFunc()	
								
							
	
		
		
		if(MACDType==1):
			if (MainAccountProfitSinceGridStart	 >=	 3	 and  MainAccountProfitSinceGridStart < 4  and	MainPositionAmount!=0  and lockProfit1==0) :	
				profitLockKey=1
				lockProfit1=1			
				SELLNOW ='NONE'						 
				ProfitPercentDynamic=2				 
				print(" >>>>>>>>>>>>>> We have Lock	  the 1 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			if (MainAccountProfitSinceGridStart	 >=	 4	 and  MainAccountProfitSinceGridStart < 5 and MainPositionAmount!=0	 and lockProfit2==0) :	
				profitLockKey=1
				lockProfit2=1	
				SELLNOW ='NONE'						 
				ProfitPercentDynamic=3				
				print(" >>>>>>>>>>>>>>> We have Lock  the 2 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")			
			if (MainAccountProfitSinceGridStart	 >=	 5	 and  MainAccountProfitSinceGridStart < 6 and MainPositionAmount!=0	 and lockProfit3==0) :	
				profitLockKey=1
				lockProfit3=1			
				SELLNOW ='NONE'						 
				ProfitPercentDynamic=4				
				print(" >>>>>>>>>>>>>> We have Lock	  the 3 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			if (MainAccountProfitSinceGridStart >=	 6	 and  MainAccountProfitSinceGridStart < 7 and MainPositionAmount!=0	 and lockProfit4==0) :	
				profitLockKey=1	
				lockProfit4=1			
				SELLNOW ='NONE'						 
				ProfitPercentDynamic=5				
				print(" >>>>>>>>>>>>>> We have Lock	  the 4 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			if (MainAccountProfitSinceGridStart >=	 7	 and  MainAccountProfitSinceGridStart < 8 and MainPositionAmount!=0	 and lockProfit5==0) :	
				profitLockKey=1	   
				lockProfit5=1			
				SELLNOW ='NONE'						 
				ProfitPercentDynamic=6				
				print(" >>>>>>>>>>>>> We have Lock	   the 5 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			if (MainAccountProfitSinceGridStart >=	 8	 and MainAccountProfitSinceGridStart < 9 and MainPositionAmount!=0	and lockProfit6==0) :	
				profitLockKey=1	
				lockProfit6=1			
				SELLNOW ='NONE'						 
				ProfitPercentDynamic=7				
				print(" >>>>>>>>>>>>>> We have Lock	   the 6 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")			
			if (MainAccountProfitSinceGridStart >=	 9	 and MainAccountProfitSinceGridStart < 10 and MainPositionAmount!=0	 and lockProfit7==0) :	
				profitLockKey=1
				lockProfit7=1			
				SELLNOW ='NONE'						 
				ProfitPercentDynamic=8				
				print(" >>>>>>>>>>>>> We have Lock	   the 7 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			if (MainAccountProfitSinceGridStart >=	 10	  and MainAccountProfitSinceGridStart < 11 and MainPositionAmount!=0  and lockProfit8==0) :	
				profitLockKey=1	  
				lockProfit8=1			
				SELLNOW ='NONE'						 
				ProfitPercentDynamic=9				
				print(" >>>>>>>>>>>> We have Lock		the 8 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			if (MainAccountProfitSinceGridStart >=	 11	  and MainAccountProfitSinceGridStart < 12 and MainPositionAmount!=0  and lockProfit9==0) :	
				profitLockKey=1		 
				lockProfit9=1			
				SELLNOW ='NONE'						 
				ProfitPercentDynamic=10				 
				print(" >>>>>>>>>>>>> We have Lock	   the 9 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			if (MainAccountProfitSinceGridStart >=	 12	  and MainAccountProfitSinceGridStart < 13 and MainPositionAmount!=0  and lockProfit10==0) :	
				profitLockKey=1
				lockProfit10=1			
				SELLNOW ='NONE'						 
				ProfitPercentDynamic=11				 
				print(" >>>>>>>>>>>>>> We have Lock the 10 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")			
			if (MainAccountProfitSinceGridStart >=	 13	  and MainAccountProfitSinceGridStart < 14 and MainPositionAmount!=0  and lockProfit11==0) :	
				profitLockKey=1		
				lockProfit11=1			
				SELLNOW ='NONE'						 
				ProfitPercentDynamic=12				 
				print(" >>>>>>>>>>>>>>> We have Lock the 11 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			if (MainAccountProfitSinceGridStart >=	 14	  and MainAccountProfitSinceGridStart < 15 and MainPositionAmount!=0  and lockProfit12==0) :	
				profitLockKey=1	 
				lockProfit12=1			
				SELLNOW ='NONE'						 
				ProfitPercentDynamic=13				 
				print(" >>>>>>>>>>>>>>> We have Lock the 12 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")	
			if (MainAccountProfitSinceGridStart >=	 15	  and  MainAccountProfitSinceGridStart < 16 and MainPositionAmount!=0  and lockProfit13==0) :	
				profitLockKey=1		
				lockProfit13=1			
				SELLNOW ='NONE'						 
				ProfitPercentDynamic=14				 
				print(" >>>>>>>>>>>>>> We have Lock the 13 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			if (MainAccountProfitSinceGridStart >=	 16	  and  MainAccountProfitSinceGridStart < 17 and MainPositionAmount!=0  and lockProfit14==0) :	
				profitLockKey=1	   
				lockProfit14=1			
				SELLNOW ='NONE'						 
				ProfitPercentDynamic=15				 
				print(" >>>>>>>>>>>>>>> We have Lock the 14 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")			
			if (MainAccountProfitSinceGridStart >=	 17	  and  MainAccountProfitSinceGridStart < 18 and MainPositionAmount!=0  and lockProfit15==0) :	
				profitLockKey=1	  
				lockProfit15=1			
				SELLNOW ='NONE'						 
				ProfitPercentDynamic=16				 
				print(" >>>>>>>>>>>>>>> We have Lock the 15 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			if (MainAccountProfitSinceGridStart >=	 18	  and MainAccountProfitSinceGridStart < 19 and MainPositionAmount!=0  and lockProfit16==0) :	
				profitLockKey=1	   
				lockProfit16=1			
				SELLNOW ='NONE'						 
				ProfitPercentDynamic=17				 
				print(" >>>>>>>>>>>>>>> We have Lock the 16 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			if (MainAccountProfitSinceGridStart >=	 19	  and MainAccountProfitSinceGridStart < 20 and MainPositionAmount!=0  and lockProfit17==0) :	
				profitLockKey=1
				lockProfit17=1			
				SELLNOW ='NONE'						 
				ProfitPercentDynamic=18				 
				print(" >>>>>>>>>>>>>>> We have Lock the 17 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			if (MainAccountProfitSinceGridStart >=	 20	  and MainAccountProfitSinceGridStart < 21 and MainPositionAmount!=0  and lockProfit18==0) :	
				profitLockKey=1	
				lockProfit18=1			
				SELLNOW ='NONE'						 
				ProfitPercentDynamic=19				 
				print(" >>>>>>>>>>>>>> We have Lock the 18 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")			
			if (MainAccountProfitSinceGridStart >=	 21	  and MainAccountProfitSinceGridStart < 22 and MainPositionAmount!=0  and lockProfit19==0) :	
				profitLockKey=1	
				lockProfit19=1
				SELLNOW ='NONE'
				ProfitPercentDynamic=20
				print(" >>>>>>>>>>>>>>> We have Lock the 19 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			if (MainAccountProfitSinceGridStart >=		  22	and MainAccountProfitSinceGridStart < 23 and MainPositionAmount!=0	and lockProfit20==0) :	
				profitLockKey=1	
				lockProfit20=1
				SELLNOW ='NONE'
				ProfitPercentDynamic=21
				print(" >>>>>>>>>>>>>> We have Locked the 20 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")	
			if (MainAccountProfitSinceGridStart >=		  23	and MainAccountProfitSinceGridStart < 24 and MainPositionAmount!=0	and lockProfit21==0) :	
				profitLockKey=1	
				lockProfit21=1
				SELLNOW ='NONE'
				ProfitPercentDynamic=22
				print(" >>>>>>>>>>>>>>> We have Locked the 21 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")	

		# if(MACDType==1):
			# if (MainAccountProfitSinceGridStart	 >=	 5	 and  MainAccountProfitSinceGridStart < 6  and	MainPositionAmount!=0  and lockProfit1==0) :	
				# profitLockKey=1
				# lockProfit1=1			
				# SELLNOW ='NONE'						 
				# ProfitPercentDynamic=4				 
				# print(" >>>>>>>>>>>>>> We have Lock	  the 1 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			# if (MainAccountProfitSinceGridStart	 >=	 6	 and  MainAccountProfitSinceGridStart < 7 and MainPositionAmount!=0	 and lockProfit2==0) :	
				# profitLockKey=1
				# lockProfit2=1	
				# SELLNOW ='NONE'						 
				# ProfitPercentDynamic=5				
				# print(" >>>>>>>>>>>>>>> We have Lock	the 2 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")			
			# if (MainAccountProfitSinceGridStart	 >=	 7	 and  MainAccountProfitSinceGridStart < 8 and MainPositionAmount!=0	 and lockProfit3==0) :	
				# profitLockKey=1
				# lockProfit3=1			
				# SELLNOW ='NONE'						 
				# ProfitPercentDynamic=6				
				# print(" >>>>>>>>>>>>>> We have Lock	  the 3 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			# if (MainAccountProfitSinceGridStart >=	 8	 and  MainAccountProfitSinceGridStart < 9 and MainPositionAmount!=0	 and lockProfit4==0) :	
				# profitLockKey=1	
				# lockProfit4=1			
				# SELLNOW ='NONE'						 
				# ProfitPercentDynamic=7				
				# print(" >>>>>>>>>>>>>> We have Lock	  the 4 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			# if (MainAccountProfitSinceGridStart >=	 9	 and  MainAccountProfitSinceGridStart < 10 and MainPositionAmount!=0	 and lockProfit5==0) :	
				# profitLockKey=1	   
				# lockProfit5=1			
				# SELLNOW ='NONE'						 
				# ProfitPercentDynamic=8				
				# print(" >>>>>>>>>>>>> We have Lock	   the 5 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			# if (MainAccountProfitSinceGridStart >=	 10	 and MainAccountProfitSinceGridStart < 11 and MainPositionAmount!=0	and lockProfit6==0) :	
				# profitLockKey=1	
				# lockProfit6=1			
				# SELLNOW ='NONE'						 
				# ProfitPercentDynamic=9				
				# print(" >>>>>>>>>>>>>> We have Lock	   the 6 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")			
			# if (MainAccountProfitSinceGridStart >=	 11	 and MainAccountProfitSinceGridStart < 12 and MainPositionAmount!=0	 and lockProfit7==0) :	
				# profitLockKey=1
				# lockProfit7=1			
				# SELLNOW ='NONE'						 
				# ProfitPercentDynamic=10				
				# print(" >>>>>>>>>>>>> We have Lock	   the 7 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			# if (MainAccountProfitSinceGridStart >=	 12	  and MainAccountProfitSinceGridStart < 13 and MainPositionAmount!=0  and lockProfit8==0) :	
				# profitLockKey=1	  
				# lockProfit8=1			
				# SELLNOW ='NONE'						 
				# ProfitPercentDynamic=11				
				# print(" >>>>>>>>>>>> We have Lock		the 8 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			# if (MainAccountProfitSinceGridStart >=	 13	  and MainAccountProfitSinceGridStart < 14 and MainPositionAmount!=0  and lockProfit9==0) :	
				# profitLockKey=1		 
				# lockProfit9=1			
				# SELLNOW ='NONE'						 
				# ProfitPercentDynamic=12				 
				# print(" >>>>>>>>>>>>> We have Lock	   the 9 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			# if (MainAccountProfitSinceGridStart >=	 14	  and MainAccountProfitSinceGridStart < 15 and MainPositionAmount!=0  and lockProfit10==0) :	
				# profitLockKey=1
				# lockProfit10=1			
				# SELLNOW ='NONE'						 
				# ProfitPercentDynamic=13				 
				# print(" >>>>>>>>>>>>>> We have Lock the 10 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")			
			# if (MainAccountProfitSinceGridStart >=	 15	  and MainAccountProfitSinceGridStart < 16 and MainPositionAmount!=0  and lockProfit11==0) :	
				# profitLockKey=1		
				# lockProfit11=1			
				# SELLNOW ='NONE'						 
				# ProfitPercentDynamic=14				 
				# print(" >>>>>>>>>>>>>>> We have Lock the 11 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			# if (MainAccountProfitSinceGridStart >=	 16	  and MainAccountProfitSinceGridStart < 17 and MainPositionAmount!=0  and lockProfit12==0) :	
				# profitLockKey=1	 
				# lockProfit12=1			
				# SELLNOW ='NONE'						 
				# ProfitPercentDynamic=15				 
				# print(" >>>>>>>>>>>>>>> We have Lock the 12 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")	
			# if (MainAccountProfitSinceGridStart >=	 17	  and  MainAccountProfitSinceGridStart < 18 and MainPositionAmount!=0  and lockProfit13==0) :	
				# profitLockKey=1		
				# lockProfit13=1			
				# SELLNOW ='NONE'						 
				# ProfitPercentDynamic=16				 
				# print(" >>>>>>>>>>>>>> We have Lock the 13 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			# if (MainAccountProfitSinceGridStart >=	 18	  and  MainAccountProfitSinceGridStart < 19 and MainPositionAmount!=0  and lockProfit14==0) :	
				# profitLockKey=1	   
				# lockProfit14=1			
				# SELLNOW ='NONE'						 
				# ProfitPercentDynamic=17				 
				# print(" >>>>>>>>>>>>>>> We have Lock the 14 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")			
			# if (MainAccountProfitSinceGridStart >=	 19	  and  MainAccountProfitSinceGridStart < 20 and MainPositionAmount!=0  and lockProfit15==0) :	
				# profitLockKey=1	  
				# lockProfit15=1			
				# SELLNOW ='NONE'						 
				# ProfitPercentDynamic=18				 
				# print(" >>>>>>>>>>>>>>> We have Lock the 15 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			# if (MainAccountProfitSinceGridStart >=	 20	  and MainAccountProfitSinceGridStart < 21 and MainPositionAmount!=0  and lockProfit16==0) :	
				# profitLockKey=1	   
				# lockProfit16=1			
				# SELLNOW ='NONE'						 
				# ProfitPercentDynamic=19				 
				# print(" >>>>>>>>>>>>>>> We have Lock the 16 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			# if (MainAccountProfitSinceGridStart >=	 21	  and MainAccountProfitSinceGridStart < 22 and MainPositionAmount!=0  and lockProfit17==0) :	
				# profitLockKey=1
				# lockProfit17=1			
				# SELLNOW ='NONE'						 
				# ProfitPercentDynamic=20				 
				# print(" >>>>>>>>>>>>>>> We have Lock the 17 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			# if (MainAccountProfitSinceGridStart >=	 22	  and MainAccountProfitSinceGridStart < 23 and MainPositionAmount!=0  and lockProfit18==0) :	
				# profitLockKey=1	
				# lockProfit18=1			
				# SELLNOW ='NONE'						 
				# ProfitPercentDynamic=21				 
				# print(" >>>>>>>>>>>>>> We have Lock the 18 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")			
			# if (MainAccountProfitSinceGridStart >=	 23	  and MainAccountProfitSinceGridStart < 24 and MainPositionAmount!=0  and lockProfit19==0) :	
				# profitLockKey=1	
				# lockProfit19=1
				# SELLNOW ='NONE'
				# ProfitPercentDynamic=22
				# print(" >>>>>>>>>>>>>>> We have Lock the 19 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")
			# if (MainAccountProfitSinceGridStart >=	24	and MainAccountProfitSinceGridStart < 25 and MainPositionAmount!=0	and lockProfit20==0) :	
				# profitLockKey=1	
				# lockProfit20=1
				# SELLNOW ='NONE'
				# ProfitPercentDynamic=23
				# print(" >>>>>>>>>>>>>> We have Locked the 20 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")	
			# if (MainAccountProfitSinceGridStart >=	 25	and MainAccountProfitSinceGridStart < 26 and MainPositionAmount!=0	and lockProfit21==0) :	
				# profitLockKey=1	
				# lockProfit21=1
				# SELLNOW ='NONE'
				# ProfitPercentDynamic=24
				# print(" >>>>>>>>>>>>>>> We have Locked the 21 profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")	






						
		if ( profitLockKey==1 and MainAccountProfitSinceGridStart <	 ProfitPercentDynamic and  ProfitPercentDynamic!=0 and MainAccountProfitSinceGridStart!=0 and MainPositionAmount!=0):
			SELLNOW ='TRUE'
			print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
			print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
			print("++++++++++++++++++++++++++++	  We Broke the Previous Profit Price . WE MUST SELL NOW . ENJOY	  ++++++++++++++++")
			print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
			print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
	

		
		if "EXIT" == SubjectGlobal and totalWalletBalance !=0 :
			SELLNOW="TRUE"	
			print(colored('66666666666666666666666666666666666666666666666666666666666666666666666666666666666666','green'))
		
		
		
		# if(BuyDirectinalGrid==1 and SellDirectinalGrid==0 and StartGrid==1):		
			# if GridBuyFlag19 == 1 and GridBuyFlag20 == 1 and MainAccountProfitSinceGridStart > .5:
				# SELLNOW="TRUE"	
		# if(BuyDirectinalGrid==0 and SellDirectinalGrid==1 and StartGrid==1):
			# if GridSellFlag19 == 1 and GridSellFlag20 == 1 and MainAccountProfitSinceGridStart > .5:
				# SELLNOW="TRUE"
		
		
		
		PostionFullInfo=binance.fapiPrivateGetPositionRisk ()
		MainPositionAmount=float(PostionFullInfo[0].get('positionAmt'))
		MainPositionEntryPrice=float(PostionFullInfo[0].get('entryPrice'))
		MainPositionLiquidationPrice=float(PostionFullInfo[0].get('liquidationPrice'))
		MainPostionProfit=float(PostionFullInfo[0].get('unRealizedProfit'))
		leverage=PostionFullInfo[0].get('leverage')
		if(MainPositionAmount==0):
			totalWalletBalance=BalanceRes.get("info").get("totalWalletBalance")
			totalWalletBalance=float(totalWalletBalance)
			DynamicFirstIntiatedWalletBalanceForGrid=totalWalletBalance
			DynamicFirstIntiatedWalletBalanceForAmountPostion=totalWalletBalance
		
		
		
		
		
					
		if(SELLNOW=="TRUE"):
			print(colored('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX','green'))
			print(colored('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX','green'))
			print(colored('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX','green'))
			print(colored('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX YOU are 11% in Profit XX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX','green'))
			print(colored('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX','green'))
			print(colored('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX','green'))
			print(colored('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX','green'))
			print(colored('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX','green'))
			StopBuyFunc=1	
			StopSellFunc=1
			binance.cancel_all_orders(symbol=symbol)
			if(MainPostionSide=='long' ):
				print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Closing LONG Postion NOW USING MARKET ORDER','green'))
				Ordertype='Sell'
				Orderside='market'
				Orderprice=LastPriceTICKS
				Orderamount=MainPositionAmount
				binance.createOrder (symbol,Orderside,Ordertype,Orderamount)
				# FirstIntiatedWalletBalanceIncreaseCount=0				
				StopBuyFunc=0	
				StopSellFunc=0
				# doubledAcountAmount=doubledAcountAmount+1
				GridNumberCount=GridNumberCount+1
				MainAccountProfitSinceGridStart=0
				AcualDollarMainAccountProfitSinceGridStart=0
				SubjectGlobal="NONE"
				SELLNOW="NONE"
				StartGrid=0
				GridBuyFlag0  =0
				GridBuyFlag1  =0
				GridBuyFlag2  =0
				GridBuyFlag3  =0
				GridBuyFlag4  =0
				GridBuyFlag5  =0
				GridBuyFlag6  =0
				GridBuyFlag7  =0
				GridBuyFlag8  =0
				GridBuyFlag9  =0
				GridBuyFlag10 =0
				GridBuyFlag11 =0
				GridBuyFlag12 =0
				GridBuyFlag13 =0
				GridBuyFlag14 =0
				GridBuyFlag15 =0
				GridBuyFlag16 =0
				GridBuyFlag17 =0
				GridBuyFlag18 =0
				GridBuyFlag19 =0
				GridBuyFlag20 =0
				GridBuyFlag21 =0
				GridBuyFlag22 =0
				GridBuyFlag23 =0
				GridBuyFlag24 =0
				GridBuyFlag25 =0
				GridBuyFlag26 =0
				GridBuyFlag27 =0
				GridBuyFlag28 =0
				GridBuyFlag29 =0
				GridBuyFlag30 =0
				lockProfit1=0 
				lockProfit2=0 
				lockProfit3=0 
				lockProfit4=0 
				lockProfit5=0 
				lockProfit6=0 
				lockProfit7=0 
				lockProfit8=0 
				lockProfit9=0 
				lockProfit10=0
				lockProfit11=0
				lockProfit12=0
				lockProfit13=0
				lockProfit14=0	
				lockProfit15=0
				lockProfit16=0
				lockProfit17=0
				lockProfit18=0	
				lockProfit19=0
				lockProfit20=0
				lockProfit21=0
				GridSellFlag0  =0
				GridSellFlag1  =0
				GridSellFlag2  =0
				GridSellFlag3  =0
				GridSellFlag4  =0
				GridSellFlag5  =0
				GridSellFlag6  =0
				GridSellFlag7  =0
				GridSellFlag8  =0
				GridSellFlag9  =0
				GridSellFlag10 =0
				GridSellFlag11 =0
				GridSellFlag12 =0
				GridSellFlag13 =0
				GridSellFlag14 =0
				GridSellFlag15 =0
				GridSellFlag16 =0
				GridSellFlag17 =0
				GridSellFlag18 =0
				GridSellFlag19 =0
				GridSellFlag20 =0
				GridSellFlag21 =0
				GridSellFlag22 =0
				GridSellFlag23 =0
				GridSellFlag24 =0
				GridSellFlag25 =0
				GridSellFlag26 =0
				GridSellFlag27 =0
				GridSellFlag28 =0
				GridSellFlag29 =0
				GridSellFlag30 =0
				lockProfit1=0 
				lockProfit2=0 
				lockProfit3=0 
				lockProfit4=0 
				lockProfit5=0 
				lockProfit6=0 
				lockProfit7=0 
				lockProfit8=0 
				lockProfit9=0 
				lockProfit10=0
				lockProfit11=0
				lockProfit12=0
				lockProfit13=0
				lockProfit14=0	
				lockProfit15=0
				lockProfit16=0
				lockProfit17=0
				lockProfit18=0	
				lockProfit19=0
				lockProfit20=0
				lockProfit21=0
				TradedamountBuy0=0
				TradedamountBuy1=0
				TradedamountBuy2 =0
				TradedamountBuy3 =0
				TradedamountBuy4 =0
				TradedamountBuy5 =0
				TradedamountBuy6 =0
				TradedamountBuy7 =0
				TradedamountBuy8 =0
				TradedamountBuy9 =0
				TradedamountBuy10=0
				TradedamountBuy11=0
				TradedamountBuy12=0
				TradedamountBuy13=0
				TradedamountBuy14=0
				TradedamountBuy15=0
				TradedamountBuy16=0
				TradedamountBuy17=0
				TradedamountBuy18=0
				TradedamountBuy19=0
				TradedamountBuy20=0
				TradedamountBuy21=0
				TradedamountBuy22=0
				TradedamountBuy23=0
				TradedamountBuy24=0
				TradedamountBuy25=0
				TradedamountBuy26=0
				TradedamountBuy27=0
				TradedamountBuy28=0
				TradedamountBuy29=0
				TradedamountBuy30=0
				TradedamountSell0=0
				TradedamountSell1=0
				TradedamountSell2 =0
				TradedamountSell3 =0
				TradedamountSell4 =0
				TradedamountSell5 =0
				TradedamountSell6 =0
				TradedamountSell7 =0
				TradedamountSell8 =0
				TradedamountSell9 =0
				TradedamountSell10=0
				TradedamountSell11=0
				TradedamountSell12=0
				TradedamountSell13=0
				TradedamountSell14=0
				TradedamountSell15=0
				TradedamountSell16=0
				TradedamountSell17=0
				TradedamountSell18=0
				TradedamountSell19=0
				TradedamountSell20=0
				TradedamountSell21=0
				TradedamountSell22=0
				TradedamountSell23=0
				TradedamountSell24=0
				TradedamountSell25=0
				TradedamountSell26=0
				TradedamountSell27=0
				TradedamountSell28=0
				TradedamountSell29=0
				TradedamountSell30=0
				grid0BuyPrice=0
				grid0SellPrice=0	
				grid1BuyPrice=0
				grid1SellPrice=0
				grid2BuyPrice=0
				grid2SellPrice=0
				grid3BuyPrice=0
				grid3SellPrice=0
				grid4BuyPrice=0
				grid4SellPrice=0
				grid5BuyPrice=0
				grid5SellPrice=0
				grid6BuyPrice=0
				grid6SellPrice=0
				grid7BuyPrice=0
				grid7SellPrice=0
				grid8BuyPrice=0
				grid8SellPrice=0
				grid9BuyPrice=0
				grid9SellPrice=0
				grid10BuyPrice=0
				grid10SellPrice=0
				grid11BuyPrice=0
				grid11SellPrice=0
				grid12BuyPrice=0
				grid12SellPrice=0
				grid13BuyPrice=0
				grid13SellPrice=0
				grid14BuyPrice=0
				grid14SellPrice=0
				grid15BuyPrice=0
				grid15SellPrice=0
				grid16BuyPrice=0
				grid16SellPrice=0
				grid17BuyPrice=0
				grid17SellPrice=0
				grid18BuyPrice=0
				grid18SellPrice=0
				grid19BuyPrice=0
				grid19SellPrice=0
				grid20BuyPrice=0
				grid20SellPrice=0
				grid21BuyPrice=0
				grid21SellPrice=0
				grid22BuyPrice=0
				grid22SellPrice=0
				grid23BuyPrice=0
				grid23SellPrice=0
				grid24BuyPrice=0
				grid24SellPrice=0
				grid25BuyPrice=0
				grid25SellPrice=0
				grid26BuyPrice=0
				grid26SellPrice=0
				grid27BuyPrice=0
				grid27SellPrice=0
				grid28BuyPrice=0
				grid28SellPrice=0
				grid29BuyPrice=0
				grid29SellPrice=0
				grid30BuyPrice=0
				grid30SellPrice=0
				BalanceRes = binance.fetchBalance ()
				totalWalletBalance=BalanceRes.get("info").get("totalWalletBalance")
				totalWalletBalance=float(totalWalletBalance)
				DynamicFirstIntiatedWalletBalanceForGrid=totalWalletBalance
				DynamicFirstIntiatedWalletBalanceForAmountPostion=totalWalletBalance
				now1M = datetime.now() 
				dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
				with open(ResultFile, 'a', newline='') as file:
					writer = csv.writer(file)
					writer.writerow([SN1M, dt_string1M,"PositionClosed","PositionClosed","ProfitPercentDynamic",ProfitPercentDynamic,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType,"PositionClosed"])
					SN1M=SN1M+1
				ProfitPercentDynamic=0
				profitLockKey=0	
				MainPostionSide="NONE"				
			if(MainPostionSide=='SHORT'	 ):
				print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Closing LONG Postion NOW USING MARKET ORDER','green'))
				Ordertype='Buy'
				Orderside='market'
				Orderprice=LastPriceTICKS
				Orderamount=-(MainPositionAmount)
				binance.createOrder (symbol,Orderside,Ordertype,Orderamount)
				# FirstIntiatedWalletBalanceIncreaseCount=0				
				StopBuyFunc=0	
				StopSellFunc=0
				# doubledAcountAmount=doubledAcountAmount+1
				MainAccountProfitSinceGridStart=0
				AcualDollarMainAccountProfitSinceGridStart=0
				GridNumberCount=GridNumberCount+1
				SubjectGlobal="NONE"
				SELLNOW="NONE"
				StartGrid=0
				GridBuyFlag0  =0
				GridBuyFlag1  =0
				GridBuyFlag2  =0
				GridBuyFlag3  =0
				GridBuyFlag4  =0
				GridBuyFlag5  =0
				GridBuyFlag6  =0
				GridBuyFlag7  =0
				GridBuyFlag8  =0
				GridBuyFlag9  =0
				GridBuyFlag10 =0
				GridBuyFlag11 =0
				GridBuyFlag12 =0
				GridBuyFlag13 =0
				GridBuyFlag14 =0
				GridBuyFlag15 =0
				GridBuyFlag16 =0
				GridBuyFlag17 =0
				GridBuyFlag18 =0
				GridBuyFlag19 =0
				GridBuyFlag20 =0
				GridBuyFlag21 =0
				GridBuyFlag22 =0
				GridBuyFlag23 =0
				GridBuyFlag24 =0
				GridBuyFlag25 =0
				GridBuyFlag26 =0
				GridBuyFlag27 =0
				GridBuyFlag28 =0
				GridBuyFlag29 =0
				GridBuyFlag30 =0
				lockProfit1=0 
				lockProfit2=0 
				lockProfit3=0 
				lockProfit4=0 
				lockProfit5=0 
				lockProfit6=0 
				lockProfit7=0 
				lockProfit8=0 
				lockProfit9=0 
				lockProfit10=0
				lockProfit11=0
				lockProfit12=0
				lockProfit13=0
				lockProfit14=0	
				lockProfit15=0
				lockProfit16=0
				lockProfit17=0
				lockProfit18=0	
				lockProfit19=0
				lockProfit20=0
				lockProfit21=0
				GridSellFlag0  =0
				GridSellFlag1  =0
				GridSellFlag2  =0
				GridSellFlag3  =0
				GridSellFlag4  =0
				GridSellFlag5  =0
				GridSellFlag6  =0
				GridSellFlag7  =0
				GridSellFlag8  =0
				GridSellFlag9  =0
				GridSellFlag10 =0
				GridSellFlag11 =0
				GridSellFlag12 =0
				GridSellFlag13 =0
				GridSellFlag14 =0
				GridSellFlag15 =0
				GridSellFlag16 =0
				GridSellFlag17 =0
				GridSellFlag18 =0
				GridSellFlag19 =0
				GridSellFlag20 =0
				GridSellFlag21 =0
				GridSellFlag22 =0
				GridSellFlag23 =0
				GridSellFlag24 =0
				GridSellFlag25 =0
				GridSellFlag26 =0
				GridSellFlag27 =0
				GridSellFlag28 =0
				GridSellFlag29 =0
				GridSellFlag30 =0
				lockProfit1=0 
				lockProfit2=0 
				lockProfit3=0 
				lockProfit4=0 
				lockProfit5=0 
				lockProfit6=0 
				lockProfit7=0 
				lockProfit8=0 
				lockProfit9=0 
				lockProfit10=0
				lockProfit11=0
				lockProfit12=0
				lockProfit13=0
				lockProfit14=0	
				lockProfit15=0
				lockProfit16=0
				lockProfit17=0
				lockProfit18=0	
				lockProfit19=0
				lockProfit20=0
				lockProfit21=0
				TradedamountBuy0=0
				TradedamountBuy1=0
				TradedamountBuy2 =0
				TradedamountBuy3 =0
				TradedamountBuy4 =0
				TradedamountBuy5 =0
				TradedamountBuy6 =0
				TradedamountBuy7 =0
				TradedamountBuy8 =0
				TradedamountBuy9 =0
				TradedamountBuy10=0
				TradedamountBuy11=0
				TradedamountBuy12=0
				TradedamountBuy13=0
				TradedamountBuy14=0
				TradedamountBuy15=0
				TradedamountBuy16=0
				TradedamountBuy17=0
				TradedamountBuy18=0
				TradedamountBuy19=0
				TradedamountBuy20=0
				TradedamountBuy21=0
				TradedamountBuy22=0
				TradedamountBuy23=0
				TradedamountBuy24=0
				TradedamountBuy25=0
				TradedamountBuy26=0
				TradedamountBuy27=0
				TradedamountBuy28=0
				TradedamountBuy29=0
				TradedamountBuy30=0
				TradedamountSell0=0
				TradedamountSell1=0
				TradedamountSell2 =0
				TradedamountSell3 =0
				TradedamountSell4 =0
				TradedamountSell5 =0
				TradedamountSell6 =0
				TradedamountSell7 =0
				TradedamountSell8 =0
				TradedamountSell9 =0
				TradedamountSell10=0
				TradedamountSell11=0
				TradedamountSell12=0
				TradedamountSell13=0
				TradedamountSell14=0
				TradedamountSell15=0
				TradedamountSell16=0
				TradedamountSell17=0
				TradedamountSell18=0
				TradedamountSell19=0
				TradedamountSell20=0
				TradedamountSell21=0
				TradedamountSell22=0
				TradedamountSell23=0
				TradedamountSell24=0
				TradedamountSell25=0
				TradedamountSell26=0
				TradedamountSell27=0
				TradedamountSell28=0
				TradedamountSell29=0
				TradedamountSell30=0
				grid0BuyPrice=0
				grid0SellPrice=0	
				grid1BuyPrice=0
				grid1SellPrice=0
				grid2BuyPrice=0
				grid2SellPrice=0
				grid3BuyPrice=0
				grid3SellPrice=0
				grid4BuyPrice=0
				grid4SellPrice=0
				grid5BuyPrice=0
				grid5SellPrice=0
				grid6BuyPrice=0
				grid6SellPrice=0
				grid7BuyPrice=0
				grid7SellPrice=0
				grid8BuyPrice=0
				grid8SellPrice=0
				grid9BuyPrice=0
				grid9SellPrice=0
				grid10BuyPrice=0
				grid10SellPrice=0
				grid11BuyPrice=0
				grid11SellPrice=0
				grid12BuyPrice=0
				grid12SellPrice=0
				grid13BuyPrice=0
				grid13SellPrice=0
				grid14BuyPrice=0
				grid14SellPrice=0
				grid15BuyPrice=0
				grid15SellPrice=0
				grid16BuyPrice=0
				grid16SellPrice=0
				grid17BuyPrice=0
				grid17SellPrice=0
				grid18BuyPrice=0
				grid18SellPrice=0
				grid19BuyPrice=0
				grid19SellPrice=0
				grid20BuyPrice=0
				grid20SellPrice=0
				grid21BuyPrice=0
				grid21SellPrice=0
				grid22BuyPrice=0
				grid22SellPrice=0
				grid23BuyPrice=0
				grid23SellPrice=0
				grid24BuyPrice=0
				grid24SellPrice=0
				grid25BuyPrice=0
				grid25SellPrice=0
				grid26BuyPrice=0
				grid26SellPrice=0
				grid27BuyPrice=0
				grid27SellPrice=0
				grid28BuyPrice=0
				grid28SellPrice=0
				grid29BuyPrice=0
				grid29SellPrice=0
				grid30BuyPrice=0
				grid30SellPrice=0
				BalanceRes = binance.fetchBalance ()
				totalWalletBalance=BalanceRes.get("info").get("totalWalletBalance")
				totalWalletBalance=float(totalWalletBalance)
				DynamicFirstIntiatedWalletBalanceForGrid=totalWalletBalance
				DynamicFirstIntiatedWalletBalanceForAmountPostion=totalWalletBalance
				now1M = datetime.now() 
				dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
				with open(ResultFile, 'a', newline='') as file:
					writer = csv.writer(file)
					writer.writerow([SN1M, dt_string1M,"PositionClosed","PositionClosed","ProfitPercentDynamic",ProfitPercentDynamic,FirstIntiatedWalletBalance,totalWalletBalance,MainAccountProfitSinceGridStart,MainPositionLiquidationPrice,MainPositionEntryPrice,MainPositionAmount,MainPostionSide,MainPostionProfit,leverage,GridNumberCount,RacingPriceFunc,BotType,"PositionClosed"])
					SN1M=SN1M+1	
				ProfitPercentDynamic=0
				profitLockKey=0
				MainPostionSide="NONE"

		print("1Subject=",Subject,"1SubjectGlobal=",SubjectGlobal,"SubjectManual=",SubjectManual)		
		PercentBetweenFirstBalanceAndCurrentBalance	 =	totalWalletBalance / FirstIntiatedWalletBalance	   
		
	except Exception as a: 
					print("!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! z !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",a)								

	threading.Timer(1, TICKSFunc).start()



def PrintFunc():
	global MainAccountProfitSinceGridStart
	global MainPositionAmount
	global MainPositionEntryPrice
	global MainPositionLiquidationPrice
	global MainPostionProfit
	global leverage
	global MainPostionSide
	global PostionunRealizedProfit
	global RacingPriceFunc
	global HowManyTimesMoveFuncTriggeredSell
	global RealProfitWithUnRealizedProfit
	global AcualDollarMainAccountProfitSinceGridStart
	global SN1M
	global profitLockKey
	global ProfitPercentDynamic
	global SELLNOW
	global MACDType
	global BotType
	global GridSellFlag0 
	global GridSellFlag1 
	global GridSellFlag2 
	global GridSellFlag3 
	global GridSellFlag4 
	global GridSellFlag5 
	global GridSellFlag6 
	global GridSellFlag7 
	global GridSellFlag8 
	global GridSellFlag9 
	global GridSellFlag10
	global GridSellFlag11
	global GridSellFlag12
	global GridSellFlag13
	global GridSellFlag14
	global GridSellFlag15
	global GridSellFlag16
	global GridSellFlag17
	global GridSellFlag18
	global GridSellFlag19
	global GridSellFlag20
	global GridSellFlag21
	global GridSellFlag22
	global GridSellFlag23
	global GridSellFlag24
	global GridSellFlag25
	global GridSellFlag26
	global GridSellFlag27
	global GridSellFlag28
	global GridSellFlag29
	global GridSellFlag30
	global GridBuyFlag0 
	global GridBuyFlag1 
	global GridBuyFlag2 
	global GridBuyFlag3 
	global GridBuyFlag4 
	global GridBuyFlag5 
	global GridBuyFlag6 
	global GridBuyFlag7 
	global GridBuyFlag8 
	global GridBuyFlag9 
	global GridBuyFlag10
	global GridBuyFlag11
	global GridBuyFlag12
	global GridBuyFlag13
	global GridBuyFlag14
	global GridBuyFlag15
	global GridBuyFlag16
	global GridBuyFlag17
	global GridBuyFlag18
	global GridBuyFlag19
	global GridBuyFlag20
	global GridBuyFlag21
	global GridBuyFlag22
	global GridBuyFlag23
	global GridBuyFlag24
	global GridBuyFlag25
	global GridBuyFlag26
	global GridBuyFlag27
	global GridBuyFlag28
	global GridBuyFlag29
	global GridBuyFlag30
	global DynamicFirstIntiatedWalletBalanceForGrid
	global DynamicFirstIntiatedWalletBalanceForAmountPostion
	global PercentBetweenFirstBalanceAndCurrentBalance
	
	try:
		if(SellDirectinalGrid==0 and BuyDirectinalGrid==1 and  BotType=="SUPERTREND-LONG" ):
			print((colored('######################	   THIS IS sobh.bot@gmail.com	SUPERTREND-LONG	   ########################','green')),"Version=",Version,"BotType",BotType)
		if(BuyDirectinalGrid==0 and SellDirectinalGrid==1  and	BotType=="SUPERTREND-SHORT"):
			print((colored('######################	   THIS IS sobh.bot.2@gmail.com SUPERTREND-SHORT	   ########################','red')),"Version=",Version,"BotType",BotType)	
			
		if(SellDirectinalGrid==0 and BuyDirectinalGrid==1  and	BotType=="LONG-MACD-ALL"):
			print((colored('#################################	   THIS IS sobh.bot.3@gmail.com Long With Indicator TRADE BOT	   #########################','green')),"Version=",Version,"BotType",BotType)
		if(BuyDirectinalGrid==0 and SellDirectinalGrid==1  and	BotType=="SHORT-MACD-ALL"):
			print((colored('#####################	   THIS IS sobh.bot.4@gmail.com Shoring Using Indicators	   ######################','red')),"Version=",Version,"BotType",BotType)	
			
		if(SellDirectinalGrid==0 and BuyDirectinalGrid==1 and  BotType=="LONG-WAVES-ALL" ):
			print((colored('#####################	   THIS IS sobh.bot.5@gmail.com Long With Indicator TRADE BOT	   #######################','green')),"Version=",Version,"BotType",BotType)
		if(BuyDirectinalGrid==0 and SellDirectinalGrid==1  and	BotType=="SHORT-WAVES-ALL"):
			print((colored('####################	   THIS IS sobh.bot.6@gmail.com Shoring Using Indicators	   #####################','red')),"Version=",Version,"BotType",BotType)	
			
		if(SellDirectinalGrid==0 and BuyDirectinalGrid==1  and	BotType=="LONG-WAVES-TREND"):
			print((colored('#####################	   THIS IS sobh.bot.7@gmail.com "LONG-WAVES-TREND"	   #####################','green')),"Version=",Version,"BotType",BotType)
		if(BuyDirectinalGrid==0 and SellDirectinalGrid==1 and  BotType=="SHORT-WAVES-TREND" ):
			print((colored('####################	   THIS IS sobh.bot.8@gmail.com "SHORT-WAVES-TREND"	  ######################','red')),"Version=",Version,"BotType",BotType)	
			
		

			
		elapsed_time = time.time() - start_time
		elapsed_timeSTR=time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
		
		
		
		
		############################################################################################### NEW GETTING INFO ###############################################################################################
		PostionFullInfo=binance.fapiPrivateGetPositionRisk ()
		positionAmt = [i["positionAmt"] for i in PostionFullInfo ]
		LAV = [i["leverage"] for i in PostionFullInfo ]
		entryPrice=	  [i["entryPrice"]	for i in PostionFullInfo ] 
		unrealizedProfit=	  [i["unRealizedProfit"]	for i in PostionFullInfo ]
		liquidationPrice=	  [i["liquidationPrice"]	for i in PostionFullInfo ]
		# RealpositionInitialMargin=[i["positionInitialMargin"]	for i in PostionFullInfo ]
	
		positionAmtarr = np.array(positionAmt)
		entryPricearr= np.array(entryPrice)
		unrealizedProfitarr= np.array(unrealizedProfit)
		liquidationPricearr= np.array(liquidationPrice)
		LAV=np.array(LAV)
		# RealpositionInitialMarginArr=np.array(RealpositionInitialMargin)
	
	
	
		positionAmtarr = positionAmtarr.astype(np.float)
		entryPricearr = entryPricearr.astype(np.float)
		unrealizedProfitarr = unrealizedProfitarr.astype(np.float)
		liquidationPricearr = liquidationPricearr.astype(np.float)
		LAV=LAV.astype(np.float)
		# RealpositionInitialMarginArr=RealpositionInitialMarginArr.astype(np.float)
		
		positionAmtarr = positionAmtarr[positionAmtarr !=0]
		try:
			positionAmtarr=Decimal(positionAmtarr[0])
			# RealpositionInitialMarginArr=RealpositionInitialMarginArr[RealpositionInitialMarginArr !=0]
			# print("pppppppppp",positionAmtarr)
		except:
			print("Dec")
		entryPricearr = entryPricearr[entryPricearr !=0]
		unrealizedProfitarr = unrealizedProfitarr[unrealizedProfitarr !=0]
		liquidationPricearr = liquidationPricearr[liquidationPricearr !=0]
		
		LAV=LAV[LAV ==Margin]
	
		balance = binance.fetch_balance()
		# print(balance['info']['positions'])
	
		MainPositionAmount=positionAmtarr
		MainPositionEntryPrice=entryPricearr
		MainPositionLiquidationPrice=liquidationPricearr
		MainPostionProfit=unrealizedProfitarr
		leverage=LAV
		
		CurrentWalletBalanceWithProfit=totalWalletBalance+CurrentPositionProfit
		RealPostionAmountToclOSeCorretcly=positionAmtarr
		try:
			MainPositionAmount=positionAmtarr[0]
			# RealpositionInitialMargin=RealpositionInitialMarginArr
		except:
			print("Err in MainPositionAmount[0]")
		
		
		RealProfitWithUnRealizedProfit=(totalWalletBalance+MainPostionProfit)
		
		
		# PostionFullInfo=binance.fapiPrivateGetPositionRisk ()
		# MainPositionAmount=float(PostionFullInfo[0].get('positionAmt'))
		# MainPositionEntryPrice=float(PostionFullInfo[0].get('entryPrice'))
		# MainPositionLiquidationPrice=float(PostionFullInfo[0].get('liquidationPrice'))
		# MainPostionProfit=float(PostionFullInfo[0].get('unRealizedProfit'))
		# leverage=PostionFullInfo[0].get('leverage')
		# RealProfitWithUnRealizedProfit=(totalWalletBalance+MainPostionProfit)
		
			
		print("---MainPostionProfit---",MainPostionProfit,"----PostionAmount----",MainPositionAmount,"----entryPrice----",MainPositionEntryPrice,'---liquidationPrice----',MainPositionLiquidationPrice,'----leverage----',leverage)
			
		if(MainPostionProfit > 0):
			print(colored('-unRealizedProfit =','green'),MainPostionProfit)	
		if(MainPostionProfit < 0):
			print(colored('-unRealizedProfit =','red'),MainPostionProfit)	
		
		
		
		
		print(colored('================================== First Intial Time and DATE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>','magenta'),StartNowTimeAndDate)
		print(colored('================================== LastPriceTICKS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>','cyan'),	LastPriceTICKS)
		print(colored('================================== First-Intiated-Wallet-Balance >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>','yellow'),FirstIntiatedWalletBalance)
		print(colored('================================== Current-totalWallet-Balance >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>','yellow'),totalWalletBalance)
		print(colored('================================== RealProfitWithUnRealizedProfit >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>','yellow'),RealProfitWithUnRealizedProfit)
		print(colored('================================== RacingPriceFunc >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>','cyan'),RacingPriceFunc)
		print(colored('================================== GridNumberCount >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>','cyan'),GridNumberCount)
		print("                                           Subject=",Subject,"SubjectGlobal=",SubjectGlobal)
		print(colored('================================== LongerTimeFrame >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>','yellow'),LongerTimeFrame)
		print(colored('================================== Cashed In Times >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>','yellow'),SN1M)
		print(colored('================================== ProfitPercentDynamic: ','yellow'),ProfitPercentDynamic,"SELLNOW=",SELLNOW,"profitLockKey",profitLockKey,"MainPostionSide",MainPostionSide,"GlobalProfit=",GlobalProfit,"DynFirstBalance4Grid",DynamicFirstIntiatedWalletBalanceForGrid)
		
		# ################## Close pos when shifted to opposite 
		# if(BuyDirectinalGrid==1 and SellDirectinalGrid==0 ):
			# if(MainPostionSide=='SHORT'):
				# SELLNOW="TRUE"
		# if(SellDirectinalGrid==1 and BuyDirectinalGrid==0 ):
			# if(MainPostionSide=='long'):
				# SELLNOW="TRUE"	
		
		
		if(doubledAcountAmount!=0):
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> YOUR ACOUNT HAD BEEN BOUDLED	>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>','yellow'),doubledAcountAmount)
		if(MainPositionAmount > 0 and MainPositionEntryPrice !=0 ):
			MainPostionSide='long'
		if(MainPositionAmount < 0  and MainPositionEntryPrice !=0 ):
			MainPostionSide='SHORT'		
		
		
		
		if(MainPositionAmount!=0):
			MainAccountProfitSinceGridStart=(((RealProfitWithUnRealizedProfit-DynamicFirstIntiatedWalletBalanceForGrid)/DynamicFirstIntiatedWalletBalanceForGrid)*100)
			AcualDollarMainAccountProfitSinceGridStart=((RealProfitWithUnRealizedProfit-DynamicFirstIntiatedWalletBalanceForGrid))
			if(MainAccountProfitSinceGridStart > 0 and RealProfitWithUnRealizedProfit !=0 and DynamicFirstIntiatedWalletBalanceForGrid != 0) :
				print(colored('----------------------------Main Account Profit Since Grid Start in Percent	-----------------------------------','green'),MainAccountProfitSinceGridStart )
				print(colored('----------------------------Main Account Profit Since Grid Start in Dollars	-----------------------------------','green'),AcualDollarMainAccountProfitSinceGridStart )
			if(MainAccountProfitSinceGridStart < 0 and RealProfitWithUnRealizedProfit !=0 and DynamicFirstIntiatedWalletBalanceForGrid != 0) :
				print(colored('----------------------------Main Account Profit Since Grid Start in Percent ------------------------------------','red'),MainAccountProfitSinceGridStart )	
				print(colored('----------------------------Main Account Profit Since Grid Start in Dollars ------------------------------------','red'),AcualDollarMainAccountProfitSinceGridStart )
	
		if(MainPostionProfit==0):
			print(colored('--------------------------------------------------------- WE ARE NOT IN POSTIONS NOW --------------------------------------------------------------','magenta') )

			
		
		
	
		if(GridBuyFlag0	 == 1  ):	print(colored('-grid0BuyP--','green'), float("%0.1f"%(grid0BuyPrice )) ,"-GridBuyProfit0P--",float("%0.1f"%(GridBuyProfit0Price )) ,"-GridBuyFlag0 --",GridBuyFlag0 ,"-amountBuy0 --",	  float("%0.5f"%(TradedamountBuy0  )),	  "Count",GridBuyProfit0PriceCount	, "PreviousGridBuyProfit0P ", float("%0.1f"%(PreviousGridBuyProfit0Price ))		,"LOCK0P",LOCKPreviousGridBuyProfit0Price)
		if(GridBuyFlag1	 == 1  ):	print(colored('-grid1BuyP--','green'), float("%0.1f"%(grid1BuyPrice )) ,"-GridBuyProfit1P--",float("%0.1f"%(GridBuyProfit1Price )) ,"-GridBuyFlag1 --",GridBuyFlag1 ,"-amountBuy1 --",	  float("%0.5f"%(TradedamountBuy1  )),	  "Count",GridBuyProfit1PriceCount	, "PreviousGridBuyProfit1P ", float("%0.1f"%(PreviousGridBuyProfit1Price ))		,"LOCK1P",LOCKPreviousGridBuyProfit1Price)
		if(GridBuyFlag2	 == 1  ):	print(colored('-grid2BuyP--','green'), float("%0.1f"%(grid2BuyPrice )) ,"-GridBuyProfit2P--",float("%0.1f"%(GridBuyProfit2Price )) ,"-GridBuyFlag2 --",GridBuyFlag2 ,"-amountBuy2 --",	  float("%0.5f"%(TradedamountBuy2  )),	  "Count",GridBuyProfit2PriceCount	, "PreviousGridBuyProfit2P ", float("%0.1f"%(PreviousGridBuyProfit2Price ))		,"LOCK2P",LOCKPreviousGridBuyProfit2Price)
		if(GridBuyFlag3	 == 1  ):	print(colored('-grid3BuyP--','green'), float("%0.1f"%(grid3BuyPrice )) ,"-GridBuyProfit3P--",float("%0.1f"%(GridBuyProfit3Price )) ,"-GridBuyFlag3 --",GridBuyFlag3 ,"-amountBuy3 --",	  float("%0.5f"%(TradedamountBuy3  )),	  "Count",GridBuyProfit3PriceCount	, "PreviousGridBuyProfit3P ", float("%0.1f"%(PreviousGridBuyProfit3Price ))		,"LOCK3P",LOCKPreviousGridBuyProfit3Price)
		if(GridBuyFlag4	 == 1  ):	print(colored('-grid4BuyP--','green'), float("%0.1f"%(grid4BuyPrice )) ,"-GridBuyProfit4P--",float("%0.1f"%(GridBuyProfit4Price )) ,"-GridBuyFlag4 --",GridBuyFlag4 ,"-amountBuy4 --",	  float("%0.5f"%(TradedamountBuy4  )),	  "Count",GridBuyProfit4PriceCount	, "PreviousGridBuyProfit4P ", float("%0.1f"%(PreviousGridBuyProfit4Price ))		,"LOCK4P",LOCKPreviousGridBuyProfit4Price)
		if(GridBuyFlag5	 == 1  ):	print(colored('-grid5BuyP--','green'), float("%0.1f"%(grid5BuyPrice )) ,"-GridBuyProfit5P--",float("%0.1f"%(GridBuyProfit5Price )) ,"-GridBuyFlag5 --",GridBuyFlag5 ,"-amountBuy5 --",	  float("%0.5f"%(TradedamountBuy5  )),	  "Count",GridBuyProfit5PriceCount	, "PreviousGridBuyProfit5P ", float("%0.1f"%(PreviousGridBuyProfit5Price ))		,"LOCK5P",LOCKPreviousGridBuyProfit5Price)
		if(GridBuyFlag6	 == 1  ):	print(colored('-grid6BuyP--','green'), float("%0.1f"%(grid6BuyPrice )) ,"-GridBuyProfit6P--",float("%0.1f"%(GridBuyProfit6Price )) ,"-GridBuyFlag6 --",GridBuyFlag6 ,"-amountBuy6 --",	  float("%0.5f"%(TradedamountBuy6  )),	  "Count",GridBuyProfit6PriceCount	, "PreviousGridBuyProfit6P ", float("%0.1f"%(PreviousGridBuyProfit6Price ))		,"LOCK6P",LOCKPreviousGridBuyProfit6Price)
		if(GridBuyFlag7	 == 1  ):	print(colored('-grid7BuyP--','green'), float("%0.1f"%(grid7BuyPrice )) ,"-GridBuyProfit7P--",float("%0.1f"%(GridBuyProfit7Price )) ,"-GridBuyFlag7 --",GridBuyFlag7 ,"-amountBuy7 --",	  float("%0.5f"%(TradedamountBuy7  )),	  "Count",GridBuyProfit7PriceCount	, "PreviousGridBuyProfit7P ", float("%0.1f"%(PreviousGridBuyProfit7Price ))		,"LOCK7P",LOCKPreviousGridBuyProfit7Price)
		if(GridBuyFlag8	 == 1  ):	print(colored('-grid8BuyP--','green'), float("%0.1f"%(grid8BuyPrice )) ,"-GridBuyProfit8P--",float("%0.1f"%(GridBuyProfit8Price )) ,"-GridBuyFlag8 --",GridBuyFlag8 ,"-amountBuy8 --",	  float("%0.5f"%(TradedamountBuy8  )),	  "Count",GridBuyProfit8PriceCount	, "PreviousGridBuyProfit8P ", float("%0.1f"%(PreviousGridBuyProfit8Price ))		,"LOCK8P",LOCKPreviousGridBuyProfit8Price)
		if(GridBuyFlag9	 == 1  ):	print(colored('-grid9BuyP--','green'), float("%0.1f"%(grid9BuyPrice )) ,"-GridBuyProfit9P--",float("%0.1f"%(GridBuyProfit9Price )) ,"-GridBuyFlag9 --",GridBuyFlag9 ,"-amountBuy9 --",	  float("%0.5f"%(TradedamountBuy9  )),	  "Count",GridBuyProfit9PriceCount	, "PreviousGridBuyProfit9P ", float("%0.1f"%(PreviousGridBuyProfit9Price ))		,"LOCK9P",LOCKPreviousGridBuyProfit9Price)
		if(GridBuyFlag10 == 1  ):	print(colored('-grid10BuyP--','green'), float("%0.1f"%(grid10BuyPrice)),"-GridBuyProfit10P--", float("%0.1f"%(GridBuyProfit10Price)) ,"-GridBuyFlag10--",GridBuyFlag10,"-amountBuy10--",float("%0.5f"%(TradedamountBuy10)),"Count",	 GridBuyProfit10PriceCount,"PreviousGridBuyProfit10P", float("%0.1f"%(PreviousGridBuyProfit10Price)),"LOCK10P",LOCKPreviousGridBuyProfit10Price)
		if(GridBuyFlag11 == 1  ):	print(colored('-grid11BuyP--','green'), float("%0.1f"%(grid11BuyPrice)),"-GridBuyProfit11P--", float("%0.1f"%(GridBuyProfit11Price)) ,"-GridBuyFlag11--",GridBuyFlag11,"-amountBuy11--",float("%0.5f"%(TradedamountBuy11)),"Count",	 GridBuyProfit11PriceCount,"PreviousGridBuyProfit11P", float("%0.1f"%(PreviousGridBuyProfit11Price)),"LOCK11P",LOCKPreviousGridBuyProfit11Price)
		if(GridBuyFlag12 == 1  ):	print(colored('-grid12BuyP--','green'), float("%0.1f"%(grid12BuyPrice)),"-GridBuyProfit12P--", float("%0.1f"%(GridBuyProfit12Price)) ,"-GridBuyFlag12--",GridBuyFlag12,"-amountBuy12--",float("%0.5f"%(TradedamountBuy12)),"Count",	 GridBuyProfit12PriceCount,"PreviousGridBuyProfit12P", float("%0.1f"%(PreviousGridBuyProfit12Price)),"LOCK12P",LOCKPreviousGridBuyProfit12Price)
		if(GridBuyFlag13 == 1  ):	print(colored('-grid13BuyP--','green'), float("%0.1f"%(grid13BuyPrice)),"-GridBuyProfit13P--", float("%0.1f"%(GridBuyProfit13Price)) ,"-GridBuyFlag13--",GridBuyFlag13,"-amountBuy13--",float("%0.5f"%(TradedamountBuy13)),"Count",	 GridBuyProfit13PriceCount,"PreviousGridBuyProfit13P", float("%0.1f"%(PreviousGridBuyProfit13Price)),"LOCK13P",LOCKPreviousGridBuyProfit13Price)
		if(GridBuyFlag14 == 1  ):	print(colored('-grid14BuyP--','green'), float("%0.1f"%(grid14BuyPrice)),"-GridBuyProfit14P--", float("%0.1f"%(GridBuyProfit14Price)) ,"-GridBuyFlag14--",GridBuyFlag14,"-amountBuy14--",float("%0.5f"%(TradedamountBuy14)),"Count",	 GridBuyProfit14PriceCount,"PreviousGridBuyProfit14P", float("%0.1f"%(PreviousGridBuyProfit14Price)),"LOCK14P",LOCKPreviousGridBuyProfit14Price)
		if(GridBuyFlag15 == 1  ):	print(colored('-grid15BuyP--','green'), float("%0.1f"%(grid15BuyPrice)),"-GridBuyProfit15P--", float("%0.1f"%(GridBuyProfit15Price)) ,"-GridBuyFlag15--",GridBuyFlag15,"-amountBuy15--",float("%0.5f"%(TradedamountBuy15)),"Count",	 GridBuyProfit15PriceCount,"PreviousGridBuyProfit15P", float("%0.1f"%(PreviousGridBuyProfit15Price)),"LOCK15P",LOCKPreviousGridBuyProfit15Price)
		if(GridBuyFlag16 == 1  ):	print(colored('-grid16BuyP--','green'), float("%0.1f"%(grid16BuyPrice)),"-GridBuyProfit16P--", float("%0.1f"%(GridBuyProfit16Price)) ,"-GridBuyFlag16--",GridBuyFlag16,"-amountBuy16--",float("%0.5f"%(TradedamountBuy16)),"Count",	 GridBuyProfit16PriceCount,"PreviousGridBuyProfit16P", float("%0.1f"%(PreviousGridBuyProfit16Price)),"LOCK16P",LOCKPreviousGridBuyProfit16Price)
		if(GridBuyFlag17 == 1  ):	print(colored('-grid17BuyP--','green'), float("%0.1f"%(grid17BuyPrice)),"-GridBuyProfit17P--", float("%0.1f"%(GridBuyProfit17Price)) ,"-GridBuyFlag17--",GridBuyFlag17,"-amountBuy17--",float("%0.5f"%(TradedamountBuy17)),"Count",	 GridBuyProfit17PriceCount,"PreviousGridBuyProfit17P", float("%0.1f"%(PreviousGridBuyProfit17Price)),"LOCK17P",LOCKPreviousGridBuyProfit17Price)
		if(GridBuyFlag18 == 1  ):	print(colored('-grid18BuyP--','green'), float("%0.1f"%(grid18BuyPrice)),"-GridBuyProfit18P--", float("%0.1f"%(GridBuyProfit18Price)) ,"-GridBuyFlag18--",GridBuyFlag18,"-amountBuy18--",float("%0.5f"%(TradedamountBuy18)),"Count",	 GridBuyProfit18PriceCount,"PreviousGridBuyProfit18P", float("%0.1f"%(PreviousGridBuyProfit18Price)),"LOCK18P",LOCKPreviousGridBuyProfit18Price)
		if(GridBuyFlag19 == 1  ):	print(colored('-grid19BuyP--','green'), float("%0.1f"%(grid19BuyPrice)),"-GridBuyProfit19P--", float("%0.1f"%(GridBuyProfit19Price)) ,"-GridBuyFlag19--",GridBuyFlag19,"-amountBuy19--",float("%0.5f"%(TradedamountBuy19)),"Count",	 GridBuyProfit19PriceCount,"PreviousGridBuyProfit19P", float("%0.1f"%(PreviousGridBuyProfit19Price)),"LOCK19P",LOCKPreviousGridBuyProfit19Price)
		if(GridBuyFlag20 == 1  ):	print(colored('-grid20BuyP--','green'), float("%0.1f"%(grid20BuyPrice)),"-GridBuyProfit20P--", float("%0.1f"%(GridBuyProfit20Price)) ,"-GridBuyFlag20--",GridBuyFlag20,"-amountBuy20--",float("%0.5f"%(TradedamountBuy20)),"Count",	 GridBuyProfit20PriceCount,"PreviousGridBuyProfit20P", float("%0.1f"%(PreviousGridBuyProfit20Price)),"LOCK20P",LOCKPreviousGridBuyProfit20Price)
		if(GridBuyFlag21 == 1  ):	print(colored('-grid21BuyP--','green'), float("%0.1f"%(grid21BuyPrice)),"-GridBuyProfit21P--", float("%0.1f"%(GridBuyProfit21Price)) ,"-GridBuyFlag21--",GridBuyFlag21,"-amountBuy21--",float("%0.5f"%(TradedamountBuy21)),"Count",	 GridBuyProfit21PriceCount,"PreviousGridBuyProfit21P", float("%0.1f"%(PreviousGridBuyProfit21Price)),"LOCK21P",LOCKPreviousGridBuyProfit21Price)
		if(GridBuyFlag22 == 1  ):	print(colored('-grid22BuyP--','green'), float("%0.1f"%(grid22BuyPrice)),"-GridBuyProfit22P--", float("%0.1f"%(GridBuyProfit22Price)) ,"-GridBuyFlag22--",GridBuyFlag22,"-amountBuy22--",float("%0.5f"%(TradedamountBuy22)),"Count",	 GridBuyProfit22PriceCount,"PreviousGridBuyProfit22P", float("%0.1f"%(PreviousGridBuyProfit22Price)),"LOCK22P",LOCKPreviousGridBuyProfit22Price)
		if(GridBuyFlag23 == 1  ):	print(colored('-grid23BuyP--','green'), float("%0.1f"%(grid23BuyPrice)),"-GridBuyProfit23P--", float("%0.1f"%(GridBuyProfit23Price)) ,"-GridBuyFlag23--",GridBuyFlag23,"-amountBuy23--",float("%0.5f"%(TradedamountBuy23)),"Count",	 GridBuyProfit23PriceCount,"PreviousGridBuyProfit23P", float("%0.1f"%(PreviousGridBuyProfit23Price)),"LOCK23P",LOCKPreviousGridBuyProfit23Price)
		if(GridBuyFlag24 == 1  ):	print(colored('-grid24BuyP--','green'), float("%0.1f"%(grid24BuyPrice)),"-GridBuyProfit24P--", float("%0.1f"%(GridBuyProfit24Price)) ,"-GridBuyFlag24--",GridBuyFlag24,"-amountBuy24--",float("%0.5f"%(TradedamountBuy24)),"Count",	 GridBuyProfit24PriceCount,"PreviousGridBuyProfit24P", float("%0.1f"%(PreviousGridBuyProfit24Price)),"LOCK24P",LOCKPreviousGridBuyProfit24Price)
		if(GridBuyFlag25 == 1  ):	print(colored('-grid25BuyP--','green'), float("%0.1f"%(grid25BuyPrice)),"-GridBuyProfit25P--", float("%0.1f"%(GridBuyProfit25Price)) ,"-GridBuyFlag25--",GridBuyFlag25,"-amountBuy25--",float("%0.5f"%(TradedamountBuy25)),"Count",	 GridBuyProfit25PriceCount,"PreviousGridBuyProfit25P", float("%0.1f"%(PreviousGridBuyProfit25Price)),"LOCK25P",LOCKPreviousGridBuyProfit25Price)
		if(GridBuyFlag26 == 1  ):	print(colored('-grid26BuyP--','green'), float("%0.1f"%(grid26BuyPrice)),"-GridBuyProfit26P--", float("%0.1f"%(GridBuyProfit26Price)) ,"-GridBuyFlag26--",GridBuyFlag26,"-amountBuy26--",float("%0.5f"%(TradedamountBuy26)),"Count",	 GridBuyProfit26PriceCount,"PreviousGridBuyProfit26P", float("%0.1f"%(PreviousGridBuyProfit26Price)),"LOCK26P",LOCKPreviousGridBuyProfit26Price)
		if(GridBuyFlag27 == 1  ):	print(colored('-grid27BuyP--','green'), float("%0.1f"%(grid27BuyPrice)),"-GridBuyProfit27P--", float("%0.1f"%(GridBuyProfit27Price)) ,"-GridBuyFlag27--",GridBuyFlag27,"-amountBuy27--",float("%0.5f"%(TradedamountBuy27)),"Count",	 GridBuyProfit27PriceCount,"PreviousGridBuyProfit27P", float("%0.1f"%(PreviousGridBuyProfit27Price)),"LOCK27P",LOCKPreviousGridBuyProfit27Price)
		if(GridBuyFlag28 == 1  ):	print(colored('-grid28BuyP--','green'), float("%0.1f"%(grid28BuyPrice)),"-GridBuyProfit28P--", float("%0.1f"%(GridBuyProfit28Price)) ,"-GridBuyFlag28--",GridBuyFlag28,"-amountBuy28--",float("%0.5f"%(TradedamountBuy28)),"Count",	 GridBuyProfit28PriceCount,"PreviousGridBuyProfit28P", float("%0.1f"%(PreviousGridBuyProfit28Price)),"LOCK28P",LOCKPreviousGridBuyProfit28Price)
		if(GridBuyFlag29 == 1  ):	print(colored('-grid29BuyP--','green'), float("%0.1f"%(grid29BuyPrice)),"-GridBuyProfit29P--", float("%0.1f"%(GridBuyProfit29Price)) ,"-GridBuyFlag29--",GridBuyFlag29,"-amountBuy29--",float("%0.5f"%(TradedamountBuy29)),"Count",	 GridBuyProfit29PriceCount,"PreviousGridBuyProfit29P", float("%0.1f"%(PreviousGridBuyProfit29Price)),"LOCK29P",LOCKPreviousGridBuyProfit29Price)
		if(GridBuyFlag30 == 1  ):	print(colored('-grid30BuyP--','green'), float("%0.1f"%(grid30BuyPrice)),"-GridBuyProfit30P--", float("%0.1f"%(GridBuyProfit30Price)) ,"-GridBuyFlag30--",GridBuyFlag30,"-amountBuy30--",float("%0.5f"%(TradedamountBuy30)),"Count",	 GridBuyProfit30PriceCount,"PreviousGridBuyProfit30P", float("%0.1f"%(PreviousGridBuyProfit30Price)),"LOCK30P",LOCKPreviousGridBuyProfit30Price)
		
		if(GridSellFlag0  == 1	):	print(colored('-grid0SellP--','red'),float("%0.1f"%(grid0SellPrice )),"-GridSellProfit0P--",float("%0.1f"%(GridSellProfit0Price )) ,"-GridSellFlag0 --",GridSellFlag0 ,"- amountSell0 --",		float("%0.5f"%(TradedamountSell0  ))	   ,"Count",GridSellProfit0PriceCount  , "PreviousGridSellProfit0P ",float("%0.1f"%(PreviousGridSellProfit0Price))		,"LOCK0P",LOCKPreviousGridSellProfit0Price)
		if(GridSellFlag1  == 1	):	print(colored('-grid1SellP--','red'),float("%0.1f"%(grid1SellPrice )),"-GridSellProfit1P--",float("%0.1f"%(GridSellProfit1Price )) ,"-GridSellFlag1 --",GridSellFlag1 ,"- amountSell1 --",		float("%0.5f"%(TradedamountSell1  ))	   ,"Count",GridSellProfit1PriceCount  , "PreviousGridSellProfit1P ",float("%0.1f"%(PreviousGridSellProfit1Price))		,"LOCK1P",LOCKPreviousGridSellProfit1Price)
		if(GridSellFlag2  == 1	):	print(colored('-grid2SellP--','red'),float("%0.1f"%(grid2SellPrice )),"-GridSellProfit2P--",float("%0.1f"%(GridSellProfit2Price )) ,"-GridSellFlag2 --",GridSellFlag2 ,"- amountSell2 --",		float("%0.5f"%(TradedamountSell2  ))	   ,"Count",GridSellProfit2PriceCount  , "PreviousGridSellProfit2P ",float("%0.1f"%(PreviousGridSellProfit2Price))		,"LOCK2P",LOCKPreviousGridSellProfit2Price)
		if(GridSellFlag3  == 1	):	print(colored('-grid3SellP--','red'),float("%0.1f"%(grid3SellPrice )),"-GridSellProfit3P--",float("%0.1f"%(GridSellProfit3Price )) ,"-GridSellFlag3 --",GridSellFlag3 ,"- amountSell3 --",		float("%0.5f"%(TradedamountSell3  ))	   ,"Count",GridSellProfit3PriceCount  , "PreviousGridSellProfit3P ",float("%0.1f"%(PreviousGridSellProfit3Price))		,"LOCK3P",LOCKPreviousGridSellProfit3Price)
		if(GridSellFlag4  == 1	):	print(colored('-grid4SellP--','red'),float("%0.1f"%(grid4SellPrice )),"-GridSellProfit4P--",float("%0.1f"%(GridSellProfit4Price )) ,"-GridSellFlag4 --",GridSellFlag4 ,"- amountSell4 --",		float("%0.5f"%(TradedamountSell4  ))	   ,"Count",GridSellProfit4PriceCount  , "PreviousGridSellProfit4P ",float("%0.1f"%(PreviousGridSellProfit4Price))		,"LOCK4P",LOCKPreviousGridSellProfit4Price)
		if(GridSellFlag5  == 1	):	print(colored('-grid5SellP--','red'),float("%0.1f"%(grid5SellPrice )),"-GridSellProfit5P--",float("%0.1f"%(GridSellProfit5Price )) ,"-GridSellFlag5 --",GridSellFlag5 ,"- amountSell5 --",		float("%0.5f"%(TradedamountSell5  ))	   ,"Count",GridSellProfit5PriceCount  , "PreviousGridSellProfit5P ",float("%0.1f"%(PreviousGridSellProfit5Price))		,"LOCK5P",LOCKPreviousGridSellProfit5Price)
		if(GridSellFlag6  == 1	):	print(colored('-grid6SellP--','red'),float("%0.1f"%(grid6SellPrice )),"-GridSellProfit6P--",float("%0.1f"%(GridSellProfit6Price )) ,"-GridSellFlag6 --",GridSellFlag6 ,"- amountSell6 --",		float("%0.5f"%(TradedamountSell6  ))	   ,"Count",GridSellProfit6PriceCount  , "PreviousGridSellProfit6P ",float("%0.1f"%(PreviousGridSellProfit6Price))		,"LOCK6P",LOCKPreviousGridSellProfit6Price)
		if(GridSellFlag7  == 1	):	print(colored('-grid7SellP--','red'),float("%0.1f"%(grid7SellPrice )),"-GridSellProfit7P--",float("%0.1f"%(GridSellProfit7Price )) ,"-GridSellFlag7 --",GridSellFlag7 ,"- amountSell7 --",		float("%0.5f"%(TradedamountSell7  ))	   ,"Count",GridSellProfit7PriceCount  , "PreviousGridSellProfit7P ",float("%0.1f"%(PreviousGridSellProfit7Price))		,"LOCK7P",LOCKPreviousGridSellProfit7Price)
		if(GridSellFlag8  == 1	):	print(colored('-grid8SellP--','red'),float("%0.1f"%(grid8SellPrice )),"-GridSellProfit8P--",float("%0.1f"%(GridSellProfit8Price )) ,"-GridSellFlag8 --",GridSellFlag8 ,"- amountSell8 --",		float("%0.5f"%(TradedamountSell8  ))	   ,"Count",GridSellProfit8PriceCount  , "PreviousGridSellProfit8P ",float("%0.1f"%(PreviousGridSellProfit8Price))		,"LOCK8P",LOCKPreviousGridSellProfit8Price)
		if(GridSellFlag9  == 1	):	print(colored('-grid9SellP--','red'),float("%0.1f"%(grid9SellPrice )),"-GridSellProfit9P--",float("%0.1f"%(GridSellProfit9Price )) ,"-GridSellFlag9 --",GridSellFlag9 ,"- amountSell9 --",		float("%0.5f"%(TradedamountSell9  ))	   ,"Count",GridSellProfit9PriceCount  , "PreviousGridSellProfit9P ",float("%0.1f"%(PreviousGridSellProfit9Price ))		 ,"LOCK90P",LOCKPreviousGridSellProfit9Price)
		if(GridSellFlag10 == 1	):	print(colored('-grid10SellP--','red'),float("%0.1f"%(grid10SellPrice)),"-GridSellProfit10P--",float("%0.1f"%(GridSellProfit10Price)) ,"-GridSellFlag10--",GridSellFlag10,"- amountSell10--", float("%0.5f"%(TradedamountSell10))	  ,"Count", GridSellProfit10PriceCount,"PreviousGridSellProfit10P",float("%0.1f"%(PreviousGridSellProfit10Price)),"LOCK10P",LOCKPreviousGridSellProfit10Price)
		if(GridSellFlag11 == 1	):	print(colored('-grid11SellP--','red'),float("%0.1f"%(grid11SellPrice)),"-GridSellProfit11P--",float("%0.1f"%(GridSellProfit11Price)) ,"-GridSellFlag11--",GridSellFlag11,"- amountSell11--", float("%0.5f"%(TradedamountSell11))	  ,"Count", GridSellProfit11PriceCount,"PreviousGridSellProfit11P",float("%0.1f"%(PreviousGridSellProfit11Price)),"LOCK11P",LOCKPreviousGridSellProfit11Price)
		if(GridSellFlag12 == 1	):	print(colored('-grid12SellP--','red'),float("%0.1f"%(grid12SellPrice)),"-GridSellProfit12P--",float("%0.1f"%(GridSellProfit12Price)) ,"-GridSellFlag12--",GridSellFlag12,"- amountSell12--", float("%0.5f"%(TradedamountSell12))	  ,"Count", GridSellProfit12PriceCount,"PreviousGridSellProfit12P",float("%0.1f"%(PreviousGridSellProfit12Price)),"LOCK12P",LOCKPreviousGridSellProfit12Price)
		if(GridSellFlag13 == 1	):	print(colored('-grid13SellP--','red'),float("%0.1f"%(grid13SellPrice)),"-GridSellProfit13P--",float("%0.1f"%(GridSellProfit13Price)) ,"-GridSellFlag13--",GridSellFlag13,"- amountSell13--", float("%0.5f"%(TradedamountSell13))	  ,"Count", GridSellProfit13PriceCount,"PreviousGridSellProfit13P",float("%0.1f"%(PreviousGridSellProfit13Price)),"LOCK13P",LOCKPreviousGridSellProfit13Price)
		if(GridSellFlag14 == 1	):	print(colored('-grid14SellP--','red'),float("%0.1f"%(grid14SellPrice)),"-GridSellProfit14P--",float("%0.1f"%(GridSellProfit14Price)) ,"-GridSellFlag14--",GridSellFlag14,"- amountSell14--", float("%0.5f"%(TradedamountSell14))	  ,"Count", GridSellProfit14PriceCount,"PreviousGridSellProfit14P",float("%0.1f"%(PreviousGridSellProfit14Price)),"LOCK14P",LOCKPreviousGridSellProfit14Price)
		if(GridSellFlag15 == 1	):	print(colored('-grid15SellP--','red'),float("%0.1f"%(grid15SellPrice)),"-GridSellProfit15P--",float("%0.1f"%(GridSellProfit15Price)) ,"-GridSellFlag15--",GridSellFlag15,"- amountSell15--", float("%0.5f"%(TradedamountSell15))	  ,"Count", GridSellProfit15PriceCount,"PreviousGridSellProfit15P",float("%0.1f"%(PreviousGridSellProfit15Price)),"LOCK15P",LOCKPreviousGridSellProfit15Price)
		if(GridSellFlag16 == 1	):	print(colored('-grid16SellP--','red'),float("%0.1f"%(grid16SellPrice)),"-GridSellProfit16P--",float("%0.1f"%(GridSellProfit16Price)) ,"-GridSellFlag16--",GridSellFlag16,"- amountSell16--", float("%0.5f"%(TradedamountSell16))	  ,"Count", GridSellProfit16PriceCount,"PreviousGridSellProfit16P",float("%0.1f"%(PreviousGridSellProfit16Price)),"LOCK16P",LOCKPreviousGridSellProfit16Price)
		if(GridSellFlag17 == 1	):	print(colored('-grid17SellP--','red'),float("%0.1f"%(grid17SellPrice)),"-GridSellProfit17P--",float("%0.1f"%(GridSellProfit17Price)) ,"-GridSellFlag17--",GridSellFlag17,"- amountSell17--", float("%0.5f"%(TradedamountSell17))	  ,"Count", GridSellProfit17PriceCount,"PreviousGridSellProfit17P",float("%0.1f"%(PreviousGridSellProfit17Price)),"LOCK17P",LOCKPreviousGridSellProfit17Price)
		if(GridSellFlag18 == 1	):	print(colored('-grid18SellP--','red'),float("%0.1f"%(grid18SellPrice)),"-GridSellProfit18P--",float("%0.1f"%(GridSellProfit18Price)) ,"-GridSellFlag18--",GridSellFlag18,"- amountSell18--", float("%0.5f"%(TradedamountSell18))	  ,"Count", GridSellProfit18PriceCount,"PreviousGridSellProfit18P",float("%0.1f"%(PreviousGridSellProfit18Price)),"LOCK18P",LOCKPreviousGridSellProfit18Price)
		if(GridSellFlag19 == 1	):	print(colored('-grid19SellP--','red'),float("%0.1f"%(grid19SellPrice)),"-GridSellProfit19P--",float("%0.1f"%(GridSellProfit19Price)) ,"-GridSellFlag19--",GridSellFlag19,"- amountSell19--", float("%0.5f"%(TradedamountSell19))	  ,"Count", GridSellProfit19PriceCount,"PreviousGridSellProfit19P",float("%0.1f"%(PreviousGridSellProfit19Price)),"LOCK19P",LOCKPreviousGridSellProfit19Price)
		if(GridSellFlag20 == 1	):	print(colored('-grid20SellP--','red'),float("%0.1f"%(grid20SellPrice)),"-GridSellProfit20P--",float("%0.1f"%(GridSellProfit20Price)) ,"-GridSellFlag20--",GridSellFlag20,"- amountSell20--", float("%0.5f"%(TradedamountSell20))	  ,"Count", GridSellProfit20PriceCount,"PreviousGridSellProfit20P",float("%0.1f"%(PreviousGridSellProfit20Price)),"LOCK20P",LOCKPreviousGridSellProfit20Price)
		if(GridSellFlag21 == 1	):	print(colored('-grid21SellP--','red'),float("%0.1f"%(grid21SellPrice)),"-GridSellProfit21P--",float("%0.1f"%(GridSellProfit21Price)) ,"-GridSellFlag21--",GridSellFlag21,"- amountSell21--", float("%0.5f"%(TradedamountSell21))	  ,"Count", GridSellProfit21PriceCount,"PreviousGridSellProfit21P",float("%0.1f"%(PreviousGridSellProfit21Price)),"LOCK21P",LOCKPreviousGridSellProfit21Price)
		if(GridSellFlag22 == 1	):	print(colored('-grid22SellP--','red'),float("%0.1f"%(grid22SellPrice)),"-GridSellProfit22P--",float("%0.1f"%(GridSellProfit22Price)) ,"-GridSellFlag22--",GridSellFlag22,"- amountSell22--", float("%0.5f"%(TradedamountSell22))	  ,"Count", GridSellProfit22PriceCount,"PreviousGridSellProfit22P",float("%0.1f"%(PreviousGridSellProfit22Price)),"LOCK22P",LOCKPreviousGridSellProfit22Price)
		if(GridSellFlag23 == 1	):	print(colored('-grid23SellP--','red'),float("%0.1f"%(grid23SellPrice)),"-GridSellProfit23P--",float("%0.1f"%(GridSellProfit23Price)) ,"-GridSellFlag23--",GridSellFlag23,"- amountSell23--", float("%0.5f"%(TradedamountSell23))	  ,"Count", GridSellProfit23PriceCount,"PreviousGridSellProfit23P",float("%0.1f"%(PreviousGridSellProfit23Price)),"LOCK23P",LOCKPreviousGridSellProfit23Price)
		if(GridSellFlag24 == 1	):	print(colored('-grid24SellP--','red'),float("%0.1f"%(grid24SellPrice)),"-GridSellProfit24P--",float("%0.1f"%(GridSellProfit24Price)) ,"-GridSellFlag24--",GridSellFlag24,"- amountSell24--", float("%0.5f"%(TradedamountSell24))	  ,"Count", GridSellProfit24PriceCount,"PreviousGridSellProfit24P",float("%0.1f"%(PreviousGridSellProfit24Price)),"LOCK24P",LOCKPreviousGridSellProfit24Price)
		if(GridSellFlag25 == 1	):	print(colored('-grid25SellP--','red'),float("%0.1f"%(grid25SellPrice)),"-GridSellProfit25P--",float("%0.1f"%(GridSellProfit25Price)) ,"-GridSellFlag25--",GridSellFlag25,"- amountSell25--", float("%0.5f"%(TradedamountSell25))	  ,"Count", GridSellProfit25PriceCount,"PreviousGridSellProfit25P",float("%0.1f"%(PreviousGridSellProfit25Price)),"LOCK25P",LOCKPreviousGridSellProfit25Price)
		if(GridSellFlag26 == 1	):	print(colored('-grid26SellP--','red'),float("%0.1f"%(grid26SellPrice)),"-GridSellProfit26P--",float("%0.1f"%(GridSellProfit26Price)) ,"-GridSellFlag26--",GridSellFlag26,"- amountSell26--", float("%0.5f"%(TradedamountSell26))	  ,"Count", GridSellProfit26PriceCount,"PreviousGridSellProfit26P",float("%0.1f"%(PreviousGridSellProfit26Price)),"LOCK26P",LOCKPreviousGridSellProfit26Price)
		if(GridSellFlag27 == 1	):	print(colored('-grid27SellP--','red'),float("%0.1f"%(grid27SellPrice)),"-GridSellProfit27P--",float("%0.1f"%(GridSellProfit27Price)) ,"-GridSellFlag27--",GridSellFlag27,"- amountSell27--", float("%0.5f"%(TradedamountSell27))	  ,"Count", GridSellProfit27PriceCount,"PreviousGridSellProfit27P",float("%0.1f"%(PreviousGridSellProfit27Price)),"LOCK27P",LOCKPreviousGridSellProfit27Price)
		if(GridSellFlag28 == 1	):	print(colored('-grid28SellP--','red'),float("%0.1f"%(grid28SellPrice)),"-GridSellProfit28P--",float("%0.1f"%(GridSellProfit28Price)) ,"-GridSellFlag28--",GridSellFlag28,"- amountSell28--", float("%0.5f"%(TradedamountSell28))	  ,"Count", GridSellProfit28PriceCount,"PreviousGridSellProfit28P",float("%0.1f"%(PreviousGridSellProfit28Price)),"LOCK28P",LOCKPreviousGridSellProfit28Price)
		if(GridSellFlag29 == 1	):	print(colored('-grid29SellP--','red'),float("%0.1f"%(grid29SellPrice)),"-GridSellProfit29P--",float("%0.1f"%(GridSellProfit29Price)) ,"-GridSellFlag29--",GridSellFlag29,"- amountSell29--", float("%0.5f"%(TradedamountSell29))	  ,"Count", GridSellProfit29PriceCount,"PreviousGridSellProfit29P",float("%0.1f"%(PreviousGridSellProfit29Price)),"LOCK29P",LOCKPreviousGridSellProfit29Price)
		if(GridSellFlag30 == 1	):	print(colored('-grid30SellP--','red'),float("%0.1f"%(grid30SellPrice)),"-GridSellProfit30P--",float("%0.1f"%(GridSellProfit30Price)) ,"-GridSellFlag30--",GridSellFlag30,"- amountSell30--", float("%0.5f"%(TradedamountSell30))	  ,"Count", GridSellProfit30PriceCount,"PreviousGridSellProfit30P",float("%0.1f"%(PreviousGridSellProfit30Price)),"LOCK30P",LOCKPreviousGridSellProfit30Price)

	
	except Exception as AA:
					# exc_type, exc_obj, exc_tb = sys.exc_info()
					# print(exc_type, fname, exc_tb.tb_lineno)	
					print("!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! PrintFunc !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",AA)								

	threading.Timer(1, PrintFunc).start()





if(SellDirectinalGrid==0 and BuyDirectinalGrid==1  and	BotType=="SUPERTREND-LONG" ):
	SUPERTRENDLONG()
	print("+++++++++++++++++++++++++++++++++++++++++++++++++ SUPERTRENDLONG FUNC ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
if(SellDirectinalGrid==1 and BuyDirectinalGrid==0  and	BotType=="SUPERTREND-SHORT" ):
	SUPERTRENDSHORT()
	
	
TICKSFunc()
PrintFunc()


