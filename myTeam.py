class MyReflexAgent(ReflexCaptureAgent):
# approximate Q-learning, NN, search problems combinations A* w/ food if winning w/ opposite agent if losing, alphabeta
# in principle a good reflexive agent should work
    def get_features(self, game_state, action):
        features = util.Counter()
        successor = self.get_successor(game_state, action)
        food_list = self.get_food(successor).as_list()
        features['successor_score'] = -len(food_list)  # self.getScore(successor)

        # Compute distance to the nearest food
        if len(food_list) > 0:  # This should always be True,  but better safe than sorry
            my_pos = successor.get_agent_state(self.index).get_position()
            min_distance = min([self.get_maze_distance(my_pos, food) for food in food_list])
            features['distance_to_food'] = min_distance

        # Consider the number of remaining capsules
        capsules = self.get_capsules(successor)
        features['num_capsules'] = len(capsules)

        # Consider the distance to the nearest capsule
        if len(capsules) > 0:
            min_capsule_distance = min([self.get_maze_distance(my_pos, cap) for cap in capsules])
            features['distance_to_capsule'] = min_capsule_distance

        # Encourage exploring the opponent's side when the agent is winning
        if self.get_score(successor) > 0:
            features['explore_opponent_side'] = 1 if my_pos[0] > successor.get_layout().width // 2 else 0

        # Defend our side when the agent is losing
        if self.get_score(successor) < 0:
            features['defend_our_side'] = 1 if my_pos[0] <= successor.get_layout().width // 2 else 0

        # Distance from the opponent
        opponents = self.get_opponents(successor)
        opponent_distances = [self.get_maze_distance(my_pos, successor.get_agent_state(opp).get_position()) for opp in opponents]
        min_opponent_distance = min(opponent_distances, default=float('inf'))
        features['distance_to_opponent'] = min_opponent_distance

        # Catch food when opponents are far
        if min_opponent_distance > 5:
            features['catch_food'] = len(food_list)


        # Use power capsules when opponents are close
        if min_opponent_distance < 5 and my_state.is_pacman:
            features['use_power_capsule'] = 1

        return features
    
    def get_weights(self, game_state, action):
        return {
            'successor_score': 100,
            'distance_to_food': -1,
            'num_capsules': -50,              # Penalty for having more capsules
            'distance_to_capsule': -10,
            'explore_opponent_side': 50,      # Encourage exploring opponent's side when winning
            'defend_our_side': 50,            # Encourage defending our side when losing
            'distance_to_opponent': -20,      # Maintaining distance from opponents
            'catch_food': 10,                 # Catch food when opponents are far
            'use_power_capsule': 20           # Use power capsules when opponents are close
        }
