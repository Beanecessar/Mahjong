from Core.MTile import MTile, AllNormalTiles
from Core.MHand import MHand

class MRuleSet(object):
	"""
	RuleSet: 规则集
	"""
	def __init__(self):
		self.allowChow = True		#吃
		self.allowPong = True		#碰
		self.allowKong = True		#杠

class MRuler(object):
	"""
	Ruler: 规则器
	"""
	def __init__(self, ruleSet):
		self.ruleSet = ruleSet

	def CheckHand(self, hand):
		hand.Sort()
		# TODO: 添加有百搭牌的情况
		# 特殊牌型1: 国士无双
		# 特殊牌型2: 七对子

		allResults = []
		# 搜索将牌
		for i in range(len(hand.Tiles)):
			tiles = hand.Tiles.copy()
			oneEye = tiles.pop(i)
			# index只判断==
			try:
				i = tiles.index(oneEye)
			except ValueError:
				continue
			eyes = [oneEye, tiles.pop(i)]
			results = self.__CheckMelds(tiles, eyes, [], [])
			allResults += results
		return allResults

	def __CheckMelds(self, tiles, eyes, chows, pongs):
		results = []
		self.__CheckChow(tiles, eyes, chows, pongs, results)
		self.__CheckPongs(tiles, eyes, chows, pongs, results)
		return results

	def __CheckChow(self, tiles, eyes, chows, pongs, results):
		first = tiles[0]
		if first.tileType not in [MTile.Dots, MTile.Bamboo, MTile.Characters]:
			return
		if first.tileNum > MTile.Seven:
			return
		try:
			i = tiles.index(first+1)
			j = tiles.index(first+2)
		except ValueError:
			return

		tiles = tiles.copy()
		chows = chows.copy()
		chow = [tiles.pop(0)]
		i = tiles.index(first+1)
		chow.append(tiles.pop(i))
		i = tiles.index(first+2)
		chow.append(tiles.pop(i))
		chows.append(chow)

		if len(tiles) == 0:
			results.append([eyes, chows, pongs])
			return
		self.__CheckChow(tiles, eyes, chows, pongs, results)
		self.__CheckPongs(tiles, eyes, chows, pongs, results)
		return

	def __CheckPongs(self, tiles, eyes, chows, pongs, results):
		first = tiles[0]
		if first.tileType not in [MTile.Dots, MTile.Bamboo, MTile.Characters]:
			return
		if tiles.count(first) < 3:
			return

		tiles = tiles.copy()
		pongs = pongs.copy()
		pong = [tiles.pop(0)]
		i = tiles.index(first)
		pong.append(tiles.pop(i))
		i = tiles.index(first)
		pong.append(tiles.pop(i))
		pongs.append(pong)

		if len(tiles) == 0:
			results.append([eyes, chows, pongs])
			return
		self.__CheckChow(tiles, eyes, chows, pongs, results)
		self.__CheckPongs(tiles, eyes, chows, pongs, results)
		return

	def FindSolve(self, hand):
		solveSpace = []
		for tile in AllNormalTiles:
			newHand = MHand(hand)
			newHand.Draw(tile)
			results = self.CheckHand(newHand)
			if len(results) > 0:
				solveSpace.append(str(tile))
		return solveSpace