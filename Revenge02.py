import ccxt
import re
import imaplib
import email
import time, threading
import sys 
import os
from termcolor import *
import numpy
import colorama
import numpy as np
import os
import random
from termcolor import colored
os.system('color')
from pynput import keyboard
from playsound import playsound
import csv
from datetime import datetime
from decimal import Decimal


from colorama import init, Fore, Back, Style

init(convert=True)





print('CCXT version:', ccxt.__version__)
binance = ccxt.binance({
	'apiKey': 'apiKey',
	'secret': 'secret',
	'enableRateLimit': True,
	'options': {
		'defaultType': 'future',  # requires CCXT version > 1.20.31
		'adjustForTimeDifference': True,
		'recvWindow': 10000000
	},
})
version=1
# binanceusdtmarkets = binance.load_markets ()
# binance.verbose = True  # uncomment this line if it doesn't work

symbol = 'BTC/USDT'
Subject='NONE'
SubjectManual='NONE'
OrderActionTakenGlobal='NONE'
AmountGlobal=0
SubjectGlobal='NONE'
profitLock=0
profitLockKey=0
i=0
AddMoreToPostion=0
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
FirstProfitLock=0
FirstProfitLockArray=[]
LocakPrecentToBeUsedAfterFirstProfitLock=2
LocakPrecentToBeUsedAfterFirstProfitLockArray=[]
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
KeyPressedToSELL=0
NextProfitPrice=0
IncreasedNumber=0
SN1M=0
lockarray1 =0
lockarray2 =0
lockarray3 =0
lockarray4 =0
lockarray5 =0
lockarray6 =0
lockarray7 =0
lockarray8 =0
lockarray9 =0
lockarray10=0
lockarray11=0
lockarray12=0
lockarray13=0
lockarray14=0
lockarray15=0
lockarray16=0
lockarray17=0
lockarray18=0
lockarray19=0
lockarray20=0
lockarray21=0
lockarray22=0
lockarray23=0
lockarray24=0
lockarray25=0
lockarray26=0
lockarray27=0
lockarray28=0
lockarray29=0
lockarray30=0
lockarray31=0
lockarray32=0
lockarray33=0
lockarray34=0
lockarray35=0
lockarray36=0
lockarray37=0
lockarray38=0
lockarray39=0
lockarray40=0
lockarray41=0
lockarray42=0
lockarray43=0
lockarray44=0
lockarray45=0
lockarray46=0
lockarray47=0
lockarray48=0
lockarray49=0
lockarray50=0
lockarray51=0
lockarray52=0
lockarray53=0
lockarray54=0
lockarray55=0
lockarray56=0
lockarray57=0
lockarray58=0
lockarray59=0
lockarray60=0
lockarray61=0
lockarray62=0
lockarray63=0
lockarray64=0
lockarray65=0
lockarray66=0
lockarray67=0
lockarray68=0
lockarray69=0
lockarray70=0
lockarray71=0
lockarray72=0
lockarray73=0
lockarray74=0
lockarray75=0
lockarray76=0
lockarray77=0
lockarray78=0
lockarray79=0
lockarray80=0
lockarray81=0
lockarray82=0
lockarray83=0
lockarray84=0
lockarray85=0
lockarray86=0
lockarray87=0
lockarray88=0
lockarray89=0
lockarray90=0
lockarray91=0
lockarray92=0
lockarray93=0
lockarray94=0
lockarray95=0
lockarray96=0
lockarray97=0
lockarray98=0
lockarray99=0
lockarray100=0
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
StartPlayingSoundN=0
UnRlealizedAcualWalletBalance=0

PostionFullInfo="NONE"
MainPositionAmount=0
MainPositionEntryPrice=0
MainPositionLiquidationPrice=0
MainPostionProfit=0
leverage=0
MainPostionSide="NONE"
FirstIntiatedWalletBalance=0
StopMultiSignals=0
Orderamount=0
previousOrderWas="NONE"
CurrentWalletBalanceWithProfit=0
version=1.1
StopWalletIncrease=0
StopFirstProfitSound=0
RealPostionAmountToclOSeCorretcly=0
RealpositionInitialMargin=0
LastProfitOnly=0
LastEntryPOstionPrice=0
StillInPostion=13
UsingSellAgainToClosePostion=0
SoldOnceAlready=0
PriceTargetPrevious=0
PriceTarget0=0
PriceTarget2=0
PriceTarget3=0
PriceTarget4=0
PriceTarget5=0
TradingAmountpercent=0
FirstProfitGain=0
PreviousProfitGain=0
SecondProfitGain=0
ThirdProfitGain=0
FourthProfitGain=0
FivthProfitGain=0
# # extra params and overrides if needed
params = {
	'test': True,  # test if it's valid, but don't actually place it
}

# # ################################### EMPTY INBOX FIRST ###############################################
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('sobh.bot.live@gmail.com', 'GMAILPASS')
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

if (Margin==125):
	TradingAmountpercent=40
if (Margin==100):
	TradingAmountpercent=35	   



