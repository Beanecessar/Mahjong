from MTile import MTile
import copy

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

		# 搜索将牌
		for i in range(hand):
			tiles = copy.deepcopy(hand.Tiles)
			oneEye = tiles.pop(i)
			# index只判断==
			try:
				i = tiles.index(oneEye)
			except ValueError:
				continue
			eyes = [oneEye, tiles.pop(i)]
			results = self.__CheckMelds(tiles, eyes, [], [])

	def __CheckMelds(self, tiles, eyes, chows, pongs):
		results = []
		self.__CheckChow(tiles, eyes, chows, pongs, results)
		self.__CheckPongs(tiles, eyes, chows, pongs, results)
		return results

	def __CheckChow(self, tiles, eyes, chows, pongs, results):
		first = tiles[0]
		if first.tileType not in [MTile.Dots, MTile.Bamboo, MTile.Characters]:
			return False
		if first.tileNum > MTile.Seven:
			return False
		try:
			i = tiles.index(first+1)
			j = tiles.index(first+2)
		except ValueError:
			return False
		chows = copy.deepcopy(chows)
		chow = [first, tiles[i], tiles[j]]
		chows.append(chow)
		tiles = copy.deepcopy(tiles)
		chowids = [id(t) for t in chow]
		for i in range(len(tiles), -1, -1):
			if id(tiles[i]) in chowids:
				tiles.pop(i)
		if (len(tiles)>0):
			self.__CheckChow(tiles, eyes, chows, pongs, results)
			self.__CheckPongs(tiles, eyes, chows, pongs, results)
		else:
			results += [eyes, chows, pongs]
			return True

	def __CheckPongs(self, tiles, eyes, chows, pongs, results):
		pass

