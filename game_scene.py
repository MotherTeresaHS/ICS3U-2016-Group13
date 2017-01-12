# Created by: Anwyl Gabutero
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the main game.

from scene import *
import ui
import random

class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
      
        self.center_of_screen_x = self.size.x
        self.center_of_screen_y = self.size.y
        center_of_screen = self.size/2
        self.left_button_down = False
        self.right_button_down = False
        self.face_move_speed = 20.0
        self.cookies = [] 
        self.cookie_fall_rate = 1
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = '#d5e3ff', 
                                     parent = self, 
                                     size = self.size)
              
                                       
        left_button_position = Vector2(self.center_of_screen_x * 0.05, self.center_of_screen_y * 0.10)
        self.left_button = SpriteNode('./assets/sprites/left_button.png',  
                                       parent = self,
                                       position = left_button_position,
                                       alpha = 0.3,
                                       scale = 0.7)
                                      
      
        right_button_position = Vector2(self.center_of_screen_x * 0.20, self.center_of_screen_y * 0.10)
        self.right_button = SpriteNode('./assets/sprites/right_button.png',
                                       parent = self,
                                       position = right_button_position,
                                       alpha = 0.3,
                                       scale = 0.7)
       
        face_position = Vector2(self.center_of_screen_x * 0.50, self.center_of_screen_y * 0.10)
        self.face = SpriteNode('./assets/sprites/face.PNG',
         						 parent = self,
         						 position = face_position,
         						 scale = 0.10)
         						 
        
    def update(self):  
        # this method is called, hopefully, 60 times a second
       
        if self.left_button_down == True:
            faceMove = Action.move_by(-1 * self.face_move_speed, 
                                           0.0, 
                                           0.1)
            self.face.run_action(faceMove)
        
        if self.right_button_down == True:
            faceMove = Action.move_by(self.face_move_speed, 
                                           0.0, 
                                           0.1)
            self.face.run_action(faceMove)
          
        cookies_create_chance = random.randint(1, 120)
        if cookies_create_chance <= self.cookies_fall_rate:
        	self.add_cookies()
        	
    def touch_began(self, touch):
        # this method is called, when user touches the screen
     
        if self.left_button.frame.contains_point(touch.location):
            self.left_button_down = True
        
        if self.right_button.frame.contains_point(touch.location):
            self.right_button_down = True
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        self.left_button_down = False
        self.right_button_down = False
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.

     def add_cookie(self):
        cookie_start_position = Vector2()
        cookie_start_position.x = random.randint(100, 
                                         self.size_of_screen_x - 100)
        cookie_start_position.y = self.size_of_screen_y + 100
        
        cookie_end_position = Vector2()
        cookie_end_position.x = random.randint(100, 
                                        self.size_of_screen_x - 100)
        cookie_end_position.y = -100
        
        self.cookie.append(SpriteNode('./assets/sprites/cookie.PNG',
                             position = cookie_start_position,
                             parent = self))
    

