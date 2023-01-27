import random
class BattleshipAI:
    def __init__(self):
        self.shots_taken = set()  # keep track of shots taken
        self.hits = set() # keep track of hits
        self.orientation = None  # keep track of orientation of hit ship
        self.potential_targets = set() # set of potential targets
        
    def take_shot(self):
        if not self.orientation:  # if orientation is not known
            shot = self._random_shot() 
        elif self.potential_targets:
            shot = self.potential_targets.pop()
        else:
            shot = self._extend_search()
        self.shots_taken.add(shot)
        return shot
    
    def process_result(self, result):
        if result == "hit":
            self.hits.add(self.shots_taken[-1])
            if self.orientation:
                self.potential_targets.update(self._get_adjacent_coordinates(self.shots_taken[-1]))
            else:
                self.potential_targets.update(self._get_adjacent_coordinates(self.shots_taken[-1]))
                if len(self.hits) >= 2:
                    self._determine_orientation()
        elif result == "miss":
            if self.potential_targets:
                self.potential_targets.discard(self.shots_taken[-1])
    
    def _random_shot(self):
        """Return a random coordinate that has not been shot at before"""
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if (x, y) not in self.shots_taken:
                return (x, y)
    
    def _get_adjacent_coordinates(self, coordinate):
        """Return a list of coordinates adjacent to the given coordinate"""
        x, y = coordinate
        return {(x+i, y+j) for i in [-1, 0, 1] for j in [-1, 0, 1] if i != 0 or j != 0}
    
    def _determine_orientation(self):
        """Determine orientation of hit ship"""
        hit1, hit2 = self.hits
        if hit1[0] == hit2[0]:
            self.orientation = "horizontal"
        else:
            self.orientation = "vertical"
    
    def _extend_search(self):
        """Return a coordinate to extend search in the current orientation"""
        if self.orientation == "horizontal":
            return (self.hits[-1][0], self.hits[-1][1] + 1) if self.hits[-1][1] < 9 else (self.hits[-1][0], self.hits[-1][1] - 1)
        else:
            return (self.hits[-1][0] + 1, self.hits[-1][1]) if self.hits[-1][0] < 9 else (self.hits[-1][0] - 1, self.hits[-1][1])
    
    def _finished_search(self):
        """Check if the search for a ship is finished"""
        if self.orientation == "h":
            if self.last_hit[1] == self.first_hit[1] + self.hit_count - 1:
                return True
        elif self.orientation == "v":
            if self.last_hit[0] == self.first_hit[0] + self.hit_count - 1:
                return True
        return False

    def _get_next_coord(self):
        """Get the next coordinate to shoot at based on the current search"""
        if self.orientation == "h":
            return (self.last_hit[0], self.last_hit[1] + self.direction)
        elif self.orientation == "v":
            return (self.last_hit[0] + self.direction, self.last_hit[1])
        else:
            return self._random_shot()

    def _update_search(self, shot_result):
        """Update the search based on the result of the previous shot"""
        if shot_result == "hit":
            self.hit_count += 1
            self.last_hit = self.shots_taken[-1]
            if self.orientation == "N/A":
                self.first_hit = self.last_hit
                if self._adjacent_hit():
                    self.orientation = self._get_orientation()
        elif shot_result == "miss":
            if self.orientation != "N/A":
                self.direction = -self.direction
                if self._finished_search():
                    self.orientation = "N/A"
                    self.hit_count = 0
                    self.direction = 1
        return shot_result

    def shoot(self):
        """Shoot at the next coordinate and update the search"""
        coord = self._get_next_coord()
        result = self.board.shoot(coord)
        self.shots_taken.append(coord)
        return self._update_search(result)