import Foundation
import SwiftSDL


@main 
final class MyGame: Game {
    private enum CodingKeys:String,CodingKeys{
      case options
    }

 @OptionGroup
 var options: GameOptions
}