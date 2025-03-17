import Foundation
import SwiftSDL


@main 
final class MyGame: Game {
    private enum CodingKeys:String,CodingKeys{
      case options
    }

 @OptionGroup
 var options: GameOptions

 private let screenwhidth = 600       // Setup Windows Dimensions 
 private let screenHeight = 800 
}