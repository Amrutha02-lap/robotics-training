				    Day 25 Report

## Task

Started the Week 4 Simulated Pick-and-Place Project.

## Work Completed

Today I started developing the ROS2 controller for the simulated pick-and-place project.

I created a `pick_place_controller.py` node and subscribed it to the `/object_detection` topic.

A simple state-based control mechanism was implemented with `SEARCHING` as the initial state.

When the controller receives an `OBJECT DETECTED` message, it changes its state from `SEARCHING` to `MOVING_TO_OBJECT`.

The ROS2 communication and first state transition were tested successfully using a test message published to the `/object_detection` topic.

## Result

OBJECT DETECTED
→ `/object_detection`
→ Pick-and-Place Controller
→ SEARCHING
→ MOVING_TO_OBJECT

The first stage of the simulated pick-and-place controller was implemented and tested successfully.

## Next Step

Continue implementing the remaining states:

PICKING
→ MOVING_TO_TARGET
→ PLACING
→ DONE
