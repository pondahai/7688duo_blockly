board=""

def sendCommand():
  board.i2c_config(0x3c,0xFD) # Unlock OLED driver IC MCU interface from entering command. i.e: Accept commands
  board.i2c_write(0x3c,0x12)
  board.i2c_write(0x3c,0xAE) # Set display off
  board.i2c_write(0x3c,0xA8) # set multiplex ratio
  board.i2c_write(0x3c,0x5F) # 96
  board.i2c_write(0x3c,0xA1) # set display start line
  board.i2c_write(0x3c,0x00)
  board.i2c_write(0x3c,0xA2) # set display offset
  board.i2c_write(0x3c,0x60)
  board.i2c_write(0x3c,0xA0) # set remap
  board.i2c_write(0x3c,0x46)
  board.i2c_write(0x3c,0xAB) # set vdd internal
  board.i2c_write(0x3c,0x01) 
  board.i2c_write(0x3c,0x81) # set contrasr
  board.i2c_write(0x3c,0x53) # 100 nit
  board.i2c_write(0x3c,0xB1) # Set Phase Length
  board.i2c_write(0x3c,0X51) 
  board.i2c_write(0x3c,0xB3) # Set Display Clock Divide Ratio/Oscillator Frequency
  board.i2c_write(0x3c,0x01)
  board.i2c_write(0x3c,0xB9)
  board.i2c_write(0x3c,0xBC) # set pre_charge voltage/VCOMH
  board.i2c_write(0x3c,0x08) # (0x08);
  board.i2c_write(0x3c,0xBE) # set VCOMH
  board.i2c_write(0x3c,0X07) # (0x07);
  board.i2c_write(0x3c,0xB6) # Set second pre-charge period
  board.i2c_write(0x3c,0x01) 
  board.i2c_write(0x3c,0xD5) # enable second precharge and enternal vsl
  board.i2c_write(0x3c,0X62) # (0x62);
  board.i2c_write(0x3c,0xA4) # Set Normal Display Mode
  board.i2c_write(0x3c,0x2E) # Deactivate Scroll
  board.i2c_write(0x3c,0xAF) # Switch on display

	
def display_init():
  board.i2c_write(0x3c,0x00,0xae)
  board.i2c_write(0x3c,0x00,0xd5)
  board.i2c_write(0x3c,0x00,0x80)
  board.i2c_write(0x3c,0x00,0xa8)
  board.i2c_write(0x3c,0x00,63)
  board.i2c_write(0x3c,0x00,0xd3)
  board.i2c_write(0x3c,0x00,0x00)
  board.i2c_write(0x3c,0x00,0x40 | 0x00)
  board.i2c_write(0x3c,0x00,0x8d)
  #board.i2c_write(0x3c,0x00,0x10)
  board.i2c_write(0x3c,0x00,0x14)
  #
  board.i2c_write(0x3c,0x00,0x20)
  board.i2c_write(0x3c,0x00,0x00)
  board.i2c_write(0x3c,0x00,0xa0 | 0x01)
  board.i2c_write(0x3c,0x00,0xc8)
  #
  board.i2c_write(0x3c,0x00,0xda)
  board.i2c_write(0x3c,0x00,0x12)
  board.i2c_write(0x3c,0x00,0x81)
  #board.i2c_write(0x3c,0x00,0x9f)
  board.i2c_write(0x3c,0x00,0xcf)
  #
  board.i2c_write(0x3c,0x00,0xd9)
  board.i2c_write(0x3c,0x00,0xf1)
  board.i2c_write(0x3c,0x00,0xdb)
  board.i2c_write(0x3c,0x00,0x40)
  board.i2c_write(0x3c,0x00,0xa4)
  board.i2c_write(0x3c,0x00,0xa6)
  #
  board.i2c_write(0x3c,0x00,0x2e)
  #
  #board.i2c_write(0x3c,0x00,0xa5)
  #
  #board.i2c_write(0x3c,0x00,0xa6)
  #board.i2c_write(0x3c,0x00,0xa7)
  #
  #board.i2c_write(0x3c,0x00,0x2f)
  #
  #board.i2c_write(0x3c,0x00,0x02)
  #
  board.i2c_write(0x3c,0x00,0xaf)


