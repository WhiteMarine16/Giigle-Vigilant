// swift-tools-version:6.0
import PackageDescription 

let package = Package(
    name: "ShellShockCosmicEdition",
    platforms: [
        .macOS(.v13),
        .linux
    ],
    dependencies: [
        .package(url: "https://github.com/KevinVitale/SwiftSDL.git", from: "0.2.0-alpha.26")
    ],
    targets: [
        .executableTarget(
            name: "ShellShockCosmicEdition",
            dependencies: [
                "SwiftSDL"
            ]
        )
    ]
)
