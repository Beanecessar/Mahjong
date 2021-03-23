from Core.MTile import MTile

class MHand(object):
	"""
	Hand: 手牌
	"""
	def __init__(self, *args):
		if len(args) == 0:
			self.tiles = []
		elif len(args) == 1 and isinstance(args[0], list):
			self.tiles = args[0]
		elif len(args) == 1 and isinstance(args[0], MHand):
			self.tiles = args[0].Tiles.copy()

	def __str__(self):
		return " ".join([str(t) for t in self.tiles])

	@property
	def Tiles(self):
		return self.tiles

	def SetupFromBrief(self, brief):
		briefs = brief.split(" ")
		for bf in briefs:
			tile = MTile(bf)
			self.tiles.append(tile)

	def Sort(self):
		dots, bamboo, characters, winds, dragons, jokers = [], [], [], [], [], []
		sortMap = {
			MTile.Dots: lambda tile: dots.append(tile),
			MTile.Bamboo: lambda tile: bamboo.append(tile),
			MTile.Characters: lambda tile: characters.append(tile),
			MTile.Winds: lambda tile: winds.append(tile),
			MTile.Dragons: lambda tile: dragons.append(tile),
			MTile.Jokers: lambda tile: jokers.append(tile),
		}
		for tile in self.tiles:
			if tile.tileType in sortMap:
				sortMap[tile.tileType](tile)
		for tg in [dots, bamboo, characters, winds, dragons, jokers]:
			tg.sort(key=lambda k: k.tileNum)
		tiles = dots + bamboo + characters + winds + dragons + jokers
		assert(len(tiles)==len(self.tiles))
		self.tiles = tiles

	def Draw(self, tile):
		self.tiles.append(tile)