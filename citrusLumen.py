from networktables import NetworkTables
import math


#THIS NUMBER REQUIRES CALIBRATION ONCE CIRCUIT BOARD IS RUNNING.
AREA_TO_DISTANCE_MULTIPLIER = 1 
#default speed
LIMELIGHT_SPEED = 0.55 
#13.5 is too close
LIMELIGHT_MAX_AREA = 8 
#degrees correction for ball. Hatch shouldn't need corrections.
LIMELIGHT_BALL_CORRECTION = 12  
LIMELIGHT_HATCH_CORRECTION = -4

LIMELIGHT_TURNSPEED = 0.5
LIMELIGHT_TOLERANCE = 2
LIMELIGHT_HEIGHT = 32.0
HATCH_VISION_STRIP_HEIGHT = 29.0
BALL_VISION_STRIP_HEIGHT = 38.0
LIMELIGHT_ANGLE = 0.0


class CitrusLumen:
	def __init__(self):
		self.currentOffset = 0
		self.ballCorrectionMultiplier = LIMELIGHT_BALL_CORRECTION / \
			LIMELIGHT_MAX_AREA
		self.hatchCorrectionMultiplier = LIMELIGHT_HATCH_CORRECTION / \
			LIMELIGHT_MAX_AREA
		#probably have to change the server
		self.limelight = NetworkTables.getTable("limelight")
		self.toggleLimelight(False)

	def toggleLimelight(self, toggle: bool) -> None:
		if toggle:
			self.limelight.putNumber('ledMode', 0)
			self.limelight.putNumber('camMode', 0)
		else:
			self.limelight.putNumber('ledMode', 1)
			self.limelight.putNumber('camMode', 1)

	def targetLocated(self) -> bool:
		self.toggleLimelight(True)
		return self.limelight.getNumber('tv', 0.0)

	def targetOffsetVertical(self) -> float:
		self.toggleLimelight(True)
		return self.limelight.getNumber('ty', 0.0)

	def targetOffsetHorizontal(self) -> float:
		self.toggleLimelight(True)
		return self.limelight.getNumber('tx', 0.0)

	def targetSkew(self) -> float:
		self.toggleLimelight(True)
		return self.limelight.getNumber('ts', 0.0)

	def targetArea(self) -> float:
		self.toggleLimelight(True)
		return self.limelight.getNumber('ta', 0.0)

	def getBallDistance(self) -> float:
		return (BALL_VISION_STRIP_HEIGHT - LIMELIGHT_HEIGHT) / \
			(math.tan(LIMELIGHT_ANGLE + self.targetOffsetVertical()*\
			math.pi / 180))

	def getHatchDistance(self) -> float:
		return (HATCH_VISION_STRIP_HEIGHT - LIMELIGHT_HEIGHT) / \
			(math.tan(LIMELIGHT_ANGLE + self.targetOffsetVertical()*\
			math.pi / 180))


	def forwardSpeed(self) -> float:
		if self.targetArea() > LIMELIGHT_MAX_AREA:
			return 0
		elif self.targetArea() > 10:
			return .25
		elif self.targetArea() > 7:
			return .4
		else:
			return LIMELIGHT_SPEED

	def horizontalBallSpeed(self) -> float:
		currentOffset = targetOffsetHorizontal() - getBallCorrection()
		if currentOffset > 0 and math.fabs(currentOffset) > LIMELIGHT_TOLERANCE:
			return min(LIMELIGHT_TURNSPEED, currentOffset * .12)
		elif currentOffset < 0 and math.fabs(currentOffset) > LIMELIGHT_TOLERANCE:
			return min(-LIMELIGHT_TURNSPEED, currentOffset * .12)
		else:
			return 0


	def horizontalHatchSpeed(self) -> float:
		currentOffset = targetOffsetHorizontal() - getHatchCorrection()
		if currentOffset > 0 and math.fabs(currentOffset) > LIMELIGHT_TOLERANCE:
			return min(LIMELIGHT_TURNSPEED, currentOffset * .12)
		elif currentOffset < 0 and math.fabs(currentOffset) > LIMELIGHT_TOLERANCE:
			return min(-LIMELIGHT_TURNSPEED, currentOffset * .12)
		else:
			return 0

	def getBallCorrection(self) -> float:
		return self.ballCorrectionMultiplier * self.targetArea()

	def getHatchCorrection(self) -> float:
		return self.hatchCorrectionMultiplier * self.targetArea()
