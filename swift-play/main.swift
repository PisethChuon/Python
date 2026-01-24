var environment = "Development"
let maxinmNumberOfLoginAttempts: Int

if environment == "Development" {
    maxinmNumberOfLoginAttempts = 100
}
else {
    maxinmNumberOfLoginAttempts = 10
}
