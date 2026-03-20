const { execSync, spawn } = require("child_process");

try {
    console.log("Installing Python...");
    execSync("apt-get update -y && apt-get install -y python3 python3-pip", { stdio: "inherit" });
} catch (e) {
    console.error("Failed to install Python:", e.message);
    process.exit(1);
}

try {
    console.log("Installing Python dependencies...");
    execSync("pip3 install -r requirements.txt", { stdio: "inherit" });
} catch (e) {
    console.error("Failed to install dependencies:", e.message);
    process.exit(1);
}

console.log("Starting bot...");
const bot = spawn("python3", ["__main__.py"], { stdio: "inherit" });

bot.on("close", (code) => {
    process.exit(code);
});