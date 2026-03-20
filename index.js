const { spawn } = require("child_process");

const install = spawn("pip3", ["install", "-r", "requirements.txt"], { stdio: "inherit" });

install.on("close", (code) => {
    if (code !== 0) {
        console.error(`pip install failed with code ${code}`);
        process.exit(code);
    }

    const bot = spawn("python3", ["__main__.py"], { stdio: "inherit" });

    bot.on("close", (code) => {
        process.exit(code);
    });
});