#buffer=[0x55,0x55,0x55,0x55,0x55,0x55,0x55,0x55,0x55,0x55,0x55,0x55,0x55,0x55,0x55,0x55]
image=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0xE0, 0xFC, 0xFE, 0xF0, 0xC0, 0x80, 0x80,
0xC0, 0xC0, 0xE0, 0xE0, 0xE0, 0xE0, 0xE0, 0xE0, 0xE0, 0xC0, 0xC0, 0x80, 0x80, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0x80, 0x80, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x06, 0x3F, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xCF, 0x07, 0x07, 0x03, 0x03, 0x03, 0x00, 0x00,
0x00, 0x00, 0xC0, 0xE0, 0xF0, 0xF0, 0xF8, 0xF8, 0xF8, 0x78, 0x90, 0xE0, 0xE0, 0xC0, 0x80, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0xC0, 0x20, 0x30, 0x18, 0x18, 0x3C, 0x7C,
0xFC, 0xFC, 0xFC, 0xFC, 0xFC, 0xFC, 0xF8, 0xF8, 0xF0, 0xE0, 0xC0, 0x80, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0xE0, 0xF0, 0xF8, 0xFC, 0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x8F,
0x07, 0x03, 0x02, 0x06, 0x8C, 0xF8, 0xE0, 0xC0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x08, 0x18, 0x1C, 0x1C, 0x3E, 0x3E, 0x7F, 0x7F, 0xFF, 0xFF, 0xFF, 0x7F,
0x3F, 0x3F, 0x1F, 0x7F, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x1E, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x01, 0xE3, 0xF3, 0xF9, 0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
0xFE, 0xFC, 0xF8, 0xE0, 0xE0, 0xE0, 0xF0, 0xE6, 0xD7, 0xB7, 0x7C, 0xE8, 0xE8, 0xE8, 0xEC, 0xFE,
0xDF, 0xDF, 0xDF, 0xFF, 0xFF, 0xBF, 0xBF, 0xBF, 0xFF, 0x7F, 0x7F, 0x7F, 0x7E, 0x00, 0x00, 0x00,
0x80, 0x80, 0xC0, 0xC0, 0xE0, 0xF0, 0xC0, 0x00, 0x00, 0x00, 0x80, 0x80, 0xC0, 0xC0, 0x80, 0x00,
0x00, 0x00, 0x9F, 0xDF, 0xDF, 0xFF, 0xEF, 0xEF, 0xEF, 0xFF, 0xF7, 0xF7, 0xFF, 0xFF, 0xFB, 0xFB,
0xFF, 0xFD, 0xBD, 0xDD, 0xEF, 0xFE, 0xF6, 0xF6, 0xFE, 0xFA, 0xFA, 0xF8, 0xE0, 0xE0, 0xE0, 0xF0,
0xF0, 0xF0, 0xF8, 0xF8, 0xF8, 0xF8, 0xF8, 0xF8, 0xC0, 0x80, 0x00, 0xC0, 0xFE, 0xFF, 0xCF, 0x80,
0x00, 0x00, 0x00, 0x00, 0x03, 0x0F, 0x0F, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x03, 0x03, 0x07, 0x0F, 0x0F, 0x1F, 0xCF, 0xFF,
0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x7C, 0x43, 0x7F, 0x7F, 0xFF,
0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFE, 0x1D, 0xF7,
0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFE, 0xF9, 0xE7, 0x3F, 0xFF, 0x7F, 0x3F, 0x0F, 0x00,
0x00, 0x0F, 0xFF, 0xFF, 0xFF, 0xFF, 0x7F, 0x7F, 0x7F, 0x3F, 0x3F, 0x3F, 0xBF, 0x9F, 0x9F, 0x9F,
0xDF, 0xC0, 0xDF, 0xFF, 0x7F, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x3F, 0xBF, 0x3F,
0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0xC0, 0xFF, 0xFF, 0x3F, 0x07, 0x0F, 0x01,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x01, 0x3D, 0x7F, 0xFF, 0xFB, 0xFB, 0xFB, 0xFF, 0xFD, 0xFD, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE,
0xFC, 0xFC, 0xFC, 0xFC, 0xFD, 0xF9, 0xF9, 0xF9, 0xF9, 0xFB, 0xF3, 0xF3, 0x73, 0x03, 0x06, 0x07,
0x03, 0x07, 0x07, 0x03, 0x03, 0x03, 0x01, 0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x04, 0x7C, 0xFE, 0xFE, 0xFE, 0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
0x7F, 0x7F, 0x7F, 0x7F, 0x3F, 0xBE, 0xBE, 0xDF, 0xDF, 0xDD, 0xFD, 0x6D, 0xAD, 0xCE, 0xE3, 0xF0,
0xE0, 0xC0, 0xC0, 0x80, 0x80, 0x00, 0x00, 0x00, 0x00, 0x1F, 0x1F, 0x03, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x60, 0xE0, 0xE0, 0xE0, 0xC0, 0xB0, 0x78, 0xF8, 0xFC, 0xFE,
0xFF, 0xFF, 0xFE, 0xFD, 0xFA, 0xF6, 0xEE, 0x5F, 0x3D, 0x1D, 0x0D, 0x05, 0x03, 0x03, 0x03, 0x83,
0xFB, 0xFF, 0xF7, 0xF7, 0xF7, 0x7F, 0x7F, 0x6F, 0x0F, 0x0F, 0x07, 0x03, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x81, 0xE1, 0x79, 0x7D, 0x7D, 0x7D, 0x7E, 0xFE, 0xFE, 0xFE,
0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x01, 0x03, 0x03, 0x0D, 0x1E, 0x3F, 0x7F, 0xFF, 0xFF, 0xFF,
0x7F, 0xBF, 0xDF, 0xEF, 0xF7, 0xF9, 0x3E, 0x1E, 0x0E, 0x07, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x03, 0x07, 0x0F, 0x1F, 0x3E, 0x7D, 0xFB,
0xE7, 0x4F, 0x1F, 0x0F, 0x03, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFC,
0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFF, 0xFF, 0xFF, 0xFC, 0xE0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x0F, 0x0F, 0x0E, 0x0E,
0x0E, 0x0E, 0x0E, 0x1C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x04,
0x07, 0x0F, 0x07, 0x03, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x70, 0x7F,
0x3B, 0x3B, 0x3B, 0x3F, 0x3D, 0x1D, 0x1D, 0x1D, 0x1E, 0x0E, 0x0E, 0x0C, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
]

