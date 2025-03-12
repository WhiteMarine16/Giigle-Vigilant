//swift-tools-version:6.0
import PackageDescription 

let Package = Package(
  name: "ShellShockCosmicEdition",
  platforms: [
    .macOS(.v13),
    .linux
  ],
  dependencies: [
    .Package(url: "https://github.com/PureSwift/SDL.git", from "2.0.0")
  ],
  targets: [
    .executableTarget(
      name: "ShellShockCosmicEdition",
      dependencies: [
        .product(name: "SDL2", package: "SDL")
      ]
    )
)