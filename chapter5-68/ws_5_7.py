# 6806021610182 ณัฐวัตร จิตอารี
import datetime

now = datetime.datetime.now()
print("Default : ",now)
print("C Time Style : ",now.ctime)
print("ISO Time : ",now.isoformat(),"\n")
print("ปี : ",now.strftime("%y %Y"))
print("เดือน : ",now.strftime("%m %b %B"))
print("วันที่ : ",now.strftime("%d %a %A"))
print("ชั่วโมง : ",now.strftime("%H %I %p"))
print("นาที : ",now.strftime("%M"))
print("วินาที : ",now.strftime("%S"))
print("ไมโครวินาที : ",now.strftime("%f"),"\n")
print("วันที่ : ",now.strftime("%d/%m/%y"))
print("วันที่แบบย่อ : ",now.strftime("%d %b %y"))
print("วันที่แบบเต็ม : ",now.strftime("%d %B %Y"), "\n")
print("เวลา : ",now.strftime("%H:%M:%S"))
print("เวลา : ",now.strftime("%I:%M:%S %p"))
