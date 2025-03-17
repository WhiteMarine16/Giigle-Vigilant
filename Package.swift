//swift-tools-version:6.0
import PackageDescription 

let Package = Package(
  name: "ShellShockCosmicEdition",
  platforms: [
    .macOS(.v13),
    .linux
  ],
  dependencies: [
    .Package(url: "https://github.com/KevinVitale/SwiftSDL.git", from "v0.2.0-alpha.26")
  ],
  targets: [
    .executableTarget(
      name: "ShellShockCosmicEdition",
      dependencies: [
        "SwiftSDL"
      ]
    )
)
