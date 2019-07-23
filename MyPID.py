class ProtoPID:
	def __init__(self, p: float, i: float, d: 
			float, filtTime: float, dt: float):
		#do all these really need to be member variables?
		self.p = p
		self.i = i
		self.d = d
		self.filtTime = filtTime
		self.dt = dt

		self.intErr = 0
		self.prevIntErr = 0
		self.prevFiltMeas = 0
		self.currFiltMeas = 0
		self.pControl = 0
		self.iControl = 0
		self.dControl = 0
		self.error = 0
		self.command = 0

	def compute(self, currMeas: float, setPoint: float) -> float:
		self.error = setPoint - currMeas
		self.intErr = prevIntErr + self.error*self.dt
		alpha = self.dt/(self.filtTime + self.dt)
		self.currFiltMeas = (1-alpha) * self.prevFiltMeas + alpha * currMeas
		self.pControl = self.p * self.error
		self.iControl = self.i * self.intErr
		self.dControl = (-self.d * currFiltMeas) / self.dt
		self.command = self.pControl + self.iControl + self.dControl		
		if self.command > 1:
			self.command = 1
		elif self.command < -1:
			self.command = -1
		self.intErr = self.intErr - self.error * self.dt
		return self.command

	def getCommand(self) -> float:
		return self.command

	def getFiltMeas(self) -> float:
		return self.currFiltMeas

	def getError(self) -> float:
		return self.error			

	def reset(self) -> None:
		self.intErr = 0
		self.prevIntErr = 0
		self.prevFiltMeas = 0
		self.currFiltMeas = 0
		self.error = 0

	def setGains(self) -> float:
		pass
