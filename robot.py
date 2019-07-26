#!/usr/bin/python3
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
			elif START_POSITION == -1:
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
			elif START_POSITION == 0:
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
				elif CENTER_TRANSPORT_RIGHTLEFT == -1:
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

		if self.driver.getAButtonPressed():
			print('a')	
		elif self.driver.getBButtonPressed():
			print('b')
		elif self.driver.getBackButtonPressed():
			self.slowMode = not self.slowMode
			if self.slowMode:
				print('Slow Mode Enabled')
			else:
				print('Slow Mode Disabled')
			#print('back')
		elif self.driver.getStartButtonPressed():
			print('start')
		elif self.driver.getStickButtonPressed(0):
			print('left stick button')
		elif self.driver.getStickButtonPressed(1):
			print('right stick button')

		'''intake'''
		if self.driver.getBumper(0):
			intakeSpeed = -0.5
			#print('left bumper')
		elif self.driver.getBumper(1):
			intakeSpeed = .8
			#print('right bumper')
		if self.driver.getXButton():
			intakeAngle = -0.7
			#print('x')
		elif self.driver.getYButton():
			intakeAngle = 0.7
			#print('y')

		'''elevator'''
		#left trigger
		if self.driver.getTriggerAxis(0) > .05:
			elevatorSpeed = -self.driver.getTriggerAxis(0)*0.7 #move slower while lowering elevator
			#print(f'left trigger: {self.driver.getTriggerAxis(0)}')

		#right trigger
		elif self.driver.getTriggerAxis(1) > .05:
			elevatorSpeed = self.driver.getTriggerAxis(1)
			#print(f'right trigger: {abs(self.driver.getTriggerAxis(1))}')

		'''drivetrain'''
		#left and right stick
		#up is negative, down is positive
		#-------------------------------------
		#left stick x axis
		if self.driver.getX(0) < -.05 or self.driver.getX(0) > .05:
			#print(f'left x: {self.driver.getX(0)}')
			pass

		#right stick x axis
		if self.driver.getX(1) < -.05 or self.driver.getX(1) > .05:
			driveAngle = self.driver.getX(1)
			#print(f'right x: {self.driver.getX(1)}')

		#left stick y axis
		if self.driver.getY(0) < -.05 or self.driver.getY(0) > .05:
			#negative because of the inverted signal
			driveSpeed = -self.driver.getY(0)
			#print(f'left y: {-self.driver.getY(0)}')

		#right stick y axis is mapped to right trigger for some reason
		#right stick y axis
		if self.driver.getY(1) < -.05 or self.driver.getY(1) > .05:
			#negative because of the inverted signal
			#print(f'right y: {-self.driver.getY(1)}')
			pass

		if self.slowMode:
			driveAngle = driveAngle * SLOW_SPEED
			driveSpeed = driveSpeed * SLOW_SPEED
			elevatorSpeed = elevatorSpeed * SLOW_SPEED
			if elevatorSpeed < .07 and elevatorSpeed >= 0:
				elevatorSpeed = .07
			intakeSpeed = intakeSpeed * SLOW_SPEED
			intakeAngle = intakeAngle * SLOW_SPEED

		#h = self.elevator.getHeight()
		#print(h)

		#apply values to motors
		self.drivetrain.arcadeDrive(driveSpeed, driveAngle)
		self.elevator.translateElevator(elevatorSpeed)
		self.intake.setSpeed(intakeSpeed)
		self.intake.setAngle(intakeAngle)



if __name__ == '__main__':
	wpilib.run(Robot)