def TICKSFunc():
	global StartPlayingSoundN
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
	global profitLock
	global profitLockKey
	global SubjectManual
	global previousDynaimicProfitPercent
	global totalWalletBalance
	global totalUnrealizedProfitBalance
	global totalUnrealizedProfitBalanceInPercent
	global LastPriceTICKS
	global FirstProfitLock
	global SELLNOW
	global PrecentProfitLock
	global PositionPrice
	global SL
	global StopLossPricePercent
	global StopLossPriceFull
	global	ClosesArrayFor14
	global	LowArrayFor14
	global	HighArrayFor14	
	global	ClosesFor50P1HArray
	global	Margin	
	global	TradeBotUsedMargin
	global	LocakPrecentToBeUsedAfterFirstProfitLock
	global MI
	global FirstProfitLockArray
	global LocakPrecentToBeUsedAfterFirstProfitLockArray
	global	CI
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
	global KeyPressedToSELL
	global KeyPressedToBuy
	global NextProfitPrice
	global IncreasedNumber
	global lockarray1
	global lockarray2
	global lockarray3
	global lockarray4
	global lockarray5
	global lockarray6
	global lockarray7
	global lockarray8
	global lockarray9
	global lockarray10
	global lockarray11
	global lockarray12
	global lockarray13
	global lockarray14
	global lockarray15
	global lockarray16
	global lockarray17
	global lockarray18
	global lockarray19
	global lockarray20
	global lockarray21
	global lockarray22
	global lockarray23
	global lockarray24
	global lockarray25
	global lockarray26
	global lockarray27
	global lockarray28
	global lockarray29
	global lockarray30
	global lockarray31
	global lockarray32
	global lockarray33
	global lockarray34
	global lockarray35
	global lockarray36
	global lockarray37
	global lockarray38
	global lockarray39
	global lockarray40
	global lockarray41
	global lockarray42
	global lockarray43
	global lockarray44
	global lockarray45
	global lockarray46
	global lockarray47
	global lockarray48
	global lockarray49
	global lockarray50
	global lockarray51
	global lockarray52
	global lockarray53
	global lockarray54
	global lockarray55
	global lockarray56
	global lockarray57
	global lockarray58
	global lockarray59
	global lockarray60
	global lockarray61
	global lockarray62
	global lockarray63
	global lockarray64
	global lockarray65
	global lockarray66
	global lockarray67
	global lockarray68
	global lockarray69
	global lockarray70
	global lockarray71
	global lockarray72
	global lockarray73
	global lockarray74
	global lockarray75
	global lockarray76
	global lockarray77
	global lockarray78
	global lockarray79
	global lockarray80
	global lockarray81
	global lockarray82
	global lockarray83
	global lockarray84
	global lockarray85
	global lockarray86
	global lockarray87
	global lockarray88
	global lockarray89
	global lockarray90
	global lockarray91
	global lockarray92
	global lockarray93
	global lockarray94
	global lockarray95
	global lockarray96
	global lockarray97
	global lockarray98
	global lockarray99
	global lockarray100
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
	global SN1M
	global UnRlealizedAcualWalletBalance
	global PostionFullInfo
	global MainPositionAmount
	global MainPositionEntryPrice
	global MainPositionLiquidationPrice
	global MainPostionProfit
	global leverage
	global MainPostionSide
	global FirstIntiatedWalletBalance
	global StopMultiSignals
	global Orderamount
	global previousOrderWas
	global version
	global AddMoreToPostion
	global CurrentWalletBalanceWithProfit
	global StopWalletIncrease
	global StopFirstProfitSound
	global RealPostionAmountToclOSeCorretcly
	global RealpositionInitialMargin
	global LastProfitOnly
	global LastEntryPOstionPrice
	global StillInPostion
	global UsingSellAgainToClosePostion
	global SoldOnceAlready
	global PriceTargetPrevious
	global PriceTarget2
	global PriceTarget3
	global PriceTarget4
	global PriceTarget5
	global PriceTarget0
	global TradingAmountpercent
	global FirstProfitGain
	global PreviousProfitGain
	global SecondProfitGain
	global ThirdProfitGain
	global FourthProfitGain
	global FivthProfitGain

	





	try:
		mail = imaplib.IMAP4_SSL('imap.gmail.com')
		mail.login('sobh.bot.live@gmail.com', 'gmailpass')
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
	try:
		TickersInfo=binance.fetchTicker (symbol)
		OpenPriceTICKS=TickersInfo.get("open")
		LastPriceTICKS=TickersInfo.get("last")
		HighPriceTICKS=TickersInfo.get("high")
		LowPriceTICKS=TickersInfo.get("low")
		VolumePriceTICKSBTC=TickersInfo.get("baseVolume")
		VolumePriceTICKSUSDT=(VolumePriceTICKSBTC*LastPriceTICKS)/1000000
		BalanceRes = binance.fetchBalance ()
		totalWalletBalance=BalanceRes.get("info").get("totalWalletBalance")
		walletBalance=BalanceRes.get("info").get("walletBalance")
		maxWithdrawAmount=BalanceRes.get("info").get("maxWithdrawAmount")
		totalWalletBalance=float(totalWalletBalance)
		# ######################################################## USING STATIC PERCENT With MANUAL ORDER ###########################################################	
		if(ManualSize!=0 and ManualPositionDirection!='NONE' and UseATRForTrading==0 and IncreasedNumber==0):
			PositionPrice=LastPriceTICKS
			FirstProfitLock= ATRValueOpenPostionTime
			previousProfitLock=(FirstProfitLock/1.1) 
			# ##################  GENERATING THE PROFIT ARRAY 
			MI=0
			CI=0
			A=FirstProfitLock
			while MI >=0 and MI < 100 :
				A=.5+A+previousProfitLock
				# LocakPrecentToBeUsedAfterFirstProfitLock=LocakPrecentToBeUsedAfterFirstProfitLock+20
				FirstProfitLockArray.append(A)
				MI=MI+1
			while CI >=0 and CI < 100 :			
				print("FirstProfitLockArray",[CI],FirstProfitLockArray[CI])
				CI=CI+1	
		# #################################################		
		


		if(PositionPrice!=0 and OrderActionTakenGlobal=='LONG' and ManualSize==0):
				TottalIntiatedMarginAuto=PositionPrice*AmountGlobal	
				CurrentPositionProfit=((LastPriceTICKS*AmountGlobal)-TottalIntiatedMarginAuto)
				CurrentPositionProfitPercent=  (CurrentPositionProfit/(TottalIntiatedMarginAuto/Margin))*100
				StopLossPricePercent=((PositionPrice/2.5)/Margin)*SL
				StopLossPriceFull=PositionPrice-StopLossPricePercent
				currentPosition='LONG'
				UnRlealizedAcualWalletBalance=totalWalletBalance+CurrentPositionProfit
				FirstProfitGain=((NextProfitPrice*AmountGlobal)-TottalIntiatedMarginAuto)
				PreviousProfitGain=((PriceTargetPrevious*AmountGlobal)-TottalIntiatedMarginAuto)
				SecondProfitGain=((PriceTarget0*AmountGlobal)-TottalIntiatedMarginAuto)
				ThirdProfitGain=((PriceTarget2*AmountGlobal)-TottalIntiatedMarginAuto)
				FourthProfitGain=((PriceTarget3*AmountGlobal)-TottalIntiatedMarginAuto)
				FivthProfitGain=((PriceTarget4*AmountGlobal)-TottalIntiatedMarginAuto)
				

		if(PositionPrice!=0 and OrderActionTakenGlobal=='SHORT' and ManualSize==0):	
				TottalIntiatedMarginAuto=PositionPrice*AmountGlobal
				CurrentPositionProfit=(TottalIntiatedMarginAuto-(LastPriceTICKS*AmountGlobal))
				CurrentPositionProfitPercent=  (CurrentPositionProfit/(TottalIntiatedMarginAuto/Margin))*100
				StopLossPricePercent=((PositionPrice/2.5)/Margin)*SL
				StopLossPriceFull=PositionPrice+StopLossPricePercent
				currentPosition='SHORT'
				UnRlealizedAcualWalletBalance=totalWalletBalance+CurrentPositionProfit
				FirstProfitGain=(TottalIntiatedMarginAuto-(NextProfitPrice*AmountGlobal))
				PreviousProfitGain=(TottalIntiatedMarginAuto-(PriceTargetPrevious*AmountGlobal))
				SecondProfitGain=(TottalIntiatedMarginAuto-(PriceTarget0*AmountGlobal))
				ThirdProfitGain=(TottalIntiatedMarginAuto-(PriceTarget2*AmountGlobal))
				FourthProfitGain=(TottalIntiatedMarginAuto-(PriceTarget3*AmountGlobal))
				FivthProfitGain=(TottalIntiatedMarginAuto-(PriceTarget4*AmountGlobal))
				
				
				


		if "SHORT" == SubjectGlobal	 and  OrderActionTakenGlobal=='LONG'	  and totalWalletBalance!=0 and StopMultiSignals==0:
			SELLNOW="TRUE"
			SubjectGlobal="SHORT" 
			OrderActionTakenGlobal='NONE'
			
		if "LONG" == SubjectGlobal	 and  OrderActionTakenGlobal=='SHORT'	  and totalWalletBalance!=0 and StopMultiSignals==0:
			SELLNOW="TRUE"
			SubjectGlobal="LONG" 
			OrderActionTakenGlobal='NONE'			





		if "SHORT" == SubjectGlobal	 and  OrderActionTakenGlobal=='NONE'	  and totalWalletBalance!=0 and StopMultiSignals==0:
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> SHORTING NOW >>>>>>>>>>>>>>>>>>>>>>>>','red'))
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> SHORTING NOW >>>>>>>>>>>>>>>>>>>>>>>>','red'))
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> SHORTING NOW >>>>>>>>>>>>>>>>>>>>>>>>','red'))
			print(" >>>>>>>>>>>>>>>>>>>>>>>> SHORTING NOW >>>>>>>>>>>>>>>>>>>>>>>>", "OrderActionTakenGlobal=====================",OrderActionTakenGlobal)
			BalanceRes = binance.fetchBalance ()
			totalWalletBalance=BalanceRes.get("info").get("totalWalletBalance")
			totalWalletBalance=float(totalWalletBalance)
			Tradedamount=( ((totalWalletBalance/TradingAmountpercent)*Margin) / LastPriceTICKS )
			Ordertype='sell'
			Orderside='market'
			Orderprice=LastPriceTICKS
			OrderActionWas='sell'
			OrderActionTakenGlobal="SHORT"
			Orderamount=Tradedamount
			# binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)  # Limit Order is different Than Market Order in Orders
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)  # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','red'),Orderamount,"totalWalletBalance",totalWalletBalance)
			AmountGlobal=Orderamount
			PositionPrice=LastPriceTICKS
			PositionPriceIndollars=(PositionPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.0400)/100
			# ######################################################## USING ATR ###########################################################
			if(PositionPrice!=0 and OrderActionTakenGlobal=='SHORT' and ManualSize==0 and ManualPositionDirection=='NONE' and UseATRForTrading==1):
				print(" >>>>>>>>>>>>>>>>>>>>>>>> USING ATR NOW SHORT")
				SLUsingATR=PositionPrice+ATRValueOpenPostionTime # STOP LOSS FOR SHORTING POS USING ATR .. POS PRICE + ATR VALUE 
				ProfitUsingATR=PositionPrice-(ATRValueOpenPostionTime*1) # PROFIT FOR SHORTING POS USING ATR .. POS PRICE - ATR VALUE
				AutoATRVALUEToProfitLock=(ATRValueOpenPostionTime*1/PositionPrice)*100		 # GETTING THE FIRST PROFIT LOCK VALUE FROM ATR
				FirstProfitLock= (AutoATRVALUEToProfitLock)*Margin		# Generating the FirstProfit Lock Using AutoATRVALUEToProfitLock times the margin
				previousProfitLock=(FirstProfitLock/1.1) # Generating the previousProfitLock Lock Using FirstProfitLock deivided by 2
				TheFirstpreviousProfit=(FirstProfitLock/1.1)
			# ######################################################## USING STATIC PERCENT ###########################################################	
			if(PositionPrice!=0 and OrderActionTakenGlobal=='SHORT' and ManualSize==0 and ManualPositionDirection=='NONE' and UseATRForTrading==13):
				print(" >>>>>>>>>>>>>>>>>>>>>>>> USING STATIC EMAIL PERCENT NOW SHORT")
				PositionPrice=LastPriceTICKS
				FirstProfitLock= UsingEmailedStaticPercent
				previousProfitLock=(FirstProfitLock/1.1)
				TheFirstpreviousProfit=(FirstProfitLock/1.1)			
			# ##################  GENERATING THE PROFIT ARRAY 
			MI=0
			CI=0
			A=(FirstProfitLock/3)
			print("previousProfitLock",previousProfitLock,"FirstProfitLock",FirstProfitLock)
			try:
				while MI >=0 and MI < 100 :
					A=A+(FirstProfitLock/3)
					if A > FirstProfitLock :
						FirstProfitLockArray.append(A)
					MI=MI+1
				while CI >=0 and CI <100 :	
					print("FirstProfitLockArray",[CI],FirstProfitLockArray[CI])
					CI=CI+1
			except Exception as asssc: 
					print("!!!!!!!!!!!!!!!!! Err is SHORTing the Array !!!!!!!!!!!!!!!",asssc)		
			# #################################################	
			CurrentPositionProfit=0
			ManualEntryPrice=0
			ManualSize=0
			ManualPositionDirection='NONE'
			CurrentPositionProfitPercent=0
			inPostion=1
			KeyPressedToBuy=0
			KeyPressedToSELL=0
			StopMultiSignals=1
			UsingSellAgainToClosePostion=1
			OrderpriceFile= open("Orderprice.txt","w+")
			OrderpriceFile.write(str(Orderprice))
			OrderpriceFile.close() 
			OrdertypeFile= open("OrdertypeFile.txt","w+")
			OrdertypeFile.write(str(Ordertype))
			OrdertypeFile.close()
			OrdertypeFile= open("Orderamount.txt","w+")
			OrdertypeFile.write(str(Orderamount))
			OrdertypeFile.close()
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			

	
		if "LONG" == SubjectGlobal and OrderActionTakenGlobal=='NONE'  and totalWalletBalance!=0 and StopMultiSignals==0:	
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> LONGING NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'))
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> LONGING NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'))
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> LONGING NOW >>>>>>>>>>>>>>>>>>>>>>>>','green'))
			# time.sleep(10)
			print(" >>>>>>>>>>>>>>>>>>>>>>>> LONGING NOW >>>>>>>>>>>>>>>>>>>>>>>> ", "OrderActionTakenGlobal====================",OrderActionTakenGlobal)
			BalanceRes = binance.fetchBalance ()
			totalWalletBalance=BalanceRes.get("info").get("totalWalletBalance")
			totalWalletBalance=float(totalWalletBalance)
			Tradedamount=( ((totalWalletBalance/TradingAmountpercent)*Margin) / LastPriceTICKS )
			Ordertype='buy'
			Orderside='market'
			Orderprice=LastPriceTICKS
			OrderActionWas='buy'
			OrderActionTakenGlobal="LONG"
			Orderamount=Tradedamount
			# binance.createOrder (symbol,Orderside,Ordertype,Orderamount,Orderprice)  # Limit Order is different Than Market Order in Orders
			binance.createOrder (symbol,Orderside,Ordertype,Orderamount)  # working 
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>> Orderamount NOW >>>>>>>>>>>>>>>>>>>>>>>>','red'),Orderamount,"totalWalletBalance",totalWalletBalance)
			AmountGlobal=Orderamount
			PositionPrice=LastPriceTICKS
			PositionPriceIndollars=(PositionPrice*Orderamount)
			FeesMarket=(PositionPriceIndollars*0.0200)/100
			# ######################################################## USING ATR ###########################################################
			if(PositionPrice!=0 and OrderActionTakenGlobal=='LONG' and ManualSize==0 and ManualPositionDirection=='NONE' and UseATRForTrading==1):
				print(" >>>>>>>>>>>>>>>>>>>>>>>> USING ATR NOW SHORT")
				SLUsingATR=PositionPrice-ATRValueOpenPostionTime # STOP LOSS FOR LONGING POS USING ATR .. POS PRICE - ATR VALUE 
				ProfitUsingATR=PositionPrice+(ATRValueOpenPostionTime*1) # PROFIT FOR LONGING POS USING ATR .. POS PRICE + ATR VALUE
				AutoATRVALUEToProfitLock=(ATRValueOpenPostionTime*1/PositionPrice)*100		 # GETTING THE FIRST PROFIT LOCK VALUE FROM ATR
				FirstProfitLock= (AutoATRVALUEToProfitLock)*Margin		# Generating the FirstProfit Lock Using AutoATRVALUEToProfitLock times the margin
				previousProfitLock=(FirstProfitLock/1.1) # Generating the previousProfitLock Lock Using FirstProfitLock deivided by 2
				TheFirstpreviousProfit=(FirstProfitLock/1.1)
			# ######################################################## USING STATIC PERCENT ###########################################################		
			if(PositionPrice!=0 and OrderActionTakenGlobal=='LONG' and ManualSize==0 and ManualPositionDirection=='NONE' and UseATRForTrading==13):
				print(" >>>>>>>>>>>>>>>>>>>>>>>> USING STATIC EMAIL PERCENT NOW LONG")
				PositionPrice=LastPriceTICKS
				FirstProfitLock= UsingEmailedStaticPercent
				previousProfitLock=(FirstProfitLock/1.1)
				TheFirstpreviousProfit=(FirstProfitLock/1.1)			
			# ##################  GENERATING THE PROFIT ARRAY 
			MI=0
			CI=0
			A=(FirstProfitLock/3)
			print("previousProfitLock",previousProfitLock,"FirstProfitLock",FirstProfitLock)
			try:
				while MI >=0 and MI < 100 :
					A=A+(FirstProfitLock/3)
					if A > FirstProfitLock :
						FirstProfitLockArray.append(A)
					MI=MI+1
				while CI >=0 and CI <100 :	
					print("FirstProfitLockArray",[CI],FirstProfitLockArray[CI])
					CI=CI+1
			except Exception as aacss: 
					print("!!!!!!!!!!!!!!!!! Err is LONG the Array !!!!!!!!!!!!!!!",aacss)		
			# #################################################	
			CurrentPositionProfit=0
			ManualEntryPrice=0
			ManualSize=0
			ManualPositionDirection='NONE'
			CurrentPositionProfitPercent=0
			inPostion=1
			KeyPressedToBuy=0
			KeyPressedToSELL=0
			StopMultiSignals=1
			UsingSellAgainToClosePostion=1
			OrderpriceFile= open("Orderprice.txt","w+")
			OrderpriceFile.write(str(Orderprice))
			OrderpriceFile.close() 
			OrdertypeFile= open("OrdertypeFile.txt","w+")
			OrdertypeFile.write(str(Ordertype))
			OrdertypeFile.close()
			OrdertypeFile= open("Orderamount.txt","w+")
			OrdertypeFile.write(str(Orderamount))
			OrdertypeFile.close()
			now1M = datetime.now() 
			dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
			


			
		if ("CHANGE" == SubjectGlobal and totalWalletBalance!=0 and currentPosition!='NONE' ) :
			# ######################################################## USING STATIC PERCENT ###########################################################		
			print(" >>>>>>>>>>>>>>>>>>>>>>>> CHNAGING PROFIT PERCENTAGE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
			FirstProfitLock= UsingEmailedStaticPercent
			previousProfitLock=(FirstProfitLock/1.1)
			TheFirstpreviousProfit=(FirstProfitLock/1.1)			
			# ##################  GENERATING THE PROFIT ARRAY 
			MI=0
			CI=0
			A=(FirstProfitLock/3)
			FirstProfitLockArray.clear()
			print("previousProfitLock",previousProfitLock,"FirstProfitLock",FirstProfitLock,"A",A,"MI",MI,"CI",CI)
			try:
				while MI >=0 and MI < 100 :
					A=A+(FirstProfitLock/3)
					if A > FirstProfitLock :
						FirstProfitLockArray.append(A)
					MI=MI+1
				while CI >=0 and CI <100 :	
					print("FirstProfitLockArray",[CI],FirstProfitLockArray[CI])
					CI=CI+1
			except Exception as eac: 
					print("!!!!!!!!!!!!!!!!! Err is changing the Array !!!!!!!!!!!!!!!",eac)		
			# #################################################	
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! THE PROFIT PERCENT	 HAD BEEN CHANGED	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! PLEASE SEND IMIDTAE EMAIL TO FIX AND STOP THIS	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")			
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			
	
	
	
	

		if ("EXIT" == SubjectGlobal and	 totalWalletBalance!=0	 and MainPostionSide=='LONG' or "EXIT" == SubjectGlobal and	 totalWalletBalance!=0	 and MainPostionSide=='SHORT') :
			SELLNOW ='TRUE'
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! SELLing USINg EXIT EXIT EXIT EXIT EXIT EXIT EXIT EXIT EXIT EXIT EXIT	  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")	
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
			print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
	
	
		
		
		
			
		
		
		if(currentPosition=='NONE'):
			print(colored('>>>> currentPosition is >>>>>>>>> NONE ','grey'))
		if(currentPosition=='LONG'):
			print(colored('>>>> currentPosition is >>>>>>>>> LONG ','green'))
			NextProfitPrice=((FirstProfitLock/Margin))
			NextProfitPrice=(PositionPrice*NextProfitPrice)/100
			NextProfitPrice=(PositionPrice+NextProfitPrice)
			PriceTargetPrevious=((previousProfitLock/Margin))
			PriceTargetPrevious=(PositionPrice*PriceTargetPrevious)/100
			PriceTargetPrevious=(PositionPrice+PriceTargetPrevious)
			PriceTarget0=((FirstProfitLockArray[0]/Margin))
			PriceTarget0=(PositionPrice*PriceTarget0)/100
			PriceTarget0=(PositionPrice+PriceTarget0)
			PriceTarget2=((FirstProfitLockArray[1]/Margin))
			PriceTarget2=(PositionPrice*PriceTarget2)/100
			PriceTarget2=(PositionPrice+PriceTarget2)
			PriceTarget3=((FirstProfitLockArray[2]/Margin))
			PriceTarget3=(PositionPrice*PriceTarget3)/100
			PriceTarget3=(PositionPrice+PriceTarget3)
			PriceTarget4=((FirstProfitLockArray[3]/Margin))
			PriceTarget4=(PositionPrice*PriceTarget4)/100
			PriceTarget4=(PositionPrice+PriceTarget4)
		if(currentPosition=='SHORT'):
			print(colored('>>>> currentPosition is >>>>>>>>> SHORT ','red'))		
			NextProfitPrice=((FirstProfitLock/Margin))
			NextProfitPrice=(PositionPrice*NextProfitPrice)/100
			NextProfitPrice=(PositionPrice-NextProfitPrice)
			PriceTargetPrevious=((previousProfitLock/Margin))
			PriceTargetPrevious=(PositionPrice*PriceTargetPrevious)/100
			PriceTargetPrevious=(PositionPrice-PriceTargetPrevious)
			PriceTarget0=((FirstProfitLockArray[0]/Margin))
			PriceTarget0=(PositionPrice*PriceTarget0)/100
			PriceTarget0=(PositionPrice-PriceTarget0)
			PriceTarget2=((FirstProfitLockArray[1]/Margin))
			PriceTarget2=(PositionPrice*PriceTarget2)/100
			PriceTarget2=(PositionPrice-PriceTarget2)
			PriceTarget3=((FirstProfitLockArray[2]/Margin))
			PriceTarget3=(PositionPrice*PriceTarget3)/100
			PriceTarget3=(PositionPrice-PriceTarget3)
			PriceTarget4=((FirstProfitLockArray[3]/Margin))
			PriceTarget4=(PositionPrice*PriceTarget4)/100
			PriceTarget4=(PositionPrice-PriceTarget4)
		
		


		if(CurrentPositionProfit!=0 and currentPosition!='NONE'):
			if( CurrentPositionProfitPercent >= FirstProfitLock and	 CurrentPositionProfitPercent	 !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 and StopFirstProfitSound==0):
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! FIRST	IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! FIRST	IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! FIRST	IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
				playsound('FirstProfitHadBeenLocked.mp3')
				StopFirstProfitSound=13
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[0] and lockarray1==0 and CurrentPositionProfitPercent	 !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					SafeFirstpreviousProfitLock=13
					previousProfitLock=FirstProfitLock
					FirstProfitLock=FirstProfitLockArray[0]
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",SafeFirstpreviousProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 1ST IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray1=1
					ProfitLevel=1
					if(StartPlayingSoundN==0):
						playsound('FirstProfitHadBeenLocked.mp3')
						# sound_thread = threading.Thread(target=lambda:playsound('FirstProfitHadBeenLocked.mp3'))
						# sound_thread.start()
						StartPlayingSoundN=13
						playsound('SecondProfitHadBeenLocked.mp3')					
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[1] and lockarray2==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ): 
					FirstProfitLock=FirstProfitLockArray[1]
					previousProfitLock=FirstProfitLockArray[0]	 
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 2 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray2=1
					ProfitLevel=2
					# playsound('ThirdProfitHadBeenLocked.mp3')
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[2] and lockarray3==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ): 
					FirstProfitLock=FirstProfitLockArray[2]	  
					previousProfitLock=FirstProfitLockArray[1]	 
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 3 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray3=1
					ProfitLevel=3
					# playsound('FourthProfitHadBeenLocked.mp3')
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[3] and lockarray4==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ): 
					FirstProfitLock=FirstProfitLockArray[3]	  
					previousProfitLock=FirstProfitLockArray[2]	 
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 4 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray4=1
					ProfitLevel=4
					# playsound('FifthProfitHadBeenLocked.mp3')
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[4] and lockarray5==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ): 
					FirstProfitLock=FirstProfitLockArray[4]	  
					previousProfitLock=FirstProfitLockArray[3]	 
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 5 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray5=1
					ProfitLevel=5
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[5] and lockarray6==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ): 
					FirstProfitLock=FirstProfitLockArray[5]	  
					previousProfitLock=FirstProfitLockArray[4]	 
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 6 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray6=1
					ProfitLevel=6
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[6] and lockarray7==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ): 
					FirstProfitLock=FirstProfitLockArray[6]	  
					previousProfitLock=FirstProfitLockArray[5]	 
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 7 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray7=1
					ProfitLevel=7
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[7] and lockarray8==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ): 
					FirstProfitLock=FirstProfitLockArray[7]	  
					previousProfitLock=FirstProfitLockArray[6]	 
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 8 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray8=1
					ProfitLevel=8
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[8] and lockarray9==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ): 
					FirstProfitLock=FirstProfitLockArray[8]	  
					previousProfitLock=FirstProfitLockArray[7]	 
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 9 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray9=1
					ProfitLevel=9
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[9] and lockarray10==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ): 
					FirstProfitLock=FirstProfitLockArray[9]	  
					previousProfitLock=FirstProfitLockArray[8]	 
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 10 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray10=1
					ProfitLevel=10
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[10] and lockarray11==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[10]  
					previousProfitLock=FirstProfitLockArray[9]	 
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 11 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray11=1
					ProfitLevel=11
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[11] and lockarray12==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[11]  
					previousProfitLock=FirstProfitLockArray[10]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 12 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray12=1
					ProfitLevel=12
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[12] and lockarray13==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[12]  
					previousProfitLock=FirstProfitLockArray[11]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 13 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray13=1
					ProfitLevel=13
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[13] and lockarray14==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[13]  
					previousProfitLock=FirstProfitLockArray[12]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 14 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray14=1
					ProfitLevel=14
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[14] and lockarray15==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[14]  
					previousProfitLock=FirstProfitLockArray[13]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 15 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray15=1
					ProfitLevel=15
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[15] and lockarray16==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[15]  
					previousProfitLock=FirstProfitLockArray[14]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 16 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray16=1
					ProfitLevel=16
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[16] and lockarray17==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[16]  
					previousProfitLock=FirstProfitLockArray[15]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 17 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray17=1
					ProfitLevel=17
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[17] and lockarray18==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[17]  
					previousProfitLock=FirstProfitLockArray[16]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 18 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray18=1
					ProfitLevel=18
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[18] and lockarray19==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[18]  
					previousProfitLock=FirstProfitLockArray[17]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 19 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray19=1
					ProfitLevel=19
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[19] and lockarray20==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[19]  
					previousProfitLock=FirstProfitLockArray[18]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 20 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray20=1
					ProfitLevel=20
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[20] and lockarray21==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[20]  
					previousProfitLock=FirstProfitLockArray[19]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 21 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray21=1
					ProfitLevel=21
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[21] and lockarray22==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[21]  
					previousProfitLock=FirstProfitLockArray[20]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 22 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray22=1
					ProfitLevel=22
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[22] and lockarray23==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[22]  
					previousProfitLock=FirstProfitLockArray[21]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 23 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray23=1
					ProfitLevel=23
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[23] and lockarray24==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[23]  
					previousProfitLock=FirstProfitLockArray[22]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 24 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray24=1
					ProfitLevel=24
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[24] and lockarray25==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[24]  
					previousProfitLock=FirstProfitLockArray[23]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 25 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray25=1
					ProfitLevel=25
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[25] and lockarray26==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[25]  
					previousProfitLock=FirstProfitLockArray[24]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 26 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray26=1
					ProfitLevel=26
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[26] and lockarray27==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[26]  
					previousProfitLock=FirstProfitLockArray[25]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 27 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray27=1
					ProfitLevel=27
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[27] and lockarray28==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[27]  
					previousProfitLock=FirstProfitLockArray[26]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 28 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray28=1
					ProfitLevel=28
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[28] and lockarray29==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[28]  
					previousProfitLock=FirstProfitLockArray[27]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 29 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray29=1
					ProfitLevel=29
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[29] and lockarray30==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[29]  
					previousProfitLock=FirstProfitLockArray[28]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 30 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray30=1
					ProfitLevel=30
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[30] and lockarray31==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[30]  
					previousProfitLock=FirstProfitLockArray[29]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 31 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray31=1
					ProfitLevel=31
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[31] and lockarray32==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[31]  
					previousProfitLock=FirstProfitLockArray[30]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 32 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray32=1
					ProfitLevel=32
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[32] and lockarray33==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[32]  
					previousProfitLock=FirstProfitLockArray[31]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 33 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray33=1
					ProfitLevel=33
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[33] and lockarray34==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[33]  
					previousProfitLock=FirstProfitLockArray[32]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 34 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray34=1
					ProfitLevel=34
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[34] and lockarray35==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[34]  
					previousProfitLock=FirstProfitLockArray[33]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 35 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray35=1
					ProfitLevel=35
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[35] and lockarray36==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[35]  
					previousProfitLock=FirstProfitLockArray[34]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 36 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray36=1
					ProfitLevel=36
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[36] and lockarray37==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[36]  
					previousProfitLock=FirstProfitLockArray[35]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 37 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray37=1
					ProfitLevel=37
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[37] and lockarray38==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[37]  
					previousProfitLock=FirstProfitLockArray[36]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 38 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray38=1
					ProfitLevel=38
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[38] and lockarray39==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[38]  
					previousProfitLock=FirstProfitLockArray[37]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 39 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray39=1
					ProfitLevel=39
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[39] and lockarray40==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[39]  
					previousProfitLock=FirstProfitLockArray[38]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 40 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray40=1
					ProfitLevel=40
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[40] and lockarray41==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[40]  
					previousProfitLock=FirstProfitLockArray[39]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 41 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray41=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[41] and lockarray42==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[41]  
					previousProfitLock=FirstProfitLockArray[40]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 42 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray42=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[42] and lockarray43==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[42]  
					previousProfitLock=FirstProfitLockArray[41]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 43 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray43=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[43] and lockarray44==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[43]  
					previousProfitLock=FirstProfitLockArray[42]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 44 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray44=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[44] and lockarray45==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[44]  
					previousProfitLock=FirstProfitLockArray[43]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 45 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray45=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[45] and lockarray46==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[45]  
					previousProfitLock=FirstProfitLockArray[44]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 46 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray46=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[46] and lockarray47==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[46]  
					previousProfitLock=FirstProfitLockArray[45]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 47 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray47=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[47] and lockarray48==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[47]  
					previousProfitLock=FirstProfitLockArray[46]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 48 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray48=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[48] and lockarray49==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[48]  
					previousProfitLock=FirstProfitLockArray[47]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 49 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray49=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[49] and lockarray50==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[49]  
					previousProfitLock=FirstProfitLockArray[48]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 50 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray50=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[50] and lockarray51==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[50]  
					previousProfitLock=FirstProfitLockArray[49]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 51 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray51=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[51] and lockarray52==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[51]  
					previousProfitLock=FirstProfitLockArray[50]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 52 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray52=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[52] and lockarray53==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[52]  
					previousProfitLock=FirstProfitLockArray[51]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 53 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray53=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[53] and lockarray54==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[53]  
					previousProfitLock=FirstProfitLockArray[52]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 54 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray54=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[54] and lockarray55==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[54]  
					previousProfitLock=FirstProfitLockArray[53]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 55 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray55=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[55] and lockarray56==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[55]  
					previousProfitLock=FirstProfitLockArray[54]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 56 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray56=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[56] and lockarray57==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[56]  
					previousProfitLock=FirstProfitLockArray[55]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 57 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray57=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[57] and lockarray58==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[57]  
					previousProfitLock=FirstProfitLockArray[56]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 58 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray58=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[58] and lockarray59==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[58]  
					previousProfitLock=FirstProfitLockArray[57]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 59 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray59=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[59] and lockarray60==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[59]  
					previousProfitLock=FirstProfitLockArray[58]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 60 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray60=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[60] and lockarray61==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[60]  
					previousProfitLock=FirstProfitLockArray[59]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 61 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray61=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[61] and lockarray62==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[61]  
					previousProfitLock=FirstProfitLockArray[60]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 62 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray62=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[62] and lockarray63==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[62]  
					previousProfitLock=FirstProfitLockArray[61]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 63 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray63=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[63] and lockarray64==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[63]  
					previousProfitLock=FirstProfitLockArray[62]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 64 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray64=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[64] and lockarray65==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[64]  
					previousProfitLock=FirstProfitLockArray[63]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 65 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray65=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[65] and lockarray66==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[65]  
					previousProfitLock=FirstProfitLockArray[64]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 66 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray66=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[66] and lockarray67==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[66]  
					previousProfitLock=FirstProfitLockArray[65]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 67 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray67=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[67] and lockarray68==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[67]  
					previousProfitLock=FirstProfitLockArray[66]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 68 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray68=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[68] and lockarray69==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[68]  
					previousProfitLock=FirstProfitLockArray[67]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 69 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray69=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[69] and lockarray70==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[69]  
					previousProfitLock=FirstProfitLockArray[68]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 70 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray70=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[70] and lockarray71==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[70]  
					previousProfitLock=FirstProfitLockArray[69]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 71 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray71=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[71] and lockarray72==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[71]  
					previousProfitLock=FirstProfitLockArray[70]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 72 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray72=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[72] and lockarray73==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[72]  
					previousProfitLock=FirstProfitLockArray[71]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 73 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray73=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[73] and lockarray74==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[73]  
					previousProfitLock=FirstProfitLockArray[72]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 74 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray74=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[74] and lockarray75==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[74]  
					previousProfitLock=FirstProfitLockArray[73]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 75 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray75=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[75] and lockarray76==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[75]  
					previousProfitLock=FirstProfitLockArray[74]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 76 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray76=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[76] and lockarray77==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[76]  
					previousProfitLock=FirstProfitLockArray[75]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 77 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray77=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[77] and lockarray78==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[77]  
					previousProfitLock=FirstProfitLockArray[76]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 78 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray78=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[78] and lockarray79==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[78]  
					previousProfitLock=FirstProfitLockArray[77]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 79 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray79=1
			if ( CurrentPositionProfitPercent >= FirstProfitLockArray[79] and lockarray80==0 and CurrentPositionProfitPercent !=0 and FirstProfitLock!=0 and FirstProfitLockArray[0] !=0 ):
					FirstProfitLock=FirstProfitLockArray[79]  
					previousProfitLock=FirstProfitLockArray[78]	  
					print("====================FirstProfitLock=======================",FirstProfitLock)
					print("====================previousProfitLock====================",previousProfitLock)	
					print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 80 IF IN THE PROFIT LOCK ARRAY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','red'))
					lockarray80=1
	
			
		
		
	
	
	
		if(CurrentPositionProfit!=0 and currentPosition!='NONE'):
			if (CurrentPositionProfitPercent >=	 FirstProfitLock  and totalWalletBalance!=0	 and CurrentPositionProfitPercent!=0 and profitLockKey==0) :	
				profitLockKey=1	
				SELLNOW ='NONE'
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','blue'))
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','blue'))
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','blue'))
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','blue'))
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','blue'))
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','blue'))
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','blue'))
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','blue'))
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','blue'))
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','blue'))
				print(" >>>>>>>>>>>>>>>> We have Locked the First profit >>>>>> WAITING TO SEE IF IT WILL RISE UP >>>>>>>>>> ")	
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','blue'))
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','blue'))
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','blue'))
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','blue'))
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','blue'))
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','blue'))
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','blue'))
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','blue'))
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','blue'))
				print(colored('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','blue'))
				# playsound('FirstProfitHadBeenLocked.mp3')	
							
			if ( profitLockKey==1 and CurrentPositionProfitPercent <=  previousProfitLock and profitLockKey!=0 and CurrentPositionProfitPercent!=0 and FirstProfitLock!=0 ):
				SELLNOW ='TRUE'
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print("++++++++++++++++++++++++++++	  We Broke the Previous Profit Price . WE MUST SELL NOW . ENJOY	  ++++++++++++++++")
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))
				print(colored('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','blue'))		
	

		if (SELLNOW =='TRUE'):
			SoldOnceAlready=1
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			print("++++++++++++++++++++++++++++++++++++++++++++++++ We are placing Order NOW ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			print("currentPosition===",currentPosition,"profitLock==",profitLock,"profitLockKey==",profitLockKey,"totalWalletBalance=",totalWalletBalance)
			if (MainPostionSide=='LONG'):
				print(" +++++++++++++++++++++++++++++++++++++++++++++++++ Closing LONG NOW	 +++++++++++++++++++++++++++++++++++++++++++++++++")
				print(" +++++++++++++++++++++++++++++++++++++++++++++++++ Closing LONG NOW	 +++++++++++++++++++++++++++++++++++++++++++++++++")
				Ordertype='sell'
				Orderside='market'
				Orderamount=(MainPositionAmount)
				binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
				# binance.createMarketBuyOrder (symbol, AmountGlobal)
				MainPostionSide='NONE'
				OrderActionTakenGlobal='NONE'
				ProfitCount=(ProfitCount+CurrentPositionProfit)-FeesMarket
				CurrentPositionProfit=CurrentPositionProfit-FeesMarket
				BalanceRes = binance.fetchBalance ()
				totalWalletBalance=BalanceRes.get("info").get("totalWalletBalance")
				totalWalletBalance=float(totalWalletBalance)
				Orderprice=LastPriceTICKS
				now1M = datetime.now() 
				dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
				now1M = datetime.now() 
				dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
				FeesMarket=0
				AmountGlobal=0
				Orderamount=0
				MainPositionAmount=0
				profitLockKey=0
				SafeFirstpreviousProfitLock=0
				TheFirstpreviousProfit=0
				TheDynaimicProfitPercent=0
				SubjectManual='WHATEVER'
				SubjectGlobal='WHATEVER'
				Subject='NONE'
				previousDynaimicProfitPercent=0
				SELLNOW ='NONE'
				PositionPrice=0
				PositionPriceIndollars=0
				PrecentProfitLock=0
				CurrentPositionProfit=0
				StopLossPricePercent=0
				StopLossPriceFull=0
				ManualEntryPrice=0
				ManualSize=0
				ManualPositionDirection='NONE'
				CurrentPositionProfitPercent=0
				inPostion=0
				NextProfitPrice=0
				currentPosition='NONE'
				IncreasedNumber=0
				SLUsingATR=0
				ATRValueOpenPostionTime=0
				ProfitUsingATR=0
				AutoATRVALUEToProfitLock=0
				FirstProfitLock=0
				MI=0
				CI=0
				A=0
				FirstProfitLockArray.clear()
				OrderpriceFile= open("Orderprice.txt","w+")
				OrderpriceFile.write("NONE")
				OrderpriceFile.close() 
				OrdertypeFile= open("OrdertypeFile.txt","w+")
				OrdertypeFile.write("NONE")
				OrdertypeFile.close()
				lockarray1 =0
				lockarray2 =0
				lockarray3 =0
				lockarray4 =0
				lockarray5 =0
				lockarray6 =0
				lockarray7 =0
				lockarray8 =0
				lockarray9 =0
				lockarray10=0
				lockarray11=0
				lockarray12=0
				lockarray13=0
				lockarray14=0
				lockarray15=0
				lockarray16=0
				lockarray17=0
				lockarray18=0
				lockarray19=0
				lockarray20=0
				lockarray21=0
				lockarray22=0
				lockarray23=0
				lockarray24=0
				lockarray25=0
				lockarray26=0
				lockarray27=0
				lockarray28=0
				lockarray29=0
				lockarray30=0
				lockarray31=0
				lockarray32=0
				lockarray33=0
				lockarray34=0
				lockarray35=0
				lockarray36=0
				lockarray37=0
				lockarray38=0
				lockarray39=0
				lockarray40=0
				lockarray41=0
				lockarray42=0
				lockarray43=0
				lockarray44=0
				lockarray45=0
				lockarray46=0
				lockarray47=0
				lockarray48=0
				lockarray49=0
				lockarray50=0
				lockarray51=0
				lockarray52=0
				lockarray53=0
				lockarray54=0
				lockarray55=0
				lockarray56=0
				lockarray57=0
				lockarray58=0
				lockarray59=0
				lockarray60=0
				lockarray61=0
				lockarray62=0
				lockarray63=0
				lockarray64=0
				lockarray65=0
				lockarray66=0
				lockarray67=0
				lockarray68=0
				lockarray69=0
				lockarray70=0
				lockarray71=0
				lockarray72=0
				lockarray73=0
				lockarray74=0
				lockarray75=0
				lockarray76=0
				lockarray77=0
				lockarray78=0
				lockarray79=0
				lockarray80=0
				lockarray81=0
				lockarray82=0
				lockarray83=0
				lockarray84=0
				lockarray85=0
				lockarray86=0
				lockarray87=0
				lockarray88=0
				lockarray89=0
				lockarray90=0
				lockarray91=0
				lockarray92=0
				lockarray93=0
				lockarray94=0
				lockarray95=0
				lockarray96=0
				lockarray97=0
				lockarray98=0
				lockarray99=0
				lockarray100=0
				StartPlayingSoundN=0
				UnRlealizedAcualWalletBalance=0
				StopMultiSignals=0
				StopFirstProfitSound=0
				ProfitLevel=0
				positionAmtarr=0
				RealPostionAmountToclOSeCorretcly=0
				RealpositionInitialMargin=0
				playsound('SellingNow.mp3')
				

			elif (MainPostionSide=='SHORT'):
				print(" +++++++++++++++++++++++++++++++++++++++++++++++++ Closing SHORT NOW	 +++++++++++++++++++++++++++++++++++++++++++++++++ ")
				print(" +++++++++++++++++++++++++++++++++++++++++++++++++ Closing SHORT NOW	 +++++++++++++++++++++++++++++++++++++++++++++++++ ")
				Ordertype='buy'
				Orderside='market'
				Orderprice=LastPriceTICKS
				Orderamount=-(MainPositionAmount)
				binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
				# binance.createMarketSELLOrder (symbol, AmountGlobal)
				OrderActionTakenGlobal='NONE'
				MainPostionSide='NONE'
				ProfitCount=(ProfitCount+CurrentPositionProfit)-FeesMarket
				CurrentPositionProfit=CurrentPositionProfit-FeesMarket
				BalanceRes = binance.fetchBalance ()
				totalWalletBalance=BalanceRes.get("info").get("totalWalletBalance")
				totalWalletBalance=float(totalWalletBalance)
				now1M = datetime.now() 
				dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
				FeesMarket=0
				AmountGlobal=0
				Orderamount=0
				MainPositionAmount=0
				profitLockKey=0
				SafeFirstpreviousProfitLock=0
				TheFirstpreviousProfit=0
				TheDynaimicProfitPercent=0
				previousDynaimicProfitPercent=0
				ManualEntryPrice=0
				ManualSize=0
				ManualPositionDirection='NONE'
				PositionPriceIndollars=0
				SubjectManual='WHATEVER'
				SubjectGlobal='WHATEVER'
				Subject='NONE'
				SELLNOW ='NONE'
				PrecentProfitLock=0
				CurrentPositionProfit=0
				StopLossPricePercent=0
				StopLossPriceFull=0
				CurrentPositionProfitPercent=0
				inPostion=0
				NextProfitPrice=0
				currentPosition='NONE'
				IncreasedNumber=0
				SLUsingATR=0
				ATRValueOpenPostionTime=0
				ProfitUsingATR=0
				AutoATRVALUEToProfitLock=0
				FirstProfitLock=0
				PositionPrice=0
				MI=0
				CI=0
				A=0
				FirstProfitLockArray.clear()
				OrderpriceFile= open("Orderprice.txt","w+")
				OrderpriceFile.write("NONE")
				OrderpriceFile.close() 
				OrdertypeFile= open("OrdertypeFile.txt","w+")
				OrdertypeFile.write("NONE")
				OrdertypeFile.close()
				lockarray1 =0
				lockarray2 =0
				lockarray3 =0
				lockarray4 =0
				lockarray5 =0
				lockarray6 =0
				lockarray7 =0
				lockarray8 =0
				lockarray9 =0
				lockarray10=0
				lockarray11=0
				lockarray12=0
				lockarray13=0
				lockarray14=0
				lockarray15=0
				lockarray16=0
				lockarray17=0
				lockarray18=0
				lockarray19=0
				lockarray20=0
				lockarray21=0
				lockarray22=0
				lockarray23=0
				lockarray24=0
				lockarray25=0
				lockarray26=0
				lockarray27=0
				lockarray28=0
				lockarray29=0
				lockarray30=0
				lockarray31=0
				lockarray32=0
				lockarray33=0
				lockarray34=0
				lockarray35=0
				lockarray36=0
				lockarray37=0
				lockarray38=0
				lockarray39=0
				lockarray40=0
				lockarray41=0
				lockarray42=0
				lockarray43=0
				lockarray44=0
				lockarray45=0
				lockarray46=0
				lockarray47=0
				lockarray48=0
				lockarray49=0
				lockarray50=0
				lockarray51=0
				lockarray52=0
				lockarray53=0
				lockarray54=0
				lockarray55=0
				lockarray56=0
				lockarray57=0
				lockarray58=0
				lockarray59=0
				lockarray60=0
				lockarray61=0
				lockarray62=0
				lockarray63=0
				lockarray64=0
				lockarray65=0
				lockarray66=0
				lockarray67=0
				lockarray68=0
				lockarray69=0
				lockarray70=0
				lockarray71=0
				lockarray72=0
				lockarray73=0
				lockarray74=0
				lockarray75=0
				lockarray76=0
				lockarray77=0
				lockarray78=0
				lockarray79=0
				lockarray80=0
				lockarray81=0
				lockarray82=0
				lockarray83=0
				lockarray84=0
				lockarray85=0
				lockarray86=0
				lockarray87=0
				lockarray88=0
				lockarray89=0
				lockarray90=0
				lockarray91=0
				lockarray92=0
				lockarray93=0
				lockarray94=0
				lockarray95=0
				lockarray96=0
				lockarray97=0
				lockarray98=0
				lockarray99=0
				lockarray100=0
				StartPlayingSoundN=0
				UnRlealizedAcualWalletBalance=0
				StopMultiSignals=0
				StopFirstProfitSound=0
				ProfitLevel=0
				positionAmtarr=0
				RealPostionAmountToclOSeCorretcly=0
				RealpositionInitialMargin=0
				playsound('SellingNow.mp3')
	
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
		
		LAV=LAV[LAV ==125]
	
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
		
		
	
		if(MainPositionAmount > 0 and MainPositionEntryPrice!=0 ):
			MainPostionSide='LONG'
		if(MainPositionAmount < 0  and MainPositionEntryPrice!=0 ):
			MainPostionSide='SHORT'		
		print((colored('################  ################	THIS IS MSOBH  TRADE BOT REVENGE################  ################	','yellow')),"REVENGE=",version)
		print(colored('================================== LastPriceTICKS =================================','green'),float("%0.2f"%(LastPriceTICKS )))	
		print(colored('================================== PositionPrice ==================================','yellow'),float("%0.2f"%(PositionPrice )))
		print(colored('================================== profitLockKey ==================================','green'),profitLockKey)
		print(colored('================================== Subject ==================','cyan'),Subject,"SubjectGlobal=",SubjectGlobal)
		print(colored('==================================  ==================================','green'),SubjectGlobal)
		print(colored('================================== totalWalletBalance =============================','yellow'),float("%0.2f"%(totalWalletBalance )))
		print(colored('================================== MainPositionAmount ========================================','green'),MainPositionAmount)
		print(colored('================================== FeesMarket =====================================','red'), float("%0.2f"%(FeesMarket )))
		print(colored('================================== SELLNOW ========================================','yellow'),SELLNOW,"TradingAmountpercent=",TradingAmountpercent)
		print(colored('================================== CurrentWalletBalanceWithProfit =================','cyan'),float("%0.0f"%CurrentWalletBalanceWithProfit))
		
		print("NOT IN IF StillInPostion===",StillInPostion) 
		print("NOT IN IF UsingSellAgainToClosePostion===",UsingSellAgainToClosePostion)
		try:
			print("--PostionAmount-000-check-later-","----entryPrice----",MainPositionEntryPrice[0],'---liquidationPrice----',MainPositionLiquidationPrice[0],'----leverage----',leverage[0])
			if(MainPostionProfit > 0):
				print(colored('-unRealizedProfit =','green'),MainPostionProfit[0])	
			if(MainPostionProfit < 0):
				print(colored('-unRealizedProfit =','red'),MainPostionProfit[0])
			if(MainPositionAmount!=0):
				StillInPostion =1
				print("StillInPostion===",StillInPostion)
				print("UsingSellAgainToClosePostion===",UsingSellAgainToClosePostion)
			if(MainPositionAmount==0):
				StillInPostion =0
				SoldOnceAlready=0
				UsingSellAgainToClosePostion=0
				print("StillInPostion===",StillInPostion)
				print("UsingSellAgainToClosePostion===",UsingSellAgainToClosePostion) 
				print("SoldOnceAlready===",SoldOnceAlready)				   
		except:
			   print("Err in PrintingTheAmount")
			   StillInPostion =0
			   SoldOnceAlready=0
			   UsingSellAgainToClosePostion=0				
			   
		if CurrentPositionProfit == 0  :
			print(colored('==================== PROFIT IS ZERO , YOU ARE NOT HOLDING POSTIONS	  ','white'))
			
		if CurrentPositionProfit < 0 :
				print("																				 ")	
				print(colored('==================== YOU ARE IN LOSS Your PNL Manual	  ','red'))
				print(colored('==================== CurrentPositionProfit	','red'), float("%0.2f"%(CurrentPositionProfit )))
				print(colored('==================== CurrentPositionProfitPercent % ','red'), float("%0.2f"%(CurrentPositionProfitPercent )))
				print(colored('>>>>>>>>>>>>>>>>>>>>> NextProfitPrice is >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>','green'),float("%0.2f"%(NextProfitPrice )))	
			
		if CurrentPositionProfit > 0 :	
				print(colored('==================== YOU ARE IN WIN Your PNL Manual	 ','green'))
				print(colored('==================== CurrentPositionProfit	','green'),CurrentPositionProfit)
				print(colored('==================== CurrentPositionProfitPercent % ','green'),CurrentPositionProfitPercent)
				print(colored('>>>>>>>>>>>>>>>>>>>>> NextProfitPrice is >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>','green'),float("%0.2f"%(NextProfitPrice )))	
		if(CurrentPositionProfit!=0 and currentPosition!='NONE'):
			print("++++++++++++++++++FirstProfitLock++++++++++++++++++=",FirstProfitLock,"NextProfitPrice=	",	float("%0.0f"%(NextProfitPrice))	 ,"FirstProfitGain=",float("%0.0f"%(FirstProfitGain)))
			print("++++++++++++++++++previousProfitLock+++++++++++++++=",float("%0.0f"%(previousProfitLock )) ,"PreviousTrgt=	",float("%0.0f"%(PriceTargetPrevious)),"PreviousProfitGain=",float("%0.0f"%(PreviousProfitGain)))
			print("++++++++++++++++++FirstProfitLockArray[0]++++++++++=",float("%0.0f"%FirstProfitLockArray[0]),"PriceTarget0=	 ",float("%0.0f"%(PriceTarget0)),"SecondProfitGain=",float("%0.0f"%(SecondProfitGain)))
			print("++++++++++++++++++FirstProfitLockArray[1]++++++++++=",float("%0.0f"%FirstProfitLockArray[1]),"PriceTarget2=	 ",float("%0.0f"%(PriceTarget2)),"ThirdProfitGain=",float("%0.0f"%(ThirdProfitGain)))
			print("++++++++++++++++++FirstProfitLockArray[2]++++++++++=",float("%0.0f"%FirstProfitLockArray[2]),"PriceTarget3=	 ",float("%0.0f"%(PriceTarget3)),"FourthProfitGain=",float("%0.0f"%(FourthProfitGain)))
			print("++++++++++++++++++FirstProfitLockArray[3]++++++++++=",float("%0.0f"%FirstProfitLockArray[3]),"PriceTarget4=	 ",float("%0.0f"%(PriceTarget4)),"FivthProfitGain=",float("%0.0f"%(FivthProfitGain)))
			print(colored('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ProfitLevel >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>','green'),ProfitLevel)
				
		if(ProfitCount == 0 ):
			print(colored('=============================== Current Profit is =================================','white'),float("%0.0f"%ProfitCount))
		if(ProfitCount > 0 ):
			print(colored('=============================== Current Profit is =================================','green'),float("%0.0f"%ProfitCount))
		if(ProfitCount < 0 ):
			print(colored('=============================== Current Profit is =================================','red'),float("%0.0f"%ProfitCount))	
			
		
	
		
		
		if(SoldOnceAlready==1 and MainPositionAmount!=0 ):
			if (MainPostionSide=='LONG'):
				print(" +++++++++++++++++++++++++++++++++++++++++++++++++ Closing LONG NOW	 +++++++++++++++++++++++++++++++++++++++++++++++++")
				print(" +++++++++++++++++++++++++++++++++++++++++++++++++ Closing LONG NOW	 +++++++++++++++++++++++++++++++++++++++++++++++++")
				Ordertype='sell'
				Orderside='market'
				Orderamount=(MainPositionAmount)
				binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
				# binance.createMarketBuyOrder (symbol, AmountGlobal)
				MainPostionSide='NONE'
				OrderActionTakenGlobal='NONE'
				ProfitCount=(ProfitCount+CurrentPositionProfit)-FeesMarket
				CurrentPositionProfit=CurrentPositionProfit-FeesMarket
				BalanceRes = binance.fetchBalance ()
				totalWalletBalance=BalanceRes.get("info").get("totalWalletBalance")
				totalWalletBalance=float(totalWalletBalance)
				Orderprice=LastPriceTICKS
				now1M = datetime.now() 
				dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
				now1M = datetime.now() 
				dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
				FeesMarket=0
				AmountGlobal=0
				Orderamount=0
				MainPositionAmount=0
				profitLockKey=0
				SafeFirstpreviousProfitLock=0
				TheFirstpreviousProfit=0
				TheDynaimicProfitPercent=0
				SubjectManual='WHATEVER'
				SubjectGlobal='WHATEVER'
				Subject='NONE'
				previousDynaimicProfitPercent=0
				SELLNOW ='NONE'
				PositionPrice=0
				PositionPriceIndollars=0
				PrecentProfitLock=0
				CurrentPositionProfit=0
				StopLossPricePercent=0
				StopLossPriceFull=0
				ManualEntryPrice=0
				ManualSize=0
				ManualPositionDirection='NONE'
				CurrentPositionProfitPercent=0
				inPostion=0
				NextProfitPrice=0
				currentPosition='NONE'
				IncreasedNumber=0
				SLUsingATR=0
				ATRValueOpenPostionTime=0
				ProfitUsingATR=0
				AutoATRVALUEToProfitLock=0
				FirstProfitLock=0
				MI=0
				CI=0
				A=0
				FirstProfitLockArray.clear()
				OrderpriceFile= open("Orderprice.txt","w+")
				OrderpriceFile.write("NONE")
				OrderpriceFile.close() 
				OrdertypeFile= open("OrdertypeFile.txt","w+")
				OrdertypeFile.write("NONE")
				OrdertypeFile.close()
				lockarray1 =0
				lockarray2 =0
				lockarray3 =0
				lockarray4 =0
				lockarray5 =0
				lockarray6 =0
				lockarray7 =0
				lockarray8 =0
				lockarray9 =0
				lockarray10=0
				lockarray11=0
				lockarray12=0
				lockarray13=0
				lockarray14=0
				lockarray15=0
				lockarray16=0
				lockarray17=0
				lockarray18=0
				lockarray19=0
				lockarray20=0
				lockarray21=0
				lockarray22=0
				lockarray23=0
				lockarray24=0
				lockarray25=0
				lockarray26=0
				lockarray27=0
				lockarray28=0
				lockarray29=0
				lockarray30=0
				lockarray31=0
				lockarray32=0
				lockarray33=0
				lockarray34=0
				lockarray35=0
				lockarray36=0
				lockarray37=0
				lockarray38=0
				lockarray39=0
				lockarray40=0
				lockarray41=0
				lockarray42=0
				lockarray43=0
				lockarray44=0
				lockarray45=0
				lockarray46=0
				lockarray47=0
				lockarray48=0
				lockarray49=0
				lockarray50=0
				lockarray51=0
				lockarray52=0
				lockarray53=0
				lockarray54=0
				lockarray55=0
				lockarray56=0
				lockarray57=0
				lockarray58=0
				lockarray59=0
				lockarray60=0
				lockarray61=0
				lockarray62=0
				lockarray63=0
				lockarray64=0
				lockarray65=0
				lockarray66=0
				lockarray67=0
				lockarray68=0
				lockarray69=0
				lockarray70=0
				lockarray71=0
				lockarray72=0
				lockarray73=0
				lockarray74=0
				lockarray75=0
				lockarray76=0
				lockarray77=0
				lockarray78=0
				lockarray79=0
				lockarray80=0
				lockarray81=0
				lockarray82=0
				lockarray83=0
				lockarray84=0
				lockarray85=0
				lockarray86=0
				lockarray87=0
				lockarray88=0
				lockarray89=0
				lockarray90=0
				lockarray91=0
				lockarray92=0
				lockarray93=0
				lockarray94=0
				lockarray95=0
				lockarray96=0
				lockarray97=0
				lockarray98=0
				lockarray99=0
				lockarray100=0
				StartPlayingSoundN=0
				UnRlealizedAcualWalletBalance=0
				StopMultiSignals=0
				StopFirstProfitSound=0
				ProfitLevel=0
				positionAmtarr=0
				RealPostionAmountToclOSeCorretcly=0
				RealpositionInitialMargin=0
				playsound('SellingNow.mp3')
				

			elif (MainPostionSide=='SHORT'):
				print(" +++++++++++++++++++++++++++++++++++++++++++++++++ Closing SHORT NOW	 +++++++++++++++++++++++++++++++++++++++++++++++++ ")
				print(" +++++++++++++++++++++++++++++++++++++++++++++++++ Closing SHORT NOW	 +++++++++++++++++++++++++++++++++++++++++++++++++ ")
				Ordertype='buy'
				Orderside='market'
				Orderprice=LastPriceTICKS
				Orderamount=-(MainPositionAmount)
				binance.createOrder (symbol,Orderside,Ordertype,Orderamount)	 # working 
				# binance.createMarketSELLOrder (symbol, AmountGlobal)
				OrderActionTakenGlobal='NONE'
				MainPostionSide='NONE'
				ProfitCount=(ProfitCount+CurrentPositionProfit)-FeesMarket
				CurrentPositionProfit=CurrentPositionProfit-FeesMarket
				BalanceRes = binance.fetchBalance ()
				totalWalletBalance=BalanceRes.get("info").get("totalWalletBalance")
				totalWalletBalance=float(totalWalletBalance)
				now1M = datetime.now() 
				dt_string1M = now1M.strftime("%d/%m/%Y %H:%M:%S")
				FeesMarket=0
				AmountGlobal=0
				Orderamount=0
				MainPositionAmount=0
				profitLockKey=0
				SafeFirstpreviousProfitLock=0
				TheFirstpreviousProfit=0
				TheDynaimicProfitPercent=0
				previousDynaimicProfitPercent=0
				ManualEntryPrice=0
				ManualSize=0
				ManualPositionDirection='NONE'
				PositionPriceIndollars=0
				SubjectManual='WHATEVER'
				SubjectGlobal='WHATEVER'
				Subject='NONE'
				SELLNOW ='NONE'
				PrecentProfitLock=0
				CurrentPositionProfit=0
				StopLossPricePercent=0
				StopLossPriceFull=0
				CurrentPositionProfitPercent=0
				inPostion=0
				NextProfitPrice=0
				currentPosition='NONE'
				IncreasedNumber=0
				SLUsingATR=0
				ATRValueOpenPostionTime=0
				ProfitUsingATR=0
				AutoATRVALUEToProfitLock=0
				FirstProfitLock=0
				PositionPrice=0
				MI=0
				CI=0
				A=0
				FirstProfitLockArray.clear()
				OrderpriceFile= open("Orderprice.txt","w+")
				OrderpriceFile.write("NONE")
				OrderpriceFile.close() 
				OrdertypeFile= open("OrdertypeFile.txt","w+")
				OrdertypeFile.write("NONE")
				OrdertypeFile.close()
				lockarray1 =0
				lockarray2 =0
				lockarray3 =0
				lockarray4 =0
				lockarray5 =0
				lockarray6 =0
				lockarray7 =0
				lockarray8 =0
				lockarray9 =0
				lockarray10=0
				lockarray11=0
				lockarray12=0
				lockarray13=0
				lockarray14=0
				lockarray15=0
				lockarray16=0
				lockarray17=0
				lockarray18=0
				lockarray19=0
				lockarray20=0
				lockarray21=0
				lockarray22=0
				lockarray23=0
				lockarray24=0
				lockarray25=0
				lockarray26=0
				lockarray27=0
				lockarray28=0
				lockarray29=0
				lockarray30=0
				lockarray31=0
				lockarray32=0
				lockarray33=0
				lockarray34=0
				lockarray35=0
				lockarray36=0
				lockarray37=0
				lockarray38=0
				lockarray39=0
				lockarray40=0
				lockarray41=0
				lockarray42=0
				lockarray43=0
				lockarray44=0
				lockarray45=0
				lockarray46=0
				lockarray47=0
				lockarray48=0
				lockarray49=0
				lockarray50=0
				lockarray51=0
				lockarray52=0
				lockarray53=0
				lockarray54=0
				lockarray55=0
				lockarray56=0
				lockarray57=0
				lockarray58=0
				lockarray59=0
				lockarray60=0
				lockarray61=0
				lockarray62=0
				lockarray63=0
				lockarray64=0
				lockarray65=0
				lockarray66=0
				lockarray67=0
				lockarray68=0
				lockarray69=0
				lockarray70=0
				lockarray71=0
				lockarray72=0
				lockarray73=0
				lockarray74=0
				lockarray75=0
				lockarray76=0
				lockarray77=0
				lockarray78=0
				lockarray79=0
				lockarray80=0
				lockarray81=0
				lockarray82=0
				lockarray83=0
				lockarray84=0
				lockarray85=0
				lockarray86=0
				lockarray87=0
				lockarray88=0
				lockarray89=0
				lockarray90=0
				lockarray91=0
				lockarray92=0
				lockarray93=0
				lockarray94=0
				lockarray95=0
				lockarray96=0
				lockarray97=0
				lockarray98=0
				lockarray99=0
				lockarray100=0
				StartPlayingSoundN=0
				UnRlealizedAcualWalletBalance=0
				StopMultiSignals=0
				StopFirstProfitSound=0
				ProfitLevel=0
				positionAmtarr=0
				RealPostionAmountToclOSeCorretcly=0
				RealpositionInitialMargin=0
				playsound('SellingNow.mp3')
		
		
		
		
	
	
	except Exception as cca:
				# exc_type, exc_obj, exc_tb = sys.exc_info()
				# print(exc_type, fname, exc_tb.tb_lineno)		
				print(" Err == TICKSFunc ",cca)
				# sys.exit(1)					

				
	threading.Timer(1, TICKSFunc).start()



# gmail()
TICKSFunc()
# PrintFunc()


