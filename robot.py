#!/usr/bin/env python3
import wpilib
import wpilib.drive
from drivetrain import Drivetrain
from elevator import Elevator
from intake import Intake
from citrusLumen import CitrusLumen
from networktables import NetworkTables

JOYSTICK_PORT = 0
JOYSTICK2_PORT = 1
ELEVATOR_SPEED = 0.75
SLOW_SPEED = .5

HATCH_BOTTOM = 30
HATCH_MIDDLE = 50
HATCH_TOP = 73
BALL_BOTTOM = 34
BALL_MIDDLE = 63#61
BALL_TOP = 73

CARGO_SHIP = 53

START_POSITION = 0
ROCKET_OR_TRANSPORT = 1
CENTER_TRANSPORT_RIGHTLEFT = 1  #-1 = LEFT. 1 = RIGHT

class Robot(wpilib.TimedRobot):
	def robotInit(self):
		print('robotinit')
		self.slowMode = True 
		self.drivetrain = Drivetrain()	
		self.elevator = Elevator()
		self.driver = wpilib.XboxController(JOYSTICK_PORT)	
		self.intake = Intake()
		self.limelight = CitrusLumen() 
		self.autonTimer = wpilib.Timer()
		self.autonCase = None
		self.autonAbort = None
		self.debugging = False


	def robotPeriodic(self):
		pass


	def autonomousInit(self):
		self.drivetrain.resetEncoders()
		self.intake.resetEncoders()
		self.intake.autonTimerPrep()
		self.autonCase = 0
		self.autonAbort = False
		self.speedMultiplier = 1.0
		self.autonTimer.reset()


	def autonomousPeriodic(self):
		if driver.getStartButtonPressed():
			self.autonAbort = True
		if self.autonAbort:
			self.driverControl()
		else:
			'''right start'''
			if START_POSITION == 1:
				if self.autonCase == 0:
					if self.drivetrain.autonStraight(3.0):
						self.drivetrain.resetEncoders()
						self.autonCase += 1
				elif self.autonCase == 1:
					self.autonTimer.start()
					if self.autonTimer.get() > 5.0:
						self.autonDrive(-0.4, 0.4, 1.0, 1.0)
						self.autonTimer.stop()
						self.autonTimer.reset()
				elif self.autonCase == 2:
					self.autonDrive(0.4, 0.4, 3.0, 3.0)
				elif self.autonCase == 3:
					if self.drivetrain.autonDrivetrain(0.4, 0.4, 3.0, 3.0):
						self.autonTimer.start()
						if self.autonTimer.get() > 5.0:
							self.drivetrain.resetEncoders()
							self.autonCase += 1
							self.autonTimer.stop()
							self.autonTimer.reset()
			'''left start'''
			if START_POSITION == -1:
				if self.autonCase == 0:
					if self.drivetrain.autonPID(2.0):
						self.drivetrain.resetEncoders()
						self.autonCase += 1
				elif self.autonCase == 1:
					if self.drivetrain.autonTurning(1.5):
						self.drivetrain.resetEncoders()
						self.autonCase += 1
				elif self.autonCase == 2:
					if self.drivetrain.autonPID(2.0):
						self.drivetrain.resetEncoders()
						self.autonCase += 1
				elif self.autonCase == 3:
					if self.drivetrain.autonTurning(1.5):
						self.drivetrain.resetEncoders()
						self.autonCase += 1
				elif self.autonCase == 4:
					if self.drivetrain.autonPID(2.0):
						self.drivetrain.resetEncoders()
						self.autonCase += 1
				elif self.autonCase == 5:
					if self.drivetrain.autonTurning(1.5):
						self.drivetrain.resetEncoders()
						self.autonCase += 1
				elif self.autonCase == 6:
					if self.drivetrain.autonPID(2.0):
						self.drivetrain.resetEncoders()
						self.autonCase += 1
				elif self.autonCase == 7:
					if self.drivetrain.autonTurning(1.5):
						self.drivetrain.resetEncoders()
						self.autonCase += 1
			'''center start'''
			if START_POSITION == 0:
				if CENTER_TRANSPORT_RIGHTLEFT == 1:
					if self.autonCase == 0:
						self.autonDrive(0.4, 0.4, 3.0, 3.0)
					elif self.autonCase == 1:
						self.autonDrive(-0.4, 0.4, 1.0, 1.0)
					elif self.autonCase == 2:
						self.autonDrive(0.4, 0.4, 3.0, 3.0)
					elif self.autonCase == 3:
						self.autonDrive(0.4, -0.4, 1.0, 1.0)
					elif self.autonCase == 4:
						self.autonDrive(0.4, 0.4, 3.0, 3.0)
					elif self.autonCase == 5:#limelight
						if self.drivetrain.autonLimeDrive(self.limelight.forwardSpeed(),
								self.limelight.horizontalHatchSpeed(),
								self.limelight.targetArea()):
							self.drivetrain.resetEncoders()
							self.autonCase += 1
					elif self.autonCase == 6:#raise elevator
						if self.elevator.autonElevator(HATCH_BOTTOM):
							self.autonCase += 1	
					elif self.autonCase == 7:#lower tilt to horizontal
						if self.intake.autonAngle(160):
							self.autonCase += 1

				'''center left'''
				if CENTER_TRANSPORT_RIGHTLEFT == -1:
					if self.autonCase == 0:
						self.autonDrive(0.4, 0.4, 3.0, 3.0)
					elif self.autonCase == 1:
						self.autonDrive(0.4, -0.4, 1.0, 1.0)
					elif self.autonCase == 2:
						self.autonDrive(0.4, 0.4, 3.0, 3.0)
					elif self.autonCase == 3:
						self.autonDrive(-0.4, 0.4, 1.0, 1.0)
					elif self.autonCase == 4:
						self.autonDrive(0.4, 0.4, 3.0, 3.0)
					elif self.autonCase == 5:#limelight
						if self.drivetrain.autonLimeDrive(self.limelight.forwardSpeed(),
								self.limelight.horizontalHatchSpeed(),
								self.limelight.targetArea()):
							self.drivetrain.resetEncoders()
							self.autonCase += 1
					elif self.autonCase == 6:#raise elevator
						if self.elevator.autonElevator(HATCH_BOTTOM):
							self.autonCase += 1	
					elif self.autonCase == 7:#lower tilt to horizontal
						if self.intake.autonAngle(160):
							self.autonCase += 1
			elif START_POSITION == 3:
				if self.autonCase == 0:
					self.autonDrive(0.4, 0.4, 3.0, 3.0)
				elif self.autonCase == 1:
					self.autonTimer.start()
					if self.autonTimer.get() > 5.0:
						self.autonDrive(0.4, 0.4, 3.0, 3.0)
						self.autonTimer.stop()
						self.autonTimer.reset()
				elif self.autonCase == 2:
					self.autonTimer.start()
					if self.autonTimer.get() > 5.0:
						self.autonDrive(-0.4, 0.4, 3.0, 3.0)
						self.autonTimer.stop()
						self.autonTimer.reset()
				elif self.autonCase == 3:
					self.autonTimer.start()
					if self.autonTimer.get() > 5.0:
						self.autonDrive(-0.4, 0.4, 1.0, 1.0)
						self.autonTimer.stop()
						self.autonTimer.reset()
				elif self.autonCase == 4:
					self.autonTimer.start()
					if self.autonTimer.get() > 5.0:
						self.autonDrive(-0.4, 0.4, 1.0, 1.0)
						self.autonTimer.stop()
						self.autonTimer.reset()
				elif self.autonCase == 5:#limelight
					if self.drivetrain.autonLimeDrive(self.limelight.forwardSpeed(),
							self.limelight.horizontalHatchSpeed(),
							self.limelight.targetArea()):
						self.drivetrain.resetEncoders()
						self.autonCase += 1
				elif self.autonCase == 6:#raise elevator
					if self.elevator.autonElevator(HATCH_BOTTOM):
						self.autonCase += 1	
				elif self.autonCase == 7:#lower tilt to horizontal
					if self.intake.autonAngle(160):
						self.autonCase += 1
		

	def teleopInit(self):
		self.drivetrain.resetEncoders()
		#set to true for print statements
		self.debugging = False
		if self.debugging:
			print('teleop init')
		

	def teleopPeriodic(self):
		self.driverControl()


	def autonDrive(self, rV: float, lV: float, rD: float, lD: float) -> bool:
		if self.drivetrain.autonDrivetrain(rV,lV,rD,lD):
			self.drivetrain.resetEncoders()
			self.autonCase += 1


	def driverControl(self):
		#Variables to hold motor values
		driveSpeed, driveAngle = 0, 0 
		elevatorSpeed = .07 #constant to maintain height
		intakeSpeed = 0
		intakeAngle = 0
		limeArea = 0
		usingLime = False

		if self.driver.getAButton():
			if self.debugging:
				print('a')
			if self.limelight.targetLocated():
				usingLime = True
				driveSpeed = self.limelight.forwardSpeed()
				driveAngle = self.limelight.horizontalHatchSpeed()
				limeArea = self.limelight.targetArea()
				if self.debugging:
					print(f'speed: {driveSpeed}, angle: {driveAngle}, area: {limeArea}')
			else:
				if self.debugging:
					print('No target found')
		elif self.driver.getBButton():
			if self.debugging:
				print('b')
			if self.limelight.targetLocated():
				usingLime = True
				driveSpeed = self.limelight.forwardSpeed()
				driveAngle = self.limelight.horizontalBallSpeed()
				limeArea = self.limelight.targetArea()
				if self.debugging:
					print(f'speed: {driveSpeed}, angle: {driveAngle}, area: {limeArea}')
			else:
				if self.debugging:
					print('No target found')
		elif self.driver.getBackButtonPressed():
			self.slowMode = not self.slowMode
			if self.slowMode:
				print('Slow Mode Enabled')
			else:
				print('Slow Mode Disabled')
			if self.debugging:
				print('back')
		elif self.driver.getStartButtonPressed():
			self.limelight.toggleLimelight(False)
			if self.debugging:
				print('start')
		elif self.driver.getStickButtonPressed(0):
			if self.debugging:
				print('left stick button')
		elif self.driver.getStickButtonPressed(1):
			if self.debugging:
				print('right stick button')

		'''intake'''
		if self.driver.getBumper(0):
			intakeSpeed = -0.5
			if self.debugging:
				print('left bumper')
		elif self.driver.getBumper(1):
			intakeSpeed = .8
			if self.debugging:
				print('right bumper')
		if self.driver.getXButton():
			intakeAngle = -0.7
			if self.debugging:
				print('x')
		elif self.driver.getYButton():
			intakeAngle = 0.7
			if self.debugging:
				print('y')

		'''elevator'''
		#left trigger
		if self.driver.getTriggerAxis(0) > .05:
			elevatorSpeed = -self.driver.getTriggerAxis(0)*0.7 #move slower while lowering elevator
			if self.debugging:
				print(f'left trigger: {self.driver.getTriggerAxis(0)}')

		#right trigger
		elif self.driver.getTriggerAxis(1) > .05:
			elevatorSpeed = self.driver.getTriggerAxis(1)
			if self.debugging:
				print(f'right trigger: {abs(self.driver.getTriggerAxis(1))}')

		'''drivetrain'''
		#left and right stick
		#up is negative, down is positive
		#-------------------------------------
		#left stick x axis
		if self.driver.getX(0) < -.05 or self.driver.getX(0) > .05:
			#driveAngle = self.driver.getX(0)
			if self.debugging:
				print(f'left x: {self.driver.getX(0)}')

		#right stick x axis
		if self.driver.getX(1) < -.05 or self.driver.getX(1) > .05:
			if self.debugging:
				print(f'right x: {self.driver.getX(1)}')

			driveAngle = self.driver.getX(1)

		#left stick y axis
		if self.driver.getY(0) < -.05 or self.driver.getY(0) > .05:
			#negative because of the inverted signal
			driveSpeed = -self.driver.getY(0)
			if self.debugging:
				print(f'left y: {-self.driver.getY(0)}')

			'''
			#this is only for the steering wheel, max values are .71 and -0.81
			if driveSpeed > 0:
				driveSpeed = self.remap(driveSpeed, 0, .71, 0, 1)
			elif driveSpeed < 0:
				driveSpeed = self.remap(driveSpeed, 0, -.81, 0, -1)
			'''

		#right stick y axis
		if self.driver.getY(1) < -.05 or self.driver.getY(1) > .05:
			#negative because of the inverted signal
			if self.debugging:
				print(f'right y: {-self.driver.getY(1)}')

		if self.slowMode and not usingLime:#lime speed is already reduced
			driveAngle = driveAngle * SLOW_SPEED
			driveSpeed = driveSpeed * SLOW_SPEED
			elevatorSpeed = elevatorSpeed * SLOW_SPEED
			if elevatorSpeed < .07 and elevatorSpeed >= 0:
				elevatorSpeed = .07
			intakeSpeed = intakeSpeed * SLOW_SPEED
			intakeAngle = intakeAngle * SLOW_SPEED

		#h = self.elevator.getHeight()
		#print(h)

		if self.debugging:
			print(f'drive speed: {driveSpeed}, drive angle {driveAngle} \
					elevator speed: {elevatorSpeed}, intake speed: {intakeSpeed} \
					intake angle {intakeAngle}')
		#apply values to motors
		self.drivetrain.arcadeDrive(driveSpeed, driveAngle)
		self.elevator.translateElevator(elevatorSpeed)
		self.intake.setSpeed(intakeSpeed)
		self.intake.setAngle(intakeAngle)


	#maps x, which has a range of a-b, to a range of c-d
	def remap(self, x, a, b, c, d):
		y = (x-a)/(b-a)*(d-c)+c
		return y


if __name__ == '__main__':
	wpilib.run(Robot)