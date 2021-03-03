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
