const express = require('express');
const fs = require('fs');
const app = express();
const PORT = 3001;

app.use(express.json());

// Login route
app.post('/login', (req, res) => {
  const { email, password } = req.body;
  const users = JSON.parse(fs.readFileSync('users.json'));
  const user = users.find(u => u.email === email && u.password === password);

  if (user) {
    res.json({ message: "Login successful", profile: user });
  } else {
    res.status(401).json({ message: "Invalid credentials" });
  }
});

app.listen(PORT, () => {
  console.log(`User-service running on http://localhost:${PORT}`);
});
