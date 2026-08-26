	 ROS2 Day 25 - Simulated Pick and Place Controller

## Objective

Start the Week 4 simulated pick-and-place project using ROS2.

## Work Completed

- Created a new ROS2 Python controller for the pick-and-place project.
- Created `pick_place_controller.py`.
- Implemented a subscriber for the `/object_detection` topic.
- Added a simple state-based control system.
- Set the initial robot state as `SEARCHING`.
- Added a callback to process object detection messages.
- When `OBJECT DETECTED` is received, the controller changes the state from `SEARCHING` to `MOVING_TO_OBJECT`.
- Tested the controller using a ROS2 topic message.
- Verified that the controller successfully received the detection message and changed its state.

## Current Project Flow

Object Detection
→ `/object_detection`
→ Pick and Place Controller
→ Detection Callback
→ SEARCHING
→ MOVING_TO_OBJECT

## Test Message

`OBJECT DETECTED`

## Verified Output

`Detection received: OBJECT DETECTED`

`State changed: SEARCHING -> MOVING_TO_OBJECT`

## Learning Outcome

Learned how a simple state-based controller can be used to control the sequence of actions in a robotics application.

The project currently handles the first transition from searching for an object to moving toward the detected object.

## Next Step

Continue the state sequence with:

MOVING_TO_OBJECT
→ PICKING
→ MOVING_TO_TARGET
→ PLACING
→ DONE
