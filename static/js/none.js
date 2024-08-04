const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
const port = process.env.PORT || 3000;

// Configurar CORS
app.use(cors());
// Conectar a MongoDB
mongoose.connect('mongodb://localhost:27017/DB1', {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(() => {
  console.log('Conectado a MongoDB');
}).catch((err) => {
  console.error('Error al conectar a MongoDB', err);
});

// Rutas
app.get('/', (req, res) => {
  res.send('Hola, Mundo!');
});

app.listen(port, () => {
  console.log(`Servidor escuchando en el puerto ${port}`);
});