buffer=image

change=[]
  

def display_buffer():
  board.i2c_write(0x3c,0x00,0x21)
  board.i2c_write(0x3c,0x00,00)
  board.i2c_write(0x3c,0x00,127)
  board.i2c_write(0x3c,0x00,0x22)
  board.i2c_write(0x3c,0x00,00)
  board.i2c_write(0x3c,0x00,63)
  message=[]
  bytecount=0
  for i in buffer:
    bytecount+=1
    message+=[i]
    if bytecount==16:
      board.i2c_write(0x3c,0x40,*message)
      message=[]
      bytecount=0
  
  
def display_change():
  global change
  for i in change:
    xx=i[0]%128      
    yy=(i[1]/8)
    board.i2c_write(0x3c,0x00,0x21,xx,xx,0x22,yy,yy)
#    board.i2c_write(0x3c,0x00,xx)
#    board.i2c_write(0x3c,0x00,xx)
#    board.i2c_write(0x3c,0x00,0x22,yy,yy)
#    board.i2c_write(0x3c,0x00,yy)
#    board.i2c_write(0x3c,0x00,yy)
#    mask=0x01<<(i[1]%8)
    board.i2c_write(0x3c,0x40,i[2])
#    message=[]
#    bytecount=0
#    for i in buffer:
#      bytecount+=1
#      message+=[i]
#      if bytecount==16:
#        board.i2c_write(0x3c,0x40,*message)
#        message=[]
#        bytecount=0
  change=[]
  

def display_clear():
  for i in range(128*8):
    buffer[i]=0
  display_buffer()




def plotXY(x,y,color):
  global change      
  xx=x%128      
  yy=(y/8)
  index=yy*128+xx
  mask=0x01<<(y%8)
  if color:
    buffer[index]=buffer[index]|mask
  else:
    buffer[index]=buffer[index]&(~mask&0xff)
  change+=[[x,y,buffer[index]]]
  #display_change()


def plotDot(x,y,color):
  xx=x*4
  yy=y*4
  plotXY(xx,yy,color)
  plotXY(xx,yy+1,color)
  plotXY(xx,yy+2,color)
  xx=xx+1
  plotXY(xx,yy,color)
  plotXY(xx,yy+1,color)
  plotXY(xx,yy+2,color)
  xx=xx+1
  plotXY(xx,yy,color)
  plotXY(xx,yy+1,color)
  plotXY(xx,yy+2,color)
  display_change()



