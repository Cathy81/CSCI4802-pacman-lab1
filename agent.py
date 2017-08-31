import pacmanGame

class SimpleReflexAgent:
    def __init__(self, game):
        #define two instance variables
        self.actions=["West", "East","North","South"]
        self.game=game

    def get_action(self, pos):
         for action in self.actions:
              (isValid, new_pos)=self.game.nextDirectionIsValid(action, pos)
              if isValid:
                   return (action, new_pos)
         return (None, pos)

