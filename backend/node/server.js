const express = require('express');
const cors = require('cors');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;
const PYTHON_API = process.env.PYTHON_API || 'http://localhost:8000';

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('../frontend'));

// Health check
app.get('/health', (req, res) => {
  res.json({ status: 'ok', server: 'Node.js', version: '0.1.0' });
});

// Root
app.get('/', (req, res) => {
  res.json({ message: 'Age of Clans Server', docs: 'Check /health' });
});

// Proxy to Python API
app.use('/api/python', async (req, res) => {
  try {
    const axios = require('axios');
    const response = await axios({
      method: req.method,
      url: `${PYTHON_API}${req.path.replace('/api/python', '')}`,
      data: req.body,
      headers: req.headers
    });
    res.json(response.data);
  } catch (error) {
    res.status(error.response?.status || 500).json({ error: error.message });
  }
});

app.listen(PORT, () => {
  console.log(`🎮 Age of Clans Server running on http://localhost:${PORT}`);
  console.log(`📡 Python API: ${PYTHON_API}`);
});