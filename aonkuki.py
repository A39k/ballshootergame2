import tkinter as tk

class BallshooterGame:
    def __int__(self, root):
        self.root = root
        self.root.title("Ball Shooter Game")
        
        # For changing background color
        self.canvas = tk.Canvas(root, width=500, height=500, bg="#d3d3d3")
        self.canvas.pack()
        
        # Create the blue ball on the canvas
        self.ball = self.canvas.create_oval(245,450,255,500, fill="blue")
        
        # Create ther red ring
        self.ring = self.canvas.create_oval(240,50,260,70, outline="red", width=2)
        
        # Start Score to 0
        self.score = 0
        
        # Create the score screen
        self.score_label = tk.Label(root, text=f"Score:{self.score}", bg="d3d3d3", fg="black")
        # This code shows the score board/window on the screen
        self.score_label.pack()
        
        self.ball_speed = 10      #Set the speed of the ball
        self.ring_speed = 5       #Set the seed of ring
        self.ring_direction = 1   #Set the starting motion or movement of the ring
        
        #Set the keyboard key for shooting
        self.root.bind("<space>", self.shoot.ball)
        
        #Start moving the ring
        self.move_ring()
        
        # Make the ball mo0ve upward when space key is pressed
        def shoot_ball(self, event):
            self.move_ball()
            
        def move_ball(self):
            if self.canvas.coords(self.ball)[1] > 0:
                # Move the ball upward as set by the ball speed
                self.canvas.move(self.ball, 0, -self.ball_speed)
                    # Create if the ring is hit
                    if not self.check_collision():
                        # Continue moving the ball if the ring is not hit
                        self.root.after(50, self.move_ball)
                    else:
                        # if the ring is hit, score reset tom zero and ball reset to start
                        self.update_score()
                        self.reset_ball()
            else:
                # if the ball reaches the top, reset its position
                self.reset_ball()
        # Move the ring horizontally
        def move_ring(self):
            self.canvas.move(self.ring, self.ring_speed * self.ring_direction, 0)
            self.canvas.coords(self.ring)[0] <= 0 or self.canvas.coords(self.ring)[2] >=500:
                self.ring_direction *= -1
            self.root.after(50, self.move_ring)
            
        def check_collision(self):
           ball_poss = self.canvas.coords(self.ball) 
           ball_poss = self.canvas.coords(self.ring)
           return ring_pos[0] < ballpos < ring_pos[2]  < ring_pos[1]  and  ring_pos[1] < ballpos < ring_pos[1] < ring_pos[3] 
        
        
        def reset_ball(self):
            self.canvas.coords(self.ball, 245, 490, 255, 500)
            
        def update_score(self):
            delf.score +=1
            self.score_label.config(text = f'Score: {self.score}")
                               


# Create the Main window where we put everything
root = tk.Tk()

# Start the game in the Main window
game = BallShooterGame(root)

# Start the game event loop
root.mainloop()