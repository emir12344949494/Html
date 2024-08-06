const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const { body, validationResult } = require('express-validator');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const path = require('path');
const fs = require('fs');
const https = require('https');

const app = express();
const port = process.env.PORT || 3000;

// Configurar CORS
app.use(cors());

// Configurar seguridad con Helmet
app.use(helmet());

// Limitar las solicitudes para evitar ataques de denegación de servicio (DoS)
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutos
  max: 100, // Limitar cada IP a 100 solicitudes por ventana
});
app.use(limiter);

// Configurar Express para manejar JSON
app.use(express.json());

// Conectar a MongoDB
mongoose.connect('mongodb+srv://22300040:Delta1500@dayrongc.b4fakiy.mongodb.net/BD1', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
}).then(() => {
  console.log('Conectado a MongoDB');
}).catch((err) => {
  console.error('Error al conectar a MongoDB', err);
});

// Definir un esquema y modelo de ejemplo
const UsuarioSchema = new mongoose.Schema({
  nombre: String,
  email: String,
});
const Usuario = mongoose.model('Usuario', UsuarioSchema);

// Rutas
app.get('/', (req, res) => {
  res.send('Hola, Mundo!');
});

app.post('/usuario', [
  body('nombre').isString().trim().escape(),
  body('email').isEmail().normalizeEmail(),
], async (req, res) => {
  // Validar los datos de entrada
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  const { nombre, email } = req.body;

  try {
    const nuevoUsuario = new Usuario({ nombre, email });
    await nuevoUsuario.save();
    res.status(201).json(nuevoUsuario);
  } catch (err) {
    res.status(500).send('Error al guardar el usuario');
  }
});

// Manejo de errores
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Algo salió mal!');
});

// Configuración de HTTPS (esto es cunadoo este en producción debes usar certificados válidos)
if (process.env.NODE_ENV === 'production') {
  const privateKey = fs.readFileSync('path/to/private-key.pem', 'utf8');
  const certificate = fs.readFileSync('path/to/certificate.pem', 'utf8');
  const credentials = { key: privateKey, cert: certificate };

  https.createServer(credentials, app).listen(port, () => {
    console.log(`Servidor HTTPS escuchando en el puerto ${port}`);
  });
} else {
  app.listen(port, () => {
    console.log(`Servidor escuchando en el puerto ${port}`);
  });
}
