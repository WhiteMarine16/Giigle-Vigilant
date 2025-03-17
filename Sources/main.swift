import Foundation
import SDL2


                                  // Constants

let WINDOW_WIDTH = 600           //Height and width of the window
let WINDOW_HEIGHT = 800
let playerSpeed = 30              //Speed of the player
let bulletSpeed = 10              //Speed of the bullet
let invadersSpeed = 5             //Speed of the invaders
let numberOfInvaders = 10         //Number of invaders

enum GameStatus {               // Check Game status
    case playing
    case gameOver
    case gameWon
}
  

enum BulletStatus {          // Check Bullet status
    case ready
    case fire
}

class GameObject {          // Common class defining properties for all game objects
    var x: Int
    var y: Int
    var width: Int
    var height: Int
    var color: SDL_Color