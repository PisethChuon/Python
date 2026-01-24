let defaultColorName = "red"
var userDefinedColorName: String?   // defaults to nil
userDefinedColorName = "blue"

var colorNameToUse = userDefinedColorName ?? defaultColorName
print("The color name is \(colorNameToUse).")