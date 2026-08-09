				 ROS2 Day 9 - ROS2 Actions

## Topics Learned

- Introduction to ROS2 Actions
- Goal, Feedback, and Result
- ROS2 Action CLI commands
- Tested an Action using turtlesim

## What is a ROS2 Action?

A ROS2 Action is used for tasks that may take some time to complete.

An Action mainly works using:

Goal -> Feedback -> Result

Goal:
The task requested by the client.

Feedback:
Progress information sent while the task is running.

Result:
The final result after completing the task.

Actions can also support cancellation of a running goal.

## Topic vs Service vs Action

Topic:
Used for continuous data communication using Publisher and Subscriber.

Service:
Used for Request and Response communication.

Action:
Used for longer-running tasks where feedback and a final result are useful.

## Commands Practiced

List available actions:

ros2 action list

Inspect an action:

ros2 action info /turtle1/rotate_absolute

Send an action goal:

ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 1.57}" --feedback

## Practical Test

Used the turtlesim node to test ROS2 Actions.

Action:
/turtle1/rotate_absolute

The turtle received a rotation goal.

During execution, feedback about the remaining rotation was displayed.

After completing the rotation, the action returned a result.

Final Status:
SUCCEEDED


