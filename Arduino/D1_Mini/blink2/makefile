BOARD?=esp8266:esp8266:d1_mini
PORT?=com3

all:
	arduino-cli compile -b $(BOARD)
	arduino-cli upload -b $(BOARD) -p $(PORT)
