# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

from util import Stack

def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""
    start_state = problem.getStartState()
    if problem.isGoalState(start_state):
        return []

    fringe = Stack()
    fringe.push((start_state, []))  # (current_state, path_taken)
    explored_set = set()

    while not fringe.isEmpty():
        state, actions = fringe.pop()

        if state in explored_set:
            continue

        explored_set.add(state)

        if problem.isGoalState(state):
            return actions

        for successor, action, step_cost in problem.getSuccessors(state):
            if successor not in explored_set:
                new_actions = actions + [action]
                fringe.push((successor, new_actions))

    return []

from util import Queue


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    start_state = problem.getStartState()
    if problem.isGoalState(start_state):
        return []

    fringe = Queue()
    fringe.push((start_state, []))
    explored_set = set()

    while not fringe.isEmpty():
        state, actions = fringe.pop()

        if state in explored_set:
            continue

        explored_set.add(state)

        if problem.isGoalState(state):
            return actions

        for successor, action, step_cost in problem.getSuccessors(state):
            if successor not in explored_set:
                new_actions = actions + [action]
                fringe.push((successor, new_actions))

    return []


from util import PriorityQueue

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    start_state = problem.getStartState()
    if problem.isGoalState(start_state):
        return []

    fringe = PriorityQueue()
    fringe.push((start_state, [], 0), 0)  # (current_state, path_taken, path_cost), priority
    explored_set = set()

    while not fringe.isEmpty():
        state, actions, cost = fringe.pop()

        if state in explored_set:
            continue

        if problem.isGoalState(state):
            return actions

        explored_set.add(state)

        for successor, action, step_cost in problem.getSuccessors(state):
            if successor not in explored_set:
                new_actions = actions + [action]
                new_cost = cost + step_cost
                fringe.push((successor, new_actions, new_cost), new_cost)

    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"


from util import PriorityQueue


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    start_state = problem.getStartState()
    if problem.isGoalState(start_state):
        return []

    fringe = PriorityQueue()
    fringe.push((start_state, [], 0), heuristic(start_state, problem))

    explored_set = set()

    while not fringe.isEmpty():
        state, actions, cost = fringe.pop()

        if state in explored_set:
            continue

        if problem.isGoalState(state):
            return actions

        explored_set.add(state)

        for successor, action, step_cost in problem.getSuccessors(state):
            if successor not in explored_set:
                new_actions = actions + [action]
                new_cost = cost + step_cost
                priority = new_cost + heuristic(successor, problem)
                fringe.push((successor, new_actions, new_cost), priority)

    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
