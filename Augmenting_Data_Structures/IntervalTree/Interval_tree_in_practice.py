# a simple scheduler
# use the following command:
# pip install intervaltree
 
import argparse
from intervaltree import Interval, IntervalTree

class Task:
    """Represents a scheduled task."""
    def __init__(self, task_id, start_time, end_time, data=None):
        self.id = task_id
        self.start = start_time
        self.end = end_time
        self.data = data # Optional

    def __repr__(self):
        return f"Task(id={self.id}, start={self.start}, end={self.end})"

class IntervalScheduler:
    def __init__(self):
        self.interval_tree = IntervalTree()
        self.task_map = {} # To quickly access Task objects by their IDs.

    def schedule(self, task_id, start_time, end_time, data=None):
        """Schedules a new task. Returns True if scheduled, False if conflicts exist"""
        if self.is_conflicting(start_time, end_time):
            return False  # Or handle conflict resolution

        new_task = Task(task_id, start_time, end_time, data)
        self.interval_tree.add(Interval(start_time, end_time, new_task))
        self.task_map[task_id] = new_task
        return True


    def is_conflicting(self, start_time, end_time):
        """Check if adding a new task at this interval would cause overlap"""
        conflicts = self.interval_tree.overlap(start_time, end_time)
        return len(conflicts) > 0


    def query(self, point_or_interval):
        """
        Finds tasks active at a given point in time or overlapping
        with a given interval.
        :param point_or_interval: A single timestamp (int/float) or a tuple (start, end)
        :return: A list of Task objects
        """
        if isinstance(point_or_interval, (int, float)):
            intervals = self.interval_tree.at(point_or_interval)
        elif isinstance(point_or_interval, tuple):
            start, end = point_or_interval
            intervals = self.interval_tree.overlap(start, end)
        else:
            raise ValueError("query must be called with a time or an interval")


        return [interval.data for interval in intervals]


    def remove(self, task_id):
      """Removes a scheduled task by its ID."""
      if task_id not in self.task_map:
        return False
      task = self.task_map[task_id]
      self.interval_tree.remove(Interval(task.start, task.end, task))
      del self.task_map[task_id]
      return True

    def update(self, task_id, new_start_time, new_end_time):
        """Updates the time interval of a scheduled task."""
        if task_id not in self.task_map:
            return False
        
        task_to_update = self.task_map[task_id]
        # check if the new interval creates conflicts. 
        original_start, original_end = task_to_update.start, task_to_update.end
        self.remove(task_id)

        if not self.schedule(task_id, new_start_time, new_end_time, task_to_update.data):
            # reschedule the original task since there was a conflict.
             self.schedule(task_id, original_start, original_end, task_to_update.data)
             return False # Can't be updated due to conflicts
        return True


    def get_all_tasks(self):
        """Gets all tasks in the scheduler."""
        return list(self.task_map.values())


def main():
    scheduler = IntervalScheduler()

    parser = argparse.ArgumentParser(description="Interval Scheduler CLI")
    subparsers = parser.add_subparsers(title="Commands", dest="command", help="Available commands")

    # Schedule command
    schedule_parser = subparsers.add_parser("schedule", help="Schedule a task")
    schedule_parser.add_argument("task_id", type=int, help="Task ID")
    schedule_parser.add_argument("start_time", type=int, help="Start time")
    schedule_parser.add_argument("end_time", type=int, help="End time")
    schedule_parser.add_argument("--data", type=str, help="Optional task data", default=None)

    # Query command
    query_parser = subparsers.add_parser("query", help="Query for active tasks")
    query_parser.add_argument("query_type", choices=["point", "interval"], help="Query type: at a point in time, or an interval")
    query_parser.add_argument("param1", type=int, help="Start of the time or time at which we need to query")
    query_parser.add_argument("param2", type=int, nargs='?', default=None, help="End of time interval, only required for the interval query type")

    # Remove command
    remove_parser = subparsers.add_parser("remove", help="Remove a scheduled task")
    remove_parser.add_argument("task_id", type=int, help="Task ID to remove")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update the time of a task")
    update_parser.add_argument("task_id", type=int, help="Task ID to update")
    update_parser.add_argument("new_start", type=int, help="New start time")
    update_parser.add_argument("new_end", type=int, help="New end time")

    # Get all command
    get_all_parser = subparsers.add_parser("get_all", help="Get all tasks")

    # Help command
    help_parser = subparsers.add_parser("help", help="Display help for a specific command")
    help_parser.add_argument("help_command", nargs="?", help="Command to get help for")

    args = parser.parse_args()


    if args.command == "help":
      if args.help_command:
        print(get_command_help(args.help_command, parser))
      else:
        parser.print_help() # Overall help if no command is specified

    elif args.command == "schedule":
        if scheduler.schedule(args.task_id, args.start_time, args.end_time, args.data):
            print(f"Scheduled task {args.task_id} from {args.start_time} to {args.end_time}")
        else:
            print(f"Could not schedule task {args.task_id}, conflict found")
    elif args.command == "query":
        if args.query_type == "point":
            result = scheduler.query(args.param1)
        elif args.query_type == "interval":
             result = scheduler.query((args.param1, args.param2))
        print("Query result:")
        if result:
            for task_data in result:
              print(f"  - {task_data}")
        else:
            print("  No tasks found.")
    elif args.command == "remove":
        if scheduler.remove(args.task_id):
           print(f"Removed task {args.task_id}")
        else:
            print(f"Task {args.task_id} not found")
    elif args.command == "update":
        if scheduler.update(args.task_id, args.new_start, args.new_end):
          print(f"Updated task {args.task_id} to run from {args.new_start} to {args.new_end}")
        else:
            print(f"Could not update task {args.task_id}, possible conflict found")
    elif args.command == "get_all":
        tasks = scheduler.get_all_tasks()
        if tasks:
            print("All tasks:")
            for task in tasks:
                print(f" - {task}")
        else:
            print("No task scheduled yet")

    elif args.command is None:
        parser.print_help()


def get_command_help(command, parser):
  """Generates help for a specific command"""
  for action in parser._actions:
        if isinstance(action, argparse._SubParsersAction):
          for choice, subparser in action.choices.items():
            if choice == command:
              return subparser.format_help()
  return "Command not found, try `python script.py --help`"


if __name__ == "__main__":
    main()