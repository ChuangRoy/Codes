BOARD?=esp8266:esp8266:nodemcuv2
PORT?=com4

all:
	arduino-cli compile -b $(BOARD)
	arduino-cli upload -b $(BOARD) -p $(PORT)
