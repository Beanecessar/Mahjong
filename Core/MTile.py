class MTile(object):
	"""
	Tile: 麻将牌
	TileType: 牌的种类
	TileNum: 牌的点数
	"""
	# TileType
	Null = 			0x00000000
	Dots = 			0x00000001 #筒牌
	Bamboo = 		0x00000010 #条牌
	Characters = 	0x00000100 #万牌
	Winds = 		0x00001000 #风牌
	Dragons = 		0x00010000 #箭牌
	Flowers = 		0x00100000 #花牌
	Seasons = 		0x01000000 #季牌
	Jokers = 		0x10000000 #百搭
	AllType = 		0x11111111
	# TileNum
	Null = 			0x000000000
	One = 			0x000000001
	Two = 			0x000000010
	Three = 		0x000000100
	Four = 			0x000001000
	Five = 			0x000010000
	Six = 			0x000100000
	Seven = 		0x001000000
	Eight = 		0x010000000
	Nine = 			0x100000000
	AllNum = 		0x111111111
	# 简记
	# 1-9筒		1-9p
	# 1-9条		1-9s
	# 1-9万		1-9m
	# 东南西北	1-4z
	# 中发白	5-7z
	# 百搭		a

	def __init__(self, *args):
		if len(args == 0):
		# 无参数
			self.tileType = self.Null
			self.tileNum = self.Null
		elif len(args == 1):
		# 一参数
			if isinstance(args[0], str):
				self.SetupFromBrief(args[0])
			else:
				raise NotImplementedError
		elif len(args == 2):
		# 两参数
			self.tileType, self.tileNum = args

	# SetupFromBrief
	__NormalBrief = {
		"1p": (Dots, One), "2p": (Dots, Two), "3p": (Dots, Three), "4p": (Dots, Four), "5p": (Dots, Five), "6p": (Dots, Six), "7p": (Dots, Seven), "8p": (Dots, Eight), "9p": (Dots, Nine), 
		"1s": (Bamboo, One), "2s": (Bamboo, Two), "3s": (Bamboo, Three), "4s": (Bamboo, Four), "5s": (Bamboo, Five), "6s": (Bamboo, Six), "7s": (Bamboo, Seven), "8s": (Bamboo, Eight), "9s": (Bamboo, Nine), 
		"1m": (Characters, One), "2m": (Characters, Two), "3m": (Characters, Three), "4m": (Characters, Four), "5m": (Characters, Five), "6m": (Characters, Six), "7m": (Characters, Seven), "8m": (Characters, Eight), "9m": (Characters, Nine), 
		"1z": (Winds, One), "2z": (Winds, Two), "3z": (Winds, Three), "4z": (Winds, Four), "5z": (Dragons, One), "6z": (Dragons, One), "7z": (Dragons, One),
		"a": (AllType, AllNum),
	}
	def SetupFromBrief(self, brief):
		# 解析简记
		assert(brief in self.__NormalBrief)
		self.tileType, self.tileNum = self.__NormalBrief[brief]
