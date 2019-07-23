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
		self.ballCorrectionMultiplier = LIMELIGHT_BALL_CORRECTION / LIMELIGHT_MAX_AREA
		self.hatchCorrectionMultiplier = LIMELIGHT_HATCH_CORRECTION / LIMELIGHT_MAX_AREA


	def toggleLimelight(self) -> float:
		pass

	def targetLocated(self) -> bool:
		pass

	def targetOffsetVertical(self) -> float:
		pass

	def targetOffsetHorizontal(self) -> float:
		pass

	def targetSkew(self) -> float:
		pass

	def targetArea(self) -> float:
		pass

	def forwardSpeed(self) -> float:
		pass

	def horizontalBallSpeed(self) -> float:
		pass

	def horizontalHatchSpeed(self) -> float:
		pass

	def getBallCorrection(self) -> float:
		pass

	def getHatchCorrection(self) -> float:
		pass

	def autonBallLimelight(self) -> bool:
		pass

	def autonHatchLimelight(self) -> bool:
		pass

	def getBallDistance(self) -> float:
		pass

	def getHatchDistance(self) -> float:
		pass




