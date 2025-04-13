class Animal:
	def __init__(self, arm_len: float = 0.0, leg_len: float = 0.0, eye_num: int = 2, tail: bool = True, fur: bool = False):
		self.arm_len = arm_len
		self.leg_len = leg_len
		self.eye_num = eye_num
		self.tail = tail
		self.fur = fur



	def description(self):
		return print(f"My favorite animal has {self.eye_num} eyes, a leg length of {self.leg_len} and an arm length of {self.arm_len} (it unfortunately does not have either). It is {self.tail} that it has a tail and {self.fur} that it has fur.")

default = Animal()

default.description()
