//swift-tools-version:6.0
import PackageDescription 

let Package = Package(
  name: "ShellShockCosmicEdition",
  dependencies: [
    .Package(url: "https://github.com/tlarsen7572/SDL2.git", from "0.0.8")
  ]
)