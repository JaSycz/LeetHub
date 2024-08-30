class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        collision_free = [asteroids[0]]
        for i in range(1,len(asteroids)):
            is_collision = collision_free and (asteroids[i] < 0 and collision_free[-1] > 0)
            while is_collision:
                if abs(collision_free[-1]) < abs(asteroids[i]):
                    collision_free.pop()
                elif abs(collision_free[-1]) == abs(asteroids[i]):
                    collision_free.pop()
                    asteroids[i] = 0
                else:
                    asteroids[i] = 0
                is_collision = collision_free and (asteroids[i] < 0 and collision_free[-1]  > 0)
            
            if asteroids[i] !=0: 
                collision_free.append(asteroids[i])
            


        return collision_free
            
            


